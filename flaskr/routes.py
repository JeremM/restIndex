from flask import Blueprint

count = Blueprint('count', __name__)

api_prefix = "/1/queries/"

@count.route(f"{api_prefix}/count")
def countA():
    return "ok count"
