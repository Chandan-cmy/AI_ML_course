# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.datasets import make_moons
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.metrics import accuracy_score
# # Non-linear dataset
# X, y = make_moons(n_samples=300, noise=0.25, random_state=42)
# X_tr, X_te, y_tr, y_te = train_test_split(
#  X, y, test_size=0.2, random_state=42
# )
# # CRITICAL: Scale before KNN (distance-based!)
# scaler = StandardScaler()
# X_tr_s = scaler.fit_transform(X_tr)
# X_te_s = scaler.transform(X_te)
# # Try different K values
# k_values = [1, 3, 5, 10, 20, 50]
# print(f"{'K':>4} | {'Train Acc':>10} | {'Test Acc':>10} | Note")
# print('-' * 55)
# for k in k_values:
#     knn = KNeighborsClassifier(n_neighbors=k)
#     knn.fit(X_tr_s, y_tr)
#     tr_acc = accuracy_score(y_tr, knn.predict(X_tr_s))
#     te_acc = accuracy_score(y_te, knn.predict(X_te_s))
#     note = ''
#     if k == 1: note = '<- memorises training (overfit)'
#     if te_acc == max([accuracy_score(y_te,KNeighborsClassifier(n_neighbors=x).fit(X_tr_s,y_tr).predict(X_te_s))
#         for x in k_values]): note = '<- best test accuracy'
#     print(f"{k:>4} | {tr_acc:>10.4f} | {te_acc:>10.4f} | {note}")
# # Best K via cross-validation
# from sklearn.model_selection import cross_val_score
# cv_scores = []
# for k in range(1, 31):
#     knn = KNeighborsClassifier(n_neighbors=k)
#     cv = cross_val_score(knn, X_tr_s, y_tr, cv=5).mean()
#     cv_scores.append(cv)
# best_k = np.argmax(cv_scores) + 1
# print(f"\nBest K by cross-validation: {best_k}")
# print(f"CV Accuracy at K={best_k}: {cv_scores[best_k-1]:.4f}")



# import numpy as np
# from sklearn.naive_bayes import GaussianNB
# from sklearn.datasets import load_breast_cancer, load_iris
# from sklearn.model_selection import train_test_split, cross_val_score
# from sklearn.preprocessing import StandardScaler
# from sklearn.metrics import accuracy_score, classification_report
# import warnings
# warnings.filterwarnings('ignore')

# data = load_breast_cancer()
# X_tr, X_te, y_tr, y_te = train_test_split(
#  data.data, data.target, test_size=0.2, random_state=42,
# stratify=data.target
# )

# gnb = GaussianNB()
# gnb.fit(X_tr, y_tr)

# print('=== Gaussian Naive Bayes: Breast Cancer ===')
# print(f'Training accuracy : {accuracy_score(y_tr, gnb.predict(X_tr)):.4f}')
# print(f'Test accuracy : {accuracy_score(y_te, gnb.predict(X_te)):.4f}')
# print(f'5-Fold CV : {cross_val_score(gnb, data.data, data.target,cv=5).mean():.4f}')
# print()
# print(classification_report(y_te, gnb.predict(X_te),target_names=data.target_names))



# from sklearn.ensemble import RandomForestClassifier
# import xgboost as xgb
# import time

# models = {
#  'Gaussian NB' : GaussianNB(),
#  'Random Forest' : RandomForestClassifier(n_estimators=100,random_state=42),
#  'XGBoost' : xgb.XGBClassifier(n_estimators=200,eval_metric='logloss',random_state=42, n_jobs=-1)
#  }

# print('\nSpeed and accuracy comparison:')
# print(f"{'Model':18} | {'Train Time':>12} | {'Test Acc':>10}")
# print('-' * 48)
# for name, m in models.items():
#     t0 = time.time()
#     m.fit(X_tr, y_tr)
#     elapsed = time.time() - t0
#     acc = accuracy_score(y_te, m.predict(X_te))
#     print(f"{name:18} | {elapsed:>10.4f}s | {acc:>10.4f}")


# import numpy as np
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score, classification_report

