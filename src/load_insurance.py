import os
import json
import pandas as pd
from tqdm import tqdm
from sqlalchemy import create_engine

# DB connection
engine = create_engine("mysql+pymysql://root:Sadab404@localhost:3306/phonepe_data")

# Paths
base_country_path = r'C:\Users\alisa\OneDrive\Desktop\PhonePe-Transaction-Insights\data\aggregated\insurance\country\india'
base_state_path = os.path.join(base_country_path, 'state')

# Initialize DataFrame
rows = []

# Step 4.1: Load country-level data
for year in range(2020, 2025):
    year_path = os.path.join(base_country_path, str(year))
    for q in range(1, 5):
        json_file = os.path.join(year_path, f"{q}.json")
        if os.path.exists(json_file):
            with open(json_file, 'r') as f:
                data = json.load(f)
                for entry in data['data']['transactionData']:
                    name = entry['name']
                    for instrument in entry['paymentInstruments']:
                        rows.append({
                            "level": "country",
                            "state_name": None,
                            "year": year,
                            "quarter": q,
                            "transaction_type": name,
                            "transaction_count": instrument['count'],
                            "transaction_amount": instrument['amount']
                        })

# Step 4.2: Load state-level data
for state in tqdm(os.listdir(base_state_path), desc="States"):
    state_path = os.path.join(base_state_path, state)
    for year in os.listdir(state_path):
        year_path = os.path.join(state_path, year)
        for q_file in os.listdir(year_path):
            if q_file.endswith(".json"):
                quarter = int(q_file.split(".")[0])
                with open(os.path.join(year_path, q_file), 'r') as f:
                    data = json.load(f)
                    for entry in data['data']['transactionData']:
                        name = entry['name']
                        for instrument in entry['paymentInstruments']:
                            rows.append({
                                "level": "state",
                                "state_name": state,
                                "year": int(year),
                                "quarter": quarter,
                                "transaction_type": name,
                                "transaction_count": instrument['count'],
                                "transaction_amount": instrument['amount']
                            })

# Convert to DataFrame and load into SQL
df = pd.DataFrame(rows)
df.to_sql(name='aggregated_insurance', con=engine, if_exists='append', index=False)

print("✅ Insurance data loaded successfully!")
