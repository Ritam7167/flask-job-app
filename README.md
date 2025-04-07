# 🧳 Job Portal Web Application

A full-featured Job Portal built using Flask, where users can register as **Job Seekers**, **Employers**, or an **Admin**. Job Seekers can search and apply for jobs, Employers can post and manage listings, and the Admin can manage users, jobs, and applications through a dedicated dashboard.

---

## 🔧 Features

- 🔐 User Authentication (Login/Signup)
- 👷‍♂️ Employers can post, update, and delete job listings
- 🔍 Job Seekers can search jobs and apply (no resume upload required)
- 📁 My Applications page for Job Seekers
- 🧾 Manage Listings page for Employers
- 🛠️ Admin Dashboard with full CRUD:
  - Manage Users
  - Manage Jobs
  - Manage Applications
- 🧹 Cascade delete: Deleting a user/job also deletes related applications
- 📂 Job Category support with filters

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask, SQLAlchemy ORM
- **Frontend**: HTML, CSS, JS, Bootstrap
- **Database**: SQLite

---

### Install the Required Dependencies
```bash
pip install -r requirements.txt
```

---

## 📁 Project Structure

flask_job-app/ │ ├── app.py # Main application script │ ├── database/ │ ├── db.py # Configure and initialize the database │ └── models.py # SQLAlchemy models with relationships │ ├── templates/ # HTML templates (Jinja2 for Flask) │ ├── screenshots/ # Screenshots used in README │ ├── requirements.txt # List of Python dependencies └── README.md # Project documentation

---

## 📁 Templates

All HTML templates are located in the `templates/` directory and rendered using **Jinja2**. Includes pages like:

- Home  
- Job Listings  
- Login/Register  
- Employer Dashboard  
- Admin Dashboard  
- My Applications  

## 👥 User Roles

### 🔹 Job Seeker
- Search and filter job listings  
- Apply for jobs (no resume required)  
- View **My Applications** page  

### 🔸 Employer
- Post new jobs  
- Manage listings (edit/delete)  
- View applications to their jobs  

### 🛡️ Admin
- Manage all users, jobs, and applications  
- Delete users (with cascade effect)  
- Full access to data and admin dashboard  

---

## 🗃️ Database Relationships

- **User** ↔ **Job**  
- **Job** ↔ **Application**  
- **User** ↔ **Application**  

> SQLAlchemy ORM handles relationships and **cascade delete** functionality.

---

## 📸 Screenshots

### 🏠 Homepage
![Homepage](screenshots/home.png)

---

### 🔐 Authentication
![Register](screenshots/register.png)
![Login](screenshots/login.png)

---

### 👤 Job Seeker View
![JobSeeker_Homepage](screenshots/jobSeeker_home.png)
![Apply_Job](screenshots/apply_job.png)
![My_Applications](screenshots/my_applications.png)

---

### 🧑‍💼 Employer View
![Post_Job](screenshots/post_job.png)
![Manage_Job_Listings](screenshots/manage_job_listings.png)
![Manage_Job](screenshots/edit_job.png)
![View_Job_Applications](screenshots/view_job_applications.png)

---

### 🛡️ Admin Panel
![Admin_Users_Lists](screenshots/admin_users.png)
![Admin_Edit_Users](screenshots/admin_edit_users.png)
![Admin_Job_Lists](screenshots/admin_jobs.png)
![Admin_Edit_Jobs](screenshots/admin_edit_jobs.png)
![Admin_Applications_Lists](screenshots/admin_applications.png)
![Admin_Edit_Applications](screenshots/admin_edit_applications.png)
