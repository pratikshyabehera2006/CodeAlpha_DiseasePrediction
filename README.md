# 🩺 Disease Prediction using Machine Learning

## 📌 About the Project

This project is part of the **CodeAlpha Internship (Task 4)**.
It predicts whether a person is diabetic using medical data.

---

## 🎯 Objective

To build a machine learning model that can classify a person as:

* Diabetic
* Not Diabetic

---

## 🧠 Model Used

* Random Forest Classifier
* Library: scikit-learn

---

## 📊 Dataset Features

* Cholesterol
* Glucose
* HDL
* Age
* Height, Weight
* Waist, Hip
* Gender, Location, Frame

👉 Target column **Outcome** is created using HbA1c values.

---

## 🚀 How to Run

### Install dependencies

```
pip install -r requirements.txt
```

### Run app

```
streamlit run app.py
```

---

## 📁 Files

* `app.py` → Streamlit app
* `model.pkl` → trained model
* `columns.pkl` → features
* `diabetes.csv` → dataset

---

## 📌 Output

* Shows whether a person is **Diabetic or Not**

---

## 👤 Author

Pratikshya Behera
