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

# print(f'\nBest iteration : {xgb_es.best_iteration}')
# print(f'Best val logloss : {xgb_es.best_score:.4f}')
# print(f'Test accuracy : {accuracy_score(y_te, xgb_es.predict(X_te)):.4f}')
# print(f'\nModel stopped at {xgb_es.best_iteration} trees instead of 1000.')
# print(f'Early stopping found the sweet spot automatically!')


# import xgboost as xgb
# from sklearn.model_selection import RandomizedSearchCV
# from sklearn.datasets import load_breast_cancer
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# import numpy as np
# data = load_breast_cancer()
# X_tr, X_te, y_tr, y_te = train_test_split(data.data, data.target, test_size=0.2, random_state=42,stratify=data.target)

# param_dist = {
#  'n_estimators' : [200, 300, 500],
#  'learning_rate' : [0.01, 0.05, 0.1],
#  'max_depth' : [3, 4, 5, 6],
#  'subsample' : [0.7, 0.8, 0.9],
#  'colsample_bytree': [0.7, 0.8, 0.9],
#  'reg_alpha' : [0, 0.1, 0.5, 1.0],
#  'min_child_weight': [1, 3, 5]
# }

# search = RandomizedSearchCV(
#  xgb.XGBClassifier(eval_metric='logloss', random_state=42, n_jobs=-1),
#  param_dist, n_iter=30, cv=5,
#  scoring='accuracy', random_state=42, n_jobs=-1
# )
# search.fit(X_tr, y_tr)

# search.fit(X_tr, y_tr)
# print(f'Best params : {search.best_params_}')
# print(f'Best CV score : {search.best_score_:.4f}')
# print(f'Test accuracy : {accuracy_score(y_te, search.predict(X_te)):.4f}')


# import numpy as np
# import lightgbm as lgb
# import xgboost as xgb
# from sklearn.datasets import load_breast_cancer
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score, roc_auc_score
# from sklearn.ensemble import RandomForestClassifier
# import time


# data = load_breast_cancer()
# X_tr, X_te, y_tr, y_te = train_test_split(data.data, data.target, test_size=0.2, random_state=42,stratify=data.target)

# lgbm = lgb.LGBMClassifier(
#  n_estimators = 300,
#  learning_rate = 0.05,
#  max_depth = 5,
#  num_leaves = 31, # key LightGBM param: max leaves per tree
#  subsample = 0.8,
#  colsample_bytree = 0.8,
#  reg_alpha = 0.1,
#  reg_lambda = 1.0,
#  random_state = 42,
#  n_jobs = -1,
#  verbose = -1 # suppress output
# )

# models = {
#  'Random Forest (100)' : RandomForestClassifier(n_estimators=100,random_state=42, n_jobs=-1),
#  'XGBoost (300)' : xgb.XGBClassifier(n_estimators=300,learning_rate=0.05, max_depth=4,eval_metric='logloss', random_state=42,n_jobs=-1),
#  'LightGBM (300)' : lgbm
# }

# print(f"{'Model':22} | {'Train Time':>12} | {'Accuracy':>10} | {'AUC':>8}")
# print('-' * 60)

# for name, model in models.items():
#     t0 = time.time()
#     model.fit(X_tr, y_tr)
#     elapsed = time.time() - t0
#     acc = accuracy_score(y_te, model.predict(X_te))
#     auc = roc_auc_score(y_te, model.predict_proba(X_te)[:,1])
#     print(f"{name:22} | {elapsed:>10.3f}s | {acc:>10.4f} | {auc:>8.4f}")
    

# import lightgbm as lgb
# from sklearn.datasets import fetch_california_housing
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import r2_score
# import numpy as np

# data = fetch_california_housing()
# X_tr, X_temp, y_tr, y_temp = train_test_split(
#  data.data, data.target, test_size=0.3, random_state=42
# )
# X_val, X_te, y_val, y_te = train_test_split(
#  X_temp, y_temp, test_size=0.5, random_state=42
# )

