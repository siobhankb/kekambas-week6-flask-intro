from flask import Flask

#since Flask is a class,
# this points to module where app is running
app = Flask(__name__)
#tell what URL
@app.route('/')
def index():
    return 'Hello World!'

@app.route("/test")
def test():
    return 'This is a test!'

#can exit out of thing