#!/usr/bin/env python
"""
This is the launcher for MIDAS
"""

import logging
from subprocess import Popen, PIPE
from os import listdir
from os.path import dirname, realpath, isfile, join, splitext, basename
from collections import namedtuple
from itertools import chain
from socket import gethostname
from time import strftime, gmtime
import syslog

from modules.lib.config import Config

# Types
TyLanguage = namedtuple("TyLanguage", "supported_extensions execution_string")

# Configurations
logging.basicConfig(format='%(message)s', level=logging.INFO)

# Contants
CURRENT_DIR = dirname(realpath(__file__))

MODULES_DIR = join(CURRENT_DIR, "modules")

LOG_DIR = join(CURRENT_DIR, "log")

HOSTNAME = gethostname()

DATE = strftime("%Y-%m-%dT%H:%M:%S%z", gmtime())

MODULES = [
    join(MODULES_DIR, fname) for fname in listdir(MODULES_DIR)\
    if isfile(join(MODULES_DIR, fname))
]

PYTHON_LANGUAGE = TyLanguage(
    supported_extensions = [".py", ".pyc"],
    execution_string = "python",
)

RUBY_LANGUAGE = TyLanguage(
    supported_extensions = [".rb"],
    execution_string = "ruby"
)

BASH_LANGUAGE = TyLanguage(
    supported_extensions = [".bash", ".sh"],
    execution_string = "/bin/bash"
)

SUPPORTED_LANGUAGES = [
    PYTHON_LANGUAGE,
    RUBY_LANGUAGE,
    BASH_LANGUAGE,
]


# Functions
def log_line(log_name, line):
    """log_line accepts a line a returns a properly formatted log line"""
    return "%s %s ty[%s]: %s" % (
        DATE,
        HOSTNAME,
        log_name,
        line,
    )

def send_syslog(msg):
    """send a log message to AlienVault"""
    Config['netsyslogger'].log(syslog.LOG_USER, syslog.LOG_NOTICE, msg, pid=True)

def spawn_module(module, current_lang, mod_name):
    """spawn_module executes an individual Tripyarn module"""
    log_file = join(LOG_DIR, mod_name + ".log")

    command = list(chain(
        current_lang.execution_string.split(" "),
        [module],
    ))

    execution = Popen(command, stdout=PIPE, stderr=PIPE)
    stdout = execution.stdout.readlines()
    stderr = execution.stderr.readlines()

    file_handler = open(log_file, "a")

    for stdout_line in stdout:
        if Config['use_netsyslogger']:
            send_syslog(log_line(mod_name, stdout_line))
        else:
            file_handler.write(log_line(mod_name, stdout_line))

    for stderr_line in stderr:
        if Config['use_netsyslogger']:
            send_syslog(log_line(mod_name, stderr_line))
        else:
            file_handler.write(log_line(mod_name, stderr_line))

def launch_modules():
    """launch_modules launches Tripyarn's executable modules"""
    if Config['use_netsyslogger'] and not Config['alienvault_instance']:
        print "[x] Error: netsyslogger enabled but no remote host defined.  Please enter the IP of your AlienVault instance in midas/modules/lib/config.py and try again."
        return
    for module in MODULES:
        current_lang = None
        mod_name, ext = splitext(basename(module))

        for language in SUPPORTED_LANGUAGES:
            if ext in language.supported_extensions:
                current_lang = language
                break

        if current_lang is not None and isinstance(current_lang, TyLanguage):
            spawn_module(module, current_lang, mod_name)


if __name__ == "__main__":
    launch_modules()
