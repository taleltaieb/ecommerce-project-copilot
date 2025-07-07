# 📦 E-Commerce Project Copilot Dashboard

An interactive data dashboard that helps e-commerce project and operations managers monitor performance, detect risks, and make data-driven decisions — built with real-world business context using the [Brazilian E-Commerce Public Dataset (Olist)](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).

---

## 🎬 Live Demo

![Dashboard Demo](screenshots/Animation.gif)

--- 

## 🎯 Project Objective

This dashboard simulates a client-style project for a company like Amazon, Olist, or Decathlon.  
It acts as an **Copilot for Project Managers**, delivering:

- 📊 Project and delivery insights
- 🚨 Risk detection (delays + bad reviews)
- 😠 Customer satisfaction tracking
- 📍 Regional performance breakdown

---

## 🧰 Tech Stack

- **Python** (Pandas, Plotly)
- **Streamlit** for dashboard UI
- **Kaggle Datasets** (100% real data)
- Optional deployment on Streamlit Cloud

---

## 📁 Project Structure

```
.
├── data/
│ └── raw/ # Original Kaggle CSVs
├── dashboard/
│ └── app_advanced.py # Streamlit app
├── screenshots/ # Demo visuals
├── notebooks/
│ ├── 01_exploration.ipynb # Data prep and EDA
├── README.md
└── requirements.txt
```

---

## 🖥️ Dashboard Features

### 📊 Overview
- KPIs: total orders, % delays, avg. review score
- Order volume trend over time

### ⏱️ Delay Analysis
- Top 10 cities by late deliveries
- Boxplot: Delay days vs review score

### 😠 Customer Satisfaction
- Review score distribution
- Delay vs on-time by score bucket

### 🚨 Risk Alerts
- Orders with **delay AND bad review**
- CSV download for ops follow-up

### 🎛️ Interactive Filters
- Filter by city, review bucket, delay range
- Dynamic visuals update instantly

---

## 🧪 How to Run Locally

1. Clone this repo
2. Install dependencies:
```bash
pip install -r requirements.txt
```
Download and unzip the dataset from Kaggle
Place the CSVs in: data/raw/

Launch the dashboard:
```bash
streamlit run dashboard/app_advanced.py
```

🌐 Live Demo
⚠️ Note: This app is deployed on Streamlit Cloud and may sleep when inactive.


📬 Contact
Built by Talel Taieb
💼 [LinkedIn](https://www.linkedin.com/in/talel-taieb/)
📫 taleltaieb20@gmail.com.com

⭐️ If you liked this project...
Give it a star ⭐ on GitHub or share your feedback!

