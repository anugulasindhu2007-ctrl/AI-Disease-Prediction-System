# Ayhu – AI Disease Prediction System

An educational Flask web application based on the handwritten architecture supplied for the project.

## What is included

- Welcome page using the wording from the sketch
- Symptoms page with 3 symptom fields and selectable symptom chips
- Disease prediction page
- Precautions page
- Responsive dark/modern UI
- Original architecture sketch in `docs/architecture-sketch.jpg`
- Clear disclaimer that the result is not a medical diagnosis
- No database or API required

## Project flow

Home → Symptoms → Guess the Disease → Precautions

The prototype uses a transparent symptom-overlap prediction function in `app.py`.
This keeps the project easy to run in a college project/demo environment.

## Run in VS Code

1. Open this folder in VS Code.
2. Open Terminal.
3. Create a virtual environment:

   Windows:
   ```powershell
   python -m venv venv
   ```

4. Activate it:

   ```powershell
   .\venv\Scripts\activate
   ```

   If PowerShell blocks activation, run:
   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   ```
   and then activate again.

5. Install Flask:
   ```powershell
   pip install -r requirements.txt
   ```

6. Start the website:
   ```powershell
   python app.py
   ```

7. Open the local address shown in the terminal, usually:
   `http://127.0.0.1:5000`

## Important

This is a student/educational prototype. It should not be used to diagnose illness, choose medication, or replace a qualified healthcare professional. The prediction logic is intentionally limited and should be replaced by a properly validated clinical ML model and dataset for any serious research use.
