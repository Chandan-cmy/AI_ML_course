# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error, r2_score
# from sklearn.model_selection import train_test_split

# np.random.seed(42)
# hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 3.2], dtype=float)
# score = 8.5 * hours + 30 + np.random.randn(20) * 5

# x_mean = np.mean(hours)
# y_mean = np.mean(score)

# w_manual= np.sum((hours - x_mean) * (score - y_mean)) / np.sum((hours -x_mean)**2)
# b_manual= y_mean - w_manual * x_mean


# print("=== From-Scratch Solution ===")
# print(f"Weight (slope) : {w_manual:.4f}")
# print(f"Bias (intercept) : {b_manual:.4f}")
# print(f"Interpretation : Each extra study hour adds {w_manual:.1f} marks")
# X = hours.reshape(-1, 1)
# print(X)
# X_train, X_test, y_train, y_test = train_test_split(X, score, test_size=0.2, random_state=42)
# model = LinearRegression()
# model.fit(X_train, y_train)

# print("\n=== Sklearn Solution ===")
# print(f"Weight (slope) : {model.coef_[0]:.4f}")
# print(f"Bias (intercept) : {model.intercept_:.4f}")

# y_pred = model.predict(X_test)
# mse = mean_squared_error(y_test, y_pred)
# rmse = np.sqrt(mse)
# r2 = r2_score(y_test, y_pred)

# print("\n=== Evaluation on Test Set ===")
# print(f"MSE : {mse:.2f}")
# print(f"RMSE : {rmse:.2f} marks (off by ~{rmse:.0f} marks on average)")
# print(f"R² : {r2:.4f} (explains {r2*100:.1f}% of score variance)")

# plt.figure(figsize=(10, 6))
# plt.scatter(hours, score, color='#2196F3', alpha=0.7,s=80, label='Actual data', edgecolors='white')

# x_line = np.linspace(hours.min(), hours.max(), 100).reshape(-1, 1)
# y_line = model.predict(x_line)
# plt.plot(x_line, y_line, color='#E91E63', lw=2.5,label=f'Fit: score = {model.coef_[0]:.1f}*hours +{model.intercept_:.1f}')
# plt.title('Study Hours vs Exam Score — Linear Regression', fontsize=15,
# fontweight='bold')
# plt.xlabel('Study Hours', fontsize=13)
# plt.ylabel('Exam Score', fontsize=13)
# plt.legend(fontsize=11)
# plt.grid(True, alpha=0.4)
# plt.tight_layout()
# # plt.savefig('linear_regression_simple.png', dpi=150, bbox_inches='tight')
# plt.show()


# import numpy as np
# import pandas as pd
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error, r2_score
# import matplotlib.pyplot as plt

# np.random.seed(42)
# n = 300

# size_sqft = np.random.uniform(500, 3000, n)
# bedrooms = np.random.randint(1, 6, n).astype(float)
# age_years = np.random.uniform(0, 40, n)
# distance_km = np.random.uniform(1, 30, n)
# bathrooms = np.random.randint(1, 4, n).astype(float)

# price = (200 * size_sqft + 50000 * bedrooms + 30000 * bathrooms - 2000 * age_years - 10000 * distance_km + 500000+ np.random.randn(n) * 50000)

# df = pd.DataFrame({
#  'size_sqft' : size_sqft,
#  'bedrooms' : bedrooms,
#  'bathrooms' : bathrooms,
#  'age_years' : age_years,
#  'distance_km': distance_km,
#  'price' : price
# })

# print("Dataset preview:")
# print(df.head())
# print(f"\nShape: {df.shape}")

# feature_cols = ['size_sqft', 'bedrooms', 'bathrooms', 'age_years',
# 'distance_km']
# X = df[feature_cols]
# y = df['price']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# model = LinearRegression()
# model.fit(X_train, y_train)

# y_pred_train = model.predict(X_train)
# y_pred_test = model.predict(X_test)

