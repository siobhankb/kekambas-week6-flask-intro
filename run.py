from flask import Flask, render_template

#since Flask is a class,
# this points to module where app is running
app = Flask(__name__)
#tell what URL
@app.route('/')
def index():
    user = {
        'username': 'siobhankb',
        'email': 'skb@coolio.org'
    }
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    return render_template('index.html', user=user, colors=colors)

@app.route("/test")
def test():
    return 'This is a test'

# when you close the terminal, it doesn't save the app you've run
# python has a package that will automatically

#can use jinja2, a package, to format 
# render_template('some_template_name', )