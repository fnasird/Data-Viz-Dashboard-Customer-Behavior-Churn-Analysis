import pandas as pd
from sqlalchemy import create_engine

# Load cleaned CSV
df = pd.read_csv('../data/cleaned_telco_customer_churn.csv')

# Connect to SQL database
engine = create_engine('postgresql://username:password@localhost:5432/yourdb')

# Insert data into SQL table
df.to_sql('customers', engine, if_exists='replace', index=False)
print("Data inserted into SQL database successfully.")
