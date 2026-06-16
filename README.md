# 📊 Customer Churn Analysis

## Overview

Customer Churn Analysis is a Machine Learning project that predicts whether a customer is likely to leave a company based on customer-related information such as tenure, monthly charges, contract type, and other service details.

This project uses a Random Forest Classifier to analyze customer data and provide churn predictions through an interactive Streamlit web application.

---

## Features

* Predict customer churn in real time
* Interactive Streamlit user interface
* Data preprocessing and feature encoding
* Machine Learning model training using Random Forest
* Easy-to-use prediction system

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Pickle

---

## Project Structure

customer-churn-analysis/

├── dataset/

├── train.py

├── app.py

├── model.pkl

├── requirements.txt

├── README.md

└── .gitignore

---

## Dataset

The project uses the Telco Customer Churn dataset containing customer information such as:

* Gender
* Senior Citizen Status
* Partner
* Dependents
* Tenure
* Phone Service
* Internet Service
* Contract Type
* Monthly Charges
* Total Charges
* Churn Status

---

## Model Performance

* Algorithm: Random Forest Classifier
* Accuracy: 78%

---

## Installation

Clone the repository:

```bash
git clone https://github.com/ananyathoke2-netizen/customer-churn-analysis.git
```

Move to the project folder:

```bash
cd customer-churn-analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Project

Train the model:

```bash
python train.py
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## Future Improvements

* Better user interface
* Additional machine learning algorithms
* Model comparison and evaluation
* Deployment on Streamlit Cloud

---

## Author

Ananya Rahul Thoke

Engineering Student (AI & ML)

GitHub: https://github.com/ananyathoke2-netizen
