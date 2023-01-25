import numpy as np
import random
from scipy.stats import multivariate_normal as MVN
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt

def stats(gen, popfit):
    print("Stats", gen, np.min(popfit))

def real_init(n):
    # get a vector of random normal values (mean 0, sd 1)
    return np.random.normal(size=n)

def estimate_diagonal(pop):
    # estimate the distribution of the samples in `pop`: the model
    # consists of a mean and variance for each DV (ie a diagonal
    # covariance matrix)
    mu = np.mean(pop, axis=0)
    sigma = np.var(pop, axis=0) # sigma = variance = sd^2
    return mu, sigma

def estimate_full(pop):
    # estimate the distribution of the samples in `pop`: the model
    # consists of the mean (a vector) and full covariance matrix.
    mu = np.mean(pop, axis=0)
    sigma = np.cov(pop, rowvar=False)
    return mu, sigma

def sample(model, popsize):
    # given a model, sample from it. this works whether sigma is just
    # a 1D array (diagonal) or a square 2D array (full)
    mu, sigma = model
    return MVN.rvs(mu, sigma, popsize)

def truncation_selection(pop, popfit, proportion):
    # given a population and their fitness values, return a list of
    # just the good ones (how many - given by proportion).
    # here we assume minimisation.
    cutoff = np.percentile(popfit, proportion * 100.0)
    # note we use <= not < because if population converged
    # we could have no individuals < cutoff
    return [x for x, fx in zip(pop, popfit) if fx <= cutoff]

def sphere(x): # test problem, easy
    return np.sum(x**2)

def rastrigin(x): # test problem, hard
    # https://en.wikipedia.org/wiki/Rastrigin_function
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.dual_annealing.html
    func = lambda x: np.sum(x*x - 10*np.cos(2*np.pi*x)) + 10*np.size(x)
    return func(x)

def rosenbrock(x): # test problem, hard
    # from https://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.optimize.rosen.html
    return np.sum(100.0*(x[1:] - x[:-1]**2.0)**2.0 + (1 - x[:-1])**2.0)



def EDA(f, init, estimate, sample, select, popsize, ngens):
    """Notice (in contrast to GA) select() now returns the
    complete set of parents, not one at a time."""
    pop = [init() for i in range(popsize)]
    popfit = [f(x) for x in pop]
    stats(0, popfit)
    history = np.zeros((ngens, popsize, n))
    history[0] = np.array(pop)
    for gen in range(1, ngens):
        
        # discard the bad ones
        pop = select(pop, popfit)

        # estimate a model...
        model = estimate(pop)
        # print(model)
        # ... and sample from it
        pop = sample(model, popsize)
        history[gen] = np.array(pop)
        popfit = [f(x) for x in pop]
        stats(gen, popfit)
    return history

    
def plot(h):
    fig2 = plt.figure(figsize=(4,4))
    ax2 = fig2.add_subplot(111)
    for i, hi in enumerate(h):
        ax2.scatter(hi[:, 0], hi[:, 1],
                    s=1.0,
                    c=[i] * h.shape[1],
                    vmin=0, vmax=h.shape[0])
    plt.axis("equal")
    plt.savefig(f"eda.pdf")
    plt.close()

n = 6
f = rosenbrock
popsize = 10
ngens = 6
truncation_proportion = 0.5

# the exercise is to write EDA so we can call it like this. 
# we use lambda to convert from a function that requires extra
# parameters to one that does not, eg convert real_init(n) to a
# function that can be called with no arguments; eg convert truncation
# selection to a function that requires only pop, popfit, does not
# require truncation proportion.
h = EDA(f,
    lambda: real_init(n), 
    estimate_full,
    sample,
    lambda pop, popfit: truncation_selection(pop, popfit, truncation_proportion),
    popsize,
    ngens
)

plot(h)
