import streamlit as st
import pandas as pd
import requests
import joblib
from datetime import datetime
import matplotlib.pyplot as plt

# Load pre-trained models
malware_model = joblib.load("malware_model.pkl")
ip_reputation_model = joblib.load("ip_reputation_model.pkl")

def get_threat_intelligence(feed_url):
    """Fetch real-time threat intelligence feed."""
    try:
        response = requests.get(feed_url)
        response.raise_for_status()
        return pd.DataFrame(response.json())
    except Exception as e:
        st.error(f"Error fetching threat intelligence: {e}")
        return pd.DataFrame()

def extract_ip_features(ip_address):
    """
    Dummy function to extract features from an IP address.
    Replace with actual feature extraction logic.
    """
    # Example: Return a fixed set of features for testing
    return [1, 0, 0.5]  # Replace with realistic feature values

def analyze_ip(ip_address):
    """
    Analyze IP reputation.
    """
    try:
        # Extract features for the IP
        features = [extract_ip_features(ip_address)]  # Replace with real logic
        
        # Predict probabilities
        proba = ip_reputation_model.predict_proba(features)
        
        # Check the output shape of `proba`
        if proba.shape[1] == 1:
            # Handle single-column output
            score = proba[0][0] * 100
        else:
            # Use the second column for "malicious" score
            score = proba[0][1] * 100

        # Predict the label
        prediction = ip_reputation_model.predict(features)[0]
        return prediction, score

    except Exception as e:
        # Handle any errors gracefully
        st.error(f"Error analyzing IP: {str(e)}")
        return "Error", 0.0


def classify_malware(file_features):
    """Classify malware based on file features."""
    # Get the prediction (class label)
    prediction = malware_model.predict([file_features])[0]
    
    # Get the probabilities
    proba = malware_model.predict_proba([file_features])[0]
    
    # Ensure the model returns probabilities for both classes
    if len(proba) > 1:
        score = proba[1] * 100  # Assuming [1] is the probability for the "malware" class
    else:
        score = 0  # In case there is only one class (non-malware)
    
    return prediction, score


# Streamlit app
st.title("Advanced Threat Intelligence Platform")
st.image('logo.png', width=500)  # Add your logo image with a width of 200px
st.sidebar.title("Navigation")
menu = st.sidebar.selectbox("Choose an option:", ["Real-Time Threat Feed", "IP Reputation Analysis", "Malware Classification", "Dashboard"])

if menu == "Real-Time Threat Feed":
    st.header("Real-Time Threat Feed")
    feed_url = st.text_input("Enter Threat Intelligence Feed URL:", "https://example.com/feed")
    if st.button("Fetch Feed"):
        data = get_threat_intelligence(feed_url)
        if not data.empty:
            st.write("Threat Feed:")
            st.dataframe(data)

elif menu == "IP Reputation Analysis":
    st.header("IP Reputation Analysis")
    ip_address = st.text_input("Enter IP Address:", "8.8.8.8")
    if st.button("Analyze IP"):
        prediction, score = analyze_ip(ip_address)
        st.write(f"Prediction: {'Malicious' if prediction else 'Safe'}")
        st.write(f"Threat Score: {score:.2f}%")

elif menu == "Malware Classification":
    st.header("Malware Classification")
    file_features = st.text_area("Enter File Features (comma-separated):")
    if st.button("Classify File"):
        file_features = list(map(float, file_features.split(",")))
        prediction, score = classify_malware(file_features)
        st.write(f"Prediction: {'Malicious' if prediction else 'Safe'}")
        st.write(f"Threat Score: {score:.2f}%")

elif menu == "Dashboard":
    st.header("Threat Intelligence Dashboard")

    # Example data for the dashboard
    data = {
        "Phishing Campaigns": [10, 20, 30, 40],
        "Ransomware Activity": [15, 25, 35, 45],
        "Nation-State Attacks": [5, 10, 15, 20],
    }
    dates = [datetime(2025, 1, i+1) for i in range(4)]

    st.write("Threat Trends")
    for key, values in data.items():
        plt.plot(dates, values, label=key)
    plt.xlabel("Date")
    plt.ylabel("Activity")
    plt.legend()
    st.pyplot(plt)

    st.write("Detailed Insights")
    st.bar_chart(pd.DataFrame(data, index=dates))
