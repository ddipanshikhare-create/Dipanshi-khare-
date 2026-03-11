import pandas as pd

data = {'Gender':['Male','Female','Male','Female']}

df = pd.DataFrame(data)

# Create dummy variable
dummies = pd.get_dummies(df)

print(dummies)
