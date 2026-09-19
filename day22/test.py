# import numpy as np
# import matplotlib.pyplot as plt

# def sigmoid(x):
#     return 1 / (1 + np.exp(-x))

# z= np.linspace(-10, 10, 300)
# p=sigmoid(z)

# print("z value | sigmoid(z) | Interpretation")
# for z_val in [-10, -5, -2, -1, 0, 1, 2, 5, 10]:
#     prob = sigmoid(z_val)
#     if prob < 0.1:
#         interp = "Almost certainly class 0"
#     elif prob < 0.4:
#         interp = "Likely class 0"
#     elif prob < 0.6:
#         interp = "Uncertain (near boundary)"
#     elif prob < 0.9:
#         interp = "Likely class 1"
#     else:
#         interp = "Almost certainly class 1"
#     print(f"{z_val:8.0f} | {prob:.6f} | {interp}")

# plt.figure(figsize=(10, 5))
# plt.plot(z, p, color='#2196F3', lw=3, label='sigmoid(z)')
# plt.axhline(y=0.5, color='red', ls='--', lw=1.5, label='Decision boundary(p=0.5)')
# plt.axvline(x=0, color='gray', ls='--', lw=1)
# plt.fill_between(z, 0.5, p, where=(p>=0.5), alpha=0.15, color='green',
# label='Predict class 1')
# plt.fill_between(z, p, 0.5, where=(p<0.5), alpha=0.15, color='red',
# label='Predict class 0')
# plt.title('The Sigmoid Function — S-Curve', fontsize=14, fontweight='bold')
# plt.xlabel('z = w*x + b (linear combination of features)')
# plt.ylabel('Probability of class 1')
# plt.legend(fontsize=11)
# plt.grid(True, alpha=0.4)
# plt.tight_layout()
# plt.savefig('sigmoid.png', dpi=150, bbox_inches='tight')
# plt.show()


