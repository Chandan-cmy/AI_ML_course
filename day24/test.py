# import numpy as np
# np.random.seed(42)
# original_data = np.arange(10)
# n = len(original_data)
# print(f'Original data: {original_data}')
# print(f'Size: {n}\n')

# for i in range(4):

#     bootstrap = np.random.choice(original_data, size=n, replace=True)
#     oob = set(original_data) - set(bootstrap) # Out-Of-Bag samples
#     print(f' Sample {i+1}: {bootstrap} <- OOB: {sorted(oob)}')

# print()
# print('On average, each bootstrap sample contains ~63.2% of unique originalrows.')
# print('The remaining ~36.8% are the Out-Of-Bag (OOB) samples.')
# print('OOB samples become a FREE validation set for each tree!')

# n_large = 10000
# prob_not_chosen = (1 - 1/n_large) ** n_large
# print(f'\nP(row excluded from bootstrap) = {prob_not_chosen:.4f} (theory:1/e = 0.3679)')



# import numpy as np
# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score, classification_report
# from sklearn.datasets import load_breast_cancer


# data= load_breast_cancer()
# X, y = data.data, data.target

# X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# single_tree = DecisionTreeClassifier(max_depth=5, random_state=42)
# single_tree.fit(X_tr, y_tr)
# acc_tree = accuracy_score(y_te, single_tree.predict(X_te))

# rf = RandomForestClassifier(
#  n_estimators = 100, # number of trees
#  max_depth = None, # let trees grow deep (forest controlsvariance)
#  random_state = 42,
#  n_jobs = -1 # use all CPU cores
# )
# rf.fit(X_tr, y_tr)
# acc_rf = accuracy_score(y_te, rf.predict(X_te))

# print(f'Single Decision Tree accuracy : {acc_tree:.4f}')
# print(f'Random Forest accuracy : {acc_rf:.4f}')
# print(f'Improvement : +{(acc_rf-acc_tree)*100:.2f}%')
# print()
# print('Full Report (Random Forest):')
# print(classification_report(y_te, rf.predict(X_te),target_names=data.target_names))

# rf_oob = RandomForestClassifier(
#  n_estimators=100, oob_score=True, random_state=42, n_jobs=-1)
# rf_oob.fit(X_tr, y_tr)
# print(f'OOB Score (no test set needed) : {rf_oob.oob_score_:.4f}')
# print(f'Test accuracy (for comparison) : {acc_rf:.4f}')


# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.datasets import load_breast_cancer
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score


# data = load_breast_cancer()
# X_tr, X_te, y_tr, y_te = train_test_split(data.data, data.target, test_size=0.2, random_state=42,stratify=data.target)

# n_trees_list = [1, 5, 10, 20, 50, 100, 200, 500]
# train_scores = []
# test_scores = []

# for n in n_trees_list:
#     rf = RandomForestClassifier(n_estimators=n, random_state=42, n_jobs=-1)
#     rf.fit(X_tr, y_tr)
#     train_scores.append(accuracy_score(y_tr, rf.predict(X_tr)))
#     test_scores.append(accuracy_score(y_te, rf.predict(X_te)))

# print(f"{'n_trees':>8} | {'Train':>8} | {'Test':>8} | Note")
# print("-" * 50)
# for n, tr, te in zip(n_trees_list, train_scores, test_scores):
#     note=''
#     if n == 1: 
#         note = '<- single tree, high variance'
#     if n == 100: 
#         note = '<- good default'
#     if n == 500: note = '<- negligible gain over 100'
#     print(f"{n:>8} | {tr:>8.4f} | {te:>8.4f} | {note}")
    
# plt.figure(figsize=(10, 5))
# plt.plot(n_trees_list, test_scores, 'r-o', lw=2.5, ms=7, label='Testaccuracy')
# plt.plot(n_trees_list, train_scores, 'b--s', lw=2, ms=7, label='Trainaccuracy')
# plt.xscale('log')
# plt.title('Random Forest: Accuracy vs Number of Trees',fontsize=13, fontweight='bold')
# plt.xlabel('Number of Trees (log scale)', fontsize=12)
# plt.ylabel('Accuracy', fontsize=12)
# plt.legend(fontsize=11)
# plt.grid(True, alpha=0.4)
# plt.tight_layout()
# plt.savefig('n_trees_vs_accuracy.png', dpi=150, bbox_inches='tight')
# plt.show()


# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import RandomizedSearchCV
# from sklearn.datasets import load_breast_cancer
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# import numpy as np
# data = load_breast_cancer()
# X_tr, X_te, y_tr, y_te = train_test_split(data.data, data.target, test_size=0.2, random_state=42,stratify=data.target)

# param_dist = {
#  'n_estimators' : [50, 100, 200, 300],
#  'max_depth' : [None, 5, 10, 20],
#  'max_features' : ['sqrt', 'log2', 0.3],
#  'min_samples_leaf': [1, 2, 4],
#  'min_samples_split': [2, 5, 10]
# }

# rf_search = RandomizedSearchCV(
#     RandomForestClassifier(random_state=42, n_jobs=-1),
#     param_distributions = param_dist,
#     n_iter = 30, # try 30 random combinations
#     cv = 5,
#     scoring = 'accuracy',
#     random_state = 42,
#     n_jobs = -1
# )

# rf_search.fit(X_tr, y_tr)
# print(f'Best params : {rf_search.best_params_}')
# print(f'Best CV score : {rf_search.best_score_:.4f}')
# print(f'Test accuracy : {accuracy_score(y_te,rf_search.predict(X_te)):.4f}')


# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.datasets import load_breast_cancer
# from sklearn.model_selection import train_test_split


# data = load_breast_cancer()
# X = pd.DataFrame(data.data, columns=data.feature_names)
# y = data.target
# X_tr, X_te, y_tr, y_te = train_test_split(
#  X, y, test_size=0.2, random_state=42, stratify=y
# )
# # Train both
# single = DecisionTreeClassifier(max_depth=5, random_state=42).fit(X_tr,y_tr)
# forest = RandomForestClassifier(n_estimators=100, random_state=42,n_jobs=-1).fit(X_tr, y_tr)

# imp_single = pd.Series(single.feature_importances_,index=data.feature_names)
# imp_forest = pd.Series(forest.feature_importances_,index=data.feature_names)

# top10 = imp_forest.sort_values(ascending=False).head(10)

# print(f"{'Feature':>30} | {'Single Tree':>12} | {'Random Forest':>13}")
# print("-" * 60)
# for feat in top10.index:
#     print(f"{feat:>30} | {imp_single[feat]:>12.4f} | {imp_forest[feat]:>13.4f}")


# fig, axes = plt.subplots(1, 2, figsize=(15, 6))
# for ax, (imp, title) in zip(axes, [
#  (imp_single.sort_values(ascending=False).head(10),
#  'Single Tree Feature Importances'),
#  (imp_forest.sort_values(ascending=False).head(10),
#  'Random Forest Feature Importances (avg of 100 trees)')]):

#     ax.barh(imp.index[::-1], imp.values[::-1],
#     color='#2196F3', edgecolor='white', height=0.7)
#     ax.set_title(title, fontsize=12, fontweight='bold')
#     ax.set_xlabel('Importance', fontsize=11)
#     ax.grid(axis='x', alpha=0.4)
# plt.tight_layout()
# plt.savefig('importance_comparison.png', dpi=150, bbox_inches='tight')
# plt.show()


# import numpy as np
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split, cross_val_score
# from sklearn.datasets import load_breast_cancer
# from sklearn.metrics import accuracy_score

# data = load_breast_cancer()
# X, y = data.data, data.target

# rf = RandomForestClassifier(
#  n_estimators = 200,
#  oob_score = True, # enable OOB evaluation
#  random_state = 42,
#  n_jobs = -1
# )
# rf.fit(X, y)

# print(f'Trained on: {len(X)} samples (all data)')
# print(f'OOB Score : {rf.oob_score_:.4f}')

# cv_scores = cross_val_score(RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1),X, y, cv=5, scoring='accuracy')
# print(f'5-Fold CV : {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})')
# print(f'CV Scores : {cv_scores.round(4)}')
# print()
# print('OOB score closely matches cross-validation score.')
# print('On small datasets, OOB is extremely valuable because')
# print('you can use ALL data for training.')

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.inspection import permutation_importance
# from sklearn.datasets import load_breast_cancer
# from sklearn.model_selection import train_test_split

