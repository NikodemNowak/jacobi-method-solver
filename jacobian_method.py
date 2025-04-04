import numpy as np

# Sprawdzenie nieredukowaln

def is_matrix_convergent(matrix):
    for i in range(len(matrix)):
        if matrix[i][i] == 0: return False

    # Warunek dominacji diagonalnej
    for i in range(len(matrix)):
        diagonal_element = abs(matrix[i][i])
        sum_of_row = 0
        for j in range(len(matrix)):
            if i != j:
                sum_of_row += abs(matrix[i][j])
        if diagonal_element <= sum_of_row:
            return False
    return True

def check_matrix(matrix):
    max_value = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if abs(matrix[i][j]) > max_value: max_value = abs(matrix[i][j])

    if max_value >= 1:
        return False
    else:
        return True



def generate_x_matrix(number_of_equations):
    matrix_x = []
    for i in range(number_of_equations):
        matrix_x.append(0)
    return matrix_x

def split_coefficient_matrix(coefficient_matrix):
    n = len(coefficient_matrix)
    matrix_l = [[0 for j in range(n)] for i in range(n)]
    matrix_d = [[0 for j in range(n)] for i in range(n)]
    matrix_u = [[0 for j in range(n)] for i in range(n)]

    # Podział macierzy
    for i in range(n):
        for j in range(n):
            if i > j:
                matrix_l[i][j] = coefficient_matrix[i][j]
            elif i == j:
                matrix_d[i][j] = coefficient_matrix[i][j]
            else:
                matrix_u[i][j] = coefficient_matrix[i][j]

    return matrix_l, matrix_d, matrix_u

def inverse_matrix(matrix_d):
    matrix_n = np.linalg.inv(matrix_d)
    return matrix_n

# Wzór iteracyjny
# x^(n+1) = Mx + Nb
# D^(-1) = N
# M = -D^(-1)(L + U) = -N(L + U)

def matrix_m_n_calculation(coefficient_matrix):
    # Get L, D, U matrices
    matrix_l, matrix_d, matrix_u = split_coefficient_matrix(coefficient_matrix)

    # Convert to numpy arrays if they aren't already
    matrix_l = np.array(matrix_l)
    matrix_d = np.array(matrix_d)
    matrix_u = np.array(matrix_u)

    # Calculate N = D^(-1)
    matrix_n = np.linalg.inv(matrix_d)

    # Calculate M = -N * (L + U)
    matrix_l_plus_u = matrix_l + matrix_u
    matrix_m = -np.matmul(matrix_n, matrix_l_plus_u)

    return matrix_m, matrix_n

def jacobian_method(matrix_x, matrix_b, matrix_m, matrix_n, stop_condition_value, stop_condition_type):

    nb = np.matmul(matrix_n, matrix_b)
    iterations = 0

    #Wyświetlenie każdej macierzy
    print("\nMacierz współczynników: \n", matrix_m)
    print("\nMacierz wyrazów wolnych: \n", matrix_b)
    print("\nMacierz N: \n", matrix_n)
    print('\nMacierz zmiennych: \n', matrix_x)

    while True:
        previous_x = matrix_x.copy()
        matrix_x = np.matmul(matrix_m, previous_x) + nb
        iterations += 1

        # Calculate error as the norm of the difference between consecutive approximations
        error = np.linalg.norm(np.subtract(matrix_x, previous_x))

        print(f"Iteration {iterations}: {matrix_x}, error = {error}")

        # Check stopping conditions
        if stop_condition_type == 'M':
            if iterations >= stop_condition_value:
                break
        else:  # stop_condition_type == 'B'
            if error < stop_condition_value:
                break
    print("Rozwiązanie: ", matrix_x)







