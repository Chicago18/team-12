"""
cma index (main) view.

URLs include:
/
"""
import arrow
import flask
import cma
from cma import model

@cma.app.route('/', methods=['POST', 'GET'])
def show_index():
    """Display / route."""
    if 'username' in flask.session:
        username = flask.session['username']
        cma_db = model.get_db()
        if flask.request.method == 'POST':
            if flask.request.form.get('like') == 'like':
                like_photo(insta_db.cursor(),
                           flask.request.form["postid"], username)
            if flask.request.form.get('unlike') == 'unlike':
                unlike_photo(insta_db.cursor(),
                             flask.request.form["postid"], username)
            if flask.request.form.get('comment') == 'comment':
                if not flask.request.form.get('text') == '':
                    add_comment(insta_db.cursor(),
                                username, flask.request.form)
        posts = get_posts(insta_db.cursor(), username)
        return flask.render_template("index.html", posts=posts,
                                     logname=username)

    return flask.render_template("index.html")
