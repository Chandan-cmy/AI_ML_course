import numpy as np
import pandas as pd

df = pd.DataFrame({
 'customer_id': range(1, 11),
 'age' : [25, 34, np.nan, 45, 28, np.nan, 52, 33, 41, np.nan],
 'income_lakh': [5.0, 12.0, np.nan, 20.0, 7.5, np.nan, 35.0, np.nan,18.0, 8.0],
 'purchased' : [0, 1, 1, 1, 0, 1, 1, 0, 1, 0]
})

print('Original data:',df)

print(f'Missing: age={df.age.isnull().sum()},income={df.income_lakh.isnull().sum()}')

df['age_missing'] = df['age'].isnull().astype(int)
df['income_missing'] = df['income_lakh'].isnull().astype(int)

df['age'] = df['age'].fillna(df['age'].median())
df['income_lakh'] = df['income_lakh'].fillna(df['income_lakh'].median())
print('\nAfter adding missing indicators and filling:')
print(df[['age', 'age_missing', 'income_lakh', 'income_missing','purchased']])

print(f'\nPurchase rate when income is known :',f"{df[df['income_missing']==0]['purchased'].mean():.2%}")
print(f'Purchase rate when income is MISSING :',f"{df[df['income_missing']==1]['purchased'].mean():.2%}")
