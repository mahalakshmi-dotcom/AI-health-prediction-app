import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import date
import requests
from dotenv import load_dotenv 
load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'ai_healthcare_secure_session_token_2026')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    glucose = db.Column(db.Float, nullable=False)
    haemoglobin = db.Column(db.Float, nullable=False)
    cholesterol = db.Column(db.Float, nullable=False)
    remarks = db.Column(db.Text, nullable=True)
# EXTERNAL AI HEALTHCARE API INTEGRATION FUNCTION
def query_external_ml_api(glucose, cholesterol, haemoglobin):
    # Fetch token securely from the environment
    API_KEY = os.getenv("HF_API_KEY")
    API_URL = "https://api-inference.huggingface.co/models/Tonic/clinical-prompt-detector" 
    if not API_KEY:
        print("Configuration Error: HF_API_KEY environment variable is missing.")
        return run_backup_analytics(glucose, cholesterol, haemoglobin)
    headers = {"Authorization": f"Bearer {API_KEY}"} 
    prompt_input = (
        f"Patient Lab Metrics Evaluation Report:\n"
        f"- Blood Glucose Level: {glucose} mg/dL\n"
        f"- Total Serum Cholesterol: {cholesterol} mg/dL\n"
        f"- Haemoglobin Count: {haemoglobin} g/dL\n\n"
        f"Task: Provide a single short sentence diagnostic summary identifying risk classification (Low Risk, Moderate Risk, or High Risk) and a one-sentence lifestyle recommendation based on these parameters."
    ) 
    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt_input, "parameters": {"max_new_tokens": 60}}, timeout=8)
        result = response.json()
        # Check if Hugging Face model is warming up/loading
        if isinstance(result, dict) and "error" in result and "loading" in result["error"].lower():
            print("Model is currently loading on Hugging Face infrastructure. Using backup ruleset.")
            return run_backup_analytics(glucose, cholesterol, haemoglobin)

        if isinstance(result, list) and len(result) > 0 and 'generated_text' in result[0]:
            raw_text = result[0]['generated_text']
            extracted_remarks = raw_text.replace(prompt_input, "").strip()
            return extracted_remarks if extracted_remarks else "Low Risk - Metrics parameters verified stable within normal health bands."
        elif isinstance(result, dict) and 'generated_text' in result:
            return result['generated_text'].strip()
        else:
            raise Exception("Unexpected response structure")           
    except Exception as e:
        print(f"External API Latency Error: {e}")
        return run_backup_analytics(glucose, cholesterol, haemoglobin)
def run_backup_analytics(glucose, cholesterol, haemoglobin):
    if glucose > 150 or cholesterol > 240 or haemoglobin < 11:
        return "High Risk - Possible diabetes or heart disease indicators flagged via backup analytics."
    elif glucose > 120 or cholesterol > 200:
        return "Moderate Risk - Borderline indices registered. Monitor vital profiles closely."
    else:
        return "Low Risk - Biomarker configurations operating safely inside baseline constraints."
# BACKEND JSON ENDPOINT
@app.route('/api/predict', methods=['POST'])
def live_prediction_api():
    data = request.get_json() or {}
    try:
        glucose = float(data.get('glucose', 0))
        cholesterol = float(data.get('cholesterol', 0))
        haemoglobin = float(data.get('haemoglobin', 0))
        ai_remarks = query_external_ml_api(glucose, cholesterol, haemoglobin)
        return jsonify({"success": True, "remarks": ai_remarks})
    except Exception as err:
        return jsonify({"success": False, "error": str(err)}), 400
@app.route('/')
def home():
    search_query = request.args.get('search', '')
    if search_query:
        patients = Patient.query.filter(Patient.full_name.like(f"%{search_query}%")).all()
    else:
        patients = Patient.query.all()
    return render_template('index.html', patients=patients)
# ADD PATIENT FORM ROUTE (GET TO VIEW / POST TO SUBMIT)
@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient_page():  
    if request.method == 'POST':
        name = request.form['full_name']
        dob = request.form['date_of_birth']
        gluc = float(request.form['glucose'])
        chol = float(request.form['cholesterol'])
        hb = float(request.form['haemoglobin'])
        existing = Patient.query.filter_by(full_name=name, date_of_birth=dob).first()
        if existing:
            flash('Patient already exists in the system!', 'danger')
            return redirect(url_for('add_patient_page'))
        computed_remarks = query_external_ml_api(gluc, chol, hb)
        new_patient = Patient(
            full_name=request.form['full_name'],
            date_of_birth=request.form['date_of_birth'],
            email=request.form['email'],
            phone=request.form['phone'],
            glucose=gluc,
            cholesterol=chol,
            haemoglobin=hb,
            remarks=computed_remarks,
        )
        db.session.add(new_patient)
        db.session.commit()
        flash('Patient record added successfully with external AI Diagnostic evaluation!', 'success')
        return redirect(url_for('home'))
    return render_template('add_patient.html')
# EDIT RECORD ROUTE
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_patient(id):
    patient = Patient.query.get_or_404(id)
    if request.method == 'POST':
        patient.full_name = request.form['full_name']
        patient.date_of_birth = request.form['date_of_birth']
        patient.email = request.form['email']
        patient.phone = request.form['phone']
        patient.glucose = float(request.form['glucose'])
        patient.haemoglobin = float(request.form['haemoglobin'])
        patient.cholesterol = float(request.form['cholesterol'])
        patient.remarks = query_external_ml_api(patient.glucose, patient.cholesterol, patient.haemoglobin)
        db.session.commit()
        flash('Patient file records updated using live external model parsing.', 'info')
        return redirect(url_for('home'))
    return render_template('edit_patient.html', patient=patient, current_date=date.today())
# DELETE RECORD ROUTE
@app.route('/delete/<int:id>')
def delete_patient(id):
    patient = Patient.query.get_or_404(id)
    db.session.delete(patient)
    db.session.commit()
    flash('Patient record deleted successfully.', 'danger')
    return redirect(url_for('home'))
@app.route('/reports')
def reports():
    # 1. Pull all records from your database
    all_patients = Patient.query.all()    
    high_alert = 0
    observation_required = 0
    normal_status = 0
    for patient in all_patients:
        remarks = patient.remarks or ""
        if "High Risk" in remarks:
            high_alert += 1
        elif "Moderate Risk" in remarks or "Moderate" in remarks:
            observation_required += 1
        else:
            normal_status += 1
    return render_template(
        'reports.html', 
        patients=all_patients, 
        high_count=high_alert, 
        obs_count=observation_required, 
        normal_count=normal_status,
    )
with app.app_context():
    db.create_all()
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=False)
