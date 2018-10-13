"""
cma index (main) view.

URLs include:
/
"""
import arrow
import flask
import cma
from cma import model

@cma.app.route('/a/<username>/managestudent/', methods=['POST', 'GET'])
def show_admin_selection(username):
    if 'username' not in flask.session:
        return flask.redirect(flask.url_for('show_login_page'))


    cma_db = model.get_db()
    logname = flask.session["username"]

    student_firstname = flask.request.form.get('firstname', False)
    student_lastname = flask.request.form.get('lastname', False)

    return flask.render_template("admin_student.html", logname=username, firstname=student_firstname, lastname=student_lastname)