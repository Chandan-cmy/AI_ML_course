# import numpy as np

# def gini_impurity(classes):
#     classes = np.array(classes)
#     n=len(classes)
#     if n==0:
#         return 0
#     unique, counts=np.unique(classes, return_counts=True)
#     proportions=counts/n
#     return 1-np.sum(proportions**2)

# print("Gini Impurity Examples:")
# print(f" all class 0 [0,0,0,0,0]:{gini_impurity([0,0,0,0,0]):.4f}(pure)")
# print(f"50/50 split [0,0,0,1,1,1]:{gini_impurity([0,0,0,1,1,1]):.4f}half and half)")
# print(f"60/40 split [0,0,0,0,1,1,1,1,1,1]:{gini_impurity([0,0,0,0,1,1,1,1,1,1]):.4f}")
# print(f" All class 1 [1,1,1,1,1] :{gini_impurity([1,1,1,1,1]):.4f} (pure)")
# print(f" 3-class equal [0,0,1,1,2,2] :{gini_impurity([0,0,1,1,2,2]):.4f}")

# before = [0,0,0,0,0,1,1,1,1,1]

# print(f"before split:{gini_impurity(before):.4f}")

# left_a=[0,0,0,0,1]
# right_a=[0,1,1,1,1]

# weighted_a=(len(left_a)*gini_impurity(left_a)+
#             len(right_a)*gini_impurity(right_a))/len(before)

# left_b=[0,0,0,0,0]
# right_b=[1,1,1,1,1]

# weighted_b=(len(left_b)*gini_impurity(left_b)+
#             len(right_b)*gini_impurity(right_b))/len(before)

# print(f" Split A weighted Gini: {weighted_a:.4f}")
# print(f" Split B weighted Gini: {weighted_b:.4f} <- perfect split!")
# print(f" The algorithm chooses Split B (lower Gini).")

# print(gini_impurity(right_a))

# import numpy as np

# def entropy(classes):
#     classes = np.array(classes)
#     n=len(classes)
#     if n==0:
#         return 0
#     unique, counts=np.unique(classes, return_counts=True)
#     proportions=counts/n
#     return -np.sum(proportions*np.log2(proportions+1e-10))

# def information_gain (parent,left,right):
    
#     n=len(parent)
#     nl=len(left)
#     nr=len(right)
#     return (entropy(parent)- (nl/n) * entropy(left)- (nr/n) * entropy(right))

# parent = [0,0,0,0,0,1,1,1,1,1]
# split_a_left = [0,0,0,0,1]; split_a_right = [0,1,1,1,1]
# split_b_left = [0,0,0,0,0]; split_b_right = [1,1,1,1,1]
# print(f"Parent entropy : {entropy(parent):.4f} (maximum disorder,50/50)")
# print(f"Split A Info Gain : {information_gain(parent, split_a_left,split_a_right):.4f}")
# print(f"Split B Info Gain : {information_gain(parent, split_b_left,split_b_right):.4f} <- maximum gain!")
# print("Higher information gain = better split.")


# import numpy as np
# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score, classification_report
# from sklearn.datasets import load_iris
# import matplotlib.pyplot as plt


# iris = load_iris()
# X = pd.DataFrame(iris.data, columns=iris.feature_names)
# y = iris.target
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)


# dt = DecisionTreeClassifier(
#  max_depth = 3,
#  criterion = 'gini',
#  random_state = 42
# )
# dt.fit(X_train, y_train)

# y_pred = dt.predict(X_test)
# print(f"Accuracy : {accuracy_score(y_test, y_pred):.4f}")
# print(classification_report(y_test, y_pred,target_names=iris.target_names))

# plt.figure(figsize=(18, 8))
# plot_tree(
#     dt,
#     feature_names = iris.feature_names,
#     class_names = iris.target_names,
#     filled = True, # colour nodes by majority class
#     rounded = True,
#     fontsize = 11
#    )

# plt.title("Decision Tree — Iris Classification (max_depth=3)",fontsize=15, fontweight='bold')
# plt.tight_layout()
# # plt.savefig('decision_tree_iris.png', dpi=150, bbox_inches='tight')
# plt.show()

