# 📊 Telco Customer Churn Prediction

An end-to-end Machine Learning project that predicts customer churn for a telecom company using Logistic Regression, model tuning, threshold optimization, and Streamlit deployment.

---

## 🚀 Project Overview

Customer churn directly affects telecom revenue.  
This project builds a complete ML pipeline to:

- Predict customers likely to churn  
- Compare multiple classification models  
- Tune hyperparameters  
- Optimize decision threshold  
- Deploy the final model using Streamlit  

---

## 🎯 Business Objective

- Identify high-risk customers  
- Improve churn detection rate  
- Balance recall and precision  
- Reduce marketing waste  

Dataset churn rate: **26%**

---

## 🤖 Models Compared

- Logistic Regression  
- Random Forest  
- AdaBoost  
- XGBoost  
- Naive Bayes  
- Decision Tree  

### ✅ Final Model Selected:
**Regularized Logistic Regression**

Why?
- Best ROC-AUC
- Balanced precision–recall tradeoff
- Stable and interpretable

---

## 📊 Final Model Performance

| Metric | Score |
|--------|--------|
| ROC-AUC | 0.842 |
| Recall | 0.716 |
| Precision | 0.554 |
| Accuracy | 0.778 |

Final threshold used: **0.35**

---

## ⚖ Threshold Optimization

Instead of default 0.5, the threshold was tuned to:

- Increase churn detection (Recall)
- Maintain acceptable targeting efficiency (Precision)
- Balance business cost tradeoff

---

## 💻 Deployment

The model is deployed using **Streamlit** with:

- Dark theme UI  
- Real-time churn probability prediction  
- Risk segmentation:
  - 🔴 High Risk  
  - 🟡 Medium Risk  
  - 🟢 Low Risk  

---

## 🛠 Tech Stack

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Streamlit  

---

## ▶ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
