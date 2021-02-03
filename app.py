from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(40), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    major = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)

class Participants(db.Model):
    __tablename__ = 'Participants'
    id = db.Column(db.Integer, db.ForeignKey('Users.id'), primary_key=True)
    is_partic = db.Column(db.Boolean, default=False)


@app.route('/')
def visit(info=None):
	return render_template('login.html', return_info=info)

@app.route('/login/', methods=['POST', 'GET'])
def login_form():
    users = {"eccpsu_admin": 'password'} #username: password


    username = request.form.get('username', False)
    password = request.form.get('password', False)
    print(username, password)

    first_time = username is False or password is False

    if not first_time:
        if username not in users:
            return render_template('login.html', return_info='Username not found')
        elif users[username] != password:
            return render_template('login.html', return_info='Incorrect password')
        else:
            return redirect(url_for('main', name=username))
    else:
        return render_template('login.html')

@app.route('/newaccount/', methods=['POST', 'GET'])
def new_account():
	return render_template('new_account.html')

@app.route('/welcome/')
def main(name=None):
	return render_template('index.html', name=name)

@app.route('/team/')
def view_team(team=None):
    team = [{'name': 'John', 'email': 'john@gmail.com'}, {'name': 'Max', 'email': 'max@gmail.com'}, {'name': 'Julia', 'email': 'julia@gmail.com'}, {'name': 'Julia', 'email': 'julia@gmail.com'}, {'name': 'Julia', 'email': 'julia@gmail.com'}]
    return render_template('team.html', team=team)

if __name__ == '__main__':
	app.run(debug=True)
