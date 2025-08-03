from flask import Flask, request, jsonify
from app import models, utils

app = Flask(__name__)

@app.route('/')
def home():
    return "User Management System"

@app.route('/users', methods=['GET'])
def get_all_users():
    users = models.get_all_users()
    return jsonify(users), 200

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = models.get_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({'error': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    if not (name and email and password):
        return jsonify({'error': 'Missing fields'}), 400
    if not utils.validate_email(email):
        return jsonify({'error': 'Invalid email'}), 400
    if not utils.validate_password(password):
        return jsonify({'error': 'Password too short'}), 400
    password_hash = utils.hash_password(password)
    try:
        user_id = models.create_user(name, email, password_hash)
        return jsonify({'user_id': user_id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    if not (name and email):
        return jsonify({'error': 'Missing fields'}), 400
    if not utils.validate_email(email):
        return jsonify({'error': 'Invalid email'}), 400
    updated = models.update_user(user_id, name, email)
    if updated:
        return jsonify({'status': 'User updated'}), 200
    return jsonify({'error': 'User not found'}), 404

@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    deleted = models.delete_user(user_id)
    if deleted:
        return jsonify({'status': 'User deleted'}), 200
    return jsonify({'error': 'User not found'}), 404

@app.route('/search', methods=['GET'])
def search_users():
    name = request.args.get('name')
    if not name:
        return jsonify({'error': 'Please provide a name to search'}), 400
    users = models.search_users_by_name(name)
    return jsonify(users), 200

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    if not (email and password):
        return jsonify({'error': 'Missing fields'}), 400
    user = models.get_user_by_email(email)
    if user and utils.verify_password(password, user[3]):
        return jsonify({'status': 'success', 'user_id': user[0]}), 200
    return jsonify({'status': 'failed'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
