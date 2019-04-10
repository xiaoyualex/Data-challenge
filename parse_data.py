from config import __init_db
import config
import json
__init_db()

from models.user_data_nonsql import User as no_sql_user
from models.user_data_sql import User as sql_user


# read data from json file
with open('user_data.txt','r') as json_file:
    data = json.load(json_file)
user_data = data['data']

for every_user in user_data:
    # import data to sql database
    # check this record if exists
    result = sql_user.query.filter(sql_user.id==every_user['id']).all()

    #if not exists
    if not result:
        newUser = sql_user()
        newUser.id = every_user['id']
        newUser.first_name = every_user['first_name']
        newUser.last_name = every_user['last_name']
        newUser.avatar = every_user['avatar']
        config.sql_db.session.add(newUser)

    # update the sql database
    try:
        config.sql_db.session.commit()
    except Exception as e:
        print('Error'+str(e))
        config.sql_db.session.rollback()
        config.sql_db.session.remove()



    # import data to nosql database
    # check this record if exists
    result = no_sql_user.query.get(every_user['id'])

    # if not exists
    if not result:
        newUser = no_sql_user()
        newUser.id = every_user['id']
        newUser.first_name = every_user['first_name']
        newUser.last_name = every_user['last_name']
        newUser.avatar = every_user['avatar']
        # update to the database
        newUser.save()



