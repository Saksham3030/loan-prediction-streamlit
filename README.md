#  Loan Prediction using Machine Learning

##  Project Overview

This project predicts whether a loan application will be **Approved** or **Rejected** based on applicant details using Machine Learning.

The project covers the complete Machine Learning workflow, including data cleaning, exploratory data analysis (EDA), feature engineering, model training, model evaluation, and deployment using Streamlit.

---

##  Dataset

- **Source:** Kaggle Loan Prediction Dataset
- **Training Records:** 614
- **Target Variable:** Loan_Status

---

##  Features

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Data Preprocessing
- Model Training
- Model Evaluation
- Streamlit Web Application

---

##  Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit

---

##  Machine Learning Models

The following models were trained and compared:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- Gradient Boosting Classifier

The best-performing model was selected based on evaluation metrics.

---

##  Evaluation Metrics

- Accuracy Score
- ROC-AUC Score
- Confusion Matrix
- Classification Report

---

##  Project Structure

```text
loan_prediction_project/
│
├── data/
│   ├── train.csv
│   └── test.csv
│
├── model/
│   ├── loan_model.pkl
│   └── scaler.pkl
│
├── notebook/
│   └── loan_prediction.ipynb
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ Run the Project Locally

### Clone Repository

```bash
git clone <repository-url>
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start Streamlit

```bash
streamlit run app.py
```

---

##  Application

The Streamlit application allows users to:

- Enter applicant details
- Predict loan approval status
- Display the prediction instantly

---

##  Project Workflow

1. Load Dataset
2. Data Inspection
3. Data Cleaning
4. Exploratory Data Analysis (EDA)
5. Feature Engineering
6. Data Preprocessing
7. Train-Test Split
8. Feature Scaling
9. Model Training
10. Model Evaluation
11. Save Best Model
12. Streamlit Deployment

---

##  Future Improvements

- Hyperparameter Tuning
- Cross Validation
- Feature Selection
- Cloud Deployment
- Docker Containerization

---

##  Author

**Saksham Tiwari**

