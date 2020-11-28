from datetime import datetime

from apis.score import Score
from apis.user import User
from db.db_helper import DbHelper

# x_user = User(user_name='Omrissssssssssssssssssssssssssssssssssssssss', password='1234')
# x_user.create_user()
# db_helper = DbHelper.get_instance()
# my_cursor = db_helper.db.cursor()
# my_cursor.execute("SHOW DATABASES")
# for x in my_cursor:
#     print(x)
# db_helper.db.close()
from utils.const import Const

now = datetime.now()

d1 = now.strftime(Const().DATETIME_FORMAT)
score = Score(user_name='Omris', country_code='IS', points=100, date=d1)
score.insert_score()
