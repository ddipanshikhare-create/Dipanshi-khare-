from sklearn.model_selection import KFold
import numpy as np

# Sample data
X = np.array([1,2,3,4,5,6])

# Create KFold object
kf = KFold(n_splits=3)

# Apply KFold
for train_index, test_index in kf.split(X):
    print("Train:", X[train_index], "Test:", X[test_index])