# train_r2 = r2_score(y_train, y_pred_train)
# test_r2 = r2_score(y_test, y_pred_test)
# test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_test))

# print(f"\n=== Model Performance ===")
# print(f"Training R² : {train_r2:.4f}")
# print(f"Test R² : {test_r2:.4f}")
# print(f"Test RMSE : Rs. {test_rmse:,.0f}")


# print("=== Model Coefficients ===")
# print(f"{'Feature':>15} | {'Coefficient':>14} | {'Interpretation'}")
# print("-" * 75)

# for feature, coef in zip(feature_cols, model.coef_):
#     if coef > 0:
#         direction = f"adds Rs. {coef:,.0f} per unit increase"
#     else:
#         direction = f"reduces Rs. {abs(coef):,.0f} per unit increase"
#         print(f"{feature:>15} | {coef:>14,.0f} | {direction}")
# print(f"\n{'Intercept':>15} | {model.intercept_:>14,.0f} | Base price whenall features are 0")
# print("\n=== True Coefficients (what we built into the data) ===")
# true_coefs = {'size_sqft': 200, 'bedrooms': 50000, 'bathrooms': 30000,'age_years': -2000, 'distance_km': -10000}


# for feat, true_val in true_coefs.items():
#     learned = dict(zip(feature_cols, model.coef_))[feat]
#     print(f" {feat:>15}: learned={learned:>8,.0f} true={true_val:>8,} ",
#     f"error={abs(learned-true_val):,.0f}")


# import matplotlib.pyplot as plt
# import numpy as np
# fig, axes = plt.subplots(1, 2, figsize=(14, 5))
# # Chart 1: Actual vs Predicted
# axes[0].scatter(y_test, y_pred_test, alpha=0.5, color='#2196F3',s=40, edgecolors='white')
# # Perfect prediction line
# min_val = min(y_test.min(), y_pred_test.min())
# max_val = max(y_test.max(), y_pred_test.max())
# axes[0].plot([min_val, max_val], [min_val, max_val],'r--', lw=2, label='Perfect prediction')

# axes[0].set_title('Actual vs Predicted Prices', fontsize=13,
# fontweight='bold')
# axes[0].set_xlabel('Actual Price (Rs.)', fontsize=11)
# axes[0].set_ylabel('Predicted Price (Rs.)', fontsize=11)
# axes[0].legend(fontsize=10)
# axes[0].grid(True, alpha=0.4)
# # Chart 2: Residuals plot
# residuals = y_test - y_pred_test
# axes[1].scatter(y_pred_test, residuals, alpha=0.5, color='#FF5722',
#  s=40, edgecolors='white')
# axes[1].axhline(y=0, color='black', lw=2, ls='--')
# axes[1].set_title('Residuals vs Predicted Values', fontsize=13,
# fontweight='bold')
# axes[1].set_xlabel('Predicted Price (Rs.)', fontsize=11)
# axes[1].set_ylabel('Residual (Actual - Predicted)', fontsize=11)
# axes[1].grid(True, alpha=0.4)
# plt.suptitle('Linear Regression Diagnostics', fontsize=15,
# fontweight='bold')
# plt.tight_layout()
# # plt.savefig('regression_diagnostics.png', dpi=150, bbox_inches='tight')
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np

# coefs = model.coef_
# colours = ['#2196F3' if c > 0 else '#E91E63' for c in coefs]

# plt.figure(figsize=(10, 6))
# bars = plt.barh(feature_cols, coefs, color=colours, edgecolor='white',height=0.6)

# for bar, val in zip(bars, coefs):
#     label = f'Rs. {val:,.0f}'
#     x_pos = val + 1000 if val > 0 else val - 1000
#     plt.text(x_pos, bar.get_y() + bar.get_height()/2,label, va='center', ha='left' if val>0 else 'right',fontsize=10)


