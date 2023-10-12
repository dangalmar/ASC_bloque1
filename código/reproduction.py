import random
from zdt3 import zdt3
import numpy as np

def reproduction(individuo, vecinos, upper_limit, lower_limit, dimensions, population_list):
    CR, F = 0.5, 0.5 
    chromosome_mutated = []
    parents = [vecinos[random.randint(0, len(vecinos) - 1)][2] for _ in range(3)]

    for i in range(dimensions):
        if random.uniform(0, 1) <= CR:
            mutated = population_list[parents[0]][i] + F * (population_list[parents[1]][i] - population_list[parents[2]][i])
            mutated = np.clip(mutated, lower_limit, upper_limit)
        else:
            mutated = individuo[i]
        chromosome_mutated.append(mutated)

    return chromosome_mutated

def actualization_z(z, f):
    if z[0] is None or f[0] < z[0]:
        z[0] = f[0]
    if z[1] is None or f[1] < z[1]:
        z[1] = f[1]
    return z

def actualization_population(vecindad_individuo, nuevo_individuo, population_list, dimensions, z, f):
    for j in vecindad_individuo:
        f1t, f2t = zdt3(population_list[j[2]], dimensions)
        gte_y_1 = j[0] * abs(f[0] - z[0])
        gte_y_2 = j[1] * abs(f[1] - z[1])
        gte_x_1 = j[0] * abs(f1t - z[0])
        gte_x_2 = j[1] * abs(f2t - z[1])
        if gte_y_1 < gte_y_2:
            gte_y_1 = gte_y_2
        if gte_x_1 < gte_x_2:
            gte_x_1 = gte_x_2
        if gte_y_1 <= gte_x_1:
            population_list[j[2]] = nuevo_individuo
    
    return population_list