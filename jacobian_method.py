from shutil import which

import numpy as np

def menu():
    while True:

        print("Podaj ile równań chcesz rozwiązać (max 10): ")
        number_of_equations = int(input())
        stop_condition_value = 0
        stop_condition_type = ''

        if number_of_equations > 10 or number_of_equations < 1:
            print("Liczba podanych równań jest niepoprawna. Podaj liczbę z przedziału 1-10")
        else:
            print("Maksymalna liczba iteracji/Błąd [M/B]:")
            user = str(input())
            if user not in ['M', 'B']:
                print("Niepoprawny wybór. Wybierz M lub B")
            else:
                if user == 'M':
                    print("Podaj maksymalną liczbę iteracji: ")
                    stop_condition_value = int(input())
                    stop_condition_type = 'M'
                if user == 'B':
                    print("Podaj błąd: ")
                    stop_condition_value = float(input())
                    stop_condition_type = 'B'

                return number_of_equations, stop_condition_value, stop_condition_type


def is_matrix_convergent(matrix):
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


def generate_x_matrix(number_of_equations):
    matrix_x = []
    for i in range(number_of_equations):
        matrix_x.append(0)
    return matrix_x


def split_coefficient_matrix(coefficient_matrix):
    matrix_L = []
    matrix_D = []
    matrix_U = []

    matrix_L.append([0 for i in range(len(coefficient_matrix))])
    matrix_D.append([0 for i in range(len(coefficient_matrix))])
    matrix_U.append([0 for i in range(len(coefficient_matrix))])

    # Podział macierzy
    for i in range(len(coefficient_matrix)):
        for j in range(len(coefficient_matrix)):
            if i > j:
                matrix_L[i][j] = coefficient_matrix[i][j]
            elif i == j:
                matrix_D[i][j] = coefficient_matrix[i][j]
            else:
                matrix_U[i][j] = coefficient_matrix[i][j]

    return matrix_L, matrix_D, matrix_U


def inverse_matrix(matrix_D):
    matrix_N = np.linalg.inv(matrix_D)
    return matrix_N


def load_file(number_of_equations):
    matrix_coefficients = np.zeros((number_of_equations, number_of_equations + 1))
    matrix_b = []
    try:
        with open(f'coefficients/{number_of_equations}.txt', 'r') as f:
            lines = f.readlines()

        for i in range(len(lines) - 1):
            for j in range(number_of_equations+1):
                matrix_coefficients[i][j] = float(lines[i].split(' ')[j])

        for x in lines[-1].split(' '):
            matrix_b.append(float(x))

        return matrix_coefficients, matrix_b

    except FileNotFoundError:
        print(f"Nie znaleziono pliku dla {number_of_equations} równań.")



# Wzór iteracyjny
# x^(n+1) = Mx + Nb
# D^(-1) = N
# M = -D^(-1)(L + U) = -N(L + U)

def matrix_m_calculation(coefficient_matrix):
    matrix_L, matrix_D, matrix_U = split_coefficient_matrix(coefficient_matrix)
    matrix_N = inverse_matrix(matrix_D)

    matrix_L_plus_U = []
    for i in range(len(matrix_L)):
        matrix_L_plus_U.append([])
        for j in range(len(matrix_L)):
            matrix_L_plus_U[i].append(matrix_L[i][j] + matrix_U[i][j])

    matrix_minus_N = []
    for i in range(len(matrix_N)):
        matrix_minus_N.append([])
        for j in range(len(matrix_N)):
            matrix_minus_N[i].append(-matrix_N[i][j])

    matrix_M = np.matmul(matrix_minus_N, matrix_L_plus_U)

    return matrix_M

def jacobian_method(coefficient_matrix, matrix_b, stop_condition_value, stop_condition_type):

    matrix_x = generate_x_matrix(len(coefficient_matrix))
    matrix_m = matrix_m_calculation(coefficient_matrix)
    i = 0

    # TODO: Implementacja petli
    # while True:
    #
    #
    #     if stop_condition_type == 'M':
    #         if i >= stop_condition_value - 1:
    #         i += 1
    #     else:
    #         if ... < stop_condition_value:


def main():
    number_of_equations, stop_condition_value, stop_condition_type = menu()
    matrix_coefficients, matrix_b = load_file(number_of_equations)
    if is_matrix_convergent(matrix_coefficients):
        jacobian_method(matrix_coefficients, matrix_b, stop_condition_value, stop_condition_type)
    else:
        print("Macierz nie jest zbieżna. Zmień macierz współczynników.")
        return