# plt.axvline(x=0, color='black', lw=1)
# plt.title('Feature Coefficients — Impact on House Price',
#  fontsize=14, fontweight='bold')
# plt.xlabel('Coefficient Value (Rs. per unit change)', fontsize=12)
# plt.grid(axis='x', alpha=0.4)
# plt.tight_layout()
# # plt.savefig('coefficients.png', dpi=150, bbox_inches='tight')
# plt.show()
# print("Blue bars = positive effect (higher value = higher price)")
# print("Pink bars = negative effect (higher value = lower price)")

# import numpy as np
# from sklearn.metrics import r2_score

# y_true = np.array([100, 150, 200, 250, 300, 350, 400])

# y_perfect = y_true.copy()

# y_good = y_true + np.array([5, -3, 8, -6, 4, -2, 7])

# y_mean = np.full_like(y_true, y_true.mean(), dtype=float)

# np.random.seed(0)
# y_terrible = np.random.uniform(50, 500, len(y_true))

# print(f"R² scores:")
# print(f" Perfect model : {r2_score(y_true, y_perfect):.4f}")
# print(f" Good model : {r2_score(y_true, y_good):.4f}")
# print(f" Mean predictor : {r2_score(y_true, y_mean):.4f}")
# print(f" Terrible model : {r2_score(y_true, y_terrible):.4f}")
# print("\nInterpretation:")
# print(" Good model explains",f"{r2_score(y_true, y_good)*100:.1f}% of the variation in thetarget")


# import numpy as np
# from sklearn.metrics import mean_squared_error, mean_absolute_error

# y_true = np.array([50, 60, 45, 80, 55, 70, 40, 90, 200])
# y_pred_a = np.array([52, 58, 47, 78, 57, 68, 42, 88, 180])
# y_pred_b = np.array([53, 61, 43, 82, 54, 73, 38, 94, 199])

# for name, y_pred in [('Model A', y_pred_a), ('Model B', y_pred_b)]:
#     rmse = np.sqrt(mean_squared_error(y_true, y_pred))
#     mae = mean_absolute_error(y_true, y_pred)
#     print(f"{name}: RMSE={rmse:.2f} MAE={mae:.2f}")
# print("\nRMSE punishes large errors more heavily (squaring effect).")
# print("MAE treats all errors equally regardless of size.")
# print("If large errors are very costly — use RMSE.")
# print("If all errors are equally important — use MAE.")
# ----------------------------------------------------------------------------------------------------------------------------------------------
# import numpy as np
# import pandas as pd
# from sklearn.linear_model import LinearRegression

# # New houses to price (not in the training set)


# X = pd.DataFrame({
#     'size_sqft': [1000, 1500, 2000, 2500, 3000],
#     'bedrooms': [2, 3, 3, 4, 5],
#     'bathrooms': [1, 2, 2, 3, 4],
#     'age_years': [10, 5, 8, 15, 2],
#     'distance_km': [15, 10, 7, 5, 8]
# })

# y = [
#     3000000,
#     4000000,
#     5000000,
#     6000000,
#     7500000
# ]

# new_houses = pd.DataFrame({
#  'size_sqft' : [1200, 2500, 800, 3000],
#  'bedrooms' : [2, 4, 1, 5 ],
#  'bathrooms' : [1, 3, 1, 4 ],
#  'age_years' : [5, 15, 30, 2 ],
#  'distance_km': [10, 5, 20, 8 ]
# })

# model = LinearRegression()
# model.fit(X, y)


# predicted_prices = model.predict(new_houses)
# print("New House Valuations:")
# print("-" * 65)

# descriptions = [
#  '2BHK starter flat near city',
#  '4BHK spacious family home, good location',
#  '1BHK old flat far from city',
#  '5BHK luxury new home, prime location'
# ]


# for i, (desc, price) in enumerate(zip(descriptions, predicted_prices)):
#     print(f"House {i+1}: {desc}")
#     print(f" Predicted price: Rs. {price:,.0f}")
#     print()

