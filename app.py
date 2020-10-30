from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

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

@app.route('/welcome/')
def main(name=None):
	return render_template('index.html', name=name)

if __name__ == '__main__':
	app.run(debug=False)
