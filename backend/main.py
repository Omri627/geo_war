from apis.user import User
from db.db_helper import DbHelper

x_user = User(user_name='Omrissssssssssssssssssssssssssssssssssssssss', password='1234')
x_user.create_user()
db_helper = DbHelper.get_instance()
my_cursor = db_helper.db.cursor()
my_cursor.execute("SHOW DATABASES")
for x in my_cursor:
    print(x)
db_helper.db.close()