# emails = [
#  # SPAM
#  'Win a free iPhone now click here',
#  'Congratulations you won Rs 1 crore claim now',
#  'Free gift waiting for you click to claim',
#  'You have been selected win free prize',
#  'Urgent claim your lottery prize today free',
#  'Special offer buy now get free gift',
#  'Click here to claim your free reward now',
#  'Win big prize today click free offer',
#  # NOT SPAM
#  'Meeting tomorrow at 10am please confirm',
#  'Please review the attached quarterly report',
#  'Can we reschedule the project meeting',
#  'The team lunch is on Friday at noon',
#  'Please find the invoice attached for review',
#  'Reminder your dentist appointment is Thursday',
#  'The project deadline has been moved to next week',
#  'Thanks for the report will review and reply',
# ]

# labels = [1,1,1,1,1,1,1,1, 0,0,0,0,0,0,0,0]
# vectorizer = CountVectorizer()
# X = vectorizer.fit_transform(emails)
# print(f'Vocabulary size: {len(vectorizer.vocabulary_)} unique words')
# print(f'Feature matrix : {X.shape}')

# X_tr, X_te, y_tr, y_te = train_test_split(X, labels, test_size=0.25, random_state=42)
# mnb = MultinomialNB(alpha=1.0) # alpha: Laplace smoothing
# mnb.fit(X_tr, y_tr)

# print(f'\nTest accuracy: {accuracy_score(y_te, mnb.predict(X_te)):.4f}')
# # Predict on new emails
# new_emails = [
#  'Win free prize click now',
#  'Meeting reminder for tomorrow'
# ]
# X_new = vectorizer.transform(new_emails)
# preds = mnb.predict(X_new)
# probas = mnb.predict_proba(X_new)

# for email, pred, prob in zip(new_emails, preds, probas):
#     label = 'SPAM' if pred == 1 else 'NOT SPAM'
#     print(f'\n"{email}"')
#     print(f' -> {label} (P(spam)={prob[1]:.3f}, P(notspam)={prob[0]:.3f})')

# import numpy as np
# from sklearn.svm import SVC
# from sklearn.datasets import load_breast_cancer
# from sklearn.model_selection import train_test_split, GridSearchCV
# from sklearn.preprocessing import StandardScaler
# from sklearn.metrics import accuracy_score, classification_report
# import warnings
# warnings.filterwarnings('ignore')

# data = load_breast_cancer()
# X_tr, X_te, y_tr, y_te = train_test_split(data.data, data.target, test_size=0.2, random_state=42,stratify=data.target)

# scaler = StandardScaler()
# X_tr_s = scaler.fit_transform(X_tr)
# X_te_s = scaler.transform(X_te)

# svm = SVC(kernel='rbf', C=1.0, gamma='scale', probability=True,random_state=42)
# svm.fit(X_tr_s, y_tr)

# print('=== SVM (RBF kernel) on Breast Cancer ===')
# print(f'Number of support vectors: {svm.n_support_}')
# print(f'Test accuracy: {accuracy_score(y_te, svm.predict(X_te_s)):.4f}')
# print(classification_report(y_te, svm.predict(X_te_s),target_names=data.target_names))

# param_grid = {
#  'C' : [0.1, 1, 10, 100],
#  'gamma': ['scale', 'auto', 0.001, 0.01, 0.1]
# }

# grid = GridSearchCV(SVC(kernel='rbf', random_state=42),param_grid, cv=5, scoring='accuracy', n_jobs=-1)
# grid.fit(X_tr_s, y_tr)
# print(f'\nBest params : {grid.best_params_}')
# print(f'Best CV score : {grid.best_score_:.4f}')
# print(f'Test accuracy : {accuracy_score(y_te, grid.predict(X_te_s)):.4f}')

# import numpy as np
# import pandas as pd
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.naive_bayes import GaussianNB
# from sklearn.svm import SVC
# from sklearn.ensemble import RandomForestClassifier
# import xgboost as xgb
# import lightgbm as lgb
# from sklearn.preprocessing import StandardScaler
# from sklearn.pipeline import Pipeline
# from sklearn.model_selection import train_test_split, cross_val_score
# from sklearn.metrics import accuracy_score, roc_auc_score
# from sklearn.datasets import load_breast_cancer, load_wine
# import warnings
# warnings.filterwarnings('ignore')

# def full_comparison(X, y, dataset_name):
    
