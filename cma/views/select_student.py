"""
cma index (main) view.

URLs include:
/
"""
import arrow
import flask
import cma
from cma import model

def get_children(cursor, username):
    children = cursor.execute('''SELECT * FROM student WHERE parentid=?''', (username, )).fetchall()
    return children
    

@cma.app.route('/p/<username>/select_student/', methods=['POST', 'GET'])
def show_student_selection(username):
    """Displayroute."""
    cma_db = model.get_db()
    children = get_children(cma_db, username)

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
        return flask.redirect(flask.url_for('show_parent_portal'), username=username, children=children)

    return flask.render_template("student_selection.html", username=username, children=children)
