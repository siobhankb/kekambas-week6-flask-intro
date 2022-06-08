from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm
from app.models import User

#tell what URL
@app.route('/index')
def index():
    user = {
        'username': 'siobhankb',
        'email': 'skb@coolio.org'
    }
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    return render_template('index.html', user=user, colors=colors)



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        print('This was a huge success')
        email = form.email.data
        username = form.username.data
        password = form.password.data
        print(email, username, password)
        if username in {'abc', 'aaa'}:
            flash('That username already exitsts')
            return redirect(url_for('index'))

        # add the user to the database
        new_user = User(email=email, username=username, password=password)

        # show message of success/failure
        flash(f'{new_user.username} has successfully signed up!', 'success')
        #redirect back to the homepage
        return redirect(url_for('index'))

    return render_template('signup.html', form=form)

# when you close the terminal, it doesn't save the app you've run
# python has a package that will automatically

#can use jinja2, a package, to format 
# render_template('some_template_name', )