# lgbm_reg = lgb.LGBMRegressor(
#  n_estimators = 2000, # will stop early
#  learning_rate = 0.03,
#  max_depth = 6,
#  num_leaves = 50,
#  subsample = 0.8,
#  colsample_bytree = 0.8,
#  random_state = 42,
#  n_jobs = -1,
#  verbose = -1
# )

# callbacks = [
#  lgb.early_stopping(stopping_rounds=50, verbose=False),
#  lgb.log_evaluation(period=100) # print every 100 rounds
# ]
# lgbm_reg.fit(
#  X_tr, y_tr,
#  eval_set = [(X_val, y_val)],
#  callbacks = callbacks
# )
# print(f'Best iteration: {lgbm_reg.best_iteration_}')
# print(f'Test R² : {r2_score(y_te, lgbm_reg.predict(X_te)):.4f}')

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import xgboost as xgb
# import lightgbm as lgb
# from sklearn.datasets import load_breast_cancer
# from sklearn.model_selection import train_test_split

# data = load_breast_cancer()
# X = pd.DataFrame(data.data, columns=data.feature_names)
# y = data.target

# X_tr, X_te, y_tr, y_te = train_test_split(
#  X, y, test_size=0.2, random_state=42, stratify=y
# )

# xgb_m = xgb.XGBClassifier(n_estimators=200, learning_rate=0.05,max_depth=4, random_state=42, n_jobs=-1,eval_metric='logloss')
# xgb_m.fit(X_tr, y_tr)

# # XGBoost: three importance types
# imp_weight = xgb_m.get_booster().get_score(importance_type='weight')
# imp_gain = xgb_m.get_booster().get_score(importance_type='gain')
# imp_cover = xgb_m.get_booster().get_score(importance_type='cover')

# print('XGBoost Feature Importance Types:')
# print(' weight = how many times a feature was used in splits')
# print(' gain = average improvement in loss from splits using this feature')
# print(' cover = average number of samples covered by splits on this feature')
# print()


# imp_gain_sorted = sorted(imp_gain.items(), key=lambda x:-x[1])[:5]
# print('Top 5 features by gain (XGBoost):')
# for feat, val in imp_gain_sorted:
#     print(f' {feat[:35]:>35}: {val:.2f}')

# lgbm_m = lgb.LGBMClassifier(n_estimators=200, learning_rate=0.05,max_depth=5, random_state=42,n_jobs=-1, verbose=-1)
# lgbm_m.fit(X_tr, y_tr)

# print('\nTop 5 features by gain (LightGBM):')
# imp_lgb = pd.Series(lgbm_m.feature_importances_,index=data.feature_names).sort_values(ascending=False)
# for feat, val in imp_lgb.head(5).items():
#     print(f' {feat[:35]:>35}: {val:.2f}')



# import numpy as np
# import pandas as pd
# import xgboost as xgb
# import lightgbm as lgb
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split, cross_val_score
# from sklearn.metrics import accuracy_score, roc_auc_score
# from sklearn.datasets import load_breast_cancer
# import warnings
# warnings.filterwarnings('ignore')

# def compare_models(X, y, dataset_name):

#     X_tr, X_te, y_tr, y_te = train_test_split(
#         X, y,
#         test_size=0.2,
#         random_state=42,
#         stratify=y
#     )

#     models = {
#         'Decision Tree': DecisionTreeClassifier(random_state=42),

#         'Random Forest': RandomForestClassifier(
#             n_estimators=100,
#             random_state=42,
#             n_jobs=-1
#         ),

#         'XGBoost' : xgb.XGBClassifier(n_estimators=200,
#             learning_rate=0.05,
#             max_depth=4, subsample=0.8,
#             eval_metric='logloss', random_state=42,
#             n_jobs=-1),
#         'LightGBM' : lgb.LGBMClassifier(n_estimators=200,
#             learning_rate=0.05,
#             max_depth=5, num_leaves=31, subsample=0.8,
#             random_state=42, n_jobs=-1, verbose=-1)
#     }

