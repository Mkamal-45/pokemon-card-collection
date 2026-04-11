from flask import Blueprint

views_blueprint = Blueprint('views', __name__)

@views_blueprint.route('/')
def home():
    return "<h1>Welcome to my Pokémon Card Collection</h1>"