# h1_manual = (198 * 1200 # size contribution
#  + 49821 * 2 # bedrooms
#  + 29954 * 1 # bathrooms
#  - 2031 * 5 # age penalty
#  - 9887 * 10 # distance penalty
#  + 498762) # intercept
# print(f"Manual calculation for House 1: Rs. {h1_manual:,.0f}")
# print(f"Model prediction for House 1 : Rs. {predicted_prices[0]:,.0f}")
# print("(Small difference due to rounding in printed coefficients)")


# import pandas as pd
# from sklearn.linear_model import LinearRegression

# # --------------------------------------------------
# # STEP 1: Training data
# # --------------------------------------------------

# data = pd.DataFrame({
#     'size_sqft': [800, 1000, 1200, 1500, 1800, 2000, 2500, 3000],
#     'bedrooms': [1, 2, 2, 3, 3, 4, 4, 5],
#     'bathrooms': [1, 1, 2, 2, 2, 3, 3, 4],
#     'age_years': [20, 15, 10, 8, 5, 10, 5, 2],
#     'distance_km': [20, 15, 12, 10, 8, 7, 5, 3],
#     'price': [500000, 650000, 800000, 1000000,
#               1200000, 1400000, 1600000, 2000000]
# })

# # --------------------------------------------------
# # STEP 2: Separate input features and target
# # --------------------------------------------------

# X = data[['size_sqft', 'bedrooms', 'bathrooms',
#           'age_years', 'distance_km']]

# y = data['price']

# # --------------------------------------------------
# # STEP 3: Create the Linear Regression model
# # --------------------------------------------------

# model = LinearRegression()

# # --------------------------------------------------
# # STEP 4: Train the model
# # --------------------------------------------------

# model.fit(X, y)

# # --------------------------------------------------
# # STEP 5: Create NEW houses
# # These houses were NOT used during training
# # --------------------------------------------------

# new_houses = pd.DataFrame({
#     'size_sqft': [1200, 2500, 800, 3000],
#     'bedrooms': [2, 4, 1, 5],
#     'bathrooms': [1, 3, 1, 4],
#     'age_years': [5, 15, 30, 2],
#     'distance_km': [10, 5, 20, 8]
# })

# # --------------------------------------------------
# # STEP 6: Predict prices for the new houses
# # --------------------------------------------------

# predicted_prices = model.predict(new_houses)

# # --------------------------------------------------
# # STEP 7: Display the predictions
# # --------------------------------------------------

# for i, price in enumerate(predicted_prices):
#     print(f"House {i + 1} predicted price: Rs. {price:,.0f}")

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from scipy import stats

# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression

# # --------------------------------------------------
# # STEP 1: Create house data
# # --------------------------------------------------

# data = pd.DataFrame({
#     'size_sqft': [800, 1000, 1200, 1500, 1800, 2000, 2200, 2500,
#                   2700, 3000, 3200, 3500],
    
#     'bedrooms': [1, 2, 2, 3, 3, 4, 4, 4,
#                  5, 5, 5, 6],
    
#     'bathrooms': [1, 1, 2, 2, 2, 3, 3, 3,
#                   4, 4, 4, 5],
    
#     'age_years': [20, 15, 10, 8, 5, 10, 7, 5,
#                   4, 3, 2, 1],
    
#     'distance_km': [20, 15, 12, 10, 8, 7, 6, 5,
#                     4, 3, 2, 2],
    
#     'price': [500000, 650000, 800000, 1000000, 1200000, 1400000,
#               1500000, 1650000, 1800000, 2000000, 2200000, 2500000]
# })

# # --------------------------------------------------
# # STEP 2: Separate features and target
# # --------------------------------------------------

# X = data[['size_sqft', 'bedrooms', 'bathrooms',
#           'age_years', 'distance_km']]

# y = data['price']

# # --------------------------------------------------
# # STEP 3: Split into training and testing data
# # --------------------------------------------------

# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.25, random_state=42
# )

