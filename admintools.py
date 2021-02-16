from app import db
from app import Users

def add_admin():
	admin_user = {'name': 'admin', 'email': 'ecc.psu@gmail.com', 'password': 'eccpsu1718'}
	admin = Users(name=admin_user['name'], email=admin_user['email'], password=admin_user['password'])
	try:
		db.session.add(admin)
		db.session.commit()
	except SQLAlchemyError as e:
		error = str(e.__dict__['orig'])
		return error