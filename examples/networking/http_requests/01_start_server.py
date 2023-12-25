#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)

# Example data store
users = {"1": {"name": "John Doe", "email": "john@example.com"}}

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    user_id = str(len(users) + 1)
    users[user_id] = request.json
    return jsonify({user_id: users[user_id]}), 201

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id in users:
        users[user_id] = request.json
        return jsonify({user_id: users[user_id]})
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/users/<user_id>', methods=['PATCH'])
def patch_user(user_id):
    if user_id in users:
        for key, value in request.json.items():
            users[user_id][key] = value
        return jsonify({user_id: users[user_id]})
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"success": "User deleted"})
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
