
import arrow
import flask
import cma
from cma import model

def get_parent_info(username):
	cursor = model.get_db()
	parent_info = cursor.execute('''SELECT * FROM parent WEHRE username=?''', (username, )).fetchall()
