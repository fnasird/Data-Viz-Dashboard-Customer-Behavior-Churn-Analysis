import pandas as pd
from sqlalchemy import create_engine

# Load raw data
data = pd.read_csv('../data/telco_customer_churn.csv')

# Data quality checks
print("Missing values:\n", data.isnull().sum())
print("\nDuplicate rows:", data.duplicated().sum())

# Drop duplicates
data = data.drop_duplicates()

# Fix TotalCharges type and fill missing
data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')
data['TotalCharges'].fillna(data['TotalCharges'].median(), inplace=True)

# Convert categorical columns
categorical_cols = ['gender', 'Partner', 'Dependents', 'PhoneService',
                    'MultipleLines', 'InternetService', 'OnlineSecurity',
                    'OnlineBackup', 'DeviceProtection', 'TechSupport',
                    'StreamingTV', 'StreamingMovies', 'Contract',
                    'PaperlessBilling', 'PaymentMethod', 'Churn']

for col in categorical_cols:
    data[col] = data[col].astype('category')

# Add derived metric: Customer Lifetime Value
data['CLV'] = data['tenure'] * data['MonthlyCharges']

# Save cleaned CSV
data.to_csv('../data/cleaned_telco_customer_churn.csv', index=False)
print("Cleaned data saved at ../data/cleaned_telco_customer_churn.csv")

# Optional: Insert into SQL database
# Uncomment and configure the following if you have PostgreSQL/MySQL
# engine = create_engine('postgresql://username:password@localhost:5432/yourdb')
# data.to_sql('customers', engine, if_exists='replace', index=False)
# print("Data loaded into SQL database successfully.")
