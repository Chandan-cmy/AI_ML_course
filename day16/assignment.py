# import numpy as np
# import matplotlib.pyplot as plt
# # Real data: years of experience vs monthly salary (Rs. thousands)
# experience = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# salary = np.array([25, 30, 35, 38, 45, 50, 55, 60, 68, 75])
# # Suppose the model learned: salary = 5.3 * experience + 19.5
# w = 5.3 # weight: for each extra year, salary increases by Rs. 5.3k
# b = 19.5 # bias: even with 0 experience, starting salary is Rs. 19.5k
# # Predictions
# predicted = w * experience + b
# print("Experience | Actual Salary | Predicted Salary")
# print("-" * 55)
# for exp, actual, pred in zip(experience, salary, predicted):
#     print(f" {exp:2d} years | Rs. {actual:4.0f}k | Rs.{pred:5.1f}k")

# print(f"\nSlope interpretation:")
# print(f"Each additional year adds Rs. {w}k to monthly salary")


# import numpy as np
# # Understanding slope with different relationships
# x = np.array([1, 2, 3, 4, 5])
# # Positive slope: more experience = more salary
# slope_positive = 5.0
# y_positive = slope_positive * x + 20
# print(f"Positive slope={slope_positive}: y = {y_positive}")
# # Negative slope: more distance from city = lower property value
# slope_negative = -3.0
# y_negative = slope_negative * x + 100
# print(f"Negative slope={slope_negative}: y = {y_negative}")
# # Steep vs gentle slope
# print(f"\nSteep slope (m=10): small x change, big y change")
# print(f"Gentle slope (m=0.5): small x change, tiny y change")


# import numpy as np
# # Actual house prices (Rs. lakhs)
# actual = np.array([45, 60, 35, 80, 55, 70, 40, 90])
# # Model A predictions (reasonable model)
# pred_a = np.array([47, 58, 38, 77, 57, 72, 41, 87])

# pred_b = np.array([60, 40, 50, 60, 50, 60, 55, 70])
# def mse(actual, predicted):
#     errors = predicted - actual # Each error
#     squared_errors= errors ** 2 # Square each error
#     return np.mean(squared_errors) # Average the squares
# def mae(actual, predicted):
#     return np.mean(np.abs(predicted - actual)) # Mean Absolute Error
# print("Model A (good predictions):")
# print(f" Errors : {pred_a - actual}")
# print(f" MSE : {mse(actual, pred_a):.2f}")
# print(f" MAE : {mae(actual, pred_a):.2f}")
# print(f" RMSE : {np.sqrt(mse(actual, pred_a)):.2f} lakhs")
# print("\nModel B (bad predictions):")
# print(f" Errors : {pred_b - actual}")
# print(f" MSE : {mse(actual, pred_b):.2f}")
# print(f" MAE : {mae(actual, pred_b):.2f}")
# print(f" RMSE : {np.sqrt(mse(actual, pred_b)):.2f} lakhs")


# import numpy as np
# # Numerical approximation of a derivative
# # 'What happens to y when we increase x by a tiny amount h?'
# def numerical_derivative(f, x, h=1e-5):
#     """Compute derivative of f at point x using finite differences."""
#     return (f(x + h) - f(x - h)) / (2 * h)

# f1 = lambda x: x**2
# print("Function: y = x^2")
# print("Point x | y value | Derivative | Meaning")
# print("-" * 65)
# for x in [-3, -1, 0, 1, 3]:
#     y = f1(x)
#     deriv= numerical_derivative(f1, x)
#     if deriv > 0.1:
#         meaning = "Going UP -> move LEFT to decrease y"
#     elif deriv < -0.1:
#         meaning = "Going DOWN -> move RIGHT to decrease y"
#     else:
#         meaning = "FLAT -> This is the MINIMUM!"
#     print(f" x={x:3d} | y={y:5.1f} | slope={deriv:+6.2f} |{meaning}")
# print("\nThe minimum of x^2 is at x=0 where derivative=0")



