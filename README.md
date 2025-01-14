<h1 align="center"> 🛡️ Advanced Threat Intelligence Platform 🛡️ </h1>

![image](https://github.com/user-attachments/assets/98639b79-2f8e-4af0-a601-189bf5cad9a4)

[![Threat Intelligence](https://img.shields.io/badge/Threat%20Intelligence%20Platform-blue?style=for-the-badge&logo=security)](https://advanced-threat-intelligence-platform-mk7obgez2n4p59zcvziiso.streamlit.app/)

## 📝 Overview

Welcome to the **Advanced Threat Intelligence Platform**! This platform is designed to analyze and classify real-time threats based on various intelligence feeds, IP reputation, and malware characteristics. It includes the following features:

- Real-Time Threat Feed
- IP Reputation Analysis
- Malware Classification
- Threat Intelligence Dashboard

## 🛠️ Features

- **Real-Time Threat Feed**: Fetches live threat data from an external feed URL.
- **IP Reputation Analysis**: Analyzes IP addresses to determine their reputation (safe or malicious).
- **Malware Classification**: Classifies files as either malware or safe based on predefined features.
- **Threat Intelligence Dashboard**: Visualizes threat trends such as phishing, ransomware, and nation-state attacks.

## Prerequisites

Ensure the following dependencies are installed:
- Python 3.8 or higher
- `pip` package manager

## 🤖 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Advanced-Threat-Intelligence-Platform.git
   cd Advanced-Threat-Intelligence-Platform

2. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

3. Install required libraries:
   ```bash
   pip install -r requirements.txt

4. Download or train the machine learning models (malware_model.pkl, ip_reputation_model.pkl) and place them in the same directory as the script.

## 🧑‍💻 Usage
## Launch the Streamlit app:
- Run the following command to start the application:
  
   ```bash
   streamlit run app.py

## 💻 Features in Detail ⚡
## 1. Real-Time Threat Feed
- Fetches real-time threat intelligence data from an external feed URL (JSON format). The data can be visualized and analyzed within the platform.

![Real-Time Threat Feed](https://github.com/user-attachments/assets/37e0e005-9931-45da-b4e6-a76651d55121)

## 2. IP Reputation Analysis
- Enter an IP address to analyze its reputation. The app uses a machine learning model to predict whether the IP is safe or malicious and assigns a threat score.

![IP Reputation Analysis](https://github.com/user-attachments/assets/43e8a23c-cc96-4018-87b1-ea1c52dd7f04)

## 3. Malware Classification
- Enter comma-separated file features for classification. The app uses a pre-trained machine learning model to predict whether the file is malware or safe.

![Malware Classification](https://github.com/user-attachments/assets/26818505-6f14-484b-89bf-6b369110e943)

## 4. Threat Intelligence Dashboard
- The dashboard visualizes various threat categories, such as phishing campaigns, ransomware activity, and nation-state attacks. The data is presented in line charts and bar charts for easy analysis.

![threat intelligence dashboard_page-0001](https://github.com/user-attachments/assets/ca801735-0659-419f-8e0c-a02a6161f845)


## 🤝 Contributing
- We welcome contributions! If you would like to improve or add new features to this project, please fork the repository and submit a pull request.

## Connect with Me 🌐

- 📧 [Email](mailto:gauravghandat12@gmail.com)
- 💼 [LinkedIn](www.linkedin.com/in/gaurav-ghandat-68a5a22b4)




















