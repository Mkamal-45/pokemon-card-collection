from flask import Blueprint, render_template, session

views_blueprint = Blueprint('views', __name__)

@views_blueprint.route('/')
def home():
    return render_template('home.html')

@views_blueprint.route('/collection')
def collection():
    return render_template('collection.html')