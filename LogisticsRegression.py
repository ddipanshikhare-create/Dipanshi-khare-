from sklearn.linear_model import LogisticRegression
import numpy as np

# Sample data
X = [[1],[2],[3],[4],[5]]
y = [0,0,0,1,1]

# Create model
model = LogisticRegression()

# Train model
model.fit(X,y)

# Prediction
print(model.predict([[2]]))
print(model.predict([[5]]))