# print("\nTree structure as text:")
# print(export_text(dt, feature_names=list(iris.feature_names)))



# import numpy as np
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# from sklearn.datasets import load_breast_cancer
# import matplotlib.pyplot as plt
# data = load_breast_cancer()
# X_tr, X_te, y_tr, y_te = train_test_split(data.data, data.target, test_size=0.2, random_state=42,stratify=data.target)
# depths = list(range(1, 21))
# train_accs = []
# test_accs = []


# for depth in depths:
#     dt = DecisionTreeClassifier(max_depth=depth, random_state=42)
#     dt.fit(X_tr, y_tr)
#     train_accs.append(accuracy_score(y_tr, dt.predict(X_tr)))
#     test_accs.append(accuracy_score(y_te, dt.predict(X_te)))


# print(f"{'Depth':>6} | {'Train Acc':>10} | {'Test Acc':>10} | Note")
# print("-" * 55)

# for d, tr, te in zip(depths, train_accs, test_accs):
#     note = ''
#     if te == max(test_accs):
#         note = '<- best test accuracy'
#     elif d >= 15:
#         note = '<- severe overfit'
#     print(f"{d:>6} | {tr:>10.4f} | {te:>10.4f} | {note}")


# plt.figure(figsize=(11, 5))
# plt.plot(depths, train_accs, 'b-o', ms=6, lw=2, label='Training accuracy')
# plt.plot(depths, test_accs, 'r-s', ms=6, lw=2, label='Test accuracy')
# best_depth = depths[np.argmax(test_accs)]

# plt.axvline(x=best_depth, color='green', ls='--', lw=2, label=f'Best depth = {best_depth}')
# plt.title('Decision Tree: Train vs Test Accuracy by Depth',fontsize=13, fontweight='bold')
# plt.xlabel('Max Depth', fontsize=12)
# plt.ylabel('Accuracy', fontsize=12)
# plt.legend(fontsize=11)
# plt.grid(True, alpha=0.4)
# plt.tight_layout()
# plt.savefig('depth_vs_accuracy.png', dpi=150, bbox_inches='tight')
# plt.show()
# print(f'\nBest test accuracy at depth = {best_depth}')


# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import GridSearchCV, train_test_split
# from sklearn.datasets import load_breast_cancer
# from sklearn.metrics import accuracy_score
# import numpy as np
# data = load_breast_cancer()
# X_tr, X_te, y_tr, y_te = train_test_split(data.data, data.target, test_size=0.2, random_state=42,stratify=data.target)

# param_grid = {
#  'max_depth' : [3, 4, 5, 6, 7, 8],
#  'min_samples_split': [2, 5, 10, 20],
#  'min_samples_leaf' : [1, 2, 4, 8],
#  'criterion' : ['gini', 'entropy']
# }

# grid = GridSearchCV(
#  DecisionTreeClassifier(random_state=42),
#  param_grid,
#  cv = 5,
#  scoring = 'accuracy',
#  n_jobs = -1
# )
# grid.fit(X_tr, y_tr)

# print(f"Best params : {grid.best_params_}")
# print(f"Best CV accuracy: {grid.best_score_:.4f}")
# print(f"Test accuracy : {accuracy_score(y_te, grid.predict(X_te)):.4f}")
# best_tree = grid.best_estimator_
# print(f"\nBest tree has {best_tree.get_n_leaves()} leaves")
# print(f"Best tree depth : {best_tree.get_depth()}")


# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.datasets import load_breast_cancer
# from sklearn.model_selection import train_test_split
# data = load_breast_cancer()
# X = pd.DataFrame(data.data, columns=data.feature_names)
# y = data.target
# X_tr, X_te, y_tr, y_te = train_test_split(
#  X, y, test_size=0.2, random_state=42, stratify=y
# )
# dt = DecisionTreeClassifier(max_depth=5, random_state=42)
# dt.fit(X_tr, y_tr)


# importances = pd.Series(dt.feature_importances_,index=data.feature_names)
# importances = importances.sort_values(ascending=False)

