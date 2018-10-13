"""
cma index (main) view.

URLs include:
/
"""
import arrow
import flask
import cma
from cma import model

@cma.app.route('/s/<username>/', methods=['POST', 'GET'])
def show_student_portal(username):
    if 'username' not in flask.session:
        return flask.redirect(flask.url_for('show_login_page'))
    cma_db = model.get_db()
    logname = flask.session["username"]

    return flask.render_template("student.html", logname=username)