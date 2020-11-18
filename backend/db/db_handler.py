from db.db_helper import DbHelper


class DbHandler:

    def __init__(self):
        self.helper = DbHelper.get_instance()