#     X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
#     models = {
#         'KNN (k=5)' : Pipeline([('sc', StandardScaler()),('m',KNeighborsClassifier(n_neighbors=5))]),
#         'Gaussian NB' : GaussianNB(),
#         'SVM (RBF)' : Pipeline([('sc', StandardScaler()),('m', SVC(kernel='rbf', C=10,probability=True, random_state=42))]),
#         'Random Forest' : RandomForestClassifier(n_estimators=100,random_state=42, n_jobs=-1),
#         'XGBoost' : xgb.XGBClassifier(n_estimators=200,learning_rate=0.05, max_depth=4,eval_metric='logloss', random_state=42,n_jobs=-1),
#         'LightGBM' : lgb.LGBMClassifier(n_estimators=200,learning_rate=0.05, random_state=42,n_jobs=-1, verbose=-1)
#         }
    
#     print(f'\n=== {dataset_name} ===')
#     print(f"{'Model':18} | {'CV Acc':>8} | {'Test Acc':>9} | {'AUC':>8}")
#     print('-' * 52)

#     for name, model in models.items():
#         cv = cross_val_score(model, X_tr, y_tr, cv=5).mean()
#         model.fit(X_tr, y_tr)
#         acc = accuracy_score(y_te, model.predict(X_te))
#         try:
#             proba = model.predict_proba(X_te)
#             auc = roc_auc_score(y_te, proba[:,1] if proba.shape[1]==2
#             else proba, multi_class='ovr')
#         except:auc = float('nan')
#         print(f"{name:18} | {cv:>8.4f} | {acc:>9.4f} | {auc:>8.4f}")
        
        
# data1 = load_breast_cancer()
# full_comparison(data1.data, data1.target,
#  'Breast Cancer (569 rows, 30 features)')
# data2 = load_wine()
# full_comparison(data2.data, data2.target,
#  'Wine (178 rows, 13 features, 3 classes)')

# import numpy as np
# import pandas as pd
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.naive_bayes import GaussianNB
# from sklearn.svm import SVC
# from sklearn.linear_model import LogisticRegression
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.ensemble import RandomForestClassifier
# import xgboost as xgb
# import lightgbm as lgb
# from sklearn.preprocessing import StandardScaler
# from sklearn.pipeline import Pipeline
# from sklearn.model_selection import train_test_split, cross_val_score
# from sklearn.metrics import accuracy_score, roc_auc_score
# from sklearn.dummy import DummyClassifier
# import warnings
# warnings.filterwarnings('ignore')
# # Load
# df = pd.read_csv('titanic_cleaned.csv')
# features = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
# X, y = df[features], df['Survived']
# X_tr, X_te, y_tr, y_te = train_test_split(
#  X, y, test_size=0.2, random_state=42, stratify=y
# )
# def sc(model):
#     return Pipeline([('sc', StandardScaler()), ('m', model)])
# models = {
#  'Baseline' : DummyClassifier(strategy='most_frequent'),
#  'Logistic Reg' : sc(LogisticRegression(max_iter=1000)),
#  'Decision Tree' : DecisionTreeClassifier(max_depth=5,random_state=42),
#  'Random Forest' : RandomForestClassifier(n_estimators=100,random_state=42, n_jobs=-1),
#  'XGBoost' : xgb.XGBClassifier(n_estimators=200,learning_rate=0.05,eval_metric='logloss', random_state=42,n_jobs=-1),
#  'LightGBM' : lgb.LGBMClassifier(n_estimators=200,learning_rate=0.05,random_state=42, n_jobs=-1, verbose=-1),
#  'KNN (k=7)' : sc(KNeighborsClassifier(n_neighbors=7)),
#  'Gaussian NB' : GaussianNB(),
#  'SVM (RBF)' : sc(SVC(kernel='rbf', C=10,probability=True, random_state=42))
# }

# results = []
# for name, model in models.items():
#     cv = cross_val_score(model, X_tr, y_tr, cv=5).mean()
#     model.fit(X_tr, y_tr)
#     acc = accuracy_score(y_te, model.predict(X_te))
#     try:
#         auc = roc_auc_score(y_te, model.predict_proba(X_te)[:,1])
#     except:
#         auc = float('nan')
#     results.append({'Model': name, 'CV Acc': cv, 'Test Acc': acc, 'AUC':auc})

# results_df = pd.DataFrame(results).sort_values('CV Acc', ascending=False)
# print(results_df.to_string(index=False))

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split, cross_val_score
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.preprocessing import StandardScaler
# from sklearn.pipeline import Pipeline
# from sklearn.metrics import accuracy_score

# data = load_iris()

# X = pd.DataFrame(data.data, columns=data.feature_names)
# y = data.target

