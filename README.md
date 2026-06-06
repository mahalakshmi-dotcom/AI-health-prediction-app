# Health Prediction Application

## Project Links

GitHub Repository:
https://github.com/mahalakshmi-dotcom/AI-health-prediction-app
#Live Application:


## Project Description

Health Prediction Application is a web-based application built using Python and Flask. This application helps users manage health records and predicts health risks based on blood test values.

The application allows users to add, view, update and delete patient records. It stores data in a SQLite database. The Health Prediction Application uses an API to provide health risk predictions.

## Features

### Patient Management

* Add records

* View patient records

* Update patient information

* Delete patient records

* Search patient records

### Health Prediction

* Generate health remarks based on blood test values like Glucose, Haemoglobin and Cholesterol

* Integrate with an API

* Have a prediction mechanism when API is down

### Reports

* View total patient records

* View High Risk patient count

* View Moderate Risk patient count

* View Low Risk patient count

### Validation

* Check for required fields

* Validate email addresses

* Validate test values

* Validate dates

## Patient Information

The Health Prediction Application stores these details:

* Full Name

* Date of Birth

* Email Address

* Glucose Level

* Haemoglobin Level

* Cholesterol Level

* Health Remarks

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

## Project Structure


health-prediction-app/

│

├── app.py

├── requirements.txt

├── README.md

│

├── templates/

│   ├── index.html

│   ├── add_patient.html

│   ├── edit_patient.html

│   ├── reports.html

│   └── privacy.html

│   └── view_db.html

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


## Installation

### Install Dependencies

To install dependencies run this command:

bash

pip install -r requirements.txt

### Configure Environment Variables

Create a.env file. Add these lines:

HF_API_KEY=your_api_key

SECRET_KEY=your_secret_key


### Run Application

To run the application use this command:

bash

python app.py



### Open in Browser

http://127.0.0.1:5000 in your browser.

## Learning Outcomes

Building the Health Prediction Application was an experience. I learned about building web applications using Flask. I worked with SQLite databases. Implemented add, view, update and delete operations. I integrated APIs. Performed form validation. I created web pages. Managed data for the Health Prediction Application.

## Future Enhancements

Some ideas for enhancements are:

* Generate PDF reports for the Health Prediction Application

* Send email notifications for the Health Prediction Application

* Track patient history for the Health Prediction Application

* Enhance health analytics, for the Health Prediction Application

## Developed By

Mahalakshmi Setti,

B.Tech.
