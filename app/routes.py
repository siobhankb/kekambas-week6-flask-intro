from app import app
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user
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


@app.route('/create-post',  methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post_title = form.title.data
        post_body = form.body.data
        user_id = current_user.id

        new_post=Post(title=post_title, body=post_body, user_id=user_id)
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

@app.route('/logout')
def logout():
    logout_user()
    flash('You have logged out', 'secondary')
    return redirect(url_for('index'))

@app.route('/posts/<post_id>')
def view_single_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('single_post.html', post=post)

@app.route('/edit-posts/<post_id>')
def edit_single_post(post_id):
    post_to_edit = Post.query.get_or_404(post_id)
    if current_user != post_to_edit.author:
        flash('You do not have permission to edit this post.', 'danger')
        return redirect(url_for('index'))
    return post_to_edit.title

# when you close the terminal, it doesn't save the app you've run
# python has a package that will automatically

#can use jinja2, a package, to format 
# render_template('some_template_name', )