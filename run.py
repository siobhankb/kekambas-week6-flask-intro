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
    return 'This is a test'

# when you close the terminal, it doesn't save the app you've run
# python has a package that will automatically