# # --------------------------------------------------
# # STEP 4: Create and train the model
# # --------------------------------------------------

# model = LinearRegression()

# model.fit(X_train, y_train)

# # --------------------------------------------------
# # STEP 5: Make predictions on test data
# # --------------------------------------------------

# y_pred_test = model.predict(X_test)

# # --------------------------------------------------
# # STEP 6: Calculate residuals
# # --------------------------------------------------

# residuals = y_test.values - y_pred_test

# # --------------------------------------------------
# # STEP 7: Create three graphs
# # --------------------------------------------------

# fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# # ==================================================
# # GRAPH 1: Histogram of residuals
# # ==================================================

# axes[0].hist(
#     residuals,
#     bins=10,
#     edgecolor='white'
# )

# axes[0].set_title('Residual Distribution')
# axes[0].set_xlabel('Residual')
# axes[0].set_ylabel('Frequency')

# # ==================================================
# # GRAPH 2: Q-Q Plot
# # ==================================================

# stats.probplot(
#     residuals,
#     dist='norm',
#     plot=axes[1]
# )

# axes[1].set_title('Q-Q Plot')

# # ==================================================
# # GRAPH 3: Residuals vs Predicted Values
# # ==================================================

# axes[2].scatter(
#     y_pred_test,
#     residuals,
#     alpha=0.6,
#     s=40
# )

# axes[2].axhline(
#     y=0,
#     linestyle='--'
# )

# axes[2].set_title('Residuals vs Predicted Values')
# axes[2].set_xlabel('Predicted Values')
# axes[2].set_ylabel('Residuals')

# # --------------------------------------------------
# # STEP 8: Overall title
# # --------------------------------------------------

# plt.suptitle(
#     'Regression Assumption Checks',
#     fontsize=14,
#     fontweight='bold'
# )

# plt.tight_layout()

# # Save the graph
# # plt.savefig(
# #     'assumption_checks.png',
# #     dpi=150,
# #     bbox_inches='tight'
# # )

# plt.show()


# import numpy as np
# import pandas as pd
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error, mean_absolute_error,r2_score
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.set_theme(style='whitegrid')


# from sklearn.datasets import load_diabetes
# data = load_diabetes()
# df = pd.DataFrame(data.data, columns=data.feature_names)
# df['target'] = data.target
# print(f'Dataset: {df.shape[0]} samples, {df.shape[1]-1} features')
# print(f'Target: Disease progression score (higher = worse)')
# print(f'Range: {df.target.min():.0f} to {df.target.max():.0f}')

# print(f'\nMissing values: {df.isnull().sum().sum()}')
# print(df.describe().round(2))

# X = df.drop(columns=['target'])
# y = df['target']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# print(f'\nTrain: {X_train.shape}, Test: {X_test.shape}')


# from sklearn.dummy import DummyRegressor
# dummy = DummyRegressor(strategy='mean').fit(X_train, y_train)
# y_d_pred = dummy.predict(X_test)
# base_rmse= np.sqrt(mean_squared_error(y_test, y_d_pred))
# print(f'\nBaseline RMSE (always predict mean): {base_rmse:.2f}')

# model = LinearRegression()
# model.fit(X_train, y_train)


# y_pred = model.predict(X_test)
# rmse = np.sqrt(mean_squared_error(y_test, y_pred))
# mae = mean_absolute_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)
# train_r2 = r2_score(y_train, model.predict(X_train))

# print(f'\nLinear Regression Results:')
# print(f' Train R² : {train_r2:.4f}')
# print(f' Test R² : {r2:.4f}')
# print(f' Test RMSE: {rmse:.2f} (vs baseline {base_rmse:.2f})')
# print(f' Test MAE : {mae:.2f}')
# print(f' Improvement over baseline: {((base_rmse - rmse) / base_rmse) * 100:.1f}%')