# import numpy as np
# # Gradient descent from scratch on a simple problem
# # Finding the minimum of f(w) = w^2 + 4w + 4 = (w+2)^2
# # Minimum is at w = -2 where f(-2) = 0
# def cost_function(w):
#     return w**2 + 4*w + 4
# def gradient(w):
#     """Derivative of w^2 + 4w + 4 with respect to w is 2w + 4"""
#     return 2*w + 4
# learning_rate = 0.1
# n_iterations = 30
# # Start at a random point
# w = 8.0 # Start far from the minimum
# print(f"{'Iteration':>10} | {'w':>8} | {'Cost':>10} | {'Gradient':>10}")
# print("-" * 50)
# for i in range(n_iterations):
#     cost = cost_function(w)
#     grad = gradient(w)
#     if i < 10 or i == n_iterations - 1:
#         print(f"{i+1:>10} | {w:>8.4f} | {cost:>10.4f} | {grad:>10.4f}")
#     # THE core update rule of gradient descent
#     w = w - learning_rate * grad
# print(f"\nFinal w = {w:.6f} (optimal is -2.0)")
# print(f"Final cost = {cost_function(w):.6f} (optimal is 0.0)")


# import numpy as np
# def cost_function(w):
#     return w**2 + 4*w + 4
# def gradient(w):
#     return 2*w + 4
# def run_gradient_descent(learning_rate, n_iter=50, w_start=8.0):
#     w = w_start
#     for _ in range(n_iter):
#         w = w - learning_rate * gradient(w)
#     return w, cost_function(w)
# # Test different learning rates
# learning_rates = [0.001, 0.05, 0.1, 0.5, 1.1]
# print(f"{'Learning Rate':>15} | {'Final w':>10} | {'Final Cost':>12} |{'Assessment'}")
# print("-" * 75)
# for lr in learning_rates:
#     final_w, final_cost = run_gradient_descent(lr)
#     if final_cost < 0.001:
#         assessment = "Converged well"
#     elif final_cost < 1.0:
#         assessment = "Converging slowly"
#     elif abs(final_w) < 1000:
#         assessment = "Learning too slow"
#     else:
#         assessment = "DIVERGED! Too large"
#     print(f"{lr:>15.3f} | {final_w:>10.4f} | {final_cost:>12.6f} |{assessment}")


# import numpy as np
# class LinearRegressionFromScratch:
#    """
#    Linear Regression using Gradient Descent.
#    Predicts y = w * x + b by finding the best w and b.
#    """
#    def __init__(self, learning_rate=0.01, n_iterations=1000):
#       self.lr = learning_rate
#       self.n_iter = n_iterations
#       self.w = None # weight (slope)
#       self.b = None # bias (intercept)
#       self.history = [] # track cost over time
#    def fit(self, X, y):
#       """Train the model on data X and labels y."""
#       n = len(X)
#       # Step 1: Initialise weights randomly
#       self.w = np.random.randn()
#       self.b = np.random.randn()
      
#       for i in range(self.n_iter):
#          y_pred = self.w * X + self.b
#          cost = np.mean((y_pred - y) ** 2)
#          self.history.append(cost)
#          dw = (2/n) * np.dot(X, (y_pred - y)) # derivative w.r.t. w
#          db = (2/n) * np.sum(y_pred - y) # derivative w.r.t. b
#          self.w = self.w - self.lr * dw
#          self.b = self.b - self.lr * db
         
#          if i % 200 == 0:
#             print(f"Iter {i:4d}: Cost={cost:.4f}, w={self.w:.4f},b={self.b:.4f}")
            
#    def predict(self, X):
      
            
#       """Make predictions on new data."""
#       return self.w * X + self.b
      
# np.random.seed(42)
# experience = np.array([1,2,3,4,5,6,7,8,9,10], dtype=float)
# salary = np.array([25,30,35,38,45,50,55,60,68,75], dtype=float)


# model = LinearRegressionFromScratch(learning_rate=0.005, n_iterations=1000)
# model.fit(experience, salary)

# print(f"\nFinal weight (slope): {model.w:.4f}")
# print(f"Final bias (intercept): {model.b:.4f}")

# new_experience = np.array([3.5, 7.0, 12.0])
# predictions = model.predict(new_experience)
# print(f"\nPredictions for new candidates:")
# for exp, pred in zip(new_experience, predictions):
#    print(f" {exp} years experience -> Rs. {pred:.1f}k/month")


# import numpy as np
# # Multiple features: predict salary from experience AND education_years
# # y = w1*experience + w2*education + b
# np.random.seed(42)
# n_samples = 100
# # Generate synthetic data
# experience = np.random.uniform(1, 15, n_samples)
# education = np.random.uniform(10, 22, n_samples)

