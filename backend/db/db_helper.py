from db.settings import Settings
import mysql.connector


class DbHelper:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if DbHelper.__instance is None:
            DbHelper()
        return DbHelper.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if DbHelper.__instance is not None:
            raise Exception("This class is a singleton!, use static method get_instance()")
        else:
            self.settings = Settings()
            self.db = mysql.connector.connect(
                host=self.settings.host,
                user=self.settings.user,
                password=self.settings.password,
                database=self.settings.database,
            )
            DbHelper.__instance = self

    def __str__(self):
        return str(self.db)
