from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///job_portal.db'
    app.config['SECRET_KEY'] = 'your_secret_key'
    
    db.init_app(app)
    with app.app_context():
        db.create_all()
        
        