# coef_df = pd.DataFrame({
#  'Feature' : X.columns,
#  'Coefficient': model.coef_
# }).sort_values('Coefficient', key=abs, ascending=False)
# print('\nFeature Importance (by absolute coefficient):')
# print(coef_df.to_string(index=False))


# Exercise 1 — Simple Regression on Advertising Data (Beginner)

# import numpy as np
# import pandas as pd
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error, r2_score
# import matplotlib.pyplot as plt

# np.random.seed(42)

# df= pd.DataFrame({
#     "tv price(in thousands)": [np.random.randint(10,300,size=10)],
# })


# sales = 0.05 * df["tv price(in thousands)"] + 7 + np.random.normal(0, 1, 10)

# X=df[["tv price(in thousands)"]]
# y=sales
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# model = LinearRegression()
# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)

# rmse = np.sqrt(mean_squared_error(y_test, y_pred))
# mae = np.mean(np.abs(y_test - y_pred))
# r2 = r2_score(y_test, y_pred)

# print(f"Test RMSE: {rmse:.2f}")
# print(f"Test MAE: {mae:.2f}")
# print(f"Test R²: {r2:.4f}")


# plt.scatter(X_test, y_test, color='RED', label='Actual data', edgecolors='white')
# plt.plot(X_test, y_pred, color='BLUE', label='Predicted data')
# plt.xlabel('TV Price (in thousands)')
# plt.ylabel('Sales (units)')
# plt.legend()
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt

# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error, r2_score


# np.random.seed(42)

# TV = np.linspace(10, 300, 100)



# true_coefficient = 0.05
# true_intercept = 7

# noise = np.random.normal(0, 1, 100)

# sales = (
#     true_coefficient * TV
#     + true_intercept
#     + noise
# )



# X_train, X_test, y_train, y_test = train_test_split(
#     TV,
#     sales,
#     test_size=0.2,
#     random_state=42
# )


# model = LinearRegression()



# model.fit(X_train.reshape(-1, 1), y_train)


# y_pred = model.predict(X_test.reshape(-1, 1))


# rmse = np.sqrt(mean_squared_error(y_test, y_pred))
# r2 = r2_score(y_test, y_pred)

# print("Model Results")
# print("-" * 30)

# print(f"True coefficient: {true_coefficient:.4f}")
# print(f"Learned coefficient: {model.coef_[0]:.4f}")

# print(f"RMSE: {rmse:.2f}")
# print(f"R²: {r2:.4f}")



# plt.scatter(TV, sales, label="Actual data")

# TV_line = np.linspace(10, 300, 100)

# sales_line = model.predict(
#     TV_line.reshape(-1, 1)
# )

# plt.plot(
#     TV_line,
#     sales_line,
#     label="Fitted regression line"
# )

# plt.xlabel("TV Advertising Spend (Rs. thousands)")
# plt.ylabel("Sales (units)")

# plt.title("TV Advertising Spend vs Sales")

# plt.legend()

# plt.show()



# print()
# print(
#     f"Business interpretation: "
#     f"For every additional Rs. 1,000 spent on TV advertising, "
#     f"sales are expected to increase by approximately "
#     f"{model.coef_[0]:.2f} units on average."
# )


# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.datasets import fetch_california_housing
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


# data = fetch_california_housing()

# df = pd.DataFrame(data.data, columns=data.feature_names)

# df["MedHouseVal"] = data.target

# print("Dataset shape:", df.shape)
# print("\nFirst 5 rows:")
# print(df.head())


# X = df.drop(columns=["MedHouseVal"])
# y = df["MedHouseVal"]


# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.20,
#     random_state=42
# )

# print("\nTraining samples:", X_train.shape[0])
# print("Testing samples :", X_test.shape[0])

# model = LinearRegression()

# model.fit(X_train, y_train)



# y_pred = model.predict(X_test)

# rmse = np.sqrt(mean_squared_error(y_test, y_pred))
# mae = mean_absolute_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)

# print("\n" + "=" * 50)
# print("LINEAR REGRESSION RESULTS")
# print("=" * 50)

