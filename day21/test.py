# import numpy as np
# import pandas as pd
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error, r2_score
# from sklearn.preprocessing import PolynomialFeatures



# n_samples = 80
# n_true = 5
# n_noise = 70
# n_features = n_true + n_noise

# X_true = np.random.randn(n_samples, n_true)
# y = (3*X_true[:,0] - 2*X_true[:,1] + 5*X_true[:,2] + 1.5*X_true[:,3] - 4*X_true[:,4] + np.random.randn(n_samples) * 2) 

# X_noise = np.random.randn(n_samples, n_noise)
# X = np.hstack([X_true, X_noise])


# print(f'Dataset: {n_samples} samples, {n_features} features')
# print(f'Truly relevant features: {n_true}')
# print(f'Noise features: {n_noise}')
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# lr = LinearRegression()
# lr.fit(X_train, y_train)
# train_r2 = r2_score(y_train, lr.predict(X_train))
# test_r2 = r2_score(y_test, lr.predict(X_test))
# train_rmse = np.sqrt(mean_squared_error(y_train, lr.predict(X_train)))
# test_rmse = np.sqrt(mean_squared_error(y_test, lr.predict(X_test)))
# # print(f'\n=== Plain Linear Regression ===')
# # print(f'Training R² : {train_r2:.4f}')
# # print(f'Test R² : {test_r2:.4f}')
# # print(f'Training RMSE: {train_rmse:.4f}')
# # print(f'Test RMSE : {test_rmse:.4f}')
# # print(f'Largest coef : {np.abs(lr.coef_).max():.2f}')
# # print(f'\nThis is SEVERE overfitting.')
# # print(f'Train R²={train_r2:.2f} but Test R²={test_r2:.2f}')
# # print(f'The model memorised noise instead of learning the true pattern.')


# import numpy as np
# import pandas as pd
# from sklearn.linear_model import Ridge, LinearRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error, r2_score
# from sklearn.preprocessing import PolynomialFeatures



# n_samples = 80
# n_true = 5
# n_noise = 70
# n_features = n_true + n_noise

# alphas = [0.001, 0.1, 1.0, 10.0, 100.0, 1000.0]

# print(f"{'Alpha':>8} | {'Train R²':>10} | {'Test R²':>10} | {'MaxCoef':>10} | Assessment")
# print("-" * 75)
# X_true = np.random.randn(n_samples, n_true)
# y = (3*X_true[:,0] - 2*X_true[:,1] + 5*X_true[:,2] + 1.5*X_true[:,3] - 4*X_true[:,4] + np.random.randn(n_samples) * 2) 

# X_noise = np.random.randn(n_samples, n_noise)
# X = np.hstack([X_true, X_noise])

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)


# for alpha in alphas:
#     ridge = Ridge(alpha=alpha)
#     ridge.fit(X_train, y_train)
#     train_r2 = r2_score(y_train, ridge.predict(X_train))
#     test_r2 = r2_score(y_test, ridge.predict(X_test))
#     max_coef = np.abs(ridge.coef_).max() #find the maximum absolute value of the coefficients
#     if test_r2 > 0.85:
#         assessment = "Excellent"
#     elif test_r2 > 0.5:
#         assessment = "Good"
#     elif test_r2 > 0.0:
#         assessment = "Moderate"
#     else:
#         assessment = '← Still overfitting or underfitting'
#     print(f"{alpha:>8} | {train_r2:>10.4f} | {test_r2:>10.4f} |{max_coef:>10.4f} | {assessment}")

# print("\nPlain LR (alpha=0) for comparison:")
# lr = LinearRegression().fit(X_train, y_train)
# print(f"{'0 (LR)':>8} | {r2_score(y_train,lr.predict(X_train)):>10.4f} | ",f"{r2_score(y_test,lr.predict(X_test)):>10.4f} | ",f"{np.abs(lr.coef_).max():>10.4f} | ← Severe overfitting")



# import numpy as np
# from sklearn.linear_model import Lasso
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import r2_score

# alphas = [0.001, 0.01, 0.1, 0.5, 1.0, 5.0]


# n_samples = 80
# n_true = 5
# n_noise = 70
# n_features = n_true + n_noise

