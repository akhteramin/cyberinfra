import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from math import sqrt
#Likelihood
# mu = np.linspace(-7, 7, 2000)
xmean = [3.2877564,3.3049376, 3.0065537,2.4179332,
2.4255153,
3.3632328,
3.3750101,
3.6351869,
2.5573695,
2.4708438,
2.7914828,
2.8363451,
3.5001336,
2.7917707,
2.3019892,
2.8733925,
2.4083626,
2.9122397,
3.1874000,
3.3319748]

def Likelihood(data,x):
    likelihood = 1
    for i in data:
        y=norm.pdf(i,x,sqrt(10))
        likelihood = likelihood*y

    plt.figure()
    plt.plot(x, likelihood)
    plt.title("Liklihood: NormalPDF({},{})".format(-7, 7))
    plt.xlabel('$x$')
    plt.ylabel('$likelihood$')
    plt.show()

#prior
def Prior(x):

    yp = np.exp((-1*(x)**2)/12)

    plt.figure()
    plt.plot(x, yp)
    plt.title("Prior: NormalPDF({},{})".format(-7, 7))

    plt.xlabel('$mu$')
    plt.ylabel('$prior$')
    plt.show()


def Posterior(data,x):
    sigma = 1/(2+(1/6))
    print(sigma)
    mu=(20*np.mean(data)/10)*sigma
    print(mu)
    # data.sort()


    plt.figure()
    plt.title("Posterior: NormalPDF({},{})".format(-7, 7))
    plt.plot(x, norm.pdf(x,mu,sqrt(sigma)))
    plt.xlabel('$mu$')
    plt.ylabel('$posterior$')

    plt.show()
def Posterior_Predictive(data):
    sigma = 10+(1 / (2 + (1 / 6)))
    mu = (20 * np.mean(data) / 10) * sigma

    print("Posterior Predictive:: "+str(norm.pdf(2.4, mu, sqrt(sigma))))

Likelihood(xmean,np.linspace(-7, 7, 2000))
Likelihood(xmean,np.linspace(-7, 15, 2000))
Likelihood(xmean,np.linspace(-1, 7, 2000))
Prior(np.linspace(-7, 7, 2000))
Prior(np.linspace(-7, 15, 2000))
Prior(np.linspace(-10, 10, 2000))
Posterior(xmean,np.linspace(-5, 15, 2000))
Posterior(xmean,np.linspace(-7, 7, 2000))
Posterior(xmean,np.linspace(-7, 7, 2000))

Posterior_Predictive(xmean)