#     print(f"\nModel Comparison on {dataset_name} Dataset:")
#     print(f"{'Model':20} | {'Accuracy':>10} | {'AUC':>10}")
#     print('-' * 45)

#     for name, model in models.items():

#         model.fit(X_tr, y_tr)

#         y_pred = model.predict(X_te)
#         y_proba = model.predict_proba(X_te)

#         acc = accuracy_score(y_te, y_pred)

#         # Binary classification
#         if len(np.unique(y)) == 2:
#             auc = roc_auc_score(y_te, y_proba[:, 1])

#         # Multiclass classification
#         else:
#             auc = roc_auc_score(
#                 y_te,
#                 y_proba,
#                 multi_class='ovr'
#             )

#         print(f"{name:20} | {acc:>10.4f} | {auc:>10.4f}")
        
# data1 = load_breast_cancer()
# compare_models(data1.data, data1.target, 'Breast Cancer (569 rows, 30 features)')
# # Dataset 2: Wine
# from sklearn.datasets import load_wine
# data2 = load_wine()
# compare_models(data2.data, data2.target, 'Wine Classification (178 rows, 13 features)')



# import numpy as np
# import pandas as pd
# import xgboost as xgb
# import lightgbm as lgb
# from sklearn.model_selection import train_test_split, cross_val_score
# from sklearn.metrics import accuracy_score, roc_auc_score,classification_report
# from sklearn.dummy import DummyClassifier
# import matplotlib.pyplot as plt
# import warnings
# warnings.filterwarnings('ignore')

# df = pd.read_csv('titanic_cleaned.csv')
# features = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
# X = df[features]; y = df['Survived']

# X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# dummy = DummyClassifier(strategy='most_frequent').fit(X_tr, y_tr)
# print(f'Baseline : {accuracy_score(y_te, dummy.predict(X_te)):.4f}')

# xgb_m = xgb.XGBClassifier(
#  n_estimators=500, learning_rate=0.05, max_depth=4,
#  subsample=0.8, colsample_bytree=0.8, reg_alpha=0.1,
#  eval_metric='logloss', early_stopping_rounds=30,
#  random_state=42, n_jobs=-1
# )
# xgb_m.fit(X_tr, y_tr, eval_set=[(X_te, y_te)], verbose=False)
# xgb_acc = accuracy_score(y_te, xgb_m.predict(X_te))
# xgb_auc = roc_auc_score(y_te, xgb_m.predict_proba(X_te)[:,1])
# print(f'XGBoost : Acc={xgb_acc:.4f} AUC={xgb_auc:.4f}',f' Best iter={xgb_m.best_iteration}')


# lgbm_m = lgb.LGBMClassifier(
#  n_estimators=500, learning_rate=0.05, max_depth=5,
#  num_leaves=31, subsample=0.8, colsample_bytree=0.8,
#  reg_alpha=0.1, random_state=42, n_jobs=-1, verbose=-1
# )
# cb = [lgb.early_stopping(30, verbose=False)]
# lgbm_m.fit(X_tr, y_tr, eval_set=[(X_te, y_te)], callbacks=cb)
# lgbm_acc = accuracy_score(y_te, lgbm_m.predict(X_te))
# lgbm_auc = roc_auc_score(y_te, lgbm_m.predict_proba(X_te)[:,1])
# print(f'LightGBM : Acc={lgbm_acc:.4f} AUC={lgbm_auc:.4f}',f' Best iter={lgbm_m.best_iteration_}')


# print('\nFeature Importances:')
# print(f"{'Feature':15} | {'XGBoost gain':>13} | {'LightGBM split':>14}")
# print('-' * 50)
# for f in features:
#     xg_gain = xgb_m.get_booster().get_score(importance_type='gain').get(f, 0)
#     lgb_split= dict(zip(features, lgbm_m.feature_importances_)).get(f, 0)
#     print(f"{f:15} | {xg_gain:>13.2f} | {lgb_split:>14.0f}")


# ================================================
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.tree import DecisionTreeRegressor
# y = np.array([5, 12, 8, 20, 15, 7, 18, 11, 9, 16])

