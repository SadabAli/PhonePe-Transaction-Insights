# queries.py

# KPIs
kpi_transaction_amount = """
SELECT SUM(transaction_amount) AS total_amount FROM aggregated_transaction;
"""

kpi_transaction_count = """
SELECT SUM(transaction_count) AS total_count FROM aggregated_transaction;
"""

kpi_registered_users = """
SELECT SUM(user_count) AS total_users FROM aggregated_user;
"""

kpi_app_opens = """
SELECT SUM(app_opens) AS total_opens FROM map_user;
"""
