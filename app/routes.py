from app import app
from flask import render_template
from app.forms import SignUpForm

#tell what URL
@app.route('/index')
def index():
    user = {
        'username': 'siobhankb',
        'email': 'skb@coolio.org'
    }
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    return render_template('index.html', user=user, colors=colors)



@app.route('/signup')
def signup():
    form = SignUpForm()
    return render_template('signup.html', form=form)

# when you close the terminal, it doesn't save the app you've run
# python has a package that will automatically

#can use jinja2, a package, to format 
# render_template('some_template_name', )