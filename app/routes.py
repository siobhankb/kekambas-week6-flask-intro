from app import app
from flask import render_template, redirect, url_for, flash
from flask_login import login_user
from app.forms import SignUpForm, PostForm, LoginForm
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


@app.route('/create_post',  methods=['GET', 'POST'])
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post_title = form.title.data
        post_body = form.body.data

        new_post=Post(title=post_title, body=post_body, user_id=1)
        flash(f'{new_post.title} successfully created!', 'success')
        return redirect(url_for('index'))

    return render_template('create_post.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #find out if there is actually a user with that username & pw
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()

        if user is not None and user.check_password(password):
            login_user(user)
            flash(f'Welcome back, {user.username}', 'primary')
            return redirect(url_for('index'))

        flash('Incorrect username and/or password. Please try again.', 'danger')
        return redirect(url_for('login'))
    
    return render_template('login.html', form=form)


# when you close the terminal, it doesn't save the app you've run
# python has a package that will automatically

#can use jinja2, a package, to format 
# render_template('some_template_name', )