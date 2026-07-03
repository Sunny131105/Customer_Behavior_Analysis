# %%
import pandas as pd
import numpy as np


# %%
df = pd.read_csv("R:\\Customer Churn Analysis\\customer_shopping_behavior.csv")

df.head()

# %%
df.info()

# %%
df.describe()

# %%
df.isnull().sum()

# %%
df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))

# %%
df.isnull().sum()

# %%
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ', '_')

# %%
df.columns

# %%
df = df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})
df.columns

# %%
labels = ['Young Adult', 'Adult', 'Middle-aged', 'Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels=labels)

df[['age', 'age_group']].head(10)

# %%
frequency_mapping = {
    'Fortnightly' : 14,
    'Weekly' : 7 ,
    'Monthly' : 30,
    'Quarterly' : 90,
    'Bi-Weekly' : 14,
    'Annually' : 365,
    'Every 3 Months' : 90
}

df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)

# %%
df[['purchase_frequency_days', 'frequency_of_purchases']].head(10)

# %%
df[['discount_applied','promo_code_used']].head(10)

# %%
df = df.drop(['promo_code_used'], axis=1)

# %%
df.columns

# %%
df.to_csv("customer_churn_analysis.csv", index=False)

# %%
pip install psycopg2-binary

# %%
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="customer_churn_analysis",   # your database name
    user="postgres",
    password="7078"                       # your PostgreSQL password
)

print("Connected Successfully!")

# %%
import pandas as pd

query = "SELECT * FROM customer_churn_analysis;"

df = pd.read_sql(query, conn)

print(df.head())

# %%



