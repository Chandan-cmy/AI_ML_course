import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

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

n_numeric = len(numeric_cols)
n_cols = 2
n_rows = (n_numeric + 1) // 2

fig, axes = plt.subplots(n_rows, n_cols,figsize=(14, 4 * n_rows))

axes = axes.flatten()

for i, col in enumerate(numeric_cols):
    axes[i].hist(df_clean[col].dropna(), bins=30,color='#2196F3', edgecolor='white', linewidth=0.8)
    axes[i].axvline(df_clean[col].median(), color='red',ls='--', lw=2, label=f'Median:{df_clean[col].median():.1f}')
    axes[i].set_title(f'Distribution of {col}', fontweight='bold')
    axes[i].set_xlabel(col)
    axes[i].set_ylabel('Count')
    axes[i].legend(fontsize=10)
    axes[i].grid(axis='y', alpha=0.5)


for j in range(i+1, len(axes)):
    axes[j].set_visible(False)
plt.suptitle('Distribution of All Numeric Variables',fontsize=16, fontweight='bold', y=1.01)
plt.tight_layout()
plt.savefig('charts/01_univariate_numeric.png', dpi=150,bbox_inches='tight')
plt.show()
print('\nChart saved: 01_univariate_numeric.png')

for col in categorical_cols:
    if df_clean[col].nunique() <= 15: 
        plt.figure(figsize=(10, 5))
        vc = df_clean[col].value_counts().head(10)
        bars = plt.bar(vc.index, vc.values, color='#4CAF50',edgecolor='white')
        for bar in bars:
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() +0.5,
            str(int(bar.get_height())), ha='center', fontsize=10,fontweight='bold')
            plt.title(f'Top 10 Values in: {col}', fontsize=14,fontweight='bold')
            plt.xlabel(col); plt.ylabel('Count')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.savefig(f'charts/02_univariate_{col}.png', dpi=150,bbox_inches='tight')
        
plt.figure(figsize=(12, 8))
corr_matrix = df_clean[numeric_cols].corr()
sns.heatmap(
    corr_matrix,
    annot = True,
    fmt = '.2f',
    cmap = 'coolwarm',
    center = 0,
    square = True,
    linewidths= 0.5,
    cbar_kws = {'shrink': 0.8}
    )
plt.title('Correlation Matrix', fontsize=15, fontweight='bold', pad=15)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('charts/03_correlation_heatmap.png', dpi=150,
bbox_inches='tight')
plt.show()

target_col = 'price' # <-- CHANGE THIS to your target column
if target_col in numeric_cols:
    print(f'\nTop correlations with {target_col}:')
    corr_with_target = corr_matrix[target_col].drop(target_col)
    print(corr_with_target.sort_values(key=abs, ascending=False))
    
for cat_col in categorical_cols[:3]: # First 3 categorical columns
    if df_clean[cat_col].nunique() <= 8:
        plt.figure(figsize=(12, 6))
        sns.boxplot(
        data = df_clean,
        x = cat_col,
        y = target_col,
        palette = 'Blues'
        )
        plt.title(f'{target_col} by {cat_col}',
        fontsize=14, fontweight='bold')
        plt.xticks(rotation=30, ha='right')
        plt.tight_layout()
        plt.savefig(f'charts/04_box_{cat_col}.png', dpi=150,bbox_inches='tight')
        plt.show()


if target_col in numeric_cols:
    top_features = corr_matrix[target_col].drop(target_col)\
    .sort_values(key=abs, ascending=False).head(2).index
    fig, axes = plt.subplots(1, len(top_features), figsize=(14, 5))
    if len(top_features) == 1:
        axes = [axes]
    for ax, feat in zip(axes, top_features):
        ax.scatter(df_clean[feat], df_clean[target_col],
        alpha=0.4, color='#2196F3', s=20)
        ax.set_xlabel(feat, fontsize=12)
        ax.set_ylabel(target_col, fontsize=12)
        ax.set_title(f'{feat} vs {target_col}', fontweight='bold')
        ax.grid(True, alpha=0.4)
        plt.suptitle('Key Feature Relationships', fontsize=15,fontweight='bold')
        plt.tight_layout()
        plt.savefig('charts/05_scatter_relationships.png', dpi=150,bbox_inches='tight')
        plt.show()