# salary = 5*experience + 2*education + 10 + np.random.randn(n_samples)*3
# X = np.column_stack([experience, education])
# print(f"Feature matrix X shape: {X.shape}")
# print(f"Target vector y shape : {salary.shape}")
# # Gradient descent with multiple features
# W = np.zeros(2) # weights for each feature
# b = 0.0
# lr = 0.001
# n = len(salary)
# for iteration in range(2000):
#    y_pred = X @ W + b # matrix multiply: shape (100,)
#    error = y_pred - salary # shape (100,)
#    dW = (2/n) * X.T @ error # gradient for weights: shape (2,)
#    db = (2/n) * np.sum(error) # gradient for bias: scalar
#    W = W - lr * dW
#    b = b - lr * db
# print(f"\nLearned weights:")
# print(f" w_experience : {W[0]:.3f} (true: 5.0)")
# print(f" w_education : {W[1]:.3f} (true: 2.0)")
# print(f" bias : {b:.3f} (true: 10.0)")

# import numpy as np

# def mini_batch_gd(X, y, learning_rate=0.01, n_epochs=50, batch_size=32):
#    n, n_features = X.shape
#    W = np.zeros(n_features)
#    b = 0.0
#    for epoch in range(n_epochs):
#    # Shuffle data at start of each epoch
#       indices = np.random.permutation(n)
#       X_shuffled = X[indices]
#       y_shuffled = y[indices]
      
#       for start in range(0, n, batch_size):
#          end = min(start + batch_size, n)
#          X_batch = X_shuffled[start:end]
#          y_batch = y_shuffled[start:end]
#          y_pred = X_batch @ W + b
#          error = y_pred - y_batch
#          batch_n = len(y_batch)
#          dW = (2/batch_n) * X_batch.T @ error
#          db = (2/batch_n) * np.sum(error)
#          W = W - learning_rate * dW
#          b = b - learning_rate * db

#    if epoch % 10 == 0:
#       cost = np.mean((X @ W + b - y)**2)
#       print(f"Epoch {epoch:3d}: MSE = {cost:.4f}")
      
#    return W, b

# np.random.seed(42)
# experience = np.random.uniform(1, 15, 200)
# education = np.random.uniform(10, 22, 200)
# salary = 5*experience + 2*education + 10 + np.random.randn(200)*3
# X = np.column_stack([experience, education])
# W_final, b_final = mini_batch_gd(X, salary, learning_rate=0.001,n_epochs=50, batch_size=32)
# print(f"\nFinal: w={W_final}, b={b_final:.2f}")

import numpy as np
# 5 data points: study hours vs exam score
hours = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
score = np.array([45.0, 55.0, 65.0, 70.0, 80.0])
def compute_mse(hours, score, slope, intercept):
   predictions = slope * hours + intercept
   return np.mean((predictions - score) ** 2)
   # Try different combinations manually
print("Manual line fitting:")
print(f"{'Slope':>8} | {'Intercept':>10} | {'MSE':>10} | Assessment")
print("-" * 60)
combinations = [
   (5, 40), # First guess
   (8, 35), # Steeper slope
   (10, 30), # Even steeper
   (8, 40), # Higher intercept
   (9, 38), # Fine-tuning
   (8.8,37), # Getting closer
   (8.75,37.5),# Very close
   ]
best_mse = float("inf")
best_combo = None
for slope, intercept in combinations:
   mse = compute_mse(hours, score, slope, intercept)
   assessment = "<-- Best so far!" if mse < best_mse else ""
   if mse < best_mse:
      best_mse = mse
      best_combo = (slope, intercept)
   print(f"{slope:>8.2f} | {intercept:>10.2f} | {mse:>10.4f} |{assessment}")
   print(f"\nBest combination found: slope={best_combo[0]},intercept={best_combo[1]}")
   print(f"Best MSE: {best_mse:.4f}")
      # Now let gradient descent find the TRUE optimal
   w, b = 0.0, 0.0
   for _ in range(10000):
      pred = w * hours + b
      err = pred - score
      w -= 0.01 * (2/5) * np.dot(hours, err)
      b -= 0.01 * (2/5) * np.sum(err)
   print(f"\nGradient descent optimal: slope={w:.4f}, intercept={b:.4f}")
   print(f"Gradient descent MSE : {compute_mse(hours, score, w, b):.6f}")