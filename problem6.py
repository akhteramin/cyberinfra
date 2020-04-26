from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import norm

plt.rcParams['figure.figsize'] = 10, 8
x = np.asarray([67, 79, 71, 68, 67, 60], dtype=np.float32)
y = np.asarray([1, 1, 1, 0, 0, 0], dtype=np.bool)

# this is just prior probability for given y= 'male' or 'female'
prior_m = (y==1).sum()/len(y)
prior_f = (y==0).sum()/len(y)

# we calculated mean of height for given y= 'male' or 'female'
mu_m = x[y==1].sum()/(y==1).sum()
mu_f = x[y==0].sum()/(y==0).sum()

# we calculated variance of height for given y= 'male' or 'female'..

Sigma_m = ((x[y==1] - mu_m) ** 2).sum() / (y==1).sum()
Sigma_f = ((x[y==0] - mu_f) ** 2).sum() / (y==0).sum()

sigma_m = Sigma_m ** 0.5
sigma_f = Sigma_f ** 0.5

print('prior_m = {0:.2f}'.format(prior_m))
print('mu_m = {0:.2f}'.format(mu_m))
print('Sigma_m = {0:.2f}\n'.format(sigma_m))

print('prior_f = {0:.2f}'.format(prior_f))
print('mu_f = {0:.2f}'.format(mu_f))
print('Sigma_f = {0:.2f}\n'.format(sigma_f))


sample = 72
pr_x_ym = norm(loc=mu_m, scale=sigma_m).pdf(sample)
pr_x_yf = norm(loc=mu_f, scale=sigma_f).pdf(sample)

pr_x = pr_x_ym * prior_m + pr_x_yf * prior_f

pr_y_mx = (pr_x_ym * prior_m) / pr_x

print('p(y = m | x = 72, \\theta_MLE) = {0:.2f}'.format(pr_y_mx))