# print("Feature Importances (sum = 1.0):")
# print("-" * 55)
# for feat, imp in importances.items():
#     bar = '█' * int(imp * 50)
#     print(f"{feat[:30]:>32}: {imp:.4f} {bar}")

# n_unused = (importances == 0).sum()
# print(f"\nFeatures used : {(importances > 0).sum()}")
# print(f"Features unused : {n_unused}")
# print(f"Top feature : {importances.index[0]}")
# print(f"Top importance : {importances.iloc[0]:.4f}")


# top10 = importances.head(10)
# plt.figure(figsize=(10, 6))
# bars = plt.barh(top10.index[::-1], top10.values[::-1],color='#2196F3', edgecolor='white', height=0.7)
# plt.title('Top 10 Feature Importances — Decision Tree',fontsize=14, fontweight='bold')
# plt.xlabel('Importance (fraction of impurity reduced)', fontsize=12)
# plt.grid(axis='x', alpha=0.4)
# plt.tight_layout()
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.tree import DecisionTreeRegressor
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error, r2_score

# np.random.seed(42)

# X = np.sort(np.random.uniform(0, 10, 200)).reshape(-1, 1)
# y=(np.sin(X).ravel() * 3 + X.ravel() * 0.5+ np.random.randn(200) * 0.5)

# X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
# fig, axes = plt.subplots(1, 3, figsize=(16, 5))
# depths = [2, 5, 15]

# for ax, depth in zip(axes, depths):
#     dtr = DecisionTreeRegressor(max_depth=depth, random_state=42)
#     dtr.fit(X_tr, y_tr)
#     r2 = r2_score(y_te, dtr.predict(X_te))
#     rmse = np.sqrt(mean_squared_error(y_te, dtr.predict(X_te)))
#     X_plot = np.linspace(0, 10, 500).reshape(-1, 1)
#     y_plot = dtr.predict(X_plot)
#     ax.scatter(X_te, y_te, color='gray', alpha=0.5, s=20, label='Testdata')
#     ax.plot(X_plot, y_plot, color='#E91E63', lw=2.5)
#     ax.set_title(f'max_depth={depth}\nR²={r2:.3f}, RMSE={rmse:.3f}',
#     fontweight='bold')
#     ax.set_xlabel('X'); ax.set_ylabel('y')
#     ax.grid(True, alpha=0.3)
# plt.suptitle('Decision Tree Regressor: Effect of Depth',fontsize=14, fontweight='bold')
# plt.tight_layout()
# # plt.savefig('regression_tree_depths.png', dpi=150, bbox_inches='tight')
# plt.show()

# -----------------------------------------------------------------------------------------------------------------------------------------
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.datasets import make_moons

# X, y = make_moons(n_samples=300, noise=0.25, random_state=42)

# fig, axes = plt.subplots(1, 3, figsize=(16, 5))
# depths = [1, 5, 15]
# colours = ['#2196F3', '#E91E63']

# for ax, depth in zip(axes, depths):
#     dt = DecisionTreeClassifier(max_depth=depth, random_state=42)
#     dt.fit(X, y)
#     x_min, x_max = X[:,0].min()-0.5, X[:,0].max()+0.5
#     y_min, y_max = X[:,1].min()-0.5, X[:,1].max()+0.5
#     xx, yy = np.meshgrid(np.linspace(x_min, x_max, 300),np.linspace(y_min, y_max, 300))
#     Z = dt.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
    
#     ax.contourf(xx, yy, Z, alpha=0.25,colors=['#90CAF9', '#F48FB1'])
#     for cls in [0, 1]:
#         ax.scatter(X[y==cls, 0], X[y==cls, 1],
#         c=colours[cls], s=30, alpha=0.7,
#         edgecolors='white', lw=0.5, label=f'Class {cls}')
#     train_acc = dt.score(X, y)
#     ax.set_title(f'max_depth={depth} Train acc={train_acc:.2f}',
#     fontweight='bold')
#     ax.set_xlabel('Feature 1'); ax.set_ylabel('Feature 2')

