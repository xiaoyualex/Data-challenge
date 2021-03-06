# MySQL configuration
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_POOL_RECYCLE = 600
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://alex001:alex001@localhost/user_data'

# MongoDB configuration
MONGOALCHEMY_DATABASE = 'user_data'
MONGOALCHEMY_SERVER = 'localhost'
MONGOALCHEMY_PORT = '27017'