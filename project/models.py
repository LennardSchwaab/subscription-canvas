from project import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class Block1(db.Model):
    __tablename__  ='block1'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    frage1 = db.Column(db.Integer)
    frage2 = db.Column(db.Integer)
    frage3 = db.Column(db.Integer)
    frage4 = db.Column(db.Integer)
    frage5 = db.Column(db.Integer)
    frage6 = db.Column(db.Integer)

    def __init__(self, current_user, frage1, frage2, frage3, frage4, frage5, frage6):
        self.user_id = current_user
        self.frage1 = frage1
        self.frage2 = frage2
        self.frage3 = frage3
        self.frage4 = frage4
        self.frage5 = frage5
        self.frage6 = frage6

    def __repr__(self):
        return f'{self.frage1}, {self.frage2}, {self.frage3}, {self.frage4}, {self.frage5}, {self.frage6}'

    def report_frage1_id(self):
        return(self.id)

class User(db.Model, UserMixin):
    __tablename__  ='users'

    id = db.Column(db.Integer, primary_key=True)
    profile_image = db.Column(db.String(64), nullable=False, default='default_profile.jpg')
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    check_password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.check_password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.check_password_hash, password)

    def __repr__(self):         # --> kann über query.get() abgefragt werden
        return self.username
