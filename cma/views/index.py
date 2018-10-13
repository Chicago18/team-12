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
    return flask.render_template("index.html")
