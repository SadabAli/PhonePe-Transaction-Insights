import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# ------------------------ MySQL Connection ------------------------
username = "root"
password = "Sadab404@"
host = "127.0.0.1"
port = 3306
database = "phonepe_data"

connection_string = f"mysql+pymysql://{username}:{password.replace('@', '%40')}@{host}:{port}/{database}"
engine = create_engine(connection_string)

# ------------------------ Page Config ------------------------
st.set_page_config(page_title="PhonePe Dashboard", layout="wide")
st.title(" PhonePe Transaction Insights Dashboard")

# ------------------------ Data Fetch ------------------------
@st.cache_data
def load_data():
    df_tx = pd.read_sql("SELECT * FROM aggregated_transaction", engine)
    df_user = pd.read_sql("SELECT * FROM aggregated_user", engine)
    df_ins = pd.read_sql("SELECT * FROM aggregated_insurance", engine)
    df_map_tx = pd.read_sql("SELECT * FROM map_transaction", engine)
    df_map_ins = pd.read_sql("SELECT * FROM map_insurance", engine)
    df_top_tx = pd.read_sql("SELECT * FROM top_transaction", engine)
    return df_tx, df_user, df_ins, df_map_tx, df_map_ins, df_top_tx

df_tx, df_user, df_ins, df_map_tx, df_map_ins, df_top_tx = load_data()

# ------------------------ KPI Metrics ------------------------
st.subheader(" Key Metrics")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Transactions", f"{df_tx['transaction_count'].sum():,}")
col2.metric("Transaction Amount (₹)", f"{df_tx['transaction_amount'].sum():,.2f}")
col3.metric("Registered Users", f"{df_user['user_count'].sum():,}")
col4.metric("Insurance Premiums (₹)", f"{df_ins['insurance_amount'].sum():,.2f}")

st.markdown("---")

# ------------------------ Graphs Layout ------------------------
st.subheader("Data Visualizations")

# 1. Transaction Amount by level
fig1 = px.bar(df_top_tx.groupby("level")[["transaction_amount"]].sum().reset_index(),
              x="level", y="transaction_amount", title="Transaction Amount by level",
              labels={"transaction_amount": "₹ Amount"})
st.plotly_chart(fig1, use_container_width=True)

# 2. Transaction Count Over Years
fig2 = px.line(df_tx.groupby("year")[["transaction_count"]].sum().reset_index(),
               x="year", y="transaction_count", title="Transaction Count Over the Years")
st.plotly_chart(fig2, use_container_width=True)

# 3. Top Device Brands by Users
fig3 = px.bar(df_user.groupby("device_brand")[["user_count"]].sum().reset_index().sort_values(by="user_count", ascending=False).head(10),
              x="device_brand", y="user_count", title="Top 10 Device Brands by User Count")
st.plotly_chart(fig3, use_container_width=True)

# 4. Insurance Premiums by State
fig4 = px.bar(df_map_ins.groupby("state")[["amount"]].sum().reset_index().sort_values(by="amount", ascending=False).head(10),
              x="state", y="amount", title="Top 10 States by Insurance Premiums")
st.plotly_chart(fig4, use_container_width=True)

# 5. Transaction Count by Category
fig5 = px.pie(df_tx.groupby("transaction_type")[["transaction_count"]].sum().reset_index(),
              names="transaction_type", values="transaction_count", title="Transaction Count by Category")
st.plotly_chart(fig5, use_container_width=True)

# 6. Insurance Count by Year
fig6 = px.line(df_ins.groupby("year")[["insurance_count"]].sum().reset_index(),
               x="year", y="insurance_count", title="Insurance Count Over the Years")
st.plotly_chart(fig6, use_container_width=True)

# 7. User Count % by Device Brand
fig7 = px.bar(df_user.groupby("device_brand")[["percentage"]].mean().reset_index().sort_values(by="percentage", ascending=False).head(10),
              x="device_brand", y="percentage", title="Top 10 Device Brands by Usage %")
st.plotly_chart(fig7, use_container_width=True)

# 8. Map Transaction Count by State (as bar chart)
fig8 = px.bar(df_map_tx.groupby("state")[["transaction_count"]].sum().reset_index(),
              x="state", y="transaction_count", title="Transaction Count by State (Map Data)")
st.plotly_chart(fig8, use_container_width=True)

# 9. Transaction Volume by Quarter
fig9 = px.bar(df_tx.groupby("quarter")[["transaction_amount"]].sum().reset_index(),
              x="quarter", y="transaction_amount", title="Transaction Amount by Quarter")
st.plotly_chart(fig9, use_container_width=True)

# # 10. Insurance Adoption (State-wise Count)
# fig10 = px.bar(df_ins.groupby("state")[["insurance_count"]].sum().reset_index().sort_values(by="insurance_count", ascending=False).head(10),
#                x="state", y="insurance_count", title="Top 10 States by Insurance Adoption")
# st.plotly_chart(fig10, use_container_width=True)
