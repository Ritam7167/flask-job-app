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
![home](https://github.com/user-attachments/assets/9b56fdaf-14b9-4417-bfbe-c27d5fcab5f9)


---

### 🔐 Authentication
![register](https://github.com/user-attachments/assets/621cfb6a-83a4-4fe9-9e56-263b4ed341a6)

![login](https://github.com/user-attachments/assets/4f4cb0f4-5c3d-46ca-b7be-e8ccfbdc9739)



---

### 👤 Job Seeker View
![jobSeeker_home](https://github.com/user-attachments/assets/8eca911d-d27d-46a3-82cd-891ef5aa608f)

![apply_job](https://github.com/user-attachments/assets/95e428b1-e2cb-4522-882a-5a001e2cac7b)

![my_applications](https://github.com/user-attachments/assets/b5c530d5-1ff8-4082-b5e2-9ef04917b656)


---

### 🧑‍💼 Employer View
![post_job](https://github.com/user-attachments/assets/6be14b7e-8728-4bac-b982-d488f5b90115)

![manage_job_listings](https://github.com/user-attachments/assets/0b5f08ca-9182-4b60-8341-4feb9461b998)

![edit_job](https://github.com/user-attachments/assets/8b22221d-417c-4f92-b6bd-8bff4dac2a44)

![view_applications](https://github.com/user-attachments/assets/da82a71d-d476-4ea3-80ba-33b02c764f30)


---

### 🛡️ Admin Panel
![admin_users](https://github.com/user-attachments/assets/9547cbf4-ab6d-4e4a-b288-cc8d3738a55e)

![admin_edit_users](https://github.com/user-attachments/assets/f1c1fd4f-6726-4a4e-905f-4621c69d2391)

![admin_jobs](https://github.com/user-attachments/assets/b2d84cb8-fd78-4c42-a99c-a3288bfe0794)

![admin_edit_jobs](https://github.com/user-attachments/assets/21e13f54-90bd-403f-94af-71be1e86b3bb)

![admin_applications](https://github.com/user-attachments/assets/e567d210-f6d0-42d3-a709-aeefc962e191)

![admin_edit_applications](https://github.com/user-attachments/assets/77d32846-9c84-4fad-aab9-2efa1e2c8a18)



