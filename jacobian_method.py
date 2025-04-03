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


def load_file(number_of_equations):
    # Create separate matrices for coefficients and constants
    coefficient_matrix = np.zeros((number_of_equations, number_of_equations))
    matrix_b = np.zeros(number_of_equations)

    try:
        with open(f'coefficients/{number_of_equations}.txt', 'r') as f:
            lines = f.readlines()

        for i in range(number_of_equations):
            values = lines[i].strip().split()
            for j in range(number_of_equations):
                coefficient_matrix[i][j] = float(values[j])
            # The last value in each row is the b value
            matrix_b[i] = float(values[number_of_equations])

        return coefficient_matrix, matrix_b

    except FileNotFoundError:
        print(f"Nie znaleziono pliku dla {number_of_equations} równań.")
        return None, None



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
    print("Macierz współczynników: \n", matrix_m)
    print("Macierz wyrazów wolnych: \n", matrix_b)
    print("Macierz N: \n", matrix_n)
    print('Macierz zmiennych: \n', matrix_x)

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



def main():

    number_of_equations, stop_condition_value, stop_condition_type = menu()
    matrix_coefficients, matrix_b = load_file(number_of_equations)

    if is_matrix_convergent(matrix_coefficients):

        matrix_m, matrix_n = matrix_m_n_calculation(matrix_coefficients)
        matrix_x = generate_x_matrix(len(matrix_coefficients))

        jacobian_method(matrix_x, matrix_b, matrix_m, matrix_n, stop_condition_value, stop_condition_type)

    else:
        print("Macierz nie jest zbieżna. Zmień macierz współczynników.")
        return


# Uruchomienie programu
if __name__ == "__main__":
    main()


