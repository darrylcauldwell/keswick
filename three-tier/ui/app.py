from flask import Flask, request, render_template, redirect, url_for
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/users', methods=['GET'])
def user_list():
    response = requests.get('http://ng-innovate-app:5000/users')
    users = response.json()
    return render_template('user_list.html', users=users)

@app.route('/users', methods=['POST'])
def create_user():
    username = request.form['username']
    user_data = {'username': username}
    requests.post('http://ng-innovate-app:5000/users', json=user_data)
    return redirect(url_for('index'))

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000)