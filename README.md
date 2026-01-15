# Vishing
🔐 VoiceShield MVP
VoiceShield is a deepfake voice detection application that analyzes audio files to identify AI-generated or synthetic voices. Built with Streamlit and machine learning, it provides real-time analysis and risk assessment for audio authenticity.<br>

🎯 Features
Audio Upload Detection: Upload WAV/MP3 files for instant deepfake analysis
Live Call Simulation: Simulate real-time call monitoring with chunk-by-chunk analysis
Confidence Scoring: Get confidence levels for each prediction
Risk Assessment: Automatic risk level categorization (LOW/HIGH)
Visual Feedback: Progress bars, audio playback, and color-coded results
🚀 Installation
Prerequisites
Python 3.7 or higher
pip package manager
Setup Steps
Clone or download the repository

cd voiceshield-mvp
Install required packages

pip install -r requirements.txt
Ensure model file exists

The application requires deepfake_voice_model.pkl in the project directory
This is a pre-trained machine learning model for voice classification
📦 Requirements
streamlit
joblib
numpy
librosa
soundfile
See requirements.txt for complete list with versions.

🎮 Usage
Running the Application
Start the Streamlit app:

streamlit run app.py
The application will open in your default web browser at http://localhost:8501

Using Audio Upload Detection<br>
Navigate to the "🎧 Audio Upload Detection" tab<br>
Click "Browse files" to upload a WAV or MP3 file<br>
Wait for the analysis to complete<br>
View the results:<br>
✅ REAL HUMAN VOICE - Low risk, authentic audio<br>
⚠️ FAKE VOICE DETECTED - High risk, potential deepfake<br>
Using Live Call Simulation<br>
Navigate to the "📞 Live Call Simulation" tab<br>
Upload a call audio file (WAV or MP3)<br>
Click "▶️ Start Call Simulation"<br>
The system will analyze the audio in 3-second chunks<br>
Monitor the real-time risk score<br>
If risk score exceeds 2.0, an alert is triggered<br>
🔬 How It Works<br>
Feature Extraction: Audio is processed using MFCC (Mel-frequency cepstral coefficients) analysis<br>
Model Prediction: Pre-trained ML model classifies voice as real or fake<br>
Confidence Calculation: Probability scores indicate prediction confidence<br>
Risk Assessment: Cumulative scoring in live mode triggers alerts<br>
📁 Project Structure<br>
voiceshield-mvp/<br>
├── app.py                      # Main Streamlit application<br>
├── requirements.txt            # Python dependencies<br>
├── deepfake_voice_model.pkl   # Pre-trained ML model (required)<br>
└── README.md                  # This file<br>
⚙️ Technical Details<br>
Audio Processing: 16kHz sampling rate, 3-second duration clips<br>
Features: 13 MFCC coefficients averaged across time<br>
Model: Scikit-learn based classifier (loaded via joblib)<br>
Chunk Size: 3-second windows for live simulation<br>
