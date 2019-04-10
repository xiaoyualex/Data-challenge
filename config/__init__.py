from flask import Flask
application = Flask(__name__)
application.config.from_object('config.default')

# create db connection
from flask_sqlalchemy import SQLAlchemy
from flask_mongoalchemy import MongoAlchemy
sql_db = SQLAlchemy(application)
nonsql_db = MongoAlchemy(application)


def __init_db():
    from models.user_data_sql import __init_user_sql_db
    __init_user_sql_db()


