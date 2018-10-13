"""
cma index (main) view.

URLs include:
/
"""
import arrow
import flask
import cma
from cma import model

def get_account_type (cursor, username):
    account = cursor.execute('''SELECT * FROM user WHERE username=?''', (username,)).fetchall()
    return account[0]

@cma.app.route('/login/', methods=['POST', 'GET'])
def show_login():
    """Display / route."""
    if flask.request.method == 'POST':
        username = flask.request.form.get('username', False)
        password = flask.request.form.get('password', False)

        cma_db = model.get_db()
        flask.session['username'] = username
        account = get_account_type(cma_db, username)
        if account["type"] == "p":
            return flask.redirect(flask.url_for('show_student_selection', username=username))

        if account["type"] == "s":
            return flask.redirect(flask.url_for('show_student_portal', username=username))

        if account["type"] == "a":
            return flask.redirect(flask.url_for('show_student_portal', username=username))


    return flask.render_template("login.html")

