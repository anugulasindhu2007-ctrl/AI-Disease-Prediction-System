from flask import Flask, render_template, request
from pathlib import Path

app = Flask(__name__)

# Educational prototype:
# This project uses a small symptom-scoring model so the website can run
# without an external database or API. It is NOT a medical diagnostic tool.
DISEASES = {
    "Common Cold": {
        "symptoms": {"cough", "sneezing", "runny nose", "sore throat", "mild fever", "headache"},
        "precaution": "Rest, drink enough fluids, and consider speaking with a qualified healthcare professional if symptoms persist or worsen."
    },
    "Flu": {
        "symptoms": {"fever", "body ache", "chills", "cough", "headache", "fatigue"},
        "precaution": "Rest and stay hydrated. Seek professional medical advice, especially for severe or persistent symptoms."
    },
    "Migraine": {
        "symptoms": {"headache", "nausea", "sensitivity to light", "blurred vision", "dizziness"},
        "precaution": "Rest in a quiet environment and seek medical advice for new, severe, or recurring headaches."
    },
    "Allergy": {
        "symptoms": {"sneezing", "runny nose", "itchy eyes", "rash", "cough"},
        "precaution": "Reduce exposure to known triggers and seek professional advice when symptoms are significant or persistent."
    },
    "Gastritis": {
        "symptoms": {"stomach pain", "nausea", "vomiting", "bloating", "loss of appetite"},
        "precaution": "Stay hydrated and seek professional medical advice for persistent stomach symptoms or warning signs."
    },
    "Food Poisoning": {
        "symptoms": {"stomach pain", "vomiting", "diarrhea", "nausea", "fever"},
        "precaution": "Maintain hydration and seek medical care if symptoms are severe, persistent, or accompanied by warning signs."
    },
}

SYMPTOM_OPTIONS = sorted({
    symptom for disease in DISEASES.values() for symptom in disease["symptoms"]
})

def predict_disease(selected_symptoms):
    """Simple transparent prototype model based on symptom overlap."""
    selected = {s.strip().lower() for s in selected_symptoms if s.strip()}
    if not selected:
        return None, 0, []

    scores = []
    for disease, data in DISEASES.items():
        matched = selected.intersection(data["symptoms"])
        # Reward matching symptoms and mildly penalize very large mismatches.
        score = len(matched) / max(len(data["symptoms"]), 1)
        scores.append((score, disease, sorted(matched)))

    scores.sort(reverse=True)
    best_score, best_disease, matched = scores[0]

    # Confidence is intentionally capped because this is an educational prototype.
    confidence = min(round(best_score * 100), 95)
    return best_disease, confidence, matched

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/symptoms")
def symptoms():
    return render_template("symptoms.html", symptom_options=SYMPTOM_OPTIONS)

@app.route("/predict", methods=["POST"])
def predict():
    selected = request.form.getlist("symptoms")
    # Also support the three text boxes from the hand-drawn architecture.
    for key in ("major_symptom", "symptom_2", "symptom_3"):
        value = request.form.get(key, "").strip().lower()
        if value:
            selected.append(value)

    disease, confidence, matched = predict_disease(selected)

    if not disease:
        return render_template(
            "result.html",
            error="Please enter or select at least one symptom.",
            disease=None,
            confidence=0,
            matched=[],
            precaution=None,
        )

    return render_template(
        "result.html",
        error=None,
        disease=disease,
        confidence=confidence,
        matched=matched,
        precaution=DISEASES[disease]["precaution"],
    )

@app.route("/precautions")
def precautions():
    return render_template("precautions.html")

if __name__ == "__main__":
    app.run(debug=True)