# X = np.arange(len(y)).reshape(-1, 1)

# learning_rate = 0.1
# n_rounds = 5

# predictions = np.full(len(y), np.mean(y))

# all_predictions = []

# print("Initial Prediction:")
# print(predictions)

# # Gradient Boosting rounds
# for round_number in range(1, n_rounds + 1):

#     # Calculate residuals
#     residuals = y - predictions

#     # Train a shallow decision tree on residuals
#     tree = DecisionTreeRegressor(max_depth=1, random_state=42)
#     tree.fit(X, residuals)

#     # Predict the residuals using the tree
#     tree_prediction = tree.predict(X)

#     # Update predictions
#     predictions = predictions + learning_rate * tree_prediction

#     # Store predictions
#     all_predictions.append(predictions.copy())

#     # Print results
#     print(f"\nRound {round_number}")
#     print("Predictions:")
#     print(np.round(predictions, 2))

#     print("Residuals:")
#     print(np.round(y - predictions, 2))


# # Plot actual values
# plt.figure(figsize=(10, 6))

# plt.plot(
#     X.flatten(),
#     y,
#     marker='o',
#     linewidth=2,
#     label='Actual y'
# )

# # Plot predictions from each round
# for i, round_predictions in enumerate(all_predictions, start=1):
#     plt.plot(
#         X.flatten(),
#         round_predictions,
#         marker='o',
#         linestyle='--',
#         label=f'Round {i}'
#     )

# plt.xlabel("Data Point")
# plt.ylabel("Value")
# plt.title("Gradient Boosting: Actual Values vs Predictions")
# plt.legend()
# plt.grid(True)

# plt.show()

# ================================================
# import numpy as np
# import pandas as pd
# import xgboost as xgb
# from sklearn.datasets import load_breast_cancer
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score, roc_auc_score,classification_report
# import matplotlib.pyplot as plt

# data=load_breast_cancer()
# X=pd.DataFrame(data.data,columns=data.feature_names)
# y=data.target

# X_tr, X_temp, y_tr, y_temp = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
# X_val, X_te, y_val, y_te = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42, stratify=y_temp)


# xgb_clf = xgb.XGBClassifier(
#     n_estimators = 1000,
#     learning_rate = 0.05, 
#     max_depth = 4, 
#     subsample = 0.8, 
#     colsample_bytree = 0.8,
#     reg_alpha = 0.1,
#     reg_lambda = 1.0, 
#     early_stopping_rounds=20,
#     eval_metric = 'logloss',
#     random_state = 42,
#     n_jobs = -1
# )

# xgb_clf.fit(X_tr,y_tr,eval_set=[(X_te,y_te),(X_val,y_val)],verbose=False)

# results = xgb_clf.evals_result()

# train_loss = results['validation_0']['logloss']
# val_loss = results['validation_1']['logloss']

# print("Best iteration:", f"{xgb_clf.best_iteration:.4f}")
# print("Best validation logloss:", f"{xgb_clf.best_score:.4f}")

# plt.figure(figsize=(10, 6))

# plt.plot(
#     train_loss,
#     label='Training Logloss'
# )

# plt.plot(
#     val_loss,
#     label='Validation Logloss'
# )

# # Mark best iteration
# plt.axvline(
#     xgb_clf.best_iteration,
#     linestyle='--',
#     label=f'Best Iteration = {xgb_clf.best_iteration}'
# )

# plt.xlabel('Boosting Iteration')
# plt.ylabel('Logloss')
# plt.title('XGBoost Training vs Validation Logloss')

# plt.legend()
# plt.grid(True)

# plt.show()


# ====================================================

# import numpy as np
# import pandas as pd 
# import xgboost as xgb
# import lightgbm as lgb
# from sklearn.datasets import fetch_california_housing
# from sklearn.model_selection import train_test_split
# import time
# from sklearn.metrics import mean_squared_error, r2_score
# import warnings
# warnings.filterwarnings('ignore')

# data = fetch_california_housing()

# X=pd.DataFrame(data.data, columns=data.feature_names)
# y=data.target

