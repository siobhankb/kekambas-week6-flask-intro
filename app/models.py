from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable = False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    posts = db.relationship('Post', backref='author') # <-- this is how to set up a foreign key!!
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.password = generate_password_hash(kwargs['password'])
        db.session.add(self)
        db.session.commit()


    def __repr__(self):
        return f"<User|{self.username}>"

    def check_password(self, password):
        return check_password_hash(self.password, password)   

    def to_dict(self):
        data = {
            'id': self.id,
            'email': self.email,
            'username': self.username,
            'joined': self.date_created,
            'post_count': len(self.posts)
        }
        return data

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String(250), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #references 'user' in table 

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"<Post|{self.title}>"

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key in {'title', 'body'}:
                setattr(self, key, value)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'date_created': self.date_created,
            'user_id': self.user_id
        }
