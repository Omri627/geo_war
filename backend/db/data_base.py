from db.settings import Settings


class DataBase:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if DataBase.__instance is None:
            DataBase()
        return DataBase.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if DataBase.__instance is not None:
            raise Exception("This class is a singleton!, use static method get_instance()")
        else:
            self.settings = Settings()
            DataBase.__instance = self