# X_true = np.random.randn(n_samples, n_true)
# y = (3*X_true[:,0] - 2*X_true[:,1] + 5*X_true[:,2] + 1.5*X_true[:,3] - 4*X_true[:,4] + np.random.randn(n_samples) * 2) 

# X_noise = np.random.randn(n_samples, n_noise)
# X = np.hstack([X_true, X_noise])

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)


# print(f"{'Alpha':>7} | {'Train R²':>10} | {'Test R²':>10} | {'Nonzero Coefs':>14} | Note")
# print("-" * 72)

# for alpha in alphas:
#     lasso = Lasso(alpha=alpha, max_iter=10000)
#     lasso.fit(X_train, y_train)
#     train_r2 = r2_score(y_train, lasso.predict(X_train))
#     test_r2 = r2_score(y_test, lasso.predict(X_test))
#     nonzero = np.sum(lasso.coef_ != 0)
    
#     note = ''
#     if nonzero <= 10 and test_r2 > 0.8:
#         note = '← Sparse + good! Feature selection worked'
#     elif test_r2 < 0:
#         note = '← Underfitting'
#     print(f"{alpha:>7} | {train_r2:>10.4f} | {test_r2:>10.4f} |{nonzero:>14} | {note}")


# best_lasso = Lasso(alpha=0.1, max_iter=10000).fit(X_train, y_train)
# kept = np.where(best_lasso.coef_ != 0)[0]
# removed = np.where(best_lasso.coef_ == 0)[0]
# print(f"\nalpha=0.1: Kept {len(kept)} features, removed {len(removed)}")
# print(f"Features kept: {kept[:10].tolist()} ...")
# print(f"True features are at indices 0-4")
# print(f"Did Lasso find them? {all(i in kept for i in range(5))}")


# import numpy as np
# from sklearn.linear_model import ElasticNet
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import r2_score


# l1_ratios = [0.0, 0.1, 0.3, 0.5, 0.7, 0.9, 1.0]
# print(f"{'l1_ratio':>10} | {'Test R²':>10} | {'Nonzero':>8} |{'Behaviour'}")
# print("-" * 65)

# np.random.seed(42)
# n_samples = 80
# n_true = 5
# n_noise = 70
# n_features = n_true + n_noise

# X_true = np.random.randn(n_samples, n_true)
# y = (3*X_true[:,0] - 2*X_true[:,1] + 5*X_true[:,2] + 1.5*X_true[:,3] - 4*X_true[:,4] + np.random.randn(n_samples) * 2) 

# X_noise = np.random.randn(n_samples, n_noise)
# X = np.hstack([X_true, X_noise])

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# for l1r in l1_ratios:
#     en = ElasticNet(alpha=0.1, l1_ratio=l1r, max_iter=10000)
#     en.fit(X_train, y_train)
#     test_r2 = r2_score(y_test, en.predict(X_test))
#     nonzero = np.sum(en.coef_ != 0)
#     if l1r == 0.0:
#         behaviour = 'Pure Ridge: all features kept'
#     elif l1r == 1.0:
#         behaviour = 'Pure Lasso: maximum sparsity'
#     else:
#         behaviour = f'Mix: {int(l1r*100)}% Lasso, {int((1-l1r)*100)}% Ridge'
#     print(f"{l1r:>10} | {test_r2:>10.4f} | {nonzero:>8} | {behaviour}")

# best_en = ElasticNet(alpha=0.1, l1_ratio=0.5, max_iter=10000)
# best_en.fit(X_train, y_train)
# print(f"\nBest ElasticNet (l1_ratio=0.5):")
# print(f" Test R² : {r2_score(y_test, best_en.predict(X_test)):.4f}")
# print(f" Features kept: {np.sum(best_en.coef_ != 0)} of {len(best_en.coef_)}")


# import numpy as np
# from sklearn.linear_model import RidgeCV, LassoCV, ElasticNetCV
# from sklearn.model_selection import cross_val_score
# from sklearn.metrics import r2_score