# X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2,random_state=42,stratify=y)
# k_values = [1, 3, 5, 7, 9, 11, 15, 21]
# train_acc = []
# test_acc = []
# cv_acc = []

# for i in k_values:
#     model=Pipeline([
#         ("scaler",StandardScaler()),
#         ("knn",KNeighborsClassifier(n_neighbors=i))
#     ])
    
#     model.fit(X_train,y_train)
#     y_tr_pred=model.predict(X_train)
#     y_te_pred=model.predict(X_test)
    
#     train_ac=accuracy_score(y_train,y_tr_pred)
#     test_ac = accuracy_score(y_test, y_te_pred)
#     train_acc.append(train_ac)
#     test_acc.append(test_ac)
    
#     scores = cross_val_score(
#         model, X_train, y_train, cv=5, scoring="accuracy"
#     )

#     cv_acc.append(scores.mean())

#     print(
#         f"k={i:2d} | "
#         f"Train Accuracy={train_ac:.4f} | "
#         f"Test Accuracy={test_ac:.4f} | "
#         f"CV Accuracy={scores.mean():.4f}"
#     )

# best_index = np.argmax(cv_acc)
# best_k = k_values[best_index]
# best_cv_score = cv_acc[best_index]

# print("\nBest k:", best_k)
# print(f"Best 5-fold CV Accuracy: {best_cv_score:.4f}")

# # 6. Plot training and testing accuracy
# plt.figure(figsize=(10, 6))

# plt.plot(
#     k_values, train_acc,
#     marker="o", label="Training Accuracy"
# )

# plt.plot(
#     k_values, test_acc,
#     marker="s", label="Test Accuracy"
# )

# plt.xlabel("Number of Neighbors (k)")
# plt.ylabel("Accuracy")
# plt.title("KNN: Training vs Test Accuracy on Iris Dataset")
# plt.xticks(k_values)
# plt.grid(True, alpha=0.3)
# plt.legend()
# plt.tight_layout()
# plt.show()

# =======================================

# import numpy as np
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import precision_score, recall_score, f1_score

# emails = [
#  # SPAM
#  'Win a free iPhone now click here',
#  'Congratulations you won Rs 1 crore claim now',
#  'Free gift waiting for you click to claim',
#  'You have been selected win free prize',
#  'Urgent claim your lottery prize today free',
#  'Special offer buy now get free gift',
#  'Click here to claim your free reward now',
#  'Win big prize today click free offer',
# 'Exclusive deal! Get cheap loans instantly. Apply now.',
# 'Congratulations! You qualify for a free vacation. Claim today.',
# 'Win cash prizes every day. Register now to participate.',
# 'Your loan is pre-approved. Get instant cash with no paperwork.',
# 'Special promotion! Buy one get three free. Shop now.',
# 'Act now to receive your bonus reward. This offer is limited.',
# 'You have won a free shopping voucher. Click here to redeem it.',
#  # NOT SPAM
#  'Meeting tomorrow at 10am please confirm',
#  'Please review the attached quarterly report',
#  'Can we reschedule the project meeting',
#  'The team lunch is on Friday at noon',
#  'Please find the invoice attached for review',
#  'Reminder your dentist appointment is Thursday',
#  'The project deadline has been moved to next week',
#  'Thanks for the report will review and reply',
#  "I have shared the lecture notes with everyone in the class.",
# "Your password was successfully updated. Contact support if this wasn't you.",
# 'The package was delivered to your registered address today.',
# "Let's have lunch together after the examination.",
# 'The conference registration details are attached to this email.',
# 'Your subscription renewal is scheduled for the first of next month.',
# 'Please confirm whether you can attend the project discussion tomorrow.'
# ]


# labels=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# vectorizer=TfidfVectorizer()
# X=vectorizer.fit_transform(emails)

# print(f'Vocabulary size: {len(vectorizer.vocabulary_)} unique words')
# print(f'Feature matrix : {X.shape}')

# X_tr, X_te, y_tr, y_te = train_test_split(X, labels, test_size=0.2, random_state=42, stratify=labels)

# mnb = MultinomialNB(alpha=1.0) 
# mnb.fit(X_tr, y_tr)

# y_pred=mnb.predict(X_te)

# print(f'Precision : {precision_score(y_te, y_pred):.4f}')
# print(f'Recall : {recall_score(y_te, y_pred):.4f}')
# print(f'F1 Score : {f1_score(y_te, y_pred):.4f}')

