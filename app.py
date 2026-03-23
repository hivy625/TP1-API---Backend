from flask import Flask
import os
from extensions import db
def create_app():
    #Creation de l'application
    app = Flask(__name__)
    #Creation du chemin vers la base de donnee
    DB_URL = os.path.abspath(os.path.dirname(__file__))

    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///'+os.path.join(DB_URL,'blog.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from routes import articles_bp
    app.register_blueprint(articles_bp)

    return app

#Lancement de l'appli

if __name__=='__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)