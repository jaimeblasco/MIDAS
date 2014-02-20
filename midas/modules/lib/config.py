#!/usr/bin/env python
"""
This is the config for MIDAS
"""
from os.path import dirname, realpath


config = {}

current_dir = dirname(realpath(__file__))
if "/Users" in current_dir:
    config['database'] = 'midas_hids.sqlite'
else:
    config['database'] = '/tmp/midas_hids.sqlite'

config['plist_check_keys'] = [
    'RunAtLoad',
    'WatchPaths',
    'KeepAlive',
    'StartInterval',
    'StartOnMount',
    'OnDemand',
    'QueueDirectories',
    'StandardInPath',
    'StandardOutPath',
    'StandardErrorPath',
    'Debug',
    'LaunchOnlyOnce',
    'Sockets',
    'OSAXHandlers',
    'LSEnvironment',
    'CFBundleVersion',
]

config['plist_check_keys_hash'] = [
    'Program',
    'ProgramArguments'
]

config['firewall_keys'] = [
    'allowsignedenabled',
    'firewallunload',
    'globalstate',
    'loggingenabled',
    'previousonstate',
    'stealthenabled',
    'version',
]

# AlienVault configuration
import netsyslog
config['alienvault_instance'] = ""
config['netsyslogger'] = netsyslog.Logger()
config['netsyslogger'].add_host(config['alienvault_instance'])

# Set this to False to use ./midas/log/*.log
config['use_netsyslogger'] = True

# Maintain backwards compatibility
Config = config
