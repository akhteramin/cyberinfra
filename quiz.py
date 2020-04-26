from scipy.stats import beta
from scipy.stats import bernoulli
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
# settings for seaborn plotting style
sns.set(color_codes=True)
# settings for seaborn plot sizes
sns.set(rc={'figure.figsize':(5,5)})

def plot_prior(alpha, bta, ax=None):
    x = np.linspace(0, 1, 1000)
    y = beta.pdf(x, 2, 2)

    if not ax:
        fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel(r"$\theta$", fontsize=20)
    ax.set_ylabel(r"$P(\theta)$", fontsize=20)
    ax.set_title("Prior: BetaPDF({},{})".format(alpha, bta))

plot_prior(alpha=2, bta=2)
plt.show()
plot_prior(alpha=3, bta=3)
plt.show()
plot_prior(alpha=10, bta=10)
plt.show()


def plot_posterior(heads, tails, alpha, bta, ax=None):
    x = np.linspace(0, 1, 1000)
    y = beta.pdf(x, heads + alpha, tails + bta)

    if not ax:
        fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel(r"$\theta$", fontsize=20)
    ax.set_ylabel(r"$P(\theta|D)$", fontsize=20)
    ax.set_title("Posterior after {} heads, {} tails, \
                 Prior: BetaPDF({},{})".format(heads, tails, alpha, bta));
plot_posterior(heads=4, tails=1, alpha=2, bta=2)
plt.show()
plot_posterior(heads=4, tails=4, alpha=3, bta=3)
plt.show()
plot_posterior(heads=5, tails=5, alpha=20, bta=20)
plt.show()

def likelihood(trials, p):
    heads = []
    for i in range(trials):
        tosses = np.random.binomial(1,p)
        heads.append(tosses)
    return heads
# Run the function
heads = likelihood(100,  0.7)
# Plot the results as a histogram
fig, ax = plt.subplots(figsize=(14,7))
ax = sns.distplot(heads, bins=11, label='Likelihood simulation results')
ax.set_xlabel("0-Tails & 1-Heads (P(H)=0.7)",fontsize=16)
ax.set_ylabel("Frequency",fontsize=16)
plt.show()

# Run the function
heads = likelihood(100,  0.5)
# Plot the results as a histogram
fig, ax = plt.subplots(figsize=(14,7))
ax = sns.distplot(heads, bins=11, label='Likelihood simulation results')
ax.set_xlabel("0-Tails & 1-Heads (P(H)=0.5)",fontsize=16)
ax.set_ylabel("Frequency",fontsize=16)
plt.show()

# Run the function
heads = likelihood(100,  0.3)
# Plot the results as a histogram
fig, ax = plt.subplots(figsize=(14,7))
ax = sns.distplot(heads, bins=11, label='Likelihood simulation results')
ax.set_xlabel("0-Tails & 1-Heads (P(H)=0.3)",fontsize=16)
ax.set_ylabel("Frequency",fontsize=16)
plt.show()

# posterior predictive P(H|HHTHH)
def predictive_posterior(alpha,bta,nh,nt):
    predictive_posterior = (nh+alpha)/(nh+alpha+bta+nt)
    print(predictive_posterior)
predictive_posterior(2,2,4,1)
