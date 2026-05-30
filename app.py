from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    appointment_message = ""
    medicine_message = ""

    if request.method == 'POST':

        # Doctor Appointment Booking
        patient_name = request.form.get('name')
        doctor_name = request.form.get('doctor')
        appointment_date = request.form.get('date')

        if patient_name and doctor_name and appointment_date:
            appointment_message = f"Appointment booked for {patient_name} with Dr. {doctor_name} on {appointment_date}"

        # Medicine Suggestion
        symptom = request.form.get('symptom')

        if symptom:

            symptom = symptom.lower()

            medicine_data = {

                "fever": "Paracetamol",
                "cold": "Cetirizine",
                "headache": "Ibuprofen",
                "cough": "Benadryl",
                "stomach pain": "Antacid",
                "vomiting": "Ondansetron",
                "body pain": "Diclofenac",
                "allergy": "Levocetirizine",
                "sore throat": "Strepsils",
                "infection": "Amoxicillin",
                "acidity": "Pantoprazole",
                "diarrhea": "Loperamide",
                "tooth pain": "Pain Relief Gel",
                "ear pain": "Ear Drops",
                "back pain": "Muscle Relaxant",
                "skin rash": "Calamine Lotion",
                "burn": "Burnol",
                "constipation": "Laxative",
                "gas": "ENO",
                "weakness": "Vitamin Tablets"

            }

            found = False

            for key in medicine_data:

                if key in symptom:

                    medicine_message = f"Suggested Medicine: {medicine_data[key]}"
                    found = True
                    break

            if not found:
                medicine_message = "No medicine found. Please consult a doctor."

    return render_template(
        'index.html',
        appointment_message=appointment_message,
        medicine_message=medicine_message
    )

if __name__ == '__main__':
    app.run(debug=True)