import pandas as pd

# Load raw data
data = pd.read_csv('../data/telco_customer_churn.csv')

# Drop duplicates
data = data.drop_duplicates()

# Fix TotalCharges type
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

# Add derived column: Customer Lifetime Value
data['CLV'] = data['tenure'] * data['MonthlyCharges']

# Save cleaned CSV
data.to_csv('../data/cleaned_telco_customer_churn.csv', index=False)
print("Cleaned data saved at ../data/cleaned_telco_customer_churn.csv")


