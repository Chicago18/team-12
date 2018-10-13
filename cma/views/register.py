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

    x = cursor.execute('''SELECT * FROM user''').fetchall()
    print(x)

@cma.app.route('/register/', methods=['POST', 'GET'])
def show_register():
    """Display /account/create route."""
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
        return flask.redirect(flask.url_for('show_login'))

    return flask.render_template("register.html")
