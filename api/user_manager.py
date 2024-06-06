from flask import Flask, request, jsonify
from persistence import DataManager


app = Flask(__name__)
datamanager = DataManager()


@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    if 'email' not in data or 'first_name' not in data or 'last_name' not in data:
        return jsonify({'error': "Missing required fields"}), 400


@app.route('/users', methods=['GET'])
def get_users():
    pass


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    pass


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    pass


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    pass


if __name__ == '__main__':
    app.run(debug=True)
