import random
import numpy as np

def window(population):
    
    step = 1 / (population - 1)
    lambda_window = []
    lambda_valor = 0

    for i in range(population):
        lambda_window.append((round(lambda_valor, 12), round(1 - lambda_valor, 12), i))
        lambda_valor += step

    return lambda_window


def calcular_vecinos(vectores_lambda, vecindad):
    vecindades = {}
    num_vectores = len(vectores_lambda)
    num_vecinos = round(num_vectores * vecindad)

    for i, vector_lambda in enumerate(vectores_lambda):
        distancia_a_vectores = []  

        for j, otro_vector_lambda in enumerate(vectores_lambda):
            if i == j:
                continue 
            distancia = np.linalg.norm(np.array(vector_lambda) - np.array(otro_vector_lambda))
            distancia_a_vectores.append((otro_vector_lambda, distancia))

        distancia_a_vectores.sort(key=lambda x: x[1])
        vecindad_i = [vec for vec, _ in distancia_a_vectores[:num_vecinos - 1]]
        vecindad_i.append(vector_lambda)

        vecindades[vector_lambda] = vecindad_i

    return vecindades
 

def initialization_zdt3(population, upper_limit, lower_limit, dimensions):
    population_list = []

    for individual in range(population):
        chromosome = []
        for dimension in range(dimensions):
            allele = random.uniform(lower_limit, upper_limit)
            chromosome.append(allele)
        population_list.append(chromosome)

    print(f"GENERATED {population} INDIVIDUALS WITH {dimensions} CHROMOSOMES")
    
    return population_list

def initialization_cf6(population, upper_limit_1, lower_limit_1, upper_limit_n, lower_limit_n, dimensions):
    population_list = []

    for individual in range(population):
        chromosome = []
        for dimension in range(dimensions):
            if dimension == 0:
                allele =  random.uniform(lower_limit_1, upper_limit_1)
                chromosome.append(allele)
            else:
                allele = random.uniform(lower_limit_n, upper_limit_n)
                chromosome.append(allele)
        population_list.append(chromosome)

    print(f"GENERATED {population} INDIVIDUALS WITH {dimensions} CHROMOSOMES")

    return population_list