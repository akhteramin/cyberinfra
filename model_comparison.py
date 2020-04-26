#following this tutorial https://docs.pymc.io/notebooks/Bayes_factor.html
from scipy.stats import beta
from scipy.special import betaln
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
# settings for seaborn plotting style
sns.set(color_codes=True)
# settings for seaborn plot sizes
sns.set(rc={'figure.figsize':(5,5)})

def beta_binom(prior, y):
    alpha, beta = prior
    h = np.sum(y)
    n = len(y)
    p_y = np.exp(betaln(alpha + h, beta+n-h) - betaln(alpha, beta))
    return p_y

y = np.repeat([1, 0], [3, 1])  # 3 "heads" and 1 "tails"
priors = ((1, 1), (2, 2))

simple_model=((0.5**3)*(0.5**1))
print(simple_model)
print((beta_binom(priors[1], y)))

ML = (beta_binom(priors[1], y))/simple_model

print(ML)
print("Simple Model Is Slighly Better than Complex model")