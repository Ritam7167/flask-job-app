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
<img width="1920" height="1080" alt="home" src="https://github.com/user-attachments/assets/c1ed45c2-e6fc-406b-8de2-05b4ecc15e96" />


---

### 🔐 Authentication
<img width="1920" height="1080" alt="register" src="https://github.com/user-attachments/assets/f1f7a132-a008-42aa-8ab4-79bd77250540" />
<img width="1920" height="1080" alt="login" src="https://github.com/user-attachments/assets/f02fa39f-5546-4a95-8f52-8bf221f872df" />


---

### 👤 Job Seeker View
<img width="1920" height="1080" alt="jobSeeker_home" src="https://github.com/user-attachments/assets/f1698884-6813-4825-ad5b-2705788ea481" />
<img width="1920" height="1080" alt="apply_job" src="https://github.com/user-attachments/assets/622a5766-b1c0-443d-895c-d638b0a93149" />
<img width="1920" height="1080" alt="my_applications" src="https://github.com/user-attachments/assets/69bfc3cf-e1e7-46df-983e-a289cfb4d480" />


---

### 🧑‍💼 Employer View
<img width="1920" height="1080" alt="post_job" src="https://github.com/user-attachments/assets/df6a588b-fd13-40f3-b602-d4e14ace1725" />
<img width="1920" height="1080" alt="manage_job_listings" src="https://github.com/user-attachments/assets/47e100f9-7746-43c9-9a8b-952d567c39d2" />
<img width="1920" height="1080" alt="edit_job" src="https://github.com/user-attachments/assets/205a9e1b-5280-437c-9196-fa9950bc2713" />
<img width="1920" height="1080" alt="view_applications" src="https://github.com/user-attachments/assets/538e05ad-c069-45f5-b1ab-c198ba5badea" />


---

### 🛡️ Admin Panel
<img width="1920" height="1080" alt="admin_users" src="https://github.com/user-attachments/assets/4a412e94-c49d-4393-b3c0-d21a51f66a30" />
<img width="1920" height="1080" alt="admin_edit_users" src="https://github.com/user-attachments/assets/fb7cbccf-660b-42c8-a983-cf3b21a63ef1" />
<img width="1920" height="1080" alt="admin_jobs" src="https://github.com/user-attachments/assets/94c79d03-ae48-447e-bc19-c6bf8c39bbe0" />
<img width="1920" height="1080" alt="admin_edit_jobs" src="https://github.com/user-attachments/assets/b02c524e-1138-4b34-91b2-4eb7e722687b" />
<img width="1920" height="1080" alt="admin_applications" src="https://github.com/user-attachments/assets/e4f887c4-b5f9-464c-b0b5-59533f674057" />
<img width="1920" height="1080" alt="admin_edit_applications" src="https://github.com/user-attachments/assets/c162035d-2117-4377-a954-0d0ec8bd99b1" />

