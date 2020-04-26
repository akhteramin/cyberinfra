import numpy as np
from sklearn.linear_model import LinearRegression

# Helper function to calculate dot product
def dot(x, y):
    return sum(x_i * y_i for x_i, y_i in zip(x, y))


x = np.array([94, 96, 94, 95, 104, 106, 108, 113, 115, 121, 131], dtype=np.float64)
y = np.array([0.47, 0.75, 0.83, 0.98, 1.18, 1.29, 1.40, 1.60, 1.75, 1.90, 2.23])
N = len(x)

regressor = LinearRegression()
x = x.reshape(-1, 1)
y = y.reshape(-1, 1)
regressor.fit(x, y)

print(regressor.intercept_)
print(regressor.coef_)

y_bar = regressor.predict(x)
ins = (y - y_bar)
sigma = dot(ins, ins)
sigma = sigma / (N - 1)
print(sigma)

var_w = sigma / (sigma + dot(x, x) - N * np.mean(x) ** 2)
mean_w = (dot(x, y) - N * np.mean(x) * np.mean(y)) / (sigma + dot(x, x) - N * np.mean(x) ** 2)
print(var_w)
print(mean_w)