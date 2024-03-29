"""
cma index (main) view.

URLs include:
/
"""
import arrow
import flask
import cma
from cma import model

def add_account(cursor, firstname, lastname, username, password, acc_type):
    """Add account into DB."""
    cursor.execute('''
        INSERT INTO user(username, firstname, lastname, password, type)
        VALUES(?,?,?,?,?)''', (username, firstname, lastname, password, acc_type))


@cma.app.route('/p/<username>/<childname>/create_student_account/', methods=['POST', 'GET'])
def show_student_register(username, childname):
    """Display /account/create route."""
    if flask.request.method == 'POST':
        firstname = flask.request.form.get('firstname', False)
        middleinitial = flask.request.form.get('middleinitial', False)
        lastname = flask.request.form.get('lastname', False)
        #username = flask.request.form.get('username', False)
        password = flask.request.form.get('password', False)

        cma_db = model.get_db()

        flask.session['username'] = username
        return flask.redirect(flask.url_for('show_student_selection'), username=username)

    return flask.render_template("student_register.html", username=username, childname=childname)
