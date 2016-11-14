from flask import Flask, render_template, request, redirect, jsonify

# import the Connector function

from mysqlconnection import MySQLConnector

app = Flask(__name__, template_folder="templates")

# connect and store the connection in "mysql" note that you pass the database name to the function

mysql = MySQLConnector(app, 'notes')

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/notes/create', methods=["POST"])
def create():
	query = "INSERT INTO notes (title, created_at, updated_at) VALUES (:title, NOW(), NOW())"
	
	data = {
		"title": request.form['title']
	}
	mysql.query_db(query, data)
	return redirect ('/notes')


@app.route('/notes')
def all_notes():
	query = "SELECT * FROM notes"
	notes = mysql.query_db(query)
	return render_template('partials/notes.html', notes=notes)


@app.route('/notes/<id>/destroy', methods=["POST"])
def destroy_note(id):
	query= "DELETE FROM notes WHERE id = :id"
	data = {'id':id}
	mysql.query_db(query, data)
	return redirect ('/notes')

# @app.route('/notes/<id>/update', methods=["POST"])
# def update_note():
# 	query= "UPDATE notes SET description = :description WHERE id = :id"
# 	data= {
# 		"description": request.form['description'], "id":id
# 	}
# 	mysql.query_db(query, data)
# 	return jsonify({"status": True})
app.run(debug=True)