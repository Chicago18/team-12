"""
cma index (main) view.

URLs include:
/
"""
import arrow
import flask
import cma
from cma import model

def get_children(cursor, username)
    

def add_account(cursor, firstname, lastname, username, password, acc_type):
    """Add account into DB."""
    cursor.execute('''
        INSERT INTO user(username, firstname, lastname, password, type)
        VALUES(?,?,?,?,?)''', (username, firstname, lastname, password, acc_type))

    x = cursor.execute('''SELECT * FROM user''').fetchall()
    print(x)

@cma.app.route('/p/<username>/select_student/', methods=['POST', 'GET'])
def show_student_selection(username):
    """Displayroute."""
    cma_db = model.get_db()
    students = get_children(cma_db, username)

    if flask.request.method == 'POST':
        firstname = flask.request.form.get('firstname', False)
        lastname = flask.request.form.get('lastname', False)
        username = flask.request.form.get('username', False)
        password = flask.request.form.get('password', False)

        cma_db = model.get_db()
        add_account(cursor=cma_db.cursor(),
                        username=username, firstname=firstname, lastname=lastname,
                        password=password, acc_type="p")

        flask.session['username'] = username
        return flask.redirect(flask.url_for('show_parent_portal'))

    return flask.render_template("select_student.html")
