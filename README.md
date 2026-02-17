📊 Telco Customer Churn Prediction
🚀 Project Overview

This project builds an end-to-end Machine Learning pipeline to predict customer churn for a telecom company.
The objective is to identify high-risk customers and assist the business in optimizing retention strategies.

The project covers:

Exploratory Data Analysis (EDA)

Model comparison

Hyperparameter tuning

Threshold optimization

Business metric interpretation

Deployment using Streamlit

🎯 Business Problem

Customer churn directly impacts telecom revenue and long-term customer lifetime value.

The goal is to:

Predict customers likely to churn

Increase churn detection rate

Balance recall and marketing cost

Optimize retention campaign efficiency

Build a deployable and business-ready prediction system

Churn rate in dataset: 26% (Imbalanced classification problem)

📂 Dataset

Telco Customer Churn Dataset containing:

Demographic information

Service subscription details

Internet and add-on services

Billing and contract information

After preprocessing and one-hot encoding, the model uses 31 engineered features.

🔍 Exploratory Data Analysis (Key Insights)

📉 Customers with month-to-month contracts have the highest churn rate

🌐 Fiber optic users show significantly higher churn probability

⏳ Customers with low tenure are more likely to churn

💳 Electronic check payment method correlates strongly with churn

📄 Customers on long-term contracts (1–2 years) show lower churn

🛠 Customers without value-added services (OnlineSecurity, TechSupport) tend to churn more

📊 Service combination patterns impact churn more than individual services

These insights highlight that churn is influenced more by contract flexibility and service dissatisfaction rather than just demographics.

🤖 Model Development
Models Compared

Logistic Regression

Random Forest

AdaBoost

XGBoost

Naive Bayes

Decision Tree

Final Model Selected

Regularized Logistic Regression

Why Logistic Regression?

Highest ROC-AUC

Balanced precision-recall tradeoff

Stable and consistent performance

Less prone to overfitting

Highly interpretable for business stakeholders

📊 Final Model Performance
Metric	Score
Accuracy	0.781
Recall	0.720
ROC-AUC	0.857
Precision	0.578

Final decision threshold: 0.35

⚖ Threshold Optimization Strategy

Instead of using the default 0.5 threshold, the decision threshold was tuned to 0.35 to optimize business impact.

Why 0.35?

Higher threshold → High precision but many churners missed

Lower threshold → High recall but excessive marketing cost

0.35 provided the best tradeoff between churn detection and retention efficiency

This approach aligns the ML model with real-world business decision-making.

💰 Business Interpretation of Metrics

Recall (72%) → Captures most potential churners

Precision (58%) → More than half of targeted customers are true churners

ROC-AUC (0.857) → Strong model discrimination capability

Accuracy alone is not reliable due to class imbalance

This demonstrates why evaluation beyond accuracy is critical in churn modeling.

💻 Deployment

The model is deployed using Streamlit with:

Dark theme UI

Full feature alignment with training data

Real-time churn probability output

Risk segmentation:

🔴 High Risk

🟡 Medium Risk

🟢 Low Risk

This allows business teams to quickly assess customer risk profiles.

📈 Potential Business Impact

Improve targeted retention campaigns

Reduce unnecessary marketing expenditure

Increase customer lifetime value

Data-driven contract optimization strategies

Early identification of dissatisfaction patterns

🛠 Tech Stack

Python

Scikit-Learn

Pandas

NumPy

Streamlit

Matplotlib

Pickle

📌 Key Learnings

ROC-AUC is more meaningful than accuracy in imbalanced datasets

Precision–Recall tradeoff drives business decision quality

Threshold tuning significantly impacts operational cost

Deployment must strictly match training feature engineering

End-to-end ML projects require both technical and business alignment

▶ Run Locally
pip install -r requirements.txt
streamlit run app.py

👨‍💻 Author

Harsh Mulimani