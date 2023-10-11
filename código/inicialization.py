import random
import numpy as np

def window(population):
    
    step = 1 / (population - 1)
    lambda_window = []
    lambda_valor = 0

    for i in range(population):
        lambda_window.append((round(lambda_valor, 12), round(1 - lambda_valor, 12)))
        lambda_valor += step

    return lambda_window


def calcular_vecinos(vectores_lambda, vecindad):
    vecindades = {}
    num_vectores = len(vectores_lambda)
    num_vecinos = round(num_vectores * vecindad)

    for i, vector_lambda in enumerate(vectores_lambda):
        distancia_a_vectores = []  # Almacenar distancias a otros vectores lambda

        # Calcular la distancia euclidiana entre el vector lambda i y todos los demás vectores lambda
        for j, otro_vector_lambda in enumerate(vectores_lambda):
            if i == j:
                continue  # Saltar la comparación consigo mismo

            distancia = np.linalg.norm(np.array(vector_lambda) - np.array(otro_vector_lambda))
            distancia_a_vectores.append((otro_vector_lambda, distancia))

        # Ordenar la lista de distancias y seleccionar los T - 1 más cercanos
        distancia_a_vectores.sort(key=lambda x: x[1])
        vecindad_i = [vec for vec, _ in distancia_a_vectores[:num_vecinos - 1]]
        vecindad_i.append(vector_lambda)

        vecindades[vector_lambda] = vecindad_i

    return vecindades
 

def initialization(population, upper_limit, lower_limit, dimensions):
    population_list = []

    for i in range(population):
        chromosome = []
        for i in range(dimensions):
            alelo = random.uniform(lower_limit, upper_limit)
            chromosome.append(alelo)
        population_list.append(chromosome)

    print(f"GENERATED {population} INDIVIDUALS WITH {dimensions} CHROMOSOMES")
    
    return population_list