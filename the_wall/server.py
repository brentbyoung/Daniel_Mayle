from flask import Flask, render_template, request, flash, redirect, jsonify, session
import re
# import the Connector function
from mysqlconnection import MySQLConnector
# imports the Bcrypt module
from flask_bcrypt import Bcrypt
app = Flask(__name__, template_folder="templates")
# connect and store the connection in "mysql" note that you pass the database name to the function
EMAIL_REGEX = re.compile(r'^[\w\.+_-]+@[\w\._-]+\.[\w]*$')
app.secret_key = 'some_secret'
db = MySQLConnector(app, 'the_wall')
mysql = MySQLConnector(app, 'the_wall')
bcrypt = Bcrypt(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/wall')
def wall():
	return render_template('wall.html')
	

@app.route('/wall/create', methods=["POST"])
def create_message():
	query = "INSERT INTO messages (message, created_at, updated_at) VALUES (:message, NOW(), NOW())"
	data = {
		"message": request.form['message']
	}
	mysql.query_db(query, data)
	return redirect ('/wall')



@app.route('/login', methods=["POST"])
def login():
    potential_errors = validate_login(request.form)

    if len(potential_errors[0]) > 0:
        print_flash_messages(potential_errors)
        return redirect('/')

    return login_user_by_id(potential_errors[1])

@app.route('/register', methods=["POST"])
def register():
    potential_errors = validate_registration(request.form)

    if len(potential_errors) > 0:
        print_flash_messages(potential_errors)
        return redirect('/')

         # Create a hashed password
    password = bcrypt.generate_password_hash(request.form['password'])

     # Create a new user for the DB

    query = 'INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())'
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : password
    }
    new_user_id = db.query_db(query, data)

    return login_user_by_id(new_user_id)



# FUNCTIONS

def validate_registration(form_info):
    errors = []

    if len(form_info['first_name']) < 2 or len(form_info['last_name']) < 2:
        errors.append("First name/last name must be at least 2 characters...")
    if not EMAIL_REGEX.match(form_info['email']) or len(form_info['email']) < 1:
        errors.append("Must be a valid email...")
    if len(form_info['password']) < 8 or form_info['password'] != form_info['password_confirm']:
        errors.append("Passwords must match and not be blank")

    return errors

def validate_login(form_info):
    errors = []
    query = "SELECT id, password FROM users WHERE email = :email"
    data = { 'email': form_info['email']}
    potential_user = db.query_db(query, data)

    if len(potential_user) < 1:
        errors.append("Email not in system")
        return (errors, None)

    if not bcrypt.check_password_hash(potential_user[0]['password'], form_info['password']):
        errors.append("Email/password don't match")
        return (errors, None)

    return (errors, potential_user[0]['id'])

def print_flash_messages(message_list):
    for message in message_list:
        flash(message)

def login_user_by_id(id):
    query = "SELECT first_name, last_name, email FROM users WHERE id = :id"
    data = { 'id': id }
    user = db.query_db(query, data)[0]
    session['user'] = user
    return redirect('/wall')
app.run(debug=True)