# X_tr, X_temp, y_tr, y_temp = train_test_split(X,y,test_size=0.2,random_state=42)

# X_val, X_te, y_val, y_te = train_test_split(X_temp,y_temp,test_size=0.5,random_state=42)

# xgb_r=xgb.XGBRegressor(
#     n_estimators=1000,
#     learning_rate=0.05,
#     max_depth=4, 
#     early_stopping_rounds=20,
#     random_state=42,
#     n_jobs=-1
# )

# xgb_r.fit(
#     X_tr,
#     y_tr,
#     eval_set=[(X_val, y_val)],
#     verbose=False
# )
# print("Best iteration:", f"{xgb_r.best_iteration:.4f}")
# t0 = time.time()
# elapsed_xgb_r = time.time() - t0
# print(f"training time:{elapsed_xgb_r:.4f}")
# print(f"test r2 score:{r2_score(y_te,xgb_r.predict(X_te)):.4f}")
# print(f"test rmse score:{np.sqrt(mean_squared_error(y_te,xgb_r.predict(X_te))):.4f}")

# lgbm_r=lgb.LGBMRegressor(
#     n_estimators=1000,
#     learning_rate=0.05,
#     max_depth=4, 
#     early_stopping_rounds=20,
#     random_state=42,
#     n_jobs=-1
# )
# lgbm_r.fit(
#     X_tr,
#     y_tr,
#     eval_set=[(X_val, y_val)],
#     eval_metric='rmse',
#     callbacks=[lgb.early_stopping(50, verbose=False)]
# )
# print("Best iteration:", f"{lgbm_r.best_iteration_:.4f}")
# t1 = time.time()
# elapsed_lgbm_r = time.time() - t1
# print(f"training time:{elapsed_lgbm_r:.4f}")
# print(f"test r2 score:{r2_score(y_te,lgbm_r.predict(X_te)):.4f}")
# print(f"test rmse score:{np.sqrt(mean_squared_error(y_te,lgbm_r.predict(X_te))):.4f}")



# import numpy as np
# from sklearn.tree import DecisionTreeRegressor

# y= np.array([5, 12, 8, 20, 15, 7, 18, 11, 9, 16])
# X = np.arange(len(y)).reshape(-1, 1)
# predictions= np.full(len(y),np.mean(y))

# final_predictions=[]
# for i in range(1,6):
#     residuals=y-predictions
#     tree=DecisionTreeRegressor(max_depth=1,random_state=42)
#     tree.fit(X,residuals)
#     predictions=predictions+0.1*tree.predict(X)
#     final_predictions.append(predictions.copy())
#     print(f"Initial Prediction: {final_predictions[i-1]}")



# import numpy as np
# import pandas as pd
# import xgboost as xgb
# from sklearn.datasets import load_breast_cancer
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score, roc_auc_score,classification_report
# import matplotlib.pyplot as plt

# data=load_breast_cancer()
# X=pd.DataFrame(data.data,columns=data.feature_names)
# y=data.target

# X_tr, X_temp, y_tr, y_temp = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
# X_val, X_te, y_val, y_te = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42, stratify=y_temp)


# xgb_clf = xgb.XGBClassifier(
#     n_estimators=1000, 
#     learning_rate=0.05,
#     max_depth=4,
#     early_stopping_rounds=20,
#     eval_metric='logloss',
#     random_state=42,
#     n_jobs=-1
# )

# xgb_clf.fit(X_tr,y_tr,eval_set=[(X_tr,y_tr),(X_val,y_val)],verbose=False)

# results = xgb_clf.evals_result()

# train_loss = results['validation_0']['logloss']
# val_loss = results['validation_1']['logloss']

# print("Best iteration:", f"{xgb_clf.best_iteration:.4f}")
# print("Best validation logloss:", f"{xgb_clf.best_score:.4f}")

# plt.figure(figsize=(10, 6))

# plt.plot(
#     train_loss,
#     label='Training Logloss'
# )

# plt.plot(
#     val_loss,
#     label='Validation Logloss'
# )