# data = load_breast_cancer()
# X = pd.DataFrame(data.data, columns=data.feature_names)
# y = data.target

# X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# rf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
# rf.fit(X_tr, y_tr)

# perm_imp = permutation_importance(
#  rf, X_te, y_te,
#  n_repeats = 10, # shuffle each feature 10 times, take mean
#  random_state = 42,
#  n_jobs = -1
# )

# imp_df = pd.DataFrame({
#     'Feature' : data.feature_names,
#     'Builtin Imp' : rf.feature_importances_,
#     'Perm Imp' : perm_imp.importances_mean,
#     'Perm Std' : perm_imp.importances_std
#     }).sort_values('Perm Imp', ascending=False)


# print('Top 10 features by permutation importance:')
# print(f"{'Feature':>30} | {'Built-in':>10} | {'Perm Imp':>10} |{'Std':>6}")
# print('-' * 65)
# for _, row in imp_df.head(10).iterrows():
#     print(f"{row['Feature']:>30} | {row['Builtin Imp']:>10.4f} | ",
#     f"{row['Perm Imp']:>10.4f} | {row['Perm Std']:>6.4f}")



# import numpy as np
# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import (train_test_split, RandomizedSearchCV, cross_val_score)
# from sklearn.metrics import (accuracy_score, classification_report,roc_auc_score, confusion_matrix)
# from sklearn.dummy import DummyClassifier
# import matplotlib.pyplot as plt
# import seaborn as sns
# import warnings
# warnings.filterwarnings('ignore')


# df = pd.read_csv('titanic_cleaned.csv')
# features = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
# X = df[features]; 
# y = df['Survived']
# print(f'Dataset: {X.shape}')

# X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# dummy = DummyClassifier(strategy='most_frequent').fit(X_tr, y_tr)
# base = accuracy_score(y_te, dummy.predict(X_te))
# print(f'Baseline: {base:.4f}')

# rf_default = RandomForestClassifier(n_estimators=100, random_state=42,n_jobs=-1)
# rf_default.fit(X_tr, y_tr)
# acc_default = accuracy_score(y_te, rf_default.predict(X_te))
# print(f'Default RF accuracy: {acc_default:.4f}')

# param_dist = {
#  'n_estimators' : [100, 200, 300],
#  'max_depth' : [None, 5, 10, 15],
#  'max_features' : ['sqrt', 'log2'],
#  'min_samples_leaf': [1, 2, 4],
#  'min_samples_split': [2, 5, 10]
# }

# search = RandomizedSearchCV(
#  RandomForestClassifier(random_state=42, n_jobs=-1),
#  param_dist, n_iter=20, cv=5, scoring='accuracy',
#  random_state=42, n_jobs=-1
# )

# search.fit(X_tr, y_tr)
# best_rf = search.best_estimator_
# y_pred = best_rf.predict(X_te)
# y_proba = best_rf.predict_proba(X_te)[:, 1]

# print(f'\nBest params : {search.best_params_}')
# print(f'Best CV score : {search.best_score_:.4f}')
# print(f'Test accuracy : {accuracy_score(y_te, y_pred):.4f}')
# print(f'ROC-AUC : {roc_auc_score(y_te, y_proba):.4f}')
# print(classification_report(y_te, y_pred,target_names=['Did not survive', 'Survived']))

# imp = pd.DataFrame({'Feature': features,'Importance': best_rf.feature_importances_})
# print('Feature Importances:')
# print(imp.sort_values('Importance',ascending=False).to_string(index=False))

# rf_oob = RandomForestClassifier(
#  **search.best_params_, oob_score=True, random_state=42, n_jobs=-1)

# rf_oob.fit(X_tr, y_tr)
# print(f'\nOOB Score: {rf_oob.oob_score_:.4f}')


# ------------------------------------------Exercise 1 — Trees vs Forest Comparison (Beginner)-----------------------

# import numpy as np
# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.datasets import load_breast_cancer
# from sklearn.metrics import accuracy_score, f1_score, roc_auc_score

# data=load_breast_cancer()
# X,y=data.data,data.target

# X_tr,X_te,y_tr,y_te=train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)

# dt = DecisionTreeClassifier(max_depth=5, random_state=42)

