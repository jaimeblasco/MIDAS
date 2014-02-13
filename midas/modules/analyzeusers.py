from os.path import isfile
from os import chmod
from time import time, gmtime, strftime
import logging
from sys import argv

from lib.ty_orm import TyORM
from lib.config import Config
from lib.data_science import DataScience
from lib.helpers.system import list_users
from lib.helpers.utilities import error_running_file
from lib.tables.example import tables

class AnalyzeUsers():
    """Analyze system users"""

    def __init__(self):
        self.data = []

    def check_users(self):
        """
        Log all users
        """

        users = list_users()
        for u in users:
            self.data.append({"name": u, "date": exec_date, })

    def analyze(self):
        self.check_users()



if __name__ == "__main__":

    start = time()

    # the "exec_date" is used as the "date" field in the datastore
    exec_date = strftime("%a, %d %b %Y %H:%M:%S", gmtime())

    # the table definitions are stored in a library file. this is instantiating
    # the ORM object and initializing the tables
    ORM = TyORM(Config.get("database"))
    if isfile(Config.get("database")):
        chmod(Config.get("database"), 0600)
    for k, v in tables.iteritems():
        ORM.initialize_table(k, v)

    ###########################################################################
    # Gather data
    ###########################################################################
    try:
        u = AnalyzeUsers()
        if u is not None:
            u.analyze()
            users = u.data
            data_science = DataScience(ORM, users, "users")
            new_entries = data_science.get_new_entries()
            if new_entries:
                for entry in new_entries:
                    next_message = "ty_name=\"%s\" " % "users"
                    for key, value in entry.iteritems():
                        if value != "KEY DNE":
                            next_message += "%s=\"%s\" " % (key, value)
                            print next_message
            data_science.get_removed_entries()
            removed_entries = data_science.get_new_entries()
            if removed_entries:
                for entry in removed_entries:
                    next_message = "ty_name=\"%s\" " % "users"
                    for key, value in entry.iteritems():
                        if value != "KEY DNE":
                            next_message += "%s=\"%s\" " % (key, value)
                            print next_message
    except Exception, error:
        print error_running_file(__file__, "lad", error)

    end = time()

    # to see how long this module took to execute, launch the module with
    # "--log" as a command line argument
    if "--log" in argv[1:]:
        logging.basicConfig(format='%(message)s', level=logging.INFO)
    logging.info("Execution took %s seconds.", str(end - start))