from . import bp as api
from flask import jsonify, request
from app.models import Post, User


@api.route('/')
def index():
    return 'Hello World'


@api.route('/users', methods=['POST'])
def new_user():
    if not request.is_json:
        return jsonify({'error': 'Your request content-type must be application/json'})
    # get data from request body
    data = request.json
    # like "validate on submit" - check for required fields
    for field in ['email', 'username', 'password']:
        if field not in data:
            return jsonify({'error': f'{field} must be in request body'}), 400
    # get fields from user data dict
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')
    user_check = User.query.filter((User.email == email) | (User.username == username))
    if user_check:
        return jsonify({"error": 'A user with that username or email already exists. Please try a different name.',}), 400
    # add new user to database with request info
    new_user = User(email=email, username=username, password=password)
    return jsonify(new_user.to_dict()), 201


#displays all users
@api.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users])

#displays one user
@api.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())


@api.route('/posts')
def get_posts():
    posts = Post.query.all()
    return jsonify([p.to_dict() for p in posts])


@api.route('/posts/<post_id>', methods=['GET'])
def get_post(post_id):
    post = Post.query.get(post_id)
    return jsonify(post.to_dict())


@api.route('/posts', methods=['POST'])
def create_post():
    if not request.is_json:
        return jsonify({'error': 'Your request content-type must be application/json'})
    # get data from request body
    data = request.json
    # instead of "validay on submit" - make sure all required fields present
    for field in ['title', 'body', 'user_id']:
        if field not in data:
            return jsonify({'error': f'{field} must be in request body'}), 400
    # get fields from data dict
    title = data.get('title')
    body = data.get('title')
    user_id = data.get('user_id')
    # add new post to database with request body info
    new_post = Post(title=title, body=body, user_id=user_id)
    return jsonify(new_post.to_dict()), 201


# use PUT request to update/edit post
@api.route('/posts/<post_id>', methods=['PUT'])
def update_post(post_id):
    post_to_edit = Post.query.get_or_404(post_id)
    if not request.is_json:
        return jsonify({'error': 'Your request content-type must be applicatin/json'})
    post_to_edit(**request.json)
    return jsonify(post_to_edit.to_dict())


# use DELETE request to delete post

@api.route('/posts/<post_id>', methods=['DELETE'])
def delete_post(post_id):
    post_to_delete = Post.query.get_or_404(post_id)
    post_to_delete.delete()
    return jsonify({'message': 'You have successfully deleted the post'})
