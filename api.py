from flask import Flask, jsonify, request, json
from flask_mysql_connector import MySQL
from dotenv import load_dotenv
import os

load_dotenv()

# Flask initializer
app = Flask(__name__)

# MySQL Config
app.config['MYSQL_USER'] = os.getenv('USERDB')
app.config['MYSQL_PASSWORD'] = os.getenv('PASSDB')
app.config['MYSQL_DATABASE'] = os.getenv('NAMEDB')
app.config['MYSQL_HOST'] = os.getenv('HOSTDB')
app.config['MYSQL_PORT'] = os.getenv('PORTDB')
mysql = MySQL(app)


# Api test
@app.route('/')
def hello():
    return 'ESTAMOS NO BRASIL!'


# Api to get all users
@app.route('/user')
def get_all_users():
    cur = mysql.new_cursor(dictionary=True)
    cur.execute('select `name`, `email`, `role` from users;')
    output = cur.fetchall()
    return jsonify(users=output)


# Api to get a user by user id
@app.route('/user/<user_id>')
def get_one_user(user_id):
    cur = mysql.new_cursor(dictionary=True)
    cur.execute(
        "SELECT `name`, `email`, `role` from users \
        WHERE user_id = {} ;"
        .format(user_id))
    output = cur.fetchall()
    return jsonify(users=output)


# Api to create a new user
@app.route('/user/', methods=['POST'])
def create_user():
    user_data = request.json
    name = user_data['name']
    email = user_data['email']
    cur = mysql.new_cursor()
    cur.execute(
        "INSERT INTO users (`name`, `email`) \
        VALUES ('{}', '{}');"
        .format(name, email))
    mysql.connection.commit()
    return jsonify({'msg': 'User registered'})


# Api to confirm a user
@app.route('/user/confirm/<user_id>', methods=['PUT'])
def confirm_user(user_id):
    cur = mysql.new_cursor()
    cur.execute(
        "UPDATE users SET `confirm` = 1, \
        `last_updated` = NOW() WHERE user_id = {};"
        .format(user_id))
    mysql.connection.commit()
    return jsonify({'msg': 'User confirmed'})


# Api to cancel a user
@app.route('/user/cancel/<user_id>', methods=['PUT'])
def cancel_user(user_id):
    cur = mysql.new_cursor()
    cur.execute(
        "UPDATE users SET `confirm` = 0, \
        `last_updated` = '{}' \
        WHERE user_id = {}; "
        .format(user_id))
    mysql.connection.commit()
    return jsonify({'msg': 'User cancelled'})


# Api to delete a user
@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    cur = mysql.new_cursor()
    cur.execute(
        "DELETE FROM users \
        WHERE user_id = {};"
        .format(user_id))
    mysql.connection.commit()
    return jsonify({'msg': 'User deleted'})


# Api initializer
if __name__ == '__main__':
    app.run(debug=True)
