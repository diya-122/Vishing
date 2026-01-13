# Vishing
🔐 VoiceShield MVP
VoiceShield is a deepfake voice detection application that analyzes audio files to identify AI-generated or synthetic voices. Built with Streamlit and machine learning, it provides real-time analysis and risk assessment for audio authenticity.

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

Using Audio Upload Detection
Navigate to the "🎧 Audio Upload Detection" tab
Click "Browse files" to upload a WAV or MP3 file
Wait for the analysis to complete
View the results:
✅ REAL HUMAN VOICE - Low risk, authentic audio
⚠️ FAKE VOICE DETECTED - High risk, potential deepfake
Using Live Call Simulation
Navigate to the "📞 Live Call Simulation" tab
Upload a call audio file (WAV or MP3)
Click "▶️ Start Call Simulation"
The system will analyze the audio in 3-second chunks
Monitor the real-time risk score
If risk score exceeds 2.0, an alert is triggered
🔬 How It Works
Feature Extraction: Audio is processed using MFCC (Mel-frequency cepstral coefficients) analysis
Model Prediction: Pre-trained ML model classifies voice as real or fake
Confidence Calculation: Probability scores indicate prediction confidence
Risk Assessment: Cumulative scoring in live mode triggers alerts
📁 Project Structure
voiceshield-mvp/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── deepfake_voice_model.pkl   # Pre-trained ML model (required)
└── README.md                  # This file
⚙️ Technical Details
Audio Processing: 16kHz sampling rate, 3-second duration clips
Features: 13 MFCC coefficients averaged across time
Model: Scikit-learn based classifier (loaded via joblib)
Chunk Size: 3-second windows for live simulation
