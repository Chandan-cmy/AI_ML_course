# import numpy as np
# import pandas as pd
# import xgboost as xgb
# from sklearn.datasets import load_breast_cancer
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score, roc_auc_score, classification_report
# from sklearn.ensemble import RandomForestClassifier
# import warnings
# warnings.filterwarnings('ignore')

# data = load_breast_cancer()
# X, y = data.data, data.target
# X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# xgb_clf = xgb.XGBClassifier(
#  n_estimators = 300,
#  learning_rate = 0.05, # eta: small lr needs more trees
#  max_depth = 4, # depth of each tree
#  subsample = 0.8, # fraction of rows per tree
#  colsample_bytree = 0.8, # fraction of features per tree
#  reg_alpha = 0.1, # L1 regularisation
#  reg_lambda = 1.0, # L2 regularisation
#  use_label_encoder = False,
#  eval_metric = 'logloss',
#  random_state = 42,
#  n_jobs = -1
# )

# xgb_clf.fit(X_tr, y_tr)

# rf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
# rf.fit(X_tr, y_tr)

# for name, model in [('Random Forest', rf), ('XGBoost', xgb_clf)]:
#     y_pred = model.predict(X_te)
#     y_proba = model.predict_proba(X_te)[:,1]
#     acc = accuracy_score(y_te, y_pred)
#     auc = roc_auc_score(y_te, y_proba)
#     print(f'{name:15}: Accuracy={acc:.4f} AUC={auc:.4f}')
# print('\nXGBoost Classification Report:')
# print(classification_report(y_te, xgb_clf.predict(X_te), target_names=data.target_names))




# import numpy as np
# import xgboost as xgb
# from sklearn.datasets import fetch_california_housing
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error, r2_score
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.linear_model import LinearRegression

# data = fetch_california_housing()
# X_tr, X_te, y_tr, y_te = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

# xgb_reg = xgb.XGBRegressor(
#  n_estimators = 500,
#  learning_rate = 0.05,
#  max_depth = 5,
#  subsample = 0.8,
#  colsample_bytree = 0.8,
#  reg_alpha = 0.1,
#  random_state = 42,
#  n_jobs = -1
# )

# xgb_reg.fit(X_tr, y_tr)

# models = {
#  'Linear Regression' : LinearRegression(),
#  'Random Forest' : RandomForestRegressor(n_estimators=100,
#  random_state=42, n_jobs=-1),
#  'XGBoost' : xgb_reg
# }

# print(f"{'Model':20} | {'Test R²':>10} | {'Test RMSE':>10}")
# print('-' * 48)
# for name, m in models.items():
#     if name != 'XGBoost':
#         m.fit(X_tr, y_tr)
#     r2 = r2_score(y_te, m.predict(X_te))
#     rmse = np.sqrt(mean_squared_error(y_te, m.predict(X_te)))
#     print(f"{name:20} | {r2:>10.4f} | {rmse:>10.4f}")

# import numpy as np
# import xgboost as xgb
# from sklearn.datasets import load_breast_cancer
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score

# data = load_breast_cancer()
# X, y = data.data, data.target

# X_tr, X_temp, y_tr, y_temp = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
# X_val, X_te, y_val, y_te = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42, stratify=y_temp)

# print(f'Train: {X_tr.shape}, Val: {X_val.shape}, Test: {X_te.shape}')

# xgb_es = xgb.XGBClassifier(
#  n_estimators = 1000, # set high; early stopping will find best
#  learning_rate = 0.05,
#  max_depth = 4,
#  subsample = 0.8,
#  colsample_bytree = 0.8,
#  eval_metric = 'logloss',
#  early_stopping_rounds = 30, # stop if no improvement for 30 rounds
#  random_state = 42,
#  n_jobs = -1
# )

# xgb_es.fit(
#     X_tr, y_tr,
#     eval_set = [(X_val, y_val)],
#     verbose = 50 # print every 50 rounds
# )

print(f'\nBest iteration : {xgb_es.best_iteration}')
print(f'Best val logloss : {xgb_es.best_score:.4f}')
print(f'Test accuracy : {accuracy_score(y_te, xgb_es.predict(X_te)):.4f}')
print(f'\nModel stopped at {xgb_es.best_iteration} trees instead of 1000.')
print(f'Early stopping found the sweet spot automatically!')

