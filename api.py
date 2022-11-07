from flask import Flask, jsonify, request, json
from flask_mysql_connector import MySQL
import time


# Flask initializer
app = Flask(__name__)

# MySQL Config
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3307
app.config['MYSQL_DATABASE'] = 'aniversario'
mysql = MySQL(app)


# Api test
@app.route('/', methods=['GET'])
def hello():
    return 'ESTAMOS NO BRASIL!'


# Api to get all users
@app.route('/user', methods=['GET'])
def get_all_users():
    cur = mysql.new_cursor(dictionary=True)
    cur.execute('select name, email, role from aniversario.usuarios;')
    output = cur.fetchall()
    return jsonify(output)


# Api to get a user by user id
@app.route('/user/<user_id>', methods=['GET'])
def get_one_user(user_id):
    cur = mysql.new_cursor(dictionary=True)
    cur.execute(
        'SELECT name, email, role from aniversario.usuarios WHERE user_id = %s ;', user_id)
    output = cur.fetchall()
    return jsonify(output)


# Api to create a new user
@app.route('/user/', methods=['POST'])
def create_user():
    timeData = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    userData = request.json
    name = userData['Name']
    email = userData['Email']
    cur = mysql.new_cursor()
    cur.execute(
        '''INSERT INTO aniversario.usuarios (`Name`,`Email`, `Signup_date`, `Last_updated`) 
        VALUES ( \'{}\', \'{}\', \'{}\', \'{}\' );'''.format(name, email, timeData, timeData))
    mysql.connection.commit()
    return jsonify({'msg': 'User registered'})


# Api to confirm a user
@ app.route('/user/confirm/<user_id>', methods=['PUT'])
def confirm_user(user_id):
    timeData = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    cur = mysql.new_cursor()
    cur.execute(
        '''UPDATE aniversario.usuarios SET `Confirm` = 1, 
        `Last_updated` = \'{}\' WHERE user_id = {};'''.format(timeData, user_id))
    mysql.connection.commit()
    return jsonify({'msg': 'User confirmed'})


# Api to cancel a user
@ app.route('/user/cancel/<user_id>', methods=['PUT'])
def cancel_user(user_id):
    timeData = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    cur = mysql.new_cursor()
    cur.execute(
        '''UPDATE aniversario.usuarios SET `Confirm` = 1, 
        `Last_updated` = \'{}\' WHERE user_id = {};'''.format(timeData, user_id))
    mysql.connection.commit()
    return jsonify({'msg': 'User cancelled'})


# Api to delete a user
@ app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    cur = mysql.new_cursor()
    cur.execute(
        '''DELETE FROM aniversario.usuarios WHERE user_id = {};'''.format(user_id))
    mysql.connection.commit()
    return jsonify({'msg': 'User cancelled'})


# Api initializer
if __name__ == '__main__':
    app.run(debug=True)
