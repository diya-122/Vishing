import streamlit as st
import joblib
import numpy as np
import librosa
import tempfile
import time

# Load model
model = joblib.load("deepfake_voice_model.pkl")

def extract_features(audio_path):
    y, sr = librosa.load(audio_path, sr=16000, duration=3.0)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return np.mean(mfcc.T, axis=0)

st.set_page_config(page_title="VoiceShield MVP", layout="centered")

st.title("🔐 VoiceShield – Deepfake Voice Detection")
st.write("Detect AI-generated voices from audio files or simulated calls.")

tab1, tab2 = st.tabs(["🎧 Audio Upload Detection", "📞 Live Call Simulation"])

# ---------------- TAB 1: AUDIO UPLOAD ----------------
with tab1:
    st.subheader("Upload Suspicious Audio")
    uploaded_file = st.file_uploader("Upload WAV/MP3 file", type=["wav", "mp3"])

    if uploaded_file is not None:

        # ✅ USER FEEDBACK
        st.info("📂 Audio file loaded successfully. Ready for analysis.")
        st.audio(uploaded_file)

        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(uploaded_file.read())
            temp_path = tmp.name

        with st.spinner("🔍 Analyzing audio for deepfake patterns..."):
            progress = st.progress(0)

            for i in range(1, 101, 20):
                time.sleep(0.15)
                progress.progress(i)

            features = extract_features(temp_path).reshape(1, -1)
            prediction = model.predict(features)[0]
            confidence = model.predict_proba(features)[0].max()

            progress.progress(100)
            time.sleep(0.2)

        st.markdown("---")

        if prediction == 1:
            st.error("⚠️ FAKE VOICE DETECTED")
            st.write(f"Confidence: **{confidence:.2f}**")
            st.write("Risk Level: **HIGH**")
        else:
            st.success("✅ REAL HUMAN VOICE")
            st.write(f"Confidence: **{confidence:.2f}**")
            st.write("Risk Level: **LOW**")

# ---------------- TAB 2: LIVE CALL SIMULATION ----------------
with tab2:
    st.subheader("Simulated Live Call Monitoring")
    st.write("This simulates analyzing a call in short audio chunks.")

    uploaded_call = st.file_uploader("Upload Call Audio", type=["wav", "mp3"], key="call")

    if uploaded_call is not None:

        # ✅ USER FEEDBACK
        st.info("📞 Call audio loaded. Ready to simulate monitoring.")
        st.audio(uploaded_call)

        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(uploaded_call.read())
            call_path = tmp.name

        y, sr = librosa.load(call_path, sr=16000)
        chunk_size = sr * 3
        risk_score = 0

        if st.button("▶️ Start Call Simulation"):
            for i in range(0, len(y), chunk_size):
                chunk = y[i:i + chunk_size]
                if len(chunk) < chunk_size:
                    break

                mfcc = librosa.feature.mfcc(y=chunk, sr=sr, n_mfcc=13)
                features = np.mean(mfcc.T, axis=0).reshape(1, -1)

                pred = model.predict(features)[0]
                conf = model.predict_proba(features)[0].max()

                if pred == 1:
                    risk_score += conf
                    st.warning(f"Chunk {i//chunk_size + 1}: FAKE detected ({conf:.2f})")
                else:
                    st.info(f"Chunk {i//chunk_size + 1}: Normal voice")

                time.sleep(0.8)

                if risk_score > 2.0:
                    st.error("🚨 HIGH RISK CALL – ALERT TRIGGERED")
                    break

            st.write(f"Final Risk Score: **{risk_score:.2f}**")
