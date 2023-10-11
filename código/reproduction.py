import random
import numpy as np

def reproduction(individuo, window, upper_limit, lower_limit, dimensions, population):
    CR, F = 0.5, 0.5  # F should be added as a parameter to try things
    chromosome_mutated = []
    parents = [window[random.randint(0, len(window) - 1)][2] for _ in range(3)]

    for i in range(dimensions):
        if random.uniform(0, 1) <= CR:
            mutated = population[parents[0]][i] + F * (population[parents[1]][i] - population[parents[2]][i])
            mutated = np.clip(mutated, lower_limit, upper_limit)
        else:
            mutated = individuo[i]
        chromosome_mutated.append(mutated)

    return chromosome_mutated

def actualization(z, f):
    if z[0] is None or f[0] < z[0]:
        z[0] = f[0]
    if z[1] is None or f[1] < z[1]:
        z[1] = f[1]
    return z