# from sklearn.model_selection import train_test_split
# import pandas as pd
# import numpy as np

# from sklearn.datasets import load_iris

# iris = load_iris()
# x = iris.data
# y = iris.target

# print(f"Full dataset: X={x.shape}, y={y.shape}")

# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)
# print(f"Training set: X={x_train.shape}, y={y_train.shape}")
# print(f"Test set: X={x_test.shape}, y={y_test.shape}")

# print(f"\nClass distribution in full dataset:")
# print(f"class0 : {np.sum(y==0)}, class1: {np.sum(y==1)}, class2: {np.sum(y==2)}")

# print(f"Class distribution in training set:")
# print(f"class0 : {np.sum(y_train==0)}, class1: {np.sum(y_train==1)}, class2: {np.sum(y_train==2)}")
# print(f"Class distribution in test set:")
# print(f"class0 : {np.sum(y_test==0)}, class1: {np.sum(y_test==1)}, class2: {np.sum(y_test==2)}")


# from sklearn.dummy import DummyClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.datasets import load_iris
# from sklearn.metrics import accuracy_score
# import numpy as np

# iris = load_iris()
# x,y = iris.data, iris.target

# X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=42, stratify=y)
# dummy_most_freq = DummyClassifier(strategy='most_frequent')
# dummy_most_freq.fit(X_train, y_train)
# y_pred_mf = dummy_most_freq.predict(X_test)
# acc_mf = accuracy_score(y_test, y_pred_mf)


# dummy_random = DummyClassifier(strategy='stratified', random_state=42)
# dummy_random.fit(X_train, y_train)
# y_pred_r = dummy_random.predict(X_test)
# acc_r = accuracy_score(y_test, y_pred_r)

# print(f"Baseline (most frequent class) accuracy: {acc_mf:.4f}({acc_mf*100:.1f}%)")
# print(f"Baseline (random stratified) accuracy : {acc_r:.4f}({acc_r*100:.1f}%)")

# print()

# print("Any real model must beat these numbers to be considered useful.")
# print(f"Most frequent class: {iris.target_names[np.bincount(y).argmax()]}")

# import numpy as np
# import pandas as pd
# from sklearn.datasets import load_iris, load_wine
# from sklearn.model_selection import train_test_split
# from sklearn.dummy import DummyClassifier
# from sklearn.metrics import accuracy_score, classification_report

# def run_ml_workflow(dataset_name, X, y, feature_names, target_names):
#     """
#     Runs the full 8-step ML workflow on any dataset.
#     This exact function structure will be reused throughout Phase 2.
#     """
#     print(f"\n{'='*60}")
#     print(f"DATASET: {dataset_name}")
#     print(f"{'='*60}")
    
#     print(f"\nStep 1 — Problem:")
#     print(f" Classify samples into {len(target_names)} classes:{[str(name) for name in target_names]}")
#     print(f" Using {len(feature_names)} features: {list(feature_names)}")
#     print(f"\nStep 2 — Data overview:")
#     print(f" Total samples : {X.shape[0]}")
#     print(f" Total features: {X.shape[1]}")
#     class_counts = np.bincount(y)
    
#     for i, (name, count) in enumerate(zip(target_names, class_counts)):
#         print(f" Class {i} ({name}): {count} samples({count/len(y)*100:.0f}%)")
        
#     print(f"\nStep 3-4 — Data is clean (built-in sklearn dataset)")
    
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
#     print(f"\nStep 5 — Train-test split:")
#     print(f" Training samples: {X_train.shape[0]}")
#     print(f" Test samples : {X_test.shape[0]}")
    
#     model = DummyClassifier(strategy='most_frequent', random_state=42)
#     model.fit(X_train, y_train)
#     print(f"\nStep 6 — Model trained: DummyClassifier (baseline)")
    
#     y_pred = model.predict(X_test)
#     train_acc = accuracy_score(y_train, model.predict(X_train))
#     test_acc = accuracy_score(y_test, y_pred)

#     print(f"\nStep 7 — Evaluation:")
#     print(f" Training accuracy : {train_acc:.4f} ({train_acc*100:.1f}%)")
#     print(f" Test accuracy : {test_acc:.4f} ({test_acc*100:.1f}%)")
#     print(f"\n This baseline must be BEATEN by any real model.")

#     return X_train, X_test, y_train, y_test, test_acc

# iris = load_iris()
# run_ml_workflow('Iris Flowers', iris.data, iris.target, iris.feature_names, iris.target_names)

# wine = load_wine()
# run_ml_workflow('Wine Classification', wine.data, wine.target, wine.feature_names, wine.target_names)


# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# data = {
#     'age' : [25, 35, 45, 28, 52, 33, 41, 29, 38, 47],
#     'monthly_spend' : [500,1200,800,300,950,700,1100,450,600,850],
#     'tenure_months' : [6, 24, 36, 3, 48, 18, 30, 9, 12, 42],
#     'support_calls' : [1, 0, 2, 4, 0, 1, 0, 3, 2, 1],
#     'churned' : [0, 0, 1, 1, 0, 0, 0, 1, 1, 0] # TARGET
#     }
# df = pd.DataFrame(data)

# X = df.drop(columns=['churned']) 
# y = df['churned'] 
# print(f"X shape: {X.shape} (10 customers, 4 features each)")
# print(f"y shape: {y.shape} (10 labels: 0=stayed, 1=churned)")
# print()
# print("X (features):")
# print(X)
# print()
# print("y (target):")
# print(y.values)
# # Split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# print(f"\nX_train: {X_train.shape}, X_test: {X_test.shape}")
# print(f"y_train: {y_train.shape}, y_test: {y_test.shape}")


from sklearn.metrics import (accuracy_score, precision_score, recall_score,f1_score, confusion_matrix, classification_report)
import numpy as np

y_true = np.array([0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0])
y_pred = np.array([0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0])


cm = confusion_matrix(y_true, y_pred)
print(cm)
print(" [TN FP]")
print(" [FN TP]")

tn, fp, fn, tp = cm.ravel()

print(f"\n True Negatives (TN): {tn} — correctly said NOT fraud")
print(f" False Positives (FP): {fp} — wrongly said fraud (false alarm)")
print(f" False Negatives (FN): {fn} — missed actual fraud (dangerous!)")
print(f" True Positives (TP): {tp} — correctly caught fraud")

print(f"\nAccuracy : {accuracy_score(y_true, y_pred):.4f} (correct / total)")
print(f"Precision : {precision_score(y_true, y_pred):.4f} (of predictedfraud, how many were real?)")
print(f"Recall : {recall_score(y_true, y_pred):.4f} (of actual fraud,how many did we catch?)")
print(f"F1 Score : {f1_score(y_true, y_pred):.4f} (harmonic mean ofprecision and recall)")
print("\nFull Report:")
print(classification_report(y_true, y_pred, target_names=['Not Fraud','Fraud']))
