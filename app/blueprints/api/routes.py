from . import bp as api
from flask import jsonify, request
from app.models import Post

@api.route('/')
def index():
    return 'Hello World'

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
        return jsonify({'error': 'Your request content-type must be applicatin/json'})
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
    #add new post to database with request body info
    new_post = Post(title=title, body=body, user_id=user_id)
    return jsonify(new_post.to_dict()), 201


# use PUT request to update/edit post
@api.route('/posts/<post_id>', methods=['PUT'])
def update_post(post_id):
    pass


# use DELETE request to delete post

@api.route('/posts/<post_id>', methods=['DELETE'])
def delete_post(post_id):
    pass

