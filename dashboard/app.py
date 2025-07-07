import streamlit as st
import pandas as pd
import os
import plotly.express as px

# Load preprocessed data
RAW_PATH = "data/raw"
orders = pd.read_csv(os.path.join(RAW_PATH, "olist_orders_dataset.csv"))
items = pd.read_csv(os.path.join(RAW_PATH, "olist_order_items_dataset.csv"))
reviews = pd.read_csv(os.path.join(RAW_PATH, "olist_order_reviews_dataset.csv"))
payments = pd.read_csv(os.path.join(RAW_PATH, "olist_order_payments_dataset.csv"))
customers = pd.read_csv(os.path.join(RAW_PATH, "olist_customers_dataset.csv"))
sellers = pd.read_csv(os.path.join(RAW_PATH, "olist_sellers_dataset.csv"))

# Merge tables
orders_full = orders.merge(items, on="order_id", how="left") \
                    .merge(reviews, on="order_id", how="left") \
                    .merge(payments, on="order_id", how="left") \
                    .merge(customers, on="customer_id", how="left") \
                    .merge(sellers, on="seller_id", how="left")

# Convert dates
orders_full["order_delivered_customer_date"] = pd.to_datetime(orders_full["order_delivered_customer_date"])
orders_full["order_estimated_delivery_date"] = pd.to_datetime(orders_full["order_estimated_delivery_date"])

# Feature engineering
orders_full["delay_days"] = (orders_full["order_delivered_customer_date"] - orders_full["order_estimated_delivery_date"]).dt.days
orders_full["is_late"] = orders_full["delay_days"] > 0
orders_full["review_score_bucket"] = pd.cut(
    orders_full["review_score"],
    bins=[0, 2, 3, 5],
    labels=["bad", "neutral", "good"]
)
orders_full["month"] = orders_full["order_delivered_customer_date"].dt.to_period("M").astype(str)

# Streamlit setup
st.set_page_config(page_title="E-commerce Copilot", layout="wide")
st.markdown("<h1 style='text-align: center;'>📦 Olist Project Copilot Dashboard</h1>", unsafe_allow_html=True)
st.markdown("Use this interactive dashboard to monitor delivery performance, customer satisfaction, and high-risk orders.")

# Filters
with st.sidebar:
    st.header("🔍 Filters")
    city_filter = st.multiselect("Select Cities", options=orders_full["customer_city"].dropna().unique())
    score_filter = st.multiselect("Review Buckets", options=["bad", "neutral", "good"], default=["bad", "neutral", "good"])
    min_delay = st.slider("Min Delay (days)", -100, 100, -10)

df_filtered = orders_full.copy()
if city_filter:
    df_filtered = df_filtered[df_filtered["customer_city"].isin(city_filter)]
if score_filter:
    df_filtered = df_filtered[df_filtered["review_score_bucket"].isin(score_filter)]
df_filtered = df_filtered[df_filtered["delay_days"] >= min_delay]

# Tabs layout
tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "⏱️ Delay Analysis", "😠 Customer Satisfaction", "🚨 Risk Alerts"])

with tab1:
    st.subheader("📊 Project Overview")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Orders", len(df_filtered))
    col2.metric("Late Deliveries (%)", f"{df_filtered['is_late'].mean() * 100:.2f}%")
    col3.metric("Avg. Review Score", f"{df_filtered['review_score'].mean():.2f}")
    
    st.subheader("Orders Over Time")
    timeline_chart = df_filtered.groupby("month")["order_id"].count().reset_index()
    st.plotly_chart(px.line(timeline_chart, x="month", y="order_id", title="Orders per Month"), use_container_width=True)

with tab2:
    st.subheader("⏱️ Delay Analysis")
    late_by_city = df_filtered[df_filtered["is_late"]].groupby("customer_city")["order_id"].count().sort_values(ascending=False).head(10)
    st.plotly_chart(px.bar(late_by_city, orientation="v", title="Top 10 Cities by Late Orders"), use_container_width=True)

    st.subheader("Delay Distribution by Review Score")
    st.plotly_chart(px.box(df_filtered.dropna(subset=["delay_days", "review_score"]), 
                           x="review_score", y="delay_days", title="Delay vs Review Score"), use_container_width=True)

with tab3:
    st.subheader("😠 Customer Satisfaction")
    score_dist = df_filtered["review_score_bucket"].value_counts().sort_index()
    st.plotly_chart(px.bar(score_dist, title="Review Bucket Distribution"), use_container_width=True)

    st.subheader("Late vs On-Time Orders by Review Score")
    cross = pd.crosstab(df_filtered["review_score_bucket"], df_filtered["is_late"])
    st.dataframe(cross)

with tab4:
    st.subheader("🚨 Orders with Delay + Bad Review")
    risk_orders = df_filtered[(df_filtered["is_late"]) & (df_filtered["review_score_bucket"] == "bad")]
    st.dataframe(risk_orders[["order_id", "customer_city", "delay_days", "review_score"]].dropna().head(100))
    st.download_button("📥 Download CSV", data=risk_orders.to_csv(index=False), file_name="high_risk_orders.csv")
