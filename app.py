from database.db import db, init_db
from database.models import User, Job, Application

from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

from datetime import datetime

app = Flask(__name__)
init_db(app)

# Home Page
@app.route('/')
@app.route('/home')
def home():
    jobs = Job.query.all()
    employer_jobs = Job.query.filter_by(employer_id=session.get('user_id')).all() if 'user_id' in session and session['role'] == 'employer' else []

    # Hide jobs from job seekers if they have already applied
    if 'user_id' in session and session['role'] == 'job_seeker':
        applied_job_ids = [app.job_id for app in Application.query.filter_by(user_id=session['user_id']).all()]
        jobs = [job for job in jobs if job.id not in applied_job_ids]

    return render_template('index.html', jobs=jobs, employer_jobs=employer_jobs)


# User Registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        role = request.form['role']
        user = User(username=username, password=password, role=role)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

# User Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            session['role'] = user.role

            # Redirect based on role
            if user.role == 'admin':
                return redirect(url_for('admin_manage_users'))
            elif user.role == 'employer':
                return redirect(url_for('manage_listings'))
            else:
                return redirect(url_for('home'))

    return render_template('login.html')


# Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

# Post a Job
@app.route('/post_job', methods=['GET', 'POST'])
def post_job():
    if 'user_id' not in session or session['role'] != 'employer':
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        job = Job(
            title=request.form['title'],
            description=request.form['description'],
            salary=request.form['salary'],
            location=request.form['location'],
            company=request.form['company'],
            employer_id=session['user_id'],
            category=request.form['category']
            
        )
        db.session.add(job)
        db.session.commit()
        
        # Redirect to manage_listings after posting a job
        return redirect(url_for('manage_listings'))

    return render_template('post_job.html')


# Apply for a Job
@app.route('/apply/<int:job_id>', methods=['GET', 'POST'])
def apply(job_id):
    if 'user_id' not in session or session['role'] != 'job_seeker':
        return redirect(url_for('login'))

    job = Job.query.get_or_404(job_id)

    if request.method == 'POST':
        name = request.form['name']
        contact = request.form['contact']
        email = request.form['email']
        location = request.form['location']
        skills = request.form['skills']
        experience = request.form['experience']

        existing_application = Application.query.filter_by(job_id=job_id, user_id=session['user_id']).first()
        if not existing_application:
            new_application = Application(
                job_id=job_id, user_id=session['user_id'],
                name=name, contact=contact, email=email,
                location=location, skills=skills, experience=experience
            )
            db.session.add(new_application)
            db.session.commit()

        return redirect(url_for('my_applications'))

    return render_template('apply.html', job=job)

# View My Applications
@app.route('/my_applications')
def my_applications():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']
    applications = Application.query.filter_by(user_id=user_id).all()

    return render_template('my_applications.html', applications=applications)

# Withdraw Application
@app.route('/withdraw_application/<int:application_id>', methods=['POST'])
def withdraw_application(application_id):
    application = Application.query.get_or_404(application_id)
    
    if application.user_id == session['user_id']:
        db.session.delete(application)
        db.session.commit()

    return redirect(url_for('my_applications'))

# Manage Listings for Employers
@app.route('/manage_listings')
def manage_listings():
    if 'user_id' not in session or session['role'] != 'employer':
        return redirect(url_for('login'))
    
    employer_jobs = Job.query.filter_by(employer_id=session['user_id']).all()
    return render_template('manage_listings.html', jobs=employer_jobs)

# Manage Specific Job
@app.route('/manage_job/<int:job_id>', methods=['GET', 'POST'])
def manage_job(job_id):
    if 'user_id' not in session or session['role'] != 'employer':
        return redirect(url_for('login'))
    
    job = Job.query.get_or_404(job_id)
    
    if job.employer_id != session['user_id']:
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        job.title = request.form['title']
        job.description = request.form['description']
        job.salary = request.form['salary']
        job.location = request.form['location']
        job.category = request.form['category']
        job.company = request.form['company']
        db.session.commit()
        return redirect(url_for('manage_listings'))
    
    return render_template('manage_job.html', job=job)

# Delete Job Listing
@app.route('/delete_job/<int:job_id>', methods=['POST'])
def delete_job(job_id):
    job = Job.query.get_or_404(job_id)
    if job.employer_id == session['user_id']:
        db.session.delete(job)
        db.session.commit()
    return redirect(url_for('manage_listings'))