# dt.fit(X_tr, y_tr)


# print("Decision Tree")
# print("Training Accuracy:", accuracy_score(y_tr, dt.predict(X_tr)))
# print("Test Accuracy:", accuracy_score(y_te, dt.predict(X_te)))
# print("Test F1 Score:", f1_score(y_te, dt.predict(X_te)))
# print("Test ROC-AUC:", roc_auc_score(y_te, dt.predict_proba(X_te)[:, 1]))

# rf=RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
# rf.fit(X_tr,y_tr)

# print("random forest")
# print("Training Accuracy:", accuracy_score(y_tr, rf.predict(X_tr)))
# print("Test Accuracy:", accuracy_score(y_te, rf.predict(X_te)))
# print("Test F1 Score:", f1_score(y_te, rf.predict(X_te)))
# print("Test ROC-AUC:", roc_auc_score(y_te, rf.predict_proba(X_te)[:, 1]))

# -------------------------------------Exercise 2 — n_estimators Study (Beginner-Intermediate)-----------------------

# import numpy as np
# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# import matplotlib.pyplot as plt

# df = pd.read_csv('titanic_cleaned.csv')
# features = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
# X = df[features]; 
# y = df['Survived']

# X_tr,X_te,y_tr,y_te=train_test_split(X,y,test_size=0.2,random_state=42)


# n_estimators = [1, 5, 10, 25, 50, 100, 200, 500]
# train_accs = []
# test_accs = []

# for n in n_estimators:
#     rf=RandomForestClassifier(n_estimators=n,random_state=42,n_jobs=-1)
#     rf.fit(X_tr,y_tr)
#     train_accs.append(accuracy_score(y_tr, rf.predict(X_tr)))
#     test_accs.append(accuracy_score(y_te, rf.predict(X_te)))
    
# print("n_estimators | Training Accuracy | Test Accuracy")

# for n, train_acc, test_acc in zip(n_estimators, train_accs, test_accs):
#     print(f"{n:12} | {train_acc:.4f}           | {test_acc:.4f}")

# plt.figure(figsize=(8, 5))

# plt.plot( n_estimators,
#     train_accs,
#     marker='o',
#     label='Training Accuracy'
#     )

# plt.plot(
#     n_estimators,
#     test_accs,
#     marker='o',
#     label='Test Accuracy'
# )

# plt.xscale('log')

# plt.xlabel('Number of Trees (n_estimators)')
# plt.ylabel('Accuracy')
# plt.title('Random Forest: Accuracy vs Number of Trees')

# plt.legend()
# plt.grid(True)

# plt.show()

# -----------------------------------------Exercise 3 — OOB Score as Validation (Intermediate)-----------------------

# import numpy as np
# import pandas as pd
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.datasets import load_diabetes
# from sklearn.metrics import r2_score
# from sklearn.model_selection import cross_val_score
# data = load_diabetes()
# X=data.data
# y=data.target

# rf=RandomForestRegressor(n_estimators=100, oob_score=True, random_state=42, n_jobs=-1)

# rf.fit(X,y)

# print(f"OOB score: {rf.oob_score_:.4f}")

# cv=cross_val_score(rf,X, y, cv=5, scoring='r2', n_jobs=-1)

# print(f'5-Fold CV : {cv.mean():.4f} (+/- {cv.std():.4f})')
# print(f'CV Scores : {cv.round(4)}')


# --------------------------------------------Exercise 4 — Feature Importance Comparison (Intermediate)-----------------------

# import numpy as np
# import pandas as pd
# from sklearn.datasets import fetch_california_housing
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.inspection import permutation_importance
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import r2_score
# import matplotlib.pyplot as plt

# data=fetch_california_housing()
# X=pd.DataFrame(data.data, columns=data.feature_names)
# y=data.target

# X_tr,X_te,y_tr,y_te=train_test_split(X,y,test_size=0.2,random_state=42)

# rf=RandomForestRegressor(n_estimators=200, random_state=42,n_jobs=-1)

# rf.fit(X_tr,y_tr)

# built_in = pd.Series(
#     rf.feature_importances_,
#     index=X.columns
# ).sort_values(ascending=False)

