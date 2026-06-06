# Health Prediction Application
# Project Links
* GitHub Repository: https://github.com/mahalakshmi-dotcom/AI-health-prediction-app
* Live Application: https://ai-health-prediction-app.onrender.com
# Project Description
* Health Prediction Application is a web-based application built using Python and Flask. This application helps users manage health records and predicts health risks based on blood test values.
* The application allows users to add, view, update and delete patient records. It stores data in a SQLite database. The Health Prediction Application uses and API to provide health risk predictions.
# Features
## Patient Management
  * Add records.
  * View patient records.
  * Update patient information.
  * Delete patient records.
  * Search patient records.
## Health Prediction
  * Generate health remarks based on blood test values like Glucose, Haemoglobin and Cholestrol.
  * Integrate with an API.
  * Have a prediction mechanism when API is down.
## Reports
  * View total patient records.
  * View High Risk patient count.
  * View Moderate Risk patient count.
  * View Low Risk patient count.
## Validation
  * Check for required fields.
  * validate email addresses
  * Validate test values
  * Validate dates
## Patient Information
-->The Health Prediction Application stores these details:
  * Full Name
  * Email Address
  * Glucose Level
  * Haemoglobin Level
  * Cholesterol Level
  * Health Remarks
# Technologies Used
 ## Backend
  * Python
  * Flask
  * Flask-SQLAlchemy
 ## Frontend
  * HTML
  * CSS
  * Bootstrap
  * JavaScript
 ## Database
  * SQLite
# API Integration
* Hugging Face Interface API
# Project Structure
```
health-prediction-app/
|
|--app.py
|--view_db.py
|--requirements.txt
|--README.md
|--templates/
|  |--index.html
|  |--add_patient.html
|  |--edit_patient.html
|  |--reports.html
|  |--privacy.html
|--static/
|  |--css/
|  |  |--style.css
|  |
|  |--js/
|  |  |--script.js
|  |
|  |--images/
|  |  |--banner.jpg
|  |  |--logo.jpg
|
```
# Installation
## Install Dependencies
-->To install dependencies run this command:
* bash
```pip install -r requirements.txt```
# Configure Environment Variables
-->Create a.env file. Add these lines:
  * HF_API_KEY=your_api_key
  * SECRET_KEY=your_secret_key
# Run Application
-->To run the application use this command:
* bash
```python app.py```
# Open in Browser for Localhost
http://127.0.0.1:5000 in your browser.
# Learning Outcomes
Building the Health Prediction Application was an experience. I learned about building web applications using Flask. I worked with SQLite databases. Implemented add, view, update and delete operations. I integrated APIs. Performed form validation. I created web pages. Managed data for the Health Prediction Application.
# Future Enhancements
   * We can take print of the reports.
   * Track the patient history.
   * We can able to send reports through email to the particular patient.
   * Enhancement of health analytics, for the Health Prediction Application.
# Developed By
Mahalakshmi Setti,
sivamahalakshmisetti@gmail.com.


B.Tech.
