from config import nonsql_db as db

class User(db.Document):
    id = db.IntField()
    first_name = db.StringField(max_length=100)
    last_name = db.StringField(max_length=100)
    avatar = db.StringField()

print('Finish the construction of non sql db.')