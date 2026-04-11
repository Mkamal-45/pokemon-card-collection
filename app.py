from flask import Flask
from views import views_blueprint
import os

def create_app():
    app = Flask(__name__)
    app.secret_key = os.urandom(24)
    app.register_blueprint(views_blueprint)
    return app

if __name__ == '__main__':
    my_app = create_app()
    my_app.run(debug=True)
