"""
Solve ZDT1 (a common benchmark problem) using a simple Pareto Archive algorithm.
"""

import numpy as np

def is_pareto_efficient_simple(costs):
    """https://stackoverflow.com/questions/32791911/fast-calculation-of-pareto-front-in-python
    
    Find the pareto-efficient points.

    Fairly fast for many datapoints, less fast for many costs,
    somewhat readable.

    :param costs: An (n_points, n_costs) array
    :return: A (n_points, ) boolean array, indicating whether
    each point is Pareto efficient

    """
    is_efficient = np.ones(costs.shape[0], dtype = bool)
    for i, c in enumerate(costs):
        if is_efficient[i]:
            # Keep any point with a lower cost
            is_efficient[is_efficient] = np.any(costs[is_efficient] < c, axis=1)  
            is_efficient[i] = True  # And keep self
    return is_efficient


def pareto_archive(f, init, mut, n_iters):
    """Pareto Archive algorithm

    Recall the algorithm:

    1. Create an empty archive and add an individual created by init
    2. Select one or more parents at random from the archive
    3. Create one or more offspring from those parents
    4. Add them to the archive, but make sure the archive contains the Pareto front only:
       4a. If the new offspring *dominates* any individuals, remove them
       4b. But if the new offspring *is dominated by* any individual, don't add it
    5. Go back to 2.
    

    f returns the multi-objective evaluation for a point x

    init and mut are as usual. ZDT1 is a problem with D real-valued
    decision variables in [0, 1].

    This implementation is mutation-only for simplicity, but we could
    easily add crossover.

    We store the archive and the objective (fitness) values
    separately, as we need the obj values in the form of a 2D array
    for use by is_pareto_efficient_simple().

    """
    arc = np.array([init()])
    fit = np.array([f(x) for x in arc])
    print("iter arc_size")
    print(0, arc.shape[0])
    for i in range(1, n_iters):
        # choose a parent at random, do mutation, and evaluate
        idx = np.random.randint(0, arc.shape[0])
        x = arc[idx]
        y = mut(x)
        fy = f(y)

        # add it to our archive
        arc = np.append(arc, y.reshape((1, -1)), axis=0)
        fit = np.append(fit, fy.reshape((1, -1)), axis=0)
        
        # update the archive to eliminate any dominated individual
        pf = is_pareto_efficient_simple(fit) # array of bool
        arc = arc[pf]
        fit = fit[pf]
        print(i, arc.shape[0])

    return arc, fit

def ZDT1(x):
    # from https://datacrayon.com/posts/search-and-optimisation/practical-evolutionary-algorithms/synthetic-objective-functions-and-zdt1/
    f1 = x[0]  # objective 1
    g = 1 + 9 * np.sum(x[1:D] / (D-1))
    h = 1 - np.sqrt(f1 / g)
    f2 = g * h  # objective 2
    return np.array([f1, f2])

def init():
    return np.random.random(D)

def mut(x):
    delta = 0.3
    x = x.copy()
    idx = np.random.randint(0, D)
    x[idx] = np.clip(x[idx] + delta * np.random.random(), 0, 1)
    return x

D = 20
arc, fit = pareto_archive(ZDT1, init, mut, 8000)
