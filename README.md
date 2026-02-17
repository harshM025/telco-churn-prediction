# 📊 Telco Customer Churn Prediction  

> 🚀 End-to-End Machine Learning Project  
> 🎯 Business-Oriented | 📈 Threshold Optimized | 💻 Streamlit Deployed  

---

## 🚀 Project Overview  

This project builds a complete **Machine Learning pipeline** to predict customer churn for a telecom company.

The objective is to **identify high-risk customers** and support the business in optimizing retention strategies.

### 🔹 Project Workflow

- 📊 Exploratory Data Analysis (EDA)  
- 🤖 Model Comparison  
- ⚙️ Hyperparameter Tuning  
- 🎚 Threshold Optimization  
- 📈 Business Metric Interpretation  
- 💻 Streamlit Deployment  

---

## 🎯 Business Problem  

Customer churn directly impacts telecom revenue and long-term customer lifetime value.

### Goals:

- Identify customers likely to churn  
- Increase churn detection rate  
- Balance recall and marketing cost  
- Build a deployable production-ready model  

📌 Dataset churn rate: **26% (Imbalanced Classification Problem)**  

---

## 📂 Dataset Description  

The dataset includes:

- 👤 Demographic Information  
- 🌐 Service Subscription Details  
- 💳 Billing & Payment Information  
- 📄 Contract Details  

After preprocessing and one-hot encoding, the model uses:

> **31 engineered features**

---

## 🔍 Key Insights from EDA  

- 📉 Month-to-month contracts show the highest churn rate  
- 🌐 Fiber optic users churn more frequently  
- ⏳ Customers with low tenure are more likely to churn  
- 💳 Electronic check payments strongly correlate with churn  
- 📄 Long-term contracts significantly reduce churn probability  
- 🛠 Lack of add-on services increases churn likelihood  

---

## 🤖 Model Development  

### Models Evaluated

- Logistic Regression  
- Random Forest  
- AdaBoost  
- XGBoost  
- Naive Bayes  
- Decision Tree  

---

## ✅ Final Model: Regularized Logistic Regression  

### Why Logistic Regression?

- 🏆 Highest ROC-AUC  
- ⚖ Balanced precision–recall tradeoff  
- 📉 Lower overfitting risk  
- 📊 Business-friendly interpretability  

---

## 📊 Final Model Performance  

| Metric      | Score |
|------------|--------|
| Accuracy   | 0.781 |
| Recall     | 0.720 |
| ROC-AUC    | 0.857 |
| Precision  | 0.578 |

🎯 Final Decision Threshold: **0.35**

---

## ⚖ Threshold Optimization Strategy  

Instead of using the default 0.5 threshold, the model threshold was tuned to **0.35** to align with business impact.

### Tradeoff Logic:

- Lower threshold → Higher Recall (capture more churners)  
- Higher threshold → Higher Precision (reduce marketing waste)  

The selected threshold provides an optimal balance between churn detection and retention cost.

---

## 💰 Business Interpretation of Metrics  

- **Recall (72%)** → Majority of churners correctly identified  
- **Precision (58%)** → Efficient targeting of retention efforts  
- **ROC-AUC (0.857)** → Strong class separation capability  

📌 Accuracy alone is insufficient due to class imbalance.

---

## 💻 Deployment  

The model is deployed using **Streamlit** with:

- 🌙 Dark Theme UI  
- 🔄 Real-time Churn Probability Prediction  
- 🎯 Risk Segmentation:
  - 🔴 High Risk  
  - 🟡 Medium Risk  
  - 🟢 Low Risk  

---

## 📈 Potential Business Impact  

- Improve targeted retention campaigns  
- Reduce unnecessary discounting  
- Increase customer lifetime value  
- Enable data-driven contract strategy  

---

## 🛠 Tech Stack  

- Python  
- Pandas  
- NumPy  
- Scikit-Learn  
- Streamlit  
- Matplotlib  
- Pickle  

---

## ▶ Run Locally  

```bash
pip install -r requirements.txt
streamlit run app.py

👨‍💻 Author

Harsh Mulimani
Machine Learning Enthusiast