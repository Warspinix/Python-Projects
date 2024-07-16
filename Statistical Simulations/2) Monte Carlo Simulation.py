# SIMULATING AN EXPERIMENT

import numpy as np


def uniform(n, m):
    return np.random.randint(1, n+1, size=m)


print(uniform(2, 10))  # Tossing a coin 10 times; there are 2 possible outcomes in each toss
print(uniform(6, 10))  # Throwing a die 10 times; there are 6 possible outcomes in each throw

# -------------------------------------------------------------------------------------------------------

# Monte Carlo Simulation for tossing a coin
# 1 is Heads and 2 is Tails

heads = 0  # No. of heads appearing after 'm' coin tosses

for i in range(10000):
    if (uniform(2, 1)) == 1:
        heads += 1
print(heads/10000)  # Probability Estimate by Monte Carlo, close to 1/2

# -------------------------------------------------------------------------------------------------------

# Monte Carlo Simulation for throwing a die

no_3 = 0  # Number of 3s appearing after 'm' die throws

for i in range(10000):
    if(uniform(6, 1)) == 3:
        no_3 += 1
print(no_3/10000)  # Probability Estimate by Monte Carlo. close to 1/6