# # Mark best iteration
# plt.axvline(
#     xgb_clf.best_iteration,
#     linestyle='--',
#     label=f'Best Iteration = {xgb_clf.best_iteration}'
# )

# plt.xlabel('Boosting Iteration')
# plt.ylabel('Logloss')
# plt.title('XGBoost Training vs Validation Logloss')

# plt.legend()
# plt.grid(True)

# plt.show()

# import numpy as np 
# import pandas as pd
# import xgboost as xgb
# from sklearn.model_selection import train_test_split
# import matplotlib.pyplot as plt


# dt=pd.read_csv('titanic_cleaned.csv')

# features=["Pclass","Age", "SibSp", "Parch", "Fare"]
# X=dt[features]
# y=dt["Survived"]

# X_tr,X_te,y_tr,y_te=train_test_split(X,y,test_size=0.2,random_state=42)

# xgb_c=xgb.XGBClassifier(
#     n_estimators=200, 
#     learning_rate=0.05,
#     random_state=42,
#     n_jobs=-1
# )

# xgb_c.fit(X_tr,y_tr)

# xgb_weight=xgb_c.get_booster().get_score(importance_type='weight').
# xgb_gain=xgb_c.get_booster().get_score(importance_type='gain')
# xgb_cover=xgb_c.get_booster().get_score(importance_type='cover')

# print('XGBoost Feature importance types:')
# print(f'weight={xgb_weight}')
# print(f"gain={xgb_gain}")
# print(f'cover={xgb_cover}')

# weight = pd.Series(xgb_weight).sort_values()
# gain = pd.Series(xgb_gain).sort_values()
# cover = pd.Series(xgb_cover).sort_values()

# fig, axes = plt.subplots(1, 3, figsize=(15, 6))


    
# axes[0].barh(weight.index, weight.values),
# axes[0].set_title("Weight"),
# axes[1].barh(gain.index, gain.values),
# axes[1].set_title("Gain"),
# axes[2].barh(cover.index, cover.values),
# axes[2].set_title("Cover")


# fig.suptitle("XGBoost Feature Importance Comparison")
# plt.tight_layout()
# plt.show()


# import numpy as np
# import pandas as pd
# import xgboost as xgb
# import lightgbm as lgb
# from sklearn.datasets import load_wine
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split, cross_val_score
# from sklearn.metrics import accuracy_score, roc_auc_score,classification_report

# data=load_wine()

# X=pd.DataFrame(data.data, columns=data.feature_names)
# y=data.target

# X_tr,X_te,y_tr,y_te=train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)

# models={
#     'decision tree_c':DecisionTreeClassifier(max_depth=5,random_state=42),
#     'random froest_c':RandomForestClassifier(n_estimators=100,random_state=42,n_jobs=-1),
#     'Xgb_c':xgb.XGBClassifier(n_estimators=200, learning_rate=0.05,random_state=42,n_jobs=-1),
#     'Lgb_c':lgb.LGBMClassifier(n_estimators=200, learning_rate=0.05,random_state=42,n_jobs=-1)
# }

# results = []

# print(f"{'Model':18} | {'CV Acc':>8} | {'Test Acc':>9} | {'TestAUC':>9}")
# print('-' * 55)
# for name, model in models.items():
#     cv = cross_val_score(model, X_tr, y_tr, cv=5,scoring='accuracy')
#     cv_accuracy = cv.mean()
#     model.fit(X_tr, y_tr)
#     acc = accuracy_score(y_te, model.predict(X_te))
#     auc = roc_auc_score(y_te, model.predict_proba(X_te),multi_class='ovr')
#     results.append({
#         'Model': name,
#         'CV Accuracy': cv_accuracy,
#         'Test Accuracy': acc,
#         'Test AUC': auc
#     })
#     print(f"{name:18} | {cv_accuracy:>8.4f} | {acc:>9.4f} | {auc:>9.4f}")
        
# results_df = pd.DataFrame(results)

# print("\nComparison Table:")
# print(results_df.to_string(index=False))