# perm = permutation_importance(
#     rf,
#     X_te,
#     y_te,
#     n_repeats=10,
#     random_state=42,
#     n_jobs=-1,
#     scoring='r2'
# )

# permutation = pd.Series(
#     perm.importances_mean,
#     index=X.columns
# ).sort_values(ascending=False)

# comparison = pd.DataFrame({
#     'Built-in Importance': rf.feature_importances_,
#     'Permutation Importance': perm.importances_mean
# }, index=X.columns)

# print("\nComparison:")
# print(comparison.sort_values('Built-in Importance',ascending=False))

# comparison.plot(
#     kind='bar',
#     figsize=(12, 6)
# )

# plt.title("Random Forest Feature Importance Comparison")
# plt.xlabel("Features")
# plt.ylabel("Importance")
# plt.xticks(rotation=45)
# plt.legend()
# plt.tight_layout()
# plt.show()

# -----------------------------------------------

# import numpy as np
# import pandas as pd

# from sklearn.datasets import load_breast_cancer
# from sklearn.model_selection import train_test_split, RandomizedSearchCV
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.dummy import DummyClassifier
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import accuracy_score, classification_report

# # --------------------------------------------------
# # 1. Load dataset
# # --------------------------------------------------

# data = load_breast_cancer()

# X = data.data
# y = data.target

# # --------------------------------------------------
# # 2. Train-test split
# # --------------------------------------------------

# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.2,
#     random_state=42,
#     stratify=y
# )

# # --------------------------------------------------
# # 3. Baseline DummyClassifier
# # --------------------------------------------------

# dummy = DummyClassifier(strategy="most_frequent")

# dummy.fit(X_train, y_train)

# dummy_pred = dummy.predict(X_test)

# dummy_accuracy = accuracy_score(y_test, dummy_pred)

# print("DummyClassifier Accuracy:", round(dummy_accuracy, 4))


# # --------------------------------------------------
# # 4. Day 17 Decision Tree
# # --------------------------------------------------

# dt = DecisionTreeClassifier(
#     random_state=42
# )

# dt.fit(X_train, y_train)

# dt_pred = dt.predict(X_test)

# dt_accuracy = accuracy_score(y_test, dt_pred)

# print("Decision Tree Accuracy:", round(dt_accuracy, 4))


# # --------------------------------------------------
# # 5. Random Forest parameter search
# # --------------------------------------------------

# param_dist = {
#     "n_estimators": [50, 100, 200, 300, 500],
#     "max_depth": [None, 3, 5, 7, 10, 15],
#     "max_features": ["sqrt", "log2", None],
#     "min_samples_leaf": [1, 2, 4, 6, 8]
# }


# # --------------------------------------------------
# # 6. RandomizedSearchCV
# # --------------------------------------------------

# rf = RandomForestClassifier(
#     random_state=42,
#     n_jobs=-1
# )

# search = RandomizedSearchCV(
#     estimator=rf,
#     param_distributions=param_dist,
#     n_iter=30,
#     cv=5,
#     scoring="accuracy",
#     random_state=42,
#     n_jobs=-1
# )

# search.fit(X_train, y_train)


# # --------------------------------------------------
# # 7. Best parameters and CV score
# # --------------------------------------------------

# print("\nBest Parameters:")
# print(search.best_params_)

# print("\nBest CV Score:")
# print(round(search.best_score_, 4))


# # --------------------------------------------------
# # 8. Test the tuned Random Forest
# # --------------------------------------------------

# rf_pred = search.predict(X_test)

# rf_accuracy = accuracy_score(y_test, rf_pred)

# print("\nTuned Random Forest Test Accuracy:")
# print(round(rf_accuracy, 4))


# # --------------------------------------------------
# # 9. Classification report
# # --------------------------------------------------

# print("\nTuned Random Forest Classification Report:")
# print(
#     classification_report(
#         y_test,
#         rf_pred,
#         target_names=data.target_names
#     )
# )


# # --------------------------------------------------
# # 10. Compare all models
# # --------------------------------------------------

# print("\nModel Comparison")
# print("-" * 40)

# print(f"DummyClassifier : {dummy_accuracy:.4f}")
# print(f"Decision Tree   : {dt_accuracy:.4f}")
# print(f"Random Forest   : {rf_accuracy:.4f}")

