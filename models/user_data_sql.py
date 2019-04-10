from config import sql_db as db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key = True)
    first_name = db.Column(db.String(100),index=True)
    last_name = db.Column(db.String(100),index=True)
    avatar = db.Column(db.Text)

def __init_user_sql_db():
    db.create_all()
    db.session.commit()
    print('Finish the construction of sql db.')
