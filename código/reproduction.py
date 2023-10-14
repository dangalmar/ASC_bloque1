import random
from zdt3 import zdt3
from cf6 import cf6, cf6_constraint_1, cf6_constraint_2
import numpy as np

def reproduction_zdt3(individuo, vecinos, upper_limit, lower_limit, dimensions, population_list, CR, F): 
    chromosome_mutated = []
    parents = [vecinos[random.randint(0, len(vecinos) - 1)][2] for _ in range(3)]

    for dimension in range(dimensions):
        if random.uniform(0, 1) <= CR:
            mutated = population_list[parents[0]][dimension] + F * (population_list[parents[1]][dimension] - population_list[parents[2]][dimension])
            mutated = np.clip(mutated, lower_limit, upper_limit)
        else:
            mutated = individuo[dimension]
        chromosome_mutated.append(mutated)

    return chromosome_mutated

def reproduction_cf6(individuo, vecinos, upper_limit_1, lower_limit_1, upper_limit_n, lower_limit_n, dimensions, population_list, CR, F): 
    chromosome_mutated = []
    parents = [vecinos[random.randint(0, len(vecinos) - 1)][2] for _ in range(3)]

    for dimension in range(dimensions):
        if random.uniform(0, 1) <= CR:
            mutated = population_list[parents[0]][dimension] + F * (population_list[parents[1]][dimension] - population_list[parents[2]][dimension])
            if dimension == 0:
                mutated = np.clip(mutated, lower_limit_1, upper_limit_1)
            else:
                mutated = np.clip(mutated, lower_limit_n, upper_limit_n)
        else:
            mutated = individuo[dimension]
        chromosome_mutated.append(mutated)

    return chromosome_mutated


def actualization_z(z, f):
    if z[0] is None or f[0] < z[0]:
        z[0] = f[0]
    if z[1] is None or f[1] < z[1]:
        z[1] = f[1]
    return z

def actualization_population_zdt3(vecindad_individuo, nuevo_individuo, population_list, dimensions, z, f):
    for vecino in vecindad_individuo:
        f1t, f2t = zdt3(population_list[vecino[2]], dimensions)
        gte_y_1 = vecino[0] * abs(f[0] - z[0])
        gte_y_2 = vecino[1] * abs(f[1] - z[1])
        gte_x_1 = vecino[0] * abs(f1t - z[0])
        gte_x_2 = vecino[1] * abs(f2t - z[1])
        if gte_y_1 < gte_y_2:
            gte_y_1 = gte_y_2
        if gte_x_1 < gte_x_2:
            gte_x_1 = gte_x_2
        if gte_y_1 <= gte_x_1:
            population_list[vecino[2]] = nuevo_individuo
    
    return population_list

def actualization_population_cf6(vecindad_individuo, nuevo_individuo, population_list, dimensions, z, f):
    for vecino in vecindad_individuo:
        f1t, f2t = cf6(population_list[vecino[2]], dimensions)
        constraint_1, constraint_2 = cf6_constraint_1(population_list[vecino[2]], dimensions), cf6_constraint_2(population_list[vecino[2]], dimensions)
        valor_restriccion =  abs(constraint_1) + abs(constraint_2)
        f1t, f2t = f1t + 0.5 * valor_restriccion, f2t + 0.5 * valor_restriccion
        gte_y_1 = vecino[0] * abs(f[0] - z[0])
        gte_y_2 = vecino[1] * abs(f[1] - z[1])
        gte_x_1 = vecino[0] * abs(f1t - z[0])
        gte_x_2 = vecino[1] * abs(f2t - z[1])
        if gte_y_1 < gte_y_2:
            gte_y_1 = gte_y_2
        if gte_x_1 < gte_x_2:
            gte_x_1 = gte_x_2
        if gte_y_1 <= gte_x_1:
            population_list[vecino[2]] = nuevo_individuo
    
    return population_list

def actualization_population_cf6_selection(vecindad_individuo, nuevo_individuo, population_list, dimensions, z, f):
    for vecino in vecindad_individuo:
        f1t, f2t = cf6(population_list[vecino[2]], dimensions)
        constraint_j_f1 = cf6_constraint_1(population_list[vecino[2]], dimensions)
        constraint_j_f2 = cf6_constraint_2(population_list[vecino[2]], dimensions)
        constraint_individuo_f1 = cf6_constraint_1(nuevo_individuo, dimensions)
        constraint_individuo_f2 = cf6_constraint_2(nuevo_individuo, dimensions)
        constraint_j = abs(constraint_j_f1) + abs(constraint_j_f2)
        constraint_individuo = abs(constraint_individuo_f1) + abs(constraint_individuo_f2)
        if constraint_j == 0 and constraint_individuo == 0:
            gte_y_1 = vecino[0] * abs(f[0] - z[0])
            gte_y_2 = vecino[1] * abs(f[1] - z[1])
            gte_x_1 = vecino[0] * abs(f1t - z[0])
            gte_x_2 = vecino[1] * abs(f2t - z[1])
            if gte_y_1 < gte_y_2:
                gte_y_1 = gte_y_2
            if gte_x_1 < gte_x_2:
                gte_x_1 = gte_x_2
            if gte_y_1 <= gte_x_1:
                population_list[vecino[2]] = nuevo_individuo
        elif constraint_individuo == 0 or constraint_individuo < constraint_j:
            population_list[vecino[2]] = nuevo_individuo

    return population_list