# print(f"RMSE : {rmse:.4f}")
# print(f"MAE  : {mae:.4f}")
# print(f"R²   : {r2:.4f}")


# coef_df = pd.DataFrame({
#     "Feature": X.columns,
#     "Coefficient": model.coef_
# })

# coef_df["Absolute_Coefficient"] = coef_df["Coefficient"].abs()

# coef_df = coef_df.sort_values(
#     by="Absolute_Coefficient",
#     ascending=False
# )

# print("\n" + "=" * 50)
# print("FEATURE COEFFICIENTS")
# print("=" * 50)

# print(
#     coef_df[
#         ["Feature", "Coefficient"]
#     ].to_string(index=False)
# )


# largest_positive = coef_df.loc[
#     coef_df["Coefficient"].idxmax()
# ]

# largest_negative = coef_df.loc[
#     coef_df["Coefficient"].idxmin()
# ]


# print(
#     f"Largest positive impact: "
#     f"{largest_positive['Feature']} "
#     f"({largest_positive['Coefficient']:.4f})"
# )

# print(
#     f"Largest negative impact: "
#     f"{largest_negative['Feature']} "
#     f"({largest_negative['Coefficient']:.4f})"
# )


# plt.scatter(y_test,y_pred,alpha=0.5)

# plt.xlabel("Actual House Value")
# plt.ylabel("Predicted House Value")
# plt.title("Actual vs Predicted House Values")


# min_value = min(y_test.min(), y_pred.min())
# max_value = max(y_test.max(), y_pred.max())

# plt.plot(
#     [min_value, max_value],
#     [min_value, max_value],
#     linestyle="--",
#     linewidth=2
# )

# plt.tight_layout()
# plt.savefig(
#     "01_actual_vs_predicted.png",
#     dpi=300,
#     bbox_inches="tight"
# )
# plt.figure(figsize=(8, 6))

# plt.scatter(
#     y_pred,
#     residuals,
#     alpha=0.5
# )

# # Zero residual reference line
# plt.axhline(
#     y=0,
#     linestyle="--",
#     linewidth=2
# )

# plt.xlabel("Predicted House Value")
# plt.ylabel("Residual")
# plt.title("Residuals vs Predicted Values")

# plt.tight_layout()

# plt.savefig(
#     "02_residuals_vs_predicted.png",
#     dpi=300,
#     bbox_inches="tight"
# )


# plt.figure(figsize=(8, 6))

# plt.hist(
#     residuals,
#     bins=30,
#     edgecolor="black"
# )

# plt.xlabel("Residual")
# plt.ylabel("Frequency")
# plt.title("Histogram of Residuals")

# plt.tight_layout()

# plt.savefig(
#     "03_residual_histogram.png",
#     dpi=300,
#     bbox_inches="tight"
# )

# plt.show()



# Exercise 4 — Manual Prediction

# import numpy as np
# import pandas as pd
# from sklearn.datasets import fetch_california_housing
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression

# data = fetch_california_housing()

# df = pd.DataFrame(data.data, columns=data.feature_names)
# df["MedHouseVal"] = data.target

# X = df.drop(columns=["MedHouseVal"])
# y = df["MedHouseVal"]


# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.20,
#     random_state=42
# )


# model = LinearRegression()
# model.fit(X_train, y_train)


# house = X_test.iloc[0].values

# print("House features:")
# print(house)


# manual_prediction = model.intercept_ + np.sum(
#     model.coef_ * house
# )

# model_prediction = model.predict(
#     house.reshape(1, -1)
# )[0]


# print(f"Intercept (b0): {model.intercept_:.10f}")

# print("\nCoefficients:")
# for feature, coefficient in zip(X.columns, model.coef_):
#     print(f"{feature:12s}: {coefficient:.10f}")

# print("\nManual prediction :", manual_prediction)
# print("model.predict()   :", model_prediction)

# print("\nDifference:", manual_prediction - model_prediction)


