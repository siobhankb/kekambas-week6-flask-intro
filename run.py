from app import app, db
from app.models import User, Post

# to change shell context to import/access different object
@app.shell_context_processor
def make_context():
    return {'db':db, 'Post': Post, 'User':User}