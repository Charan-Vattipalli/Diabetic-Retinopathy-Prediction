# Diabetic-Retinopathy-Detection

## 🔹 Project Overview
This project focuses on detecting diabetic retinopathy in patients based on blood test features using machine learning. Diabetic retinopathy is a severe complication of diabetes that affects the eyes and can lead to vision loss if not detected early. Our goal is to develop a predictive model to assist in early diagnosis and preventive healthcare.

## 🔹 Business Objective
#### ✔ **Detect** the risk of diabetic retinopathy using medical test data
#### ✔ Automate patient screening to assist doctors in decision-making
#### ✔ Reduce manual diagnosis time and help in early detection
#### ✔ Improve patient outcomes by enabling timely treatment

## 🔹 Dataset Details
The dataset consists of 6000 patient records with 6 key medical features:

Feature	Description
#### ID - Unique patient identifier
#### Age - Age of the patient (numeric)
#### Systolic_BP - Blood pressure when the heart beats (normal: <120mmHg)
#### Diastolic_BP - Blood pressure when the heart rests (normal: <80mmHg)
#### Cholesterol - Blood cholesterol level (normal: 125-200 mg/dl)
#### Prognosis	Target variable: 1 (Retinopathy), 0 (No Retinopathy)

## 🔹 Technologies Used
#### ✔ Programming: Python
#### ✔ Web Framework: Flask
#### ✔ Data Processing: Pandas, NumPy
#### ✔ Machine Learning: Scikit-learn (Logistic Regression, Random Forest, XGBoost)
#### ✔ Visualization: Matplotlib, Seaborn

## 🔹 prediction

🔹 How to Run the Project Locally (Flask Deployment)

#### 📌 1. Clone the Repository
#### git clone https://github.com/yourusername/retinopathy-prediction.git
 cd retinopathy-prediction

#### 📌 2. Install Dependencies
 pip install -r requirements.txt

#### 📌 3. Run the Flask App
 python app.py

####📌 4. Test the API (Using Postman or cURL)
#### Send a POST request with patient data to get a prediction:
 curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"Age": 45, "Systolic_BP": 130, "Diastolic_BP": 85, "Cholesterol": 180}'

✔ The API will return a predicted risk of diabetic retinopathy.

## 🔹 Expected Outcome
#### ✔ Accurate predictions for diabetic retinopathy risk
#### ✔ Automated patient screening, reducing manual effort
#### ✔ Early diagnosis, leading to better treatment and prevention

## 🔹 Future Improvements
#### 🚀 Enhance the dataset with more medical parameters
#### 🚀 Improve model accuracy using advanced deep learning techniques
#### 🚀 Integrate with healthcare APIs for real-time medical records

## 🔹 Contributors
#### 👤 Sri Charan Vattipalli – Data Scientist
#### 📧 Contact: sricharanvattipalli@gmail.com