# alphas_to_try = np.logspace(-3, 4, 50) # 50 values from 0.001 to 10000
# ridge_cv = RidgeCV(
#  alphas = alphas_to_try,
#  cv = 5, # 5-fold cross-validation
#  scoring = 'r2'
# )
# ridge_cv.fit(X_train, y_train)
# print(f'RidgeCV best alpha: {ridge_cv.alpha_:.4f}')
# print(f'Test R² : {r2_score(y_test,ridge_cv.predict(X_test)):.4f}')


# lasso_cv = LassoCV(
#  alphas = np.logspace(-3, 2, 50),
#  cv = 5,
#  max_iter= 10000
# )
# lasso_cv.fit(X_train, y_train)
# print(f'\nLassoCV best alpha: {lasso_cv.alpha_:.4f}')
# print(f'Test R² : {r2_score(y_test,lasso_cv.predict(X_test)):.4f}')
# print(f'Features kept : {np.sum(lasso_cv.coef_ != 0)}')


# elastic_cv = ElasticNetCV(
#  l1_ratio= [0.1, 0.3, 0.5, 0.7, 0.9],
#  alphas = np.logspace(-3, 2, 30),
#  cv = 5,
#  max_iter= 10000
# )
# elastic_cv.fit(X_train, y_train)


# print(f'\nElasticNetCV best alpha : {elastic_cv.alpha_:.4f}')
# print(f'ElasticNetCV best l1_ratio: {elastic_cv.l1_ratio_:.2f}')
# print(f'Test R² : {r2_score(y_test, elastic_cv.predict(X_test)):.4f}')

# print(f'\n=== Final Comparison ===')
# results = {
#  'Linear Regression': r2_score(y_test, lr.predict(X_test)),
#  'Ridge (CV-tuned)' : r2_score(y_test, ridge_cv.predict(X_test)),
#  'Lasso (CV-tuned)' : r2_score(y_test, lasso_cv.predict(X_test)),
#  'ElasticNet (CV)' : r2_score(y_test, elastic_cv.predict(X_test)),
# }
# for name, score in sorted(results.items(), key=lambda x:-x[1]):
#     print(f' {name:25}: Test R² = {score:.4f}')


# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.linear_model import Ridge, Lasso

# np.random.seed(42)
# X_path = np.random.randn(100, 8)
# true_w = np.array([5, -3, 4, 0, 0, 2, 0, -1])

# y_path = X_path @ true_w + np.random.randn(100)
# alphas = np.logspace(-2, 4, 100)


# fig, axes = plt.subplots(1, 2, figsize=(15, 6))
# labels = [f'w{i+1}(true={true_w[i]})' for i in range(8)]
# colours = plt.cm.tab10(np.linspace(0, 1, 8))

# for ax, ModelClass, title in zip(
#  axes,
#  [Ridge, Lasso],
#  ['Ridge Regularisation Path', 'Lasso Regularisation Path']
# ):
#     coefs = []
#     for alpha in alphas:
#         m = ModelClass(alpha=alpha, max_iter=10000)
#         m.fit(X_path, y_path)
#         coefs.append(m.coef_)
#     coefs = np.array(coefs)

#     for i in range(8):
#         ax.plot(np.log10(alphas), coefs[:, i],
#         color=colours[i], lw=2, label=labels[i])
        
#     ax.axhline(y=0, color='black', lw=1, ls='-')
#     ax.set_title(title, fontsize=13, fontweight='bold')
#     ax.set_xlabel('log10(alpha) [Left=less regularisation, Right=more]')
#     ax.set_ylabel('Coefficient value')
#     ax.legend(fontsize=8, loc='upper right')
#     ax.grid(True, alpha=0.4)
# plt.tight_layout()
# plt.savefig('regularisation_paths.png', dpi=150, bbox_inches='tight')
# plt.show()



# ----------------------------------------------------------------------------------------------------------------------------

