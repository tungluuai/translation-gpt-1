from flask import Blueprint,render_template

bp = Blueprint("home", __name__, url_prefix="/")

@bp.route("/")
def index():
    """Show all the posts, most recent first."""
    return render_template("home.html")

@bp.app_errorhandler(404)
def handle_404(err):
    return render_template("404.html")

# or, without the decorator