# import numpy as np
# import pandas as pd
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.metrics import (
#  accuracy_score, precision_score, recall_score,
#  f1_score, confusion_matrix, classification_report
# )
# from sklearn.datasets import load_breast_cancer

# data = load_breast_cancer()
# X = pd.DataFrame(data.data, columns=data.feature_names)
# y = data.target

# print(f'Dataset: {X.shape[0]} samples, {X.shape[1]} features')
# print(f'Classes: {data.target_names}')
# print(f'Class 0 (malignant): {np.sum(y==0)}')
# print(f'Class 1 (benign) : {np.sum(y==1)}')

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# scaler = StandardScaler()
# X_train_s= scaler.fit_transform(X_train)
# X_test_s = scaler.transform(X_test)

# model = LogisticRegression(max_iter=1000, random_state=42)
# model.fit(X_train_s, y_train)

# y_pred = model.predict(X_test_s)
# y_pred_proba = model.predict_proba(X_test_s)[:, 1]


# print(f'\nAccuracy : {accuracy_score(y_test, y_pred):.4f}')
# print(f'Precision : {precision_score(y_test, y_pred):.4f}')
# print(f'Recall : {recall_score(y_test, y_pred):.4f}')
# print(f'F1 Score : {f1_score(y_test, y_pred):.4f}')

# print(f'\nFull Classification Report:')
# print(classification_report(y_test, y_pred,target_names=['Malignant', 'Benign']))


# print('Sample predictions with probabilities:')
# for i in range(5):
#     prob = y_pred_proba[i]
#     pred = y_pred[i]
#     actual= y_test[i]
#     label = data.target_names[pred]
#     print(f' Sample {i+1}: P(benign)={prob:.3f} -> Predicted={label}', f'-> Actual={data.target_names[actual]}')



# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.metrics import confusion_matrix

# from sklearn.metrics import confusion_matrix
# from sklearn.datasets import load_breast_cancer

# data = load_breast_cancer()
# X = pd.DataFrame(data.data, columns=data.feature_names)
# y = data.target

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# scaler = StandardScaler()
# X_train_s= scaler.fit_transform(X_train)
# X_test_s = scaler.transform(X_test)


# cm = confusion_matrix(y_test, y_pred)
# tn, fp, fn, tp = cm.ravel()

# print('Confusion Matrix:')
# print(cm)
# print(f'\nTN={tn} FP={fp} FN={fn} TP={tp}')


# accuracy = (tp + tn) / (tp + tn + fp + fn)
# precision = tp / (tp + fp)
# recall = tp / (tp + fn)
# f1 = 2 * precision * recall / (precision + recall)
# specificity = tn / (tn + fp) 

# print(f'\nFrom the confusion matrix:')
# print(f' Accuracy = (TP+TN)/Total = ({tp}+{tn})/{tp+tn+fp+fn} ={accuracy:.4f}')
# print(f' Precision = TP/(TP+FP) = {tp}/({tp}+{fp}) ={precision:.4f}')
# print(f' Recall = TP/(TP+FN) = {tp}/({tp}+{fn}) = {recall:.4f}')
# print(f' F1 Score = 2*P*R/(P+R) = = {f1:.4f}')
# print(f' Specificity = TN/(TN+FP) = {tn}/({tn}+{fp}) ={specificity:.4f}')


# plt.figure(figsize=(7, 5))
# sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
#  xticklabels=['Malignant', 'Benign'],
#  yticklabels=['Malignant', 'Benign'],
#  linewidths=2, linecolor='white')
# plt.title('Confusion Matrix — Breast Cancer Classifier',fontsize=13, fontweight='bold')
# plt.ylabel('Actual Class', fontsize=12)
# plt.xlabel('Predicted Class', fontsize=12)
# plt.tight_layout()
# plt.savefig('confusion_matrix.png', dpi=150, bbox_inches='tight')
# plt.show()


# # Accuracy is misleading with imbalanced classes
# import numpy as np
# from sklearn.metrics import accuracy_score
# # 1000 transactions: 990 legitimate, 10 fraud
# y_true = np.array([0]*990 + [1]*10)
# # Model that ALWAYS predicts legitimate (no fraud detected ever)
# y_lazy = np.zeros(1000, dtype=int)
# # Real fraud detector (catches 8 of 10 frauds)
# y_real = np.array([0]*990 + [0,0,1,1,1,1,1,1,1,1])
# print(f'Lazy model accuracy: {accuracy_score(y_true, y_lazy):.2%}')
# print(f'Real model accuracy: {accuracy_score(y_true, y_real):.2%}')
# print(f'Frauds caught by lazy model: 0 out of 10')
# print(f'Frauds caught by real model: 8 out of 10')
# print(f'\nAccuracy alone makes the lazy model look equally good!')
# print(f'Always use Precision + Recall for imbalanced problems.')

# from sklearn.metrics import precision_score, recall_score
# import numpy as np
# # Scenario: Email spam filter
# # 1=spam, 0=legitimate
# y_true = np.array([1,1,1,1,1,0,0,0,0,0,0,0,0,0,0])
# # 5 spam, 10 legitimate
# # Model A: aggressive (catches all spam but also blocks some real emails)
# y_pred_a = np.array([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0])
# # Caught all 5 spam + blocked 3 real emails
# # Model B: conservative (only blocks very obvious spam)
# y_pred_b = np.array([1,1,1,0,0,0,0,0,0,0,0,0,0,0,0])
# # Caught 3 spam, blocked no real emails
# for name, y_pred in [('Model A (aggressive)', y_pred_a),('Model B (conservative)', y_pred_b)]:
#     p = precision_score(y_true, y_pred)
#     r = recall_score(y_true, y_pred)
#     print(f'{name}:')
#     print(f' Precision = {p:.2f} (of flagged emails, {p*100:.0f}% trulyspam)')
#     print(f' Recall = {r:.2f} (of actual spam, caught {r*100:.0f}%)')
#     print()



# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.metrics import roc_curve, roc_auc_score
# from sklearn.linear_model import LogisticRegression
# from sklearn.datasets import load_breast_cancer
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# # Load and prepare data
# data = load_breast_cancer()
# X_tr, X_te, y_tr, y_te = train_test_split(
#  data.data, data.target, test_size=0.2, random_state=42,
# stratify=data.target
# )
# sc = StandardScaler()
# X_tr = sc.fit_transform(X_tr)
# X_te = sc.transform(X_te)
# model = LogisticRegression(max_iter=1000).fit(X_tr, y_tr)
# y_proba = model.predict_proba(X_te)[:, 1]
# # Compute ROC curve
# fpr, tpr, thresholds = roc_curve(y_te, y_proba)
# auc = roc_auc_score(y_te, y_proba)
# print(f'ROC-AUC Score: {auc:.4f}')
# print(f'\nAUC interpretation:')
# print(f' AUC = 0.50 -> Random guessing (no better than coin flip)')
# print(f' AUC = 0.70 -> Acceptable discriminating ability')
# print(f' AUC = 0.80 -> Good discriminating ability')
# print(f' AUC = 0.90 -> Excellent discriminating ability')
# print(f' AUC = 1.00 -> Perfect classifier')
# print(f' Our model -> {auc:.4f} = {"Excellent" if auc>0.9 else "Good"}')
# # Plot
# plt.figure(figsize=(8, 6))
# plt.plot(fpr, tpr, color='#2196F3', lw=2.5,label=f'Logistic Regression (AUC = {auc:.3f})')
# plt.plot([0,1],[0,1], color='gray', lw=1.5, ls='--', label='Random (AUC = 0.50)')
# plt.fill_between(fpr, tpr, alpha=0.15, color='#2196F3')
# plt.xlabel('False Positive Rate (1 - Specificity)', fontsize=12)
# plt.ylabel('True Positive Rate (Recall)', fontsize=12)
# plt.title('ROC Curve — Breast Cancer Classifier', fontsize=13,fontweight='bold')
# plt.legend(fontsize=11)
# plt.grid(True, alpha=0.4)
# plt.tight_layout()
# # plt.savefig('roc_curve.png', dpi=150, bbox_inches='tight')
# plt.show()


# import numpy as np
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.metrics import classification_report, confusion_matrix
# from sklearn.datasets import load_iris
# import seaborn as sns
# import matplotlib.pyplot as plt
# # ── Iris: 3-class classification ──────────────────────────────
# iris = load_iris()
# X, y = iris.data, iris.target
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
# sc = StandardScaler()
# X_train_s = sc.fit_transform(X_train)
# X_test_s = sc.transform(X_test)
# # multi_class='ovr' = One vs Rest (default for many solvers)
# model = LogisticRegression(max_iter=1000, random_state=42, )

# model.fit(X_train_s, y_train)
# y_pred = model.predict(X_test_s)
# print('=== Multi-class Classification Report ===')
# print(classification_report(y_test, y_pred,target_names=iris.target_names))

# cm = confusion_matrix(y_test, y_pred)
# plt.figure(figsize=(7, 5))
# sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
#  xticklabels=iris.target_names,
#  yticklabels=iris.target_names,
#  linewidths=2, linecolor='white')
# plt.title('Confusion Matrix — Iris 3-Class', fontsize=13,fontweight='bold')
# plt.ylabel('Actual')
# plt.xlabel('Predicted')
# plt.tight_layout()
# # plt.savefig('multiclass_cm.png', dpi=150, bbox_inches='tight')
# plt.show()

# proba = model.predict_proba(X_test_s[:3])
# print('\nClass probabilities for first 3 test samples:')
# for i, row in enumerate(proba):
#     print(f' Sample {i+1}: ',f'setosa={row[0]:.3f}, versicolor={row[1]:.3f},virginica={row[2]:.3f}',f'-> Predicted: {iris.target_names[np.argmax(row)]}')


# import numpy as np
# import pandas as pd
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.metrics import (
#  accuracy_score, precision_score, recall_score,
#  f1_score, confusion_matrix, classification_report
# )
# from sklearn.datasets import load_breast_cancer

# data = load_breast_cancer()
# X = pd.DataFrame(data.data, columns=data.feature_names)
# y = data.target

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
# scaler = StandardScaler()
# X_train_s= scaler.fit_transform(X_train)
# X_test_s = scaler.transform(X_test)

# model = LogisticRegression(max_iter=1000, random_state=42)
# model.fit(X_train_s, y_train)


# y_pred = model.predict(X_test_s)
# y_pred_proba = model.predict_proba(X_test_s)[:, 1]

# thresholds = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
# print(f"{'Threshold':>10} | {'Precision':>10} | {'Recall':>8} | ",f"{'F1':>8} | {'Predicted+':>11} | Note")
# print("-" * 85)

# for t in thresholds:
#     y_pred_t = (y_pred_proba >= t).astype(int)
#     p = precision_score(y_test, y_pred_t, zero_division=0)
#     r = recall_score(y_test, y_pred_t)
#     f1 = f1_score(y_test, y_pred_t, zero_division=0)
#     n_pos = y_pred_t.sum()
#     note = ''
#     if t == 0.5:
#         note = '<- default'
#     elif t < 0.4:
#         note = '<- high recall, more false alarms'
#     elif t > 0.6:
#         note = '<- high precision, misses more cancers'
#     print(f"{t:>10.1f} | {p:>10.4f} | {r:>8.4f} | {f1:>8.4f} | ",f"{n_pos:>11} | {note}")

# print(f'\nFor cancer detection: choose threshold = 0.3 or lower.')
# print(f'Catching every cancer (recall) matters more than false alarms.')

# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import GridSearchCV
# from sklearn.datasets import load_breast_cancer
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# import numpy as np
# data = load_breast_cancer()
# X_tr, X_te, y_tr, y_te = train_test_split(
#  data.data, data.target, test_size=0.2, random_state=42,
# stratify=data.target
# )

# sc = StandardScaler()
# X_tr_s = sc.fit_transform(X_tr)
# X_te_s = sc.transform(X_te)

# param_grid = {'C': [0.001, 0.01, 0.1, 1, 10, 100]}

# grid_search = GridSearchCV(
#  LogisticRegression(max_iter=1000, random_state=42),
#  param_grid,
#  cv=5,
#  scoring='f1',
#  n_jobs=-1
# )

# grid_search.fit(X_tr_s, y_tr)
# print(f'Best C : {grid_search.best_params_["C"]}')
# print(f'Best CV F1 : {grid_search.best_score_:.4f}')
# print(f'Test F1 : {grid_search.score(X_te_s, y_te):.4f}')

# results = grid_search.cv_results_
# print(f'\nAll C values vs CV F1 score:')
# for c, score in zip(param_grid['C'], results['mean_test_score']):
#     marker = ' <- best' if c == grid_search.best_params_['C'] else ''
#     print(f' C={c:>6}: CV F1={score:.4f}{marker}')




import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
 accuracy_score, precision_score, recall_score,
 f1_score, roc_auc_score, classification_report
)
from sklearn.dummy import DummyClassifier
from sklearn.datasets import load_breast_cancer
import warnings
warnings.filterwarnings('ignore')

data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target
print(f'Dataset: {X.shape}, Classes: {data.target_names}')

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

sc = StandardScaler()
X_trs = sc.fit_transform(X_tr)
X_tes = sc.transform(X_te)

dummy = DummyClassifier(strategy='most_frequent').fit(X_trs, y_tr)
print(f'Baseline accuracy: {accuracy_score(y_te, dummy.predict(X_tes)):.4f}')

model = LogisticRegression(C=0.1, max_iter=1000, random_state=42)
model.fit(X_trs, y_tr)

y_pred = model.predict(X_tes)
y_proba = model.predict_proba(X_tes)[:, 1]
print(f'\nLogistic Regression Results:')
print(f' Accuracy : {accuracy_score(y_te, y_pred):.4f}')
print(f' Precision : {precision_score(y_te, y_pred):.4f}')
print(f' Recall : {recall_score(y_te, y_pred):.4f}')
print(f' F1 Score : {f1_score(y_te, y_pred):.4f}')
print(f' ROC-AUC : {roc_auc_score(y_te, y_proba):.4f}')
# ── Cross-validation for robust estimate ──────────────────────
from sklearn.pipeline import Pipeline
pipe = Pipeline([('scaler', StandardScaler()),
 ('clf', LogisticRegression(C=0.1, max_iter=1000))])
cv_scores = cross_val_score(pipe, X, y, cv=5, scoring='f1')
print(f'\n5-Fold CV F1: {cv_scores.mean():.4f} (+/-{cv_scores.std():.4f})')
print(f'CV Scores : {cv_scores.round(4)}')

