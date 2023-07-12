from flask import Blueprint
from flaskr.model_translation import translation

bp = Blueprint("translation", __name__, url_prefix="/")

@bp.route("translation/en-to-vi/<script>")
def index(script):
    result = translation(script)
    return result