#Employee view application for review
@app.route('/view_job_applications/<int:job_id>')
def view_job_applications(job_id):
    if 'user_id' not in session or session['role'] != 'employer':
        return redirect(url_for('login'))

    job = Job.query.get_or_404(job_id)
    if job.employer_id != session['user_id']:
        return redirect(url_for('home'))

    applications = Application.query.filter_by(job_id=job_id).all()
    return render_template('view_job_applications.html', job=job, applications=applications)

#Employee update applications status
@app.route('/update_application_status/<int:application_id>', methods=['POST'])
def update_application_status(application_id):
    if 'user_id' not in session or session['role'] != 'employer':
        return redirect(url_for('login'))

    application = Application.query.get_or_404(application_id)

    if application.job.employer_id != session['user_id']:
        return redirect(url_for('home'))

    new_status = request.form['status']
    application.status = new_status
    db.session.commit()

    return redirect(url_for('view_job_applications', job_id=application.job_id))

#Admin work
@app.route('/admin_manage_users')
def admin_manage_users():
    if 'user_id' not in session or session['role'] != 'admin':
        return redirect(url_for('login'))
    users = User.query.all()
    return render_template('admin_manage_users.html', users=users)

@app.route('/admin_manage_jobs')
def admin_manage_jobs():
    if 'user_id' not in session or session['role'] != 'admin':
        return redirect(url_for('login'))
    jobs = Job.query.all()
    return render_template('admin_manage_jobs.html', jobs=jobs)

@app.route('/admin_manage_applications')
def admin_manage_applications():
    if 'user_id' not in session or session['role'] != 'admin':
        return redirect(url_for('login'))
    applications = Application.query.all()
    return render_template('admin_manage_applications.html', applications=applications)

@app.route('/admin/delete_user/<int:user_id>', methods=['POST'])
def admin_delete_user(user_id):
    if 'role' not in session or session['role'] != 'admin':
        return redirect(url_for('login'))

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('admin_manage_users'))


@app.route('/admin/delete_job/<int:job_id>', methods=['POST'])
def admin_delete_job(job_id):
    if 'user_id' not in session or session['role'] != 'admin':
        return redirect(url_for('login'))

    job = Job.query.get_or_404(job_id)
    db.session.delete(job)
    db.session.commit()
    return redirect(url_for('admin_manage_jobs'))


@app.route('/admin/delete_application/<int:application_id>', methods=['POST'])
def admin_delete_application(application_id):
    if 'user_id' not in session or session['role'] != 'admin':
        return redirect(url_for('login'))

    application = Application.query.get_or_404(application_id)
    db.session.delete(application)
    db.session.commit()
    return redirect(url_for('admin_manage_applications'))

# Admin Edit User
@app.route('/admin/edit_user/<int:user_id>', methods=['GET', 'POST'])
def admin_edit_user(user_id):
    if 'role' not in session or session['role'] != 'admin':
        return redirect(url_for('login'))

    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        user.username = request.form['username']
        user.role = request.form['role']
        db.session.commit()
        return redirect(url_for('admin_manage_users'))

    return render_template('admin_edit_user.html', user=user)

# Admin Edit Job
@app.route('/admin/edit_job/<int:job_id>', methods=['GET', 'POST'])
def admin_edit_job(job_id):
    if 'role' not in session or session['role'] != 'admin':
        return redirect(url_for('login'))

    job = Job.query.get_or_404(job_id)
    if request.method == 'POST':
        job.title = request.form['title']
        job.description = request.form['description']
        job.salary = request.form['salary']
        job.location = request.form['location']
        job.company = request.form['company']
        job.category = request.form['category']
        db.session.commit()
        return redirect(url_for('admin_manage_jobs'))

    return render_template('admin_edit_job.html', job=job)

# Admin Edit Application
@app.route('/admin/edit_application/<int:application_id>', methods=['GET', 'POST'])
def admin_edit_application(application_id):
    if 'role' not in session or session['role'] != 'admin':
        return redirect(url_for('login'))

    application = Application.query.get_or_404(application_id)
    if request.method == 'POST':
        application.name = request.form['name']
        application.email = request.form['email']
        application.contact = request.form['contact']
        application.location = request.form['location']
        application.skills = request.form['skills']
        application.experience = request.form['experience']
        application.status = request.form['status']
        db.session.commit()
        return redirect(url_for('admin_manage_applications'))

    return render_template('admin_edit_application.html', application=application)

@app.context_processor
def inject_year():
    return {'year': datetime.now().year}

if __name__ == '__main__':
    app.run(debug=True)