# plt.suptitle('Decision Tree Decision Boundaries on Moon Dataset',fontsize=13, fontweight='bold')
# plt.tight_layout()
# # plt.savefig('decision_boundaries.png', dpi=150, bbox_inches='tight')
# plt.show()


# ------------------------------------------------------------------------------------------------------

# import numpy as np
# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
# from sklearn.model_selection import train_test_split, GridSearchCV
# from sklearn.metrics import (accuracy_score, classification_report,confusion_matrix)
# from sklearn.dummy import DummyClassifier
# import matplotlib.pyplot as plt
# import seaborn as sns
# import warnings
# warnings.filterwarnings('ignore')

# df=pd.read_csv("titanic_cleaned.csv")
# features= ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']

# x= df[features]
# y=df["Survived"]

# print(f'Dataset: {x.shape}, Survival rate: {y.mean():.2%}')

# x_tr,x_te,y_tr,y_te=train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)

# dummy = DummyClassifier(strategy='most_frequent').fit(x_tr, y_tr)
# print(f'Baseline accuracy: {accuracy_score(y_te,dummy.predict(x_te)):.4f}')

# param_grid = {
#  'max_depth' : [3, 4, 5, 6, 7],
#  'min_samples_split': [2, 10, 20],
#  'min_samples_leaf' : [1, 5, 10],
#  'criterion' : ['gini', 'entropy']
# }

# grid = GridSearchCV(
#     DecisionTreeClassifier(random_state=42),
#     param_grid, 
#     cv=5, 
#     scoring='accuracy', 
#     n_jobs=-1
# )

# grid.fit(x_tr,y_tr)

# best_dt = grid.best_estimator_
# y_pred = best_dt.predict(x_te)

# print(f'\nBest params : {grid.best_params_}')
# print(f'CV accuracy : {grid.best_score_:.4f}')
# print(f'Test accuracy: {accuracy_score(y_te, y_pred):.4f}')
# print(classification_report(y_te, y_pred,target_names=['Did not survive', 'Survived']))


# imp_df = pd.DataFrame({
#     'Feature' : features,
#  'Importance': best_dt.feature_importances_
#  }).sort_values('Importance', ascending=False)
# print('Feature Importances:')
# print(imp_df.to_string(index=False))


# plt.figure(figsize=(18, 8))
# plot_tree(best_dt, feature_names=features,
#  class_names=['Not Survived', 'Survived'],
#  filled=True, rounded=True, fontsize=10)
# plt.title('Decision Tree — Titanic Survival', fontsize=14,fontweight='bold')
# plt.tight_layout()
# plt.savefig('titanic_tree.png', dpi=150, bbox_inches='tight')
# plt.show()

# ---------------------------Exercise 1 — Tree on Iris with Visualisation (Beginner)-------------------------------
# import numpy as np
# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
# from sklearn.model_selection import train_test_split, GridSearchCV
# from sklearn.metrics import (accuracy_score, classification_report,confusion_matrix)
# from sklearn.datasets import load_iris
# import matplotlib.pyplot as plt

# data=load_iris()

# X = pd.DataFrame(data.data, columns=data.feature_names)
# y=data.target

# X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)

# dt=DecisionTreeClassifier(
#     max_depth=3,
#     random_state=42,
#     criterion='gini')

# dt.fit(X_train,y_train)

# y_pred=dt.predict(X_test)

# print(classification_report(y_test,y_pred,target_names=data.target_names))

# plt.figure(figsize=(18, 8))
# plot_tree(
#  dt,
#  feature_names = data.feature_names,
#  class_names = data.target_names,
#  filled = True, # colour nodes by majority class
#  rounded = True,
#  fontsize = 11
# )

# plt.title("Decision Tree — Iris Classification (max_depth=3)",
#  fontsize=15, fontweight='bold')
# plt.tight_layout()
# # plt.savefig('decision_tree_iris.png', dpi=150, bbox_inches='tight')
# plt.show()

# print(export_text(dt, feature_names=list(data.feature_names)))



# ----------------------------Exercise 2 — Depth vs Accuracy Plot (Beginner-Intermediate)------------------

