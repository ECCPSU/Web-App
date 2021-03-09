from sqlalchemy.exc import SQLAlchemyError

def add_connection(db, table, id1, id2):
	connection_forward = table(id1=id1, id2=id2)
	connection_backward = table(id1=id2, id2=id1)
	try:
		db.session.add(connection_forward)
		db.session.add(connection_backward)
		db.session.commit()
	except SQLAlchemyError as e:
		error = str(e.__dict__['orig'])
		return error

def get_team(TeamTable, UserTable, user_id) -> dict:
	connections = TeamTable.query.filter_by(id1=user_id).all()
	team = []
	for conn in connections:
		teammate_id = conn.id2
		teammate = UserTable.query.filter_by(id=teammate_id).first()
		teammate_data = {"name": teammate.name, "email": teammate.email}
		team.append(teammate_data)
	return team