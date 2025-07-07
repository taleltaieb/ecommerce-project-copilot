# 📦 E-commerce Project Copilot Dashboard

A business-focused, data-driven dashboard that empowers project and operations managers in e-commerce to monitor risk, track delays, and optimize customer experience — built using **Python**, **Streamlit**, and real-world data from [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).

---

## 🚀 Overview

This dashboard simulates an AI-powered project assistant that provides:
- 📊 Executive-level KPIs (delivery rates, review scores, trends)
- ⏱️ Delay tracking by city and product category
- 😠 Sentiment analysis of customer reviews
- 🚨 Real-time risk alerts for delayed and low-rated orders
- 🧭 Interactive filtering by city, review score, delay days

---

## 📁 Project Structure

```bash
ecommerce-project-copilot/
├── data/
│   └── raw/                    # Original datasets (Olist CSVs from Kaggle)
├── dashboard/
│   ├── app.py         # Streamlit dashboard code
├── notebooks/
│   └── 01_exploration.ipynb    # Data cleaning & feature engineering
├── assets/
│   └── screenshots/            # Visual samples for the README/demo
├── README.md
└── requirements.txt