# import numpy as np
# import pandas as pd 
# from sklearn.datasets import load_breast_cancer
# from sklearn.metrics import accuracy_score
# from sklearn.model_selection import train_test_split
# import matplotlib.pyplot as plt
# from sklearn.tree import DecisionTreeClassifier

# data= load_breast_cancer()

# X=pd.DataFrame(data.data, columns=data.feature_names)
# y=data.target

# X_tr, X_te, y_tr, y_te = train_test_split(X,y, test_size=0.2, random_state=42,stratify=data.target)

# depths = list(range(1, 21))
# train_accs = []
# test_accs = []

# for depth in depths:
#     dt=DecisionTreeClassifier(
#         max_depth=depth,
#         random_state=42
#     )
#     dt.fit(X_tr,y_tr)
#     train_accs.append(accuracy_score(y_tr, dt.predict(X_tr)))
#     test_accs.append(accuracy_score(y_te, dt.predict(X_te)))
    
# plt.figure(figsize=(11, 5))
# plt.plot(depths, train_accs, 'b-o', ms=6, lw=2, label='Training accuracy')
# plt.plot(depths, test_accs, 'r-s', ms=6, lw=2, label='Test accuracy')
# best_depth = depths[np.argmax(test_accs)]
# plt.axvline(x=best_depth, color='green', ls='--', lw=2,label=f'Best depth = {best_depth}')
# plt.title('Decision Tree: Train vs Test Accuracy by Depth',fontsize=13, fontweight='bold')
# plt.xlabel('Max Depth', fontsize=12)
# plt.ylabel('Accuracy', fontsize=12)
# plt.legend(fontsize=11)
# plt.grid(True, alpha=0.4)
# plt.tight_layout()
# # plt.savefig('depth_vs_accuracy.png', dpi=150, bbox_inches='tight')
# plt.show()
# print(f'\nBest test accuracy at depth = {best_depth}')


# ----------------------------------Exercise 3 — GridSearchCV Tuning (Intermediate)----------------------

# import numpy as np
# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split, GridSearchCV
# from sklearn.metrics import accuracy_score
# import matplotlib.pyplot as plt

# df = pd.read_csv("titanic_cleaned.csv")

# X=df[["Pclass","Age", "SibSp", "Parch", "Fare"]]
# y=df["Survived"]

# X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42,stratify=y)

# param_grid = {
#  'max_depth' : [3, 4, 5, 6, 7, 8],
#  'min_samples_split': [2, 10, 20],
#  'min_samples_leaf' : [1, 5,10],
# }

# grid = GridSearchCV(
#  DecisionTreeClassifier(random_state=42),
#  param_grid,
#  cv = 5,
#  scoring = 'accuracy',
#  n_jobs = -1
# )

# grid.fit(X_tr,y_tr)

# best_dt = grid.best_estimator_

# y_pred = best_dt.predict(X_te)


# print(grid.best_params_)
# print(f"{grid.best_score_:.4f}")
# print(f"{accuracy_score(y_te, y_pred):.4f}")

# imp_df = pd.DataFrame({
#     'Feature' : ["Pclass","Age", "SibSp", "Parch", "Fare"] ,
#  'Importance': best_dt.feature_importances_
#  }).sort_values('Importance', ascending=False)
# print('Feature Importances:')
# print(imp_df.to_string(index=False))

# plt.figure(figsize=(8, 5))

# plt.barh(
#     imp_df['Feature'],
#     imp_df['Importance']
# )

# plt.xlabel("Importance")
# plt.ylabel("Feature")
# plt.title("Titanic Decision Tree - Feature Importances")
# plt.gca().invert_yaxis()

# plt.tight_layout()
# plt.show()


# -------------------------------------Exercise 4 — Regression Tree on Housing Data (Intermediate)-----------------------------

# import numpy as np
# import pandas as pd
# from sklearn.datasets import fetch_california_housing
# from sklearn.tree import DecisionTreeRegressor
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error, r2_score
# import matplotlib.pyplot as plt


# data = fetch_california_housing()

# X = pd.DataFrame(data.data, columns=data.feature_names)