# new_emails = [
#     "Congratulations! You have won a brand new smartphone. Claim it now!",
#     "Earn extra income from home. Register today for this exclusive offer.",
#     "Hi, please share the notes from yesterday's machine learning class.",
#     "Your interview has been scheduled for Monday at 11 AM. Please confirm.",
#     "Hello, I am following up to check whether you received my project report."
# ]

# X_new=vectorizer.transform(new_emails)

# preds = mnb.predict(X_new)
# probas = mnb.predict_proba(X_new)

# for email, pred, prob in zip(new_emails, preds, probas):
#     label = 'SPAM' if pred == 1 else'NOT SPAM'
#     print(f'\n"{email}"')
#     print(f' -> {label} (P(spam)={prob[1]:.3f}, P(notspam)={prob[0]:.3f})')


# import numpy as np
# import pandas as pd
# from sklearn.svm import SVC
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.datasets import load_breast_cancer
# from sklearn.model_selection import train_test_split, GridSearchCV
# from sklearn.preprocessing import StandardScaler
# from sklearn.metrics import accuracy_score, classification_report
# from sklearn.pipeline import Pipeline
# import warnings
# warnings.filterwarnings('ignore')

# data=load_breast_cancer()

# X=pd.DataFrame(data.data, columns=data.feature_names)
# y=data.target

# X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42, stratify=y)


# pipeline = Pipeline([
#     ("scaler", StandardScaler()),
#     ("svc", SVC())
# ])

# param_grid = [
#     {
#         "svc__kernel": ["rbf"],
#         "svc__C": [0.01, 0.1, 1, 10, 100],
#         "svc__gamma": ["scale", 0.001, 0.01, 0.1, 1]
#     },
#     {
#         "svc__kernel": ["linear"],
#         "svc__C": [0.01, 0.1, 1, 10, 100]
#     }
# ]

# grid = GridSearchCV(pipeline,param_grid,cv=5,scoring="accuracy",n_jobs=-1,return_train_score=True)

# grid.fit(X_train, y_train)


# results = pd.DataFrame(grid.cv_results_)

# results_table = results[
#     [
#         "param_svc__kernel",
#         "param_svc__C",
#         "param_svc__gamma",
#         "mean_test_score"
#     ]
# ].copy()

# results_table.columns = ["Kernel", "C", "Gamma", "CV Accuracy"]

# print("\nCV Accuracy for Every Parameter Combination:")
# print(results_table.to_string(index=False))

# print("\nBest Parameters:", grid.best_params_)
# print(f"Best CV Accuracy: {grid.best_score_:.4f}")

# y_pred = grid.predict(X_test)

# print(f"Test Accuracy: {accuracy_score(y_test, y_pred):.4f}")

# rbf_results = results[
#     results["param_svc__kernel"] == "rbf"
# ].copy()

# heatmap_data = rbf_results.pivot(
#     index="param_svc__gamma",
#     columns="param_svc__C",
#     values="mean_test_score"
# )


# heatmap_data = heatmap_data.reindex(
#     index=["scale", 0.001, 0.01, 0.1, 1],
#     columns=[0.01, 0.1, 1, 10, 100]
# )

# plt.figure(figsize=(10, 6))

# sns.heatmap(
#     heatmap_data,
#     annot=True,
#     fmt=".4f",
#     cmap="YlGnBu",
#     vmin=0,
#     vmax=1
# )
# plt.title("SVC RBF Kernel: 5-Fold CV Accuracy")
# plt.xlabel("C")
# plt.ylabel("Gamma")
# plt.tight_layout()
# plt.show()


# ===============================================


# import time
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# from sklearn.datasets import load_iris, load_digits
# from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
# from sklearn.pipeline import Pipeline
# from sklearn.preprocessing import StandardScaler
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.naive_bayes import GaussianNB
# from sklearn.svm import SVC
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score

# from xgboost import XGBClassifier
# from lightgbm import LGBMClassifier
# import warnings
# warnings.filterwarnings('ignore')


# def sc(model):
#  return Pipeline([('sc', StandardScaler()), ('m', model)])



# def comparison(X, y, dataset_name):

#     X_train, X_test, y_train, y_test = train_test_split(
#         X, y,
#         test_size=0.2,
#         random_state=42,
#         stratify=y
#     )

