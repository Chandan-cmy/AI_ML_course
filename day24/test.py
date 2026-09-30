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

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

rf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
rf.fit(X_tr, y_tr)

perm_imp = permutation_importance(
 rf, X_te, y_te,
 n_repeats = 10, # shuffle each feature 10 times, take mean
 random_state = 42,
 n_jobs = -1
)

imp_df = pd.DataFrame({
    'Feature' : data.feature_names,
    'Builtin Imp' : rf.feature_importances_,
    'Perm Imp' : perm_imp.importances_mean,
    'Perm Std' : perm_imp.importances_std
    }).sort_values('Perm Imp', ascending=False)


print('Top 10 features by permutation importance:')
print(f"{'Feature':>30} | {'Built-in':>10} | {'Perm Imp':>10} |{'Std':>6}")
print('-' * 65)
for _, row in imp_df.head(10).iterrows():
    print(f"{row['Feature']:>30} | {row['Builtin Imp']:>10.4f} | ",
    f"{row['Perm Imp']:>10.4f} | {row['Perm Std']:>6.4f}")