# y= data.target

# X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)

# depths = [3,5,8,15]
# train_r2=[]
# test_r2=[]
# test_rmse=[]
# for depth in depths:
#     dt=DecisionTreeRegressor(max_depth=depth, random_state=42)
#     dt.fit(X_tr,y_tr)
#     y_pred=dt.predict(X_te)
#     train_r2.append(r2_score(y_tr,dt.predict(X_tr)))
#     test_r2.append(r2_score(y_te,y_pred))
#     test_rmse.append(np.sqrt(mean_squared_error(y_te,y_pred)))
    

# print(f"{'Depths':>6} | {'train r2':>10} | {'Test r2':>10} | {'Test rmse':>10} ")
# for d,tr_r2,te_r2,te_rmse in zip(depths,train_r2,test_r2,test_rmse):
#     print(f"{d:>6} | {tr_r2:>10.4f} | {te_r2:>10.4f} | {te_rmse:>10.4f} ")


# best_index = np.argmax(test_r2)

# best_depth = depths[best_index]
# best_test_r2 = test_r2[best_index]

# print("\nSweet Spot:")
# print(f"Depth = {best_depth}")
# print(f"Test R² = {best_test_r2:.4f}")

# plt.figure(figsize=(8, 5))

# plt.plot(
#     depths,
#     test_r2,
#     marker='o',
#     linewidth=2
# )

# plt.xlabel("Tree Depth")
# plt.ylabel("Test R²")
# plt.title("Test R² vs Decision Tree Depth")

# plt.xticks(depths)
# plt.grid(True)

# plt.tight_layout()
# plt.show()



#-------------------------------------------

import numpy as np
from sklearn.tree import DecisionTreeClassifier

X = np.array([
    [20, 30],
    [25, 35],
    [30, 40],
    [40, 60],
    [45, 65],
    [50, 70]
])

y = np.array([0, 0, 0, 1, 1, 1])

def gini_impurity(y):
    
    y = np.array(y)
    if len(y) == 0:
        return 0
    unique, counts = np.unique(y, return_counts=True)
    proportions = counts / len(y)
    
    return 1 - np.sum(proportions ** 2)

def weighted_gini(left_y,right_y):
    total= len(left_y)+len(right_y)
    
    gini_left = gini_impurity(left_y)
    gini_right = gini_impurity(right_y)
    
    return (
        (len(left_y)/total)*gini_left
        + (len(right_y)/total)*gini_right)
    
def best_split(X, y):

    best_feature = None
    best_threshold = None
    best_gini = float("inf")

    # Go through each column
    for feature in range(X.shape[1]):

        # Get the current column
        values = X[:, feature]

        # Try every value as a threshold
        for threshold in np.unique(values):

            # Which rows have value <= threshold?
            left_rows = values <= threshold

            # Which rows have value > threshold?
            right_rows = values > threshold

            # Get the class labels for those rows
            left_y = y[left_rows]
            right_y = y[right_rows]

            # Ignore empty groups
            if len(left_y) == 0 or len(right_y) == 0:
                continue

            # Calculate Gini
            gini = weighted_gini(left_y, right_y)

            # If this is the best split so far
            if gini < best_gini:

                best_gini = gini
                best_feature = feature
                best_threshold = threshold

    return best_feature, best_threshold

our_feature, our_threshold = best_split(X, y)

print("Our Decision Tree")
print("------------------")
print("Best feature   :", our_feature)
print("Best threshold :", our_threshold)

tree = DecisionTreeClassifier(
    criterion="gini",
    max_depth=1,
    random_state=42
)

tree.fit(X, y)


sklearn_feature = tree.tree_.feature[0]
sklearn_threshold = tree.tree_.threshold[0]

print("\nSklearn Decision Tree")
print("---------------------")
print("Best feature   :", sklearn_feature)
print("Best threshold :", sklearn_threshold)

print("\nComparison")


print("Our feature   :", our_feature)
print("Sklearn feature:", sklearn_feature)

print("Our threshold :", our_threshold)
print("Sklearn threshold:", sklearn_threshold)