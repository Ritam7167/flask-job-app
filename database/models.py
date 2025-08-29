from .db import db

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'job_seeker', 'employer', 'admin'
    
    # When a User is deleted, all their Jobs are deleted (cascade)
    jobs = db.relationship('Job', backref='employer', cascade='all, delete-orphan', lazy=True)
    
    # When a User is deleted, all their Applications are deleted (cascade)
    applications = db.relationship('Application', backref='applicant', cascade='all, delete-orphan', lazy=True)

# Job Model
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    salary = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    
    # When a User (employer) is deleted, their Jobs are deleted (ondelete='CASCADE')
    employer_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=True)
    
    # When a Job is deleted, all its Applications are deleted (cascade)
    applications = db.relationship('Application', backref='job', cascade='all, delete-orphan', lazy=True)

# Application Model
class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    # When a Job is deleted, its Applications are deleted (ondelete='CASCADE')
    job_id = db.Column(db.Integer, db.ForeignKey('job.id', ondelete='CASCADE'), nullable=True)
    
    # When a User (applicant) is deleted, their Applications are deleted (ondelete='CASCADE')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=True)
    
    name = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100))
    skills = db.Column(db.String(255))
    experience = db.Column(db.String(50))
    status = db.Column(db.String(20), default="Pending")
