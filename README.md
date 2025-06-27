# PhonePe Transaction Insights

An end-to-end data analysis and dashboard project that explores India’s digital payment ecosystem using PhonePe transaction data. This project extracts, transforms, and visualizes transaction, user, and insurance metrics using Python, MySQL, and Streamlit.

---

## Project Overview

This project performs ETL on JSON-based datasets from PhonePe and builds a powerful Streamlit dashboard to explore:

- State-wise & category-wise transactions
- Insurance premiums over time
- Device brand usage patterns
- Yearly growth trends in digital payments

---

## Objectives

- Parse and clean structured JSON data
- Load data into MySQL using Python
- Query and analyze data using SQL
- Visualize trends with Streamlit
- Derive insights to guide business strategy

---

## Tech Stack

| Tool         | Use                         |
|--------------|-----------------------------|
| Python       | Data parsing and automation |
| Pandas       | Data transformation         |
| MySQL        | Relational data storage     |
| SQLAlchemy   | Python-DB connectivity      |
| Streamlit    | Dashboard and visualization |
| DBeaver      | DB management               |
| Git & VS Code| Dev tools                   |

---

## Data Description

- **Transaction Count**: 235.3 Billion  
- **Transaction Amount**: ₹345.58 Trillion  
- **Insurance Premiums**: ₹20.01 Billion  
- **Registered Users**: 3.46 Billion  

Data covers multiple levels: country → state → district → pincode, and multiple categories: transactions, users, insurance.

---

## Visual Insights

### 🔹 Yearly Transaction Growth
2018 to 2024:  
1B → 99.3B Transactions  
 _Exponential digital adoption across India_

### 🔹 Top Device Brands by User Count
- Xiaomi: 869.4M  
- Samsung, Vivo, Oppo follow  

 _Focus on Android-first experience_

### 🔹 Category-wise Transaction Share
- Merchant Payments: 55.3%  
- P2P Payments: 36.1%  
- Recharge & Bills: 8.3%  

 _Retail and P2P drive the ecosystem_

### 🔹 Top States by Insurance Premium
- Karnataka: ₹2.7B  
- Maharashtra: ₹2.3B  
- Uttar Pradesh: ₹1.74B  

_Insurance adoption is strong in developed states_

---

##  Geographic Performance

- High: Maharashtra (₹32B), Karnataka, UP  
- Low: Mizoram, Ladakh, Lakshadweep (~₹170M)  
- Promising: Jharkhand, Odisha, Rajasthan

---

##  Key Insights

- Massive surge in digital payments between 2018–2024
- Android brands dominate user base
- Q3 & Q4 see highest transaction volumes
- Insurance adoption has grown steadily year-on-year
- Tier-2 states offer untapped market potential

---

## ✅ Actionable Recommendations

1. **Expand digital campaigns** in underperforming regions  
2. **Optimize app** for Xiaomi, Vivo, Realme  
3. **Boost insurance awareness** in Tier-2 cities  
4. **Launch features in Q3/Q4** for max engagement  
5. **Empower rural merchants** via incentives and onboarding

---


## ▶️ How to Run

1. Clone the repo  
```bash
git clone https://github.com/SadabAli/PhonePe-Transaction-Insights.git
cd PhonePe-Transaction-Insights
``` 
2. Install dependencie 
```
pip install -r requarments.txt 
``` 
3. Counfigure your MySQL 
4. In SQL Workbench create all the table only 
5. Run dashboard

```
streamlit run dashboard/app.py
```