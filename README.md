# MIRA AI Health Prediction Application

## Project Description

This project was developed as part of the Junior AI/ML Developer technical assessment.

The application is designed to store the patient blood test information and generate AI-based health remarks using an external health prediction API. It provides a simple interface for managing patient records and viewing health risk predictions.

The system allows users to add, view, update, and delete patient information while storing the data in a database for the future access.

---

## Features

### Patient Management

* Add new patient records
* View patient records
* Update patient information
* Delete patient records
* Search patients by name

### User Authentication

* Admin registration
* Admin login
* Secure password storage
* Session-based access control

### Health Prediction

* AI-generated health remarks
* External API integration
* Automatic risk assessment based on blood test values
* Backup prediction logic when API service is unavailable

### Reports Dashboard

* View patient statistics
* High Risk patient count
* Moderate Risk patient count
* Low Risk patient count

### Validation

* Required field validation
* Email format validation
* Numeric validation for blood test values
* Date validation

---

## Patient Information

The application stores the following details:

* Full Name
* Date of Birth
* Email Address
* Phone Number
* Glucose Level
* Haemoglobin Level
* Cholesterol Level
* AI Generated Remarks

---

## Technologies Used

### Backend

* Python
* Flask
* Flask-SQLAlchemy

### Frontend

* HTML
* CSS
* Bootstrap
* JavaScript

### Database

* SQLite

### API Integration

* Hugging Face Inference API

---

## Project Structure

health-prediction-app/
│
├── app.py
├── requirements.txt
├── README.md
├── view_db.py
│
├── templates/
│   ├── index.html
│   ├── add_patient.html
│   ├── edit_patient.html
│   ├── login.html
│   ├── signup.html
│   ├── reports.html
│   └── privacy.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── script.js
│   │
│   └── images/
│       └── banner.jpg
│
└── instance/
    └── patients.db


---

## Installation

### 1. Install Dependencies
pip install -r requirements.txt

### 2. Create Environment Variables
Create a .env file and add:

HF_API_KEY=your_api_key
SECRET_KEY=your_secret_key


### 3. Run the Application

python app.py


### 4. Open in Browser

text
http://127.0.0.1:5000


---

## What I Learned

While developing this project, I gained practical experience in:

* Building the web applications using Flask
* Working with SQLite databases
* Implementing CRUD operations
* Integrating external APIs
* Handling user authentication
* Validating user input
* Creating responsive web pages
* Working with the AI-powered services

---

## Future Improvements

* PDF report generation
* Email notifications
* Patient history tracking
* Advanced health analytics
* Cloud database integration

---

## Developed By

Mahalakshmi Setti

B.Tech