# import numpy as np
# import pandas as pd
# from sklearn.datasets import fetch_california_housing
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import (
#  LinearRegression, Ridge, Lasso, ElasticNet,
#  RidgeCV, LassoCV, ElasticNetCV
# )
# from sklearn.preprocessing import StandardScaler
# from sklearn.metrics import mean_squared_error, r2_score
# import warnings
# warnings.filterwarnings('ignore')

# data = fetch_california_housing()
# X = pd.DataFrame(data.data, columns=data.feature_names)
# y=data.target

# print(f'Dataset: {X.shape[0]} rows, {X.shape[1]} features')
# print(f'Target: Median house value (hundreds of thousands USD)')

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# scaler = StandardScaler()
# X_train_s= scaler.fit_transform(X_train) 
# X_test_s = scaler.transform(X_test)

# models = {
#  'Linear Regression': LinearRegression(),
#  'Ridge (CV)' : RidgeCV(alphas=np.logspace(-3,4,50), cv=5),
#  'Lasso (CV)' : LassoCV(alphas=np.logspace(-3,2,50), cv=5,max_iter=10000),
#  'ElasticNet (CV)' : ElasticNetCV(l1_ratio=[0.1,0.3,0.5,0.7,0.9],alphas=np.logspace(-3,2,30),cv=5, max_iter=10000)
# }

# results = {}

# for name, model in models.items():
#     model.fit(X_train_s, y_train)
#     y_pred = model.predict(X_test_s)
#     train_r2 = r2_score(y_train, model.predict(X_train_s))
#     test_r2 = r2_score(y_test, y_pred)
#     rmse = np.sqrt(mean_squared_error(y_test, y_pred))
#     results[name] = {'train_r2':train_r2, 'test_r2':test_r2, 'rmse':rmse}

# print(f'\n{"Model":25} | {"Train R²":>10} | {"Test R²":>10} | {"Test RMSE":>10}')
# print('-' * 65)
# for name, r in results.items():
#     print(f'{name:25} | {r["train_r2"]:>10.4f} | {r["test_r2"]:>10.4f} | {r["rmse"]:>10.4f}')

# print(f'\nBest alpha (Ridge) : {models["Ridge (CV)"].alpha_:.4f}')
# print(f'Best alpha (Lasso) : {models["Lasso (CV)"].alpha_:.4f}')
# print(f'Lasso features kept : {np.sum(models["Lasso (CV)"].coef_ !=0)}')

# print(f'Best alpha (ElasticNet): {models["ElasticNet (CV)"].alpha_:.4f}')

# print(f'Best l1_ratio : {models["ElasticNet (CV)"].l1_ratio_:.2f}')


# import numpy as np
# import pandas as pd

# from sklearn.datasets import fetch_california_housing
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import (
#     LinearRegression, Ridge, Lasso, ElasticNet,
#     RidgeCV, LassoCV, ElasticNetCV
# )
# from sklearn.metrics import mean_squared_error, r2_score

# import warnings
# warnings.filterwarnings('ignore')


# # Load dataset
# data = fetch_california_housing()

# X = pd.DataFrame(data.data, columns=data.feature_names)
# y = data.target

# print(f'Dataset: {X.shape[0]} rows, {X.shape[1]} features')
# print(f'Target: Median house value (hundreds of thousands USD)')


# # Train-test split
# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.2,
#     random_state=42
# )


# # Models
# models = {
#     'Linear Regression': LinearRegression(),

#     'Ridge (CV)': RidgeCV(
#         alphas=np.logspace(-3, 4, 50),
#         cv=5
#     ),

#     'Lasso (CV)': LassoCV(
#         alphas=np.logspace(-3, 2, 50),
#         cv=5,
#         max_iter=10000
#     ),

#     'ElasticNet (CV)': ElasticNetCV(
#         l1_ratio=[0.1, 0.3, 0.5, 0.7, 0.9],
#         alphas=np.logspace(-3, 2, 30),
#         cv=5,
#         max_iter=10000
#     )
# }


# # Train and evaluate models
# results = {}

# for name, model in models.items():

#     model.fit(X_train, y_train)

#     y_pred = model.predict(X_test)

#     train_r2 = r2_score(
#         y_train,
#         model.predict(X_train)
#     )

#     test_r2 = r2_score(
#         y_test,
#         y_pred
#     )

#     rmse = np.sqrt(
#         mean_squared_error(y_test, y_pred)
#     )

#     results[name] = {
#         'train_r2': train_r2,
#         'test_r2': test_r2,
#         'rmse': rmse
#     }


# # Display results
# print(
#     f'\n{"Model":25} | '
#     f'{"Train R²":>10} | '
#     f'{"Test R²":>10} | '
#     f'{"Test RMSE":>10}'
# )

# print('-' * 65)

# for name, r in results.items():

#     print(
#         f'{name:25} | '
#         f'{r["train_r2"]:>10.4f} | '
#         f'{r["test_r2"]:>10.4f} | '
#         f'{r["rmse"]:>10.4f}'
#     )


# # Best parameters
# print(
#     f'\nBest alpha (Ridge) : '
#     f'{models["Ridge (CV)"].alpha_:.4f}'
# )

# print(
#     f'Best alpha (Lasso) : '
#     f'{models["Lasso (CV)"].alpha_:.4f}'
# )

# print(
#     f'Lasso features kept : '
#     f'{np.sum(models["Lasso (CV)"].coef_ != 0)}'
# )

# print(
#     f'Best alpha (ElasticNet): '
#     f'{models["ElasticNet (CV)"].alpha_:.4f}'
# )

# print(
#     f'Best l1_ratio : '
#     f'{models["ElasticNet (CV)"].l1_ratio_:.2f}'
# )

# from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import Ridge
# import numpy as np
# # Demonstrate the effect of scaling on coefficients
# np.random.seed(42)
# n = 200
# # Two features with very different scales
# income_lakhs = np.random.uniform(2, 100, n) # scale: 2 to 100
# age_years = np.random.uniform(20, 65, n) # scale: 20 to 65
# # True relationship: income matters 3x more than age
# # But their raw numbers make this hard for the model to see
# y = 0.5 * income_lakhs + 0.5 * age_years + np.random.randn(n) * 5
# X_raw = np.column_stack([income_lakhs, age_years])
# # Without scaling
# ridge_no_scale = Ridge(alpha=10).fit(X_raw, y)
# print("Without scaling:")
# print(f" income_lakhs coef: {ridge_no_scale.coef_[0]:.4f}")
# print(f" age_years coef : {ridge_no_scale.coef_[1]:.4f}")
# # With scaling
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X_raw)
# ridge_scaled = Ridge(alpha=10).fit(X_scaled, y)
# print("\nWith scaling (StandardScaler):")
# print(f" income_lakhs coef: {ridge_scaled.coef_[0]:.4f}")
# print(f" age_years coef : {ridge_scaled.coef_[1]:.4f}")
# print(" (Now both features are comparable. Larger coef = more important.)") 


# Exercise 1 — Reproduce the Overfitting Demo (Beginner)


# import numpy as np
# import pandas as pd
# from sklearn.linear_model import LinearRegression, Ridge
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error, r2_score
# from sklearn.preprocessing import PolynomialFeatures

# np.random.seed(42)

# n_samples = 80
# n_true = 5 
# n_noise = 70
# n_features = n_true + n_noise

# X_true = np.random.randn(n_samples, n_true)
# X_noise = np.random.randn(n_samples, n_noise)
# X = np.hstack([X_true, X_noise])
# y = (3*X_true[:,0] - 2*X_true[:,1] + 5*X_true[:,2] + 1.5*X_true[:,3] - 4*X_true[:,4] + np.random.randn(n_samples) * 2) 

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# model = LinearRegression()
# model.fit(X_train, y_train)

# results = []

# train_r2 = r2_score(y_train, model.predict(X_train))
# test_r2 = r2_score(y_test, model.predict(X_test))
# train_rmse = np.sqrt(mean_squared_error(y_train, model.predict(X_train)))
# test_rmse = np.sqrt(mean_squared_error(y_test, model.predict(X_test)))

# results.append([ "Linear Regression", train_r2, test_r2, train_rmse, test_rmse ])

# # print(f'Training R² : {train_r2:.4f}')
# # print(f'Test R² : {test_r2:.4f}')
# # print(f'Training RMSE: {train_rmse:.4f}')
# # print(f'Test RMSE : {test_rmse:.4f}')

# ridge_model = Ridge(alpha=100)
# ridge_model.fit(X_train, y_train)
# ridge_train_r2 = r2_score(y_train, ridge_model.predict(X_train))
# ridge_test_r2 = r2_score(y_test, ridge_model.predict(X_test))

# ridge_train_rmse = np.sqrt(mean_squared_error(y_train, ridge_model.predict(X_train)))
# ridge_test_rmse = np.sqrt(mean_squared_error(y_test, ridge_model.predict(X_test)))

# results.append([ "Ridge (alpha=100)", ridge_train_r2, ridge_test_r2, ridge_train_rmse, ridge_test_rmse ])

# # print(f'ridge Training R² : {ridge_train_r2:.4f}')
# # print(f'ridge Test R² : {ridge_test_r2:.4f}')
# # print(f'ridge Training RMSE: {ridge_train_rmse:.4f}')
# # print(f'ridge Test RMSE : {ridge_test_rmse:.4f}')

# results_df = pd.DataFrame( results, columns=[ "Model", "Training R²", "Test R²", "Training RMSE", "Test RMSE" ] ) 
# print("\nBEFORE AND AFTER RIDGE REGULARIZATION") 
# print("=" * 80) 
# print( results_df.to_string( index=False, formatters={ "Training R²": "{:.4f}".format, "Test R²": "{:.4f}".format, "Training RMSE": "{:.4f}".format, "Test RMSE": "{:.4f}".format } ) )

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# from sklearn.datasets import fetch_california_housing
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import Ridge
# from sklearn.metrics import r2_score

# data = fetch_california_housing()

# X = pd.DataFrame(data.data, columns=data.feature_names)
# y = data.target

# X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2,random_state=42)

# alphas = [0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000]


# train_r2 = []
# test_r2 = []
# max_coeff = []


# for alpha in alphas:

#     model = Ridge(alpha=alpha)

#     model.fit(X_train, y_train)

#     train_pred = model.predict(X_train)
#     test_pred = model.predict(X_test)

#     train_r2.append(r2_score(y_train, train_pred))
#     test_r2.append(r2_score(y_test, test_pred))

#     max_coeff.append(np.max(np.abs(model.coef_)))



# results = pd.DataFrame({
#     "Alpha": alphas,
#     "Training R2": train_r2,
#     "Test R2": test_r2,
#     "Max |Coefficient|": max_coeff
# })

# print("\nRidge Alpha Sweep")
# print(results.to_string(index=False))


# best_index = np.argmax(test_r2)
# best_alpha = alphas[best_index]
# best_test_r2 = test_r2[best_index]

# print("\nBest Alpha:", best_alpha)
# print("Best Test R2:", round(best_test_r2, 4))

# plt.figure(figsize=(7, 5))
# plt.plot(alphas, train_r2, marker='o')
# plt.xscale('log')
# plt.xlabel("Alpha (log scale)")
# plt.ylabel("Training R2")
# plt.title("Training R2 vs Alpha")
# plt.grid(True)
# plt.show()


# plt.figure(figsize=(7, 5))
# plt.plot(alphas, test_r2, marker='o')
# plt.xscale('log')
# plt.xlabel("Alpha (log scale)")
# plt.ylabel("Test R2")
# plt.title("Test R2 vs Alpha")
# plt.grid(True)
# plt.show()


# plt.figure(figsize=(7, 5))
# plt.plot(alphas, max_coeff, marker='o')
# plt.xscale('log')
# plt.xlabel("Alpha (log scale)")
# plt.ylabel("Maximum Absolute Coefficient")
# plt.title("Maximum |Coefficient| vs Alpha")
# plt.grid(True)
# plt.show()


# import numpy as np
# import pandas as pd
# from sklearn.datasets import load_diabetes
# from sklearn.linear_model import LassoCV

# data = load_diabetes()

# X = data.data
# y = data.target

# model = LassoCV(cv=5)
# model.fit(X, y)

# print("Best Alpha:", model.alpha_)

# df = pd.DataFrame({
#     "Feature": data.feature_names,
#     "Coefficient": model.coef_
# })

# df["Abs Coefficient"] = abs(df["Coefficient"])
# df = df.sort_values("Abs Coefficient", ascending=False)

# print("\nLasso Coefficients:")
# print(df.to_string(index=False))

# zero_count = sum(model.coef_ == 0)

# print("\nNumber of zero coefficients:", zero_count)

# top_feature = df.iloc[0]["Feature"]

# print("Most important feature:", top_feature)

# correlation = np.corrcoef(X.T, y)[0, 1:]

# top_corr_feature = data.feature_names[np.argmax(abs(correlation))]

# print("Highest correlation feature:", top_corr_feature)

# if top_feature == top_corr_feature:
#     print("Verification: YES")
# else:
#     print("Verification: NO")

# import numpy as np
# import pandas as pd
# from sklearn.datasets import fetch_california_housing
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import Ridge
# from sklearn.preprocessing import StandardScaler
# from sklearn.metrics import mean_squared_error

# data = fetch_california_housing()

# X = data.data
# y = data.target

# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# ridge_without_scaler = Ridge(alpha=10)
# ridge_without_scaler.fit(X_train, y_train)

# rmse_without_scaler = np.sqrt(
#     mean_squared_error(y_test, ridge_without_scaler.predict(X_test))
# )


# scaler = StandardScaler()

# X_train_scaled = scaler.fit_transform(X_train)
# X_test_scaled = scaler.transform(X_test)

# ridge_with_scaler = Ridge(alpha=10)
# ridge_with_scaler.fit(X_train_scaled, y_train)


# rmse_with_scaler = np.sqrt(
#     mean_squared_error(y_test, ridge_with_scaler.predict(X_test_scaled))
# )

# coef_table = pd.DataFrame({
#     "Feature": data.feature_names,
#     "Without Scaler": ridge_without_scaler.coef_,
#     "With Scaler": ridge_with_scaler.coef_
# })

# print("\nRidge Coefficients Comparison")
# print(coef_table.to_string(index=False))


# print("\nTest RMSE Comparison")
# print("Without StandardScaler:", round(rmse_without_scaler, 4))
# print("With StandardScaler   :", round(rmse_with_scaler, 4))


# import numpy as np
# import pandas as pd

# from sklearn.datasets import fetch_california_housing
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import (
#     LinearRegression,
#     RidgeCV,
#     LassoCV,
#     ElasticNetCV
# )
# from sklearn.metrics import r2_score, mean_squared_error

# data = fetch_california_housing()

# X = data.data
# y = data.target

# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# linear = LinearRegression()

# ridge = RidgeCV(
#     alphas=[0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000],
#     cv=5
# )

# lasso = LassoCV(
#     cv=5,
#     random_state=42
# )

# elastic = ElasticNetCV(
#     cv=5,
#     random_state=42,
#     l1_ratio=[0.1, 0.5, 0.7, 0.9, 1.0]
# )

# models = [
#     ("Linear Regression", linear),
#     ("Ridge", ridge),
#     ("Lasso", lasso),
#     ("ElasticNet", elastic)
# ]



# results = []

# for name, model in models:

#     model.fit(X_train, y_train)

#     train_pred = model.predict(X_train)
#     test_pred = model.predict(X_test)

#     train_r2 = r2_score(y_train, train_pred)
#     test_r2 = r2_score(y_test, test_pred)

#     test_rmse = np.sqrt(mean_squared_error(y_test, test_pred))

#     nonzero = np.sum(model.coef_ != 0)

    
#     if name == "Linear Regression":
#         hyperparameter = "None"

#     elif name == "Ridge":
#         hyperparameter = "alpha = " + str(model.alpha_)

#     elif name == "Lasso":
#         hyperparameter = "alpha = " + str(model.alpha_)

#     else:
#         hyperparameter = (
#             "alpha = " + str(model.alpha_)
#             + ", l1_ratio = " + str(model.l1_ratio_)
#         )

#     results.append([
#         name,
#         train_r2,
#         test_r2,
#         test_rmse,
#         nonzero,
#         hyperparameter
#     ])

# results_df = pd.DataFrame(
#     results,
#     columns=[
#         "Model",
#         "Training R²",
#         "Test R²",
#         "Test RMSE",
#         "Nonzero Coefficients",
#         "Best Hyperparameters"
#     ]
# )

# print("\nFULL MODEL COMPARISON")

# print(
#     results_df.to_string(
#         index=False,
#         formatters={
#             "Training R²": "{:.4f}".format,
#             "Test R²": "{:.4f}".format,
#             "Test RMSE": "{:.4f}".format
#         }
#     )
# )

# best_model = results_df.loc[
#     results_df["Test R²"].idxmax()
# ]

# print("\nBest Model based on Test R²:")
# print(best_model["Model"])
