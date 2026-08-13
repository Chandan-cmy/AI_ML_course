import numpy as np
import pandas as pd

df = pd.read_csv('data/Listings.csv',encoding='latin1', nrows=50000)

print("data shape:", df.shape)
# print("data head:\n", df.head())
# print("data tail:\n", df.tail())


# print("data info:\n", df.info())

# print("missing values:\n", df.isnull().sum())
# print("missing values percentage:\n", df.isnull().sum()/len(df)*100)

print("duplicate rows:", df.duplicated().sum())
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

df_clean = df.copy()

cols_to_drop = [] # Add column names here after inspecting
if cols_to_drop:
    df_clean = df_clean.drop(columns=cols_to_drop)
    print(f'Dropped columns: {cols_to_drop}')


for col in numeric_cols:
    if df_clean[col].isnull().sum() > 0:
        fill_val = df_clean[col].median() # Use median for skewed data
        df_clean[col] = df_clean[col].fillna(fill_val)
        print(f' Filled {col} missing values with median: {fill_val:.2f}')
        
for col in categorical_cols:
    if df_clean[col].isnull().sum() > 0:
        fill_val = df_clean[col].mode()[0]
        df_clean[col] = df_clean[col].fillna(fill_val)
        print(f' Filled {col} missing values with mode: {fill_val}')

df_clean = df_clean.drop_duplicates()
print("duplicate rows after cleaning:", df_clean.duplicated().sum())

print(f'\nCleaning Summary:')
print(f' Before: {df.shape}')
print(f' After : {df_clean.shape}')
print(f' Missing values remaining: {df_clean.isnull().sum().sum()}')