#     models = {
#         "KNN": sc(KNeighborsClassifier(n_neighbors=5)),
#         "Naive Bayes": sc(GaussianNB()),
#         "SVM": sc(SVC(kernel="rbf", C=1, random_state=42)),
#         "Random Forest": sc(RandomForestClassifier(
#             n_estimators=100, random_state=42, n_jobs=-1
#         )),
#         "XGBoost": sc(XGBClassifier(
#             n_estimators=100, max_depth=4, learning_rate=0.1,
#             random_state=42, n_jobs=-1, verbosity=0
#         )),
#         "LightGBM": sc(LGBMClassifier(
#             n_estimators=100, learning_rate=0.1,
#             random_state=42, n_jobs=-1, verbosity=-1
#         ))
#     }

#     results = []

#     print(f"\nDataset: {dataset_name}")

#     for name, model in models.items():

#         # 1. Five-fold cross-validation
#         cv_scores = cross_val_score(
#             model, X_train, y_train,
#             cv=5, scoring="accuracy", n_jobs=1
#         )
#         cv_accuracy = cv_scores.mean()

#         # 2. Train the model and measure training time
#         t = time.perf_counter()
#         model.fit(X_train, y_train)
#         training_time = time.perf_counter() - t

#         # 3. Predict and calculate test accuracy
#         y_pred = model.predict(X_test)
#         test_accuracy = accuracy_score(y_test, y_pred)

#         results.append({
#             "Dataset": dataset_name,
#             "Model": name,
#             "CV Accuracy": cv_accuracy,
#             "Test Accuracy": test_accuracy,
#             "Training Time (s)": training_time
#         })

#         print(
#             f"{name:15} | CV: {cv_accuracy:.4f} | "
#             f"Test: {test_accuracy:.4f} | "
#             f"Time: {training_time:.4f}s"
#         )

#     return pd.DataFrame(results)

# data1=load_iris()
# iris_results = comparison(data1.data, data1.target, "Iris")

# data2=load_digits()
# digits_results = comparison(data2.data, data2.target, "Digits")

# print("\n\nFINAL RESULTS TABLE")
# print(all_results.round(4).to_string(index=False))

# plot_data = all_results.pivot(
#     index="Model",
#     columns="Dataset",
#     values="Test Accuracy"
# )

# plot_data.plot(
#     kind="bar",
#     figsize=(12, 6),
#     width=0.8
# )

# plt.title("Six-Algorithm Tournament: Test Accuracy")
# plt.xlabel("Machine Learning Model")
# plt.ylabel("Test Accuracy")
# plt.ylim(0, 1.05)
# plt.xticks(rotation=25, ha="right")
# plt.legend(title="Dataset")
# plt.grid(axis="y", linestyle="--", alpha=0.4)
# plt.tight_layout()
# plt.show()
# import numpy as np
# import pandas as pd
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.naive_bayes import GaussianNB
# from sklearn.svm import SVC
# from sklearn.preprocessing import StandardScaler
# from sklearn.pipeline import Pipeline
# from sklearn.model_selection import train_test_split, cross_val_score
# from sklearn.metrics import accuracy_score, roc_auc_score
# from sklearn.datasets import load_iris

# data = load_iris()
# X,y=data.data,data.target

# X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2,random_state=42,stratify=y)

# models = {
#  'KNN (k=5)' : Pipeline([('sc', StandardScaler()),('m',KNeighborsClassifier(n_neighbors=5))]),
#  'Gaussian NB' : GaussianNB(),
#  'SVM (RBF)' : Pipeline([('sc', StandardScaler()),('m', SVC(kernel='rbf', C=10,probability=True, random_state=42))])
#  }

# for name,model in models.items():
#     cv=cross_val_score(X,y,model,cv=5,n_jobs=-1)
#     print (f"cv_score:{(cv):.4f}")

# Pipeline=clone(model["KNN (k=5)"])

# Pipeline.fit(X_train,y_train)
# Pipeline_pred=Pipeline.predict(X_test)
# Pipeline_acc=accuracy_score(y_test,Pipeline_pred)

# print(f"KNN_acc:{Pipeline_acc}")

# sc=StandardScaler()
# X_train_sc=sc.fit_tansform(X_train)
# X_test_sc=sc.transform(X_test)

# knn=KNeighborsClassifier(n_neighbors=5)
# knn.fit(X_test_sc,y_train)

# knn_acc=accuracy_score(y_test,knn.predict(X_test_sc))
# print(f"KNN_acc_manual:{knn_acc}")


