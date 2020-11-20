from db.db_helper import DbHelper

db_handler = DbHelper.get_instance()
my_cursor = db_handler.db.cursor()
my_cursor.execute("SHOW DATABASES")
for x in my_cursor:
    print(x)
db_handler.db.close()