# import numpy as np
# import pandas as pd
# from sklearn.datasets import fetch_california_housing
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression

# data = fetch_california_housing()

# df = pd.DataFrame(data.data, columns=data.feature_names)

# df["MedHouseVal"] = data.target

# correlation_matrix = df.corr()[["MedHouseVal"]].drop("MedHouseVal")

# correlation_raking = correlation_matrix["MedHouseVal"].abs().sort_values(ascending=False)
# print("Correlation with Median House Value:")
# print(correlation_raking)

# X=df[data.feature_names]
# y=df["MedHouseVal"]

# X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.20, random_state=42)

# model = LinearRegression()
# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)

# coefficients_df = pd.Series(
#     model.coef_, 
#     index = X.columns
#     )

# coefficents_ranking = coefficients_df.abs().sort_values(ascending=False)
# print("coefficients ranking:")
# print(coefficents_ranking)

# import numpy as np
# import pandas as pd
# from sklearn.datasets import fetch_california_housing
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression

# data = fetch_california_housing()
# df = pd.DataFrame(data.data, columns=data.feature_names)

# df["MedHouseVa



import numpy as np
import pandas as pd

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


data = fetch_california_housing()

df = pd.DataFrame(
    data.data,
    columns=data.feature_names
)

df["MedHouseVal"] = data.target


X = df.drop(columns=["MedHouseVal"])
y = df["MedHouseVal"]


X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20,random_state=42)


X_train_np = X_train.to_numpy()
X_test_np = X_test.to_numpy()

X_train_intercept = np.column_stack(
    (np.ones(X_train_np.shape[0]), X_train_np)
)

X_test_intercept = np.column_stack(
    (np.ones(X_test_np.shape[0]), X_test_np)
)


W = (
    np.linalg.inv(
        X_train_intercept.T @ X_train_intercept
    )
    @ X_train_intercept.T
    @ y_train.to_numpy()
)

intercept_manual = W[0]

coefficients_manual = W[1:]

y_pred_manual = X_test_intercept @ W


rmse_manual = np.sqrt(
    np.mean((y_test.to_numpy() - y_pred_manual) ** 2)
)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred_sklearn = model.predict(X_test)

rmse_sklearn = np.sqrt(
    np.mean((y_test.to_numpy() - y_pred_sklearn) ** 2)
)



print("NORMAL EQUATION vs SKLEARN LINEAR REGRESSION")

print("\nIntercept:")
print(f"Manual  : {intercept_manual:.10f}")
print(f"sklearn : {model.intercept_:.10f}")

print("\nCoefficients:")
print(
    f"{'Feature':<15}"
    f"{'Manual':>18}"
    f"{'sklearn':>18}"
    f"{'Difference':>18}"
)


for feature, manual, sklearn_coef in zip(
    X.columns,
    coefficients_manual,
    model.coef_
):
    difference = manual - sklearn_coef

    print(
        f"{feature:<15}"
        f"{manual:>18.10f}"
        f"{sklearn_coef:>18.10f}"
        f"{difference:>18.10f}"
    )


print("RMSE COMPARISON")

print(f"Manual RMSE  : {rmse_manual:.10f}")
print(f"sklearn RMSE : {rmse_sklearn:.10f}")

print(f"\nRMSE Difference: {abs(rmse_manual - rmse_sklearn):.10f}")

print("VERIFICATION")

if np.allclose(
    coefficients_manual,
    model.coef_,
    rtol=1e-6,
    atol=1e-6
) and np.isclose(
    intercept_manual,
    model.intercept_,
    rtol=1e-6,
    atol=1e-6
):
    print("Coefficients match to 6+ decimal places")

else:
    print("Coefficients do not match")


if np.isclose(
    rmse_manual,
    rmse_sklearn,
    rtol=1e-6,
    atol=1e-6
):
    print("RMSE values match to 6+ decimal places")

else:
    print("RMSE values do not match")