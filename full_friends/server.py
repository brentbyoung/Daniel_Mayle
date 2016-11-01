from flask import Flask, render_template, request, redirect
from mysqlconnection import MySQLConnector
app = Flask(__name__)
db = MySQLConnector(app, 'friends_db')
app.secret_key = "ThisIsSecret!"

# ROUTING
@app.route('/')
def index():
    query = "SELECT * FROM friends"
    data = {}
    friends = db.query_db(query, data)
    return render_template('index.html', friends=friends)

@app.route('/friends', methods=["POST"])
def create():
    query = "INSERT INTO friends (first_name, last_name, email, created_at) VALUES (:first_name, :last_name, :email, NOW())"
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email']
    }
    db.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>', methods=["POST"])
def update(id):
    query = "UPDATE friends SET first_name=:first_name, last_name = :last_name, email=:email WHERE id = :id"
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'id' : id
    }
    db.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>/edit', methods=["GET"])
def edit(id):
    query = "SELECT * FROM friends WHERE id = :id"
    data = {
        'id': id
    }
    friend = db.query_db(query, data)[0]
    return render_template('edit.html', friend=friend )

@app.route('/friends/<id>/delete', methods=["POST"])
def delete(id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {
        'id' : id
    }
    db.query_db(query, data)
    return redirect('/')

app.run(debug=True)

