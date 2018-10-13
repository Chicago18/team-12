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

@cma.app.route('/p/<username>/', methods=['POST', 'GET'])
def show_parent_portal(username):
    if 'username' not in flask.session:
        return flask.redirect(flask.url_for('show_login_page'))
    cma_db = model.get_db()
    logname = flask.session["username"]

    return flask.render_template("parent.html", logname=logname)
