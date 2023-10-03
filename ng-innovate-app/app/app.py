from flask import Flask, request, jsonify
from db import init_db, User, db

app = Flask(__name__)
init_db(app)

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = [{'id': user.id, 'username': user.username} for user in users]
    return jsonify(user_list)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    if not username:
        return jsonify({'error': 'Username is required'}), 400

    new_user = User(username=username)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)