VoiceShield is a machine learning–based web application designed to detect vishing (voice phishing) and AI-generated/deepfake voices from audio files and simulated phone calls.
The system analyzes voice characteristics using audio signal processing techniques and classifies the input as Real (Bonafide) or Fake (Spoof).

🚨 Problem Statement

With the rapid advancement of AI voice synthesis, voice phishing (vishing) attacks have become more convincing and difficult to detect. Fraudsters impersonate trusted individuals such as bank officials or relatives to manipulate victims into sharing sensitive information.
Existing fraud detection systems largely focus on text-based threats and lack voice authenticity verification, creating a need for an automated, voice-based detection solution.

💡 Proposed Solution

VoiceShield provides an AI-driven solution that:

*Analyzes uploaded call audio files

*Extracts meaningful voice features

*Uses a trained machine learning model to detect spoofed voices

*Displays confidence scores and risk levels to assist users in identifying fraudulent calls

The system is deployed as a web-based application, making it easily accessible and user-friendly.

🧠 System Overview

The application follows a modular workflow:

User uploads an audio file (WAV/MP3)

Audio preprocessing and MFCC feature extraction

Prediction using a trained ML classifier

Result display (Real/Fake, confidence score, risk level)

A Live Call Simulation mode is also included, where long call audio is analyzed in short chunks to simulate real-time call monitoring.

⚙️ Algorithm & Methodology

Feature Extraction:
Mel-Frequency Cepstral Coefficients (MFCC)

Model Type:
Supervised Machine Learning Classifier

Classification Output:

Bonafide (Real Human Voice)

Spoof (Fake / Vishing Voice)

📊 Dataset

ASVspoof 2019 – Logical Access (LA) Dataset

Contains labeled bonafide and spoofed voice samples

Includes AI-generated and voice-converted audio

Widely used benchmark dataset for voice anti-spoofing research

🌐 Deployment

The application is deployed using Streamlit Cloud and is publicly accessible.

🔗 Live Application Link:
https://deepfake-vishing-voiceshield.streamlit.app/

The deployed system allows users to:

Upload suspicious audio files

Detect spoofed or real voices

Simulate live call monitoring

View confidence scores and risk levels in real time

▶️ How to Run the Application Locally

1️⃣ Clone the Repository

git clone https://github.com/<your-username>/<your-repo-name>.git

cd <your-repo-name>

2️⃣ Create a Virtual Environment (Optional but Recommended)

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Run the Streamlit App

streamlit run app.py

5️⃣ Open in Browser

http://localhost:8501

🛠 Tech Stack
Programming Language: Python

Machine Learning & Audio Processing:

*Librosa

*Scikit-learn

*NumPy

*Joblib

Web Framework & Deployment:

*Streamlit

*Streamlit Cloud

Dataset: ASVspoof2019_LA

📂 Project Structure<br>
vishing/<br>
│<br>
├── app.py                     # Main Streamlit application<br>
├── deepfake_voice_model.pkl   # Trained ML model<br>
├── requirements.txt           # Required dependencies<br>
├── bonafide audio samples     # Sample real voice files<br>
├── spoof audio samples        # Sample fake voice files<br>
└── call simulation samples    # Audio files for live call simulation<br>

📈 Results

Successfully classifies uploaded audio as Real or Fake

Displays confidence score and risk level

Live call simulation detects spoofed voices across multiple audio chunks

Triggers a High Risk Call Alert when repeated spoofing is detected

⚠️ Limitations & Current Scope

The model is trained primarily on the ASVspoof2019_LA dataset

Performance is highest for audio patterns similar to the training data

Accuracy may vary due to:

Background noise

Different accents

Unseen spoofing techniques

Live telecom call interception is not implemented (simulation-based analysis only)

🚀 Future Scope

The system can be enhanced by training on larger and more diverse real-world datasets to improve generalization. Future improvements include real-time call integration, better noise robustness, adaptive learning for evolving spoofing techniques, and cloud-based scaling for large-scale deployment.

This project demonstrates the practical application of machine learning and audio signal processing in addressing real-world cybersecurity challenges.
