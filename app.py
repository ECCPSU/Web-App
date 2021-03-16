from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError

import teamtools

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

#Hello Sameep!


#-------------------------------------------------------------------------
class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100))
    name = db.Column(db.String(40))
    password = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

class Participants(db.Model):
    __tablename__ = 'Participants'
    id = db.Column(db.Integer, db.ForeignKey('Users.id'), primary_key=True)
    is_partic = db.Column(db.Boolean, default=False)

class TeamConnection(db.Model):
    __tablename__ = 'TeamConnection'
    cid = db.Column(db.Integer, primary_key=True)
    id1 = db.Column(db.Integer, db.ForeignKey('Users.id'))
    id2 = db.Column(db.Integer, db.ForeignKey('Users.id'))

#--------------------------------------------------------------------------

@app.route('/')
def visit(info=None):
	#return render_template('login.html', return_info=info)
    return redirect('/login/')



@app.route('/login/', methods=['POST', 'GET'])
def login_form():
    username = request.form.get('username', False)
    password = request.form.get('password', False)

    user = Users.query.filter_by(name=username).first()

    first_time = username is False or password is False

    if not first_time:
        if user is None:
            return render_template('login.html', return_info='Username not found')
        elif user.password != password:
            return render_template('login.html', return_info='Incorrect password')
        else:
            return redirect(url_for('main', name=username))
    else:
        return render_template('login.html')



@app.route('/newaccount/', methods=['POST', 'GET'])
def new_account():
    if request.method == 'POST':
        name = request.form['username']
        email = request.form['email']
        password = request.form['password1']
        user = Users(name=name, email=email, password=password)
        try:
            db.session.add(user)
            db.session.commit()
            return redirect('/login/')
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            return error
    else:
        return render_template('new_account.html')



@app.route('/welcome/')
def main(name=None):
	return render_template('index.html', name=name)



@app.route('/team/')
def view_team(team=None):
    user_id = 1
    team = teamtools.get_team(TeamConnection, Users, user_id)
    return render_template('team.html', team=team)


#---------------------------------------------------------------------------


if __name__ == '__main__':
	app.run(debug=True)
