from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm, PostForm
from app.models import User, Post

#tell what URL
@app.route('/index')
def index():
    users=User.query.all()
    posts=Post.query.all()
    return render_template('index.html', users=users, posts=posts)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        print('This was a huge success')
        email = form.email.data
        username = form.username.data
        password = form.password.data
        print(email, username, password)
        # Query user table to make sure info entered is unique
        user_check = User.query.filter((User.email == email)|(User.username== username)).all()
        if user_check:
            flash('A user with that username or email already exitsts', 'danger')
            return redirect(url_for('signup'))

        # add the user to the database
        new_user = User(email=email, username=username, password=password)
        
        # show message of success/failure
        flash(f'{new_user.username} has successfully signed up!', 'success')
        #redirect back to the homepage
        return redirect(url_for('index'))

    return render_template('signup.html', form=form)


@app.route('/create_post')
def create_post():
    form = PostForm()
    

    return render_template('create_post.html', form=form)

# when you close the terminal, it doesn't save the app you've run
# python has a package that will automatically

#can use jinja2, a package, to format 
# render_template('some_template_name', )