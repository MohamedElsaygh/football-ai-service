import joblib
import numpy as np
from sklearn.linear_model import LogisticRegression

X = np.random.rand(1000, 3)
y = (X[:, 0] + X[:, 1]*0.5 + X[:, 2]*0.2 > 1).astype(int)

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, "model.joblib")
print("model saved")
