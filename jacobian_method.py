import numpy as np

def is_irreducible(coefficient_matrix):
    # Ta funkcja sprawdza czy macierz jest nieredukowalna
    # Macierz jest nieredukowalna, jeśli odpowiadający jej graf jest silnie spójny - istnieje ścieżka między dowolnymi 2 wierzchołkami.

    size = len(coefficient_matrix)

    # Dla każdego wierzchołka sprawdzamy czy można dotrzeć do wszystkich innych
    for start in range(size):
        # Lista wierzchołków, które można odwiedzić z wierzchołka startowego
        visited = [False] * size
        check_list = [start]  # Lista wierzchołków do sprawdzenia (jako kolejka)

        visited[start] = True

        # Przeszukiwanie grafu wszerz
        while len(check_list) > 0:
            a = check_list.pop(0)  # Pobierz pierwszy element z kolejki

            # Sprawdź wszystkie połączenia z aktualnego wierzchołka
            for neighbor in range(size):
                # Jeżeli istnieje krawędź i sąsiad nie był jeszcze odwiedzony
                if coefficient_matrix[a][neighbor] != 0 and not visited[neighbor]:
                    visited[neighbor] = True
                    check_list.append(neighbor)

        # Jeśli nie wszystkie wierzchołki zostały odwiedzone, macierz nie jest nieredukowalna
        if False in visited:
            return False

    # Jeśli dla każdego wierzchołka można dotrzeć do wszystkich innych,
    # to macierz jest nieredukowalna
    return True


def is_weakly_diagonally_dominant_with_strict_one(matrix):
    # Pobieramy rozmiar macierzy (liczbę wierszy)
    size = len(matrix)

    # Zmienna do śledzenia, czy znaleziono wiersz ze ścisłą dominacją
    found_strict_dominance = False

    # Sprawdzamy każdy wiersz macierzy
    for i in range(size):
        # Pobieramy wartość bezwzględną elementu na diagonali
        diagonal_element = np.abs(matrix[i, i])

        # Obliczamy sumę wartości bezwzględnych pozostałych elementów w wierszu
        sum_other_elements = 0
        for j in range(size):
            if i != j:  # Pomijamy element diagonalny
                sum_other_elements += np.abs(matrix[i, j])

        # Jeśli element diagonalny jest mniejszy od sumy pozostałych elementów,
        # to macierz nie jest diagonalnie dominująca
        if diagonal_element < sum_other_elements:
            return False

        # Sprawdzamy czy wiersz jest ściśle diagonalnie dominujący
        if diagonal_element > sum_other_elements:
            found_strict_dominance = True

    # Macierz jest słabo diagonalnie dominująca, jeśli wszystkie elementy diagonalne
    # są większe lub równe sumie pozostałych elementów w ich wierszach, oraz
    # istnieje co najmniej jeden wiersz, gdzie element diagonalny jest ściśle większy
    return found_strict_dominance


def is_zero_on_diagonal(matrix):
    # Sprawdzamy, czy na diagonali macierzy znajdują się same zera
    for i in range(len(matrix)):
        if matrix[i][i] == 0:
            return False  # Zwracamy True, jeśli znajdziemy zero na diagonali
    return True  # Zwracamy False, jeśli nie znaleziono zer na diagonali

# Warunek dominacji diagonalnej
def is_diagonal_dominance(matrix):

    # Sprawdzamy warunek ścisłej dominacji diagonalnej dla każdego wiersza
    for i in range(len(matrix)):
        diagonal_element = abs(matrix[i][i])  # Wartość bezwzględna elementu diagonalnego
        sum_of_row = 0
        # Sumujemy wartości bezwzględne pozostałych elementów w wierszu
        for j in range(len(matrix)):
            if i != j:  # Pomijamy element diagonalny
                sum_of_row += abs(matrix[i][j])
        # Jeśli element diagonalny nie jest większy od sumy pozostałych elementów
        # to macierz nie spełnia warunku ścisłej dominacji diagonalnej
        if diagonal_element <= sum_of_row:
            return False
    # Jeśli wszystkie warunki zostały spełnione, macierz jest ściśle diagonalnie dominująca
    return True

def generate_x_matrix(number_of_equations):
    # Inicjalizacja macierzy x jako wektor zerowy o rozmiarze number_of_equations
    matrix_x = []
    for i in range(number_of_equations):
        matrix_x.append(0)  # Dodanie zera dla każdego równania
    return matrix_x

def split_coefficient_matrix(coefficient_matrix):
    n = len(coefficient_matrix)
    matrix_l = [[0 for _ in range(n)] for _ in range(n)]  # Inicjalizacja macierzy L zerami
    matrix_d = [[0 for _ in range(n)] for _ in range(n)]  # Inicjalizacja macierzy D zerami
    matrix_u = [[0 for _ in range(n)] for _ in range(n)]  # Inicjalizacja macierzy U zerami

    # Podział macierzy
    for i in range(n):
        for j in range(n):
            if i > j:
                matrix_l[i][j] = coefficient_matrix[i][j]  # Wypełnianie macierzy L (poniżej diagonali)
            elif i == j:
                matrix_d[i][j] = coefficient_matrix[i][j]  # Wypełnianie macierzy D (diagonala)
            else:
                matrix_u[i][j] = coefficient_matrix[i][j]  # Wypełnianie macierzy U (powyżej diagonali)

    return matrix_l, matrix_d, matrix_u

def inverse_matrix(matrix_d):
    # Oblicza macierz odwrotną do macierzy D
    matrix_n = np.linalg.inv(matrix_d)
    return matrix_n

# Wzór iteracyjny
# x^(n+1) = Mx + Nb
# D^(-1) = N
# M = -D^(-1)(L + U) = -N(L + U)

def matrix_m_n_calculation(coefficient_matrix):
    # Podział macierzy współczynników na macierze L, D i U
    matrix_l, matrix_d, matrix_u = split_coefficient_matrix(coefficient_matrix)

    # Konwersja list na macierze numpy
    matrix_l = np.array(matrix_l)
    matrix_d = np.array(matrix_d)
    matrix_u = np.array(matrix_u)

    # Obliczenie macierzy N jako odwrotność macierzy D
    matrix_n = np.linalg.inv(matrix_d)

    # Obliczenie macierzy M jako -N * (L + U)
    matrix_l_plus_u = matrix_l + matrix_u
    matrix_m = -np.matmul(matrix_n, matrix_l_plus_u)

    # Zwrócenie macierzy M i N
    return matrix_m, matrix_n

def jacobian_method(matrix_x, matrix_b, matrix_m, matrix_n, stop_condition_value, stop_condition_type):
    # Obliczenie Nb (N * b), gdzie N to macierz odwrotna do D, a b to wektor wyrazów wolnych
    nb = np.matmul(matrix_n, matrix_b)
    iterations = 0  # Inicjalizacja licznika iteracji

    # Wyświetlenie każdej macierzy
    print("\nMacierz współczynników: \n", matrix_m)
    print("\nMacierz wyrazów wolnych: \n", matrix_b)
    print("\nMacierz N: \n", matrix_n)
    print('\nMacierz zmiennych: \n', matrix_x)

    calc_continue = True  # Ustawienie flagi kontynuacji obliczeń
    while calc_continue:  # Pętla iteracyjna metody Jacobiego
        previous_x = matrix_x.copy()  # Zachowanie poprzedniej wartości wektora x
        matrix_x = np.matmul(matrix_m, previous_x) + nb  # Obliczenie nowej wartości wektora x
        iterations += 1  # Zwiększenie licznika iteracji

        # Obliczenie błędu jako norma różnicy między aktualnym a poprzednim wektorem x
        error = np.linalg.norm(np.subtract(matrix_x, previous_x))

        print(f"Iteration {iterations}: {matrix_x}, error = {error}")

        # Sprawdzenie warunku stopu
        if stop_condition_type == 'M':  # Warunek stopu: maksymalna liczba iteracji
            if iterations >= stop_condition_value:  # Sprawdzenie, czy osiągnięto maksymalną liczbę iteracji
                calc_continue = False  # Ustawienie flagi na False, aby zakończyć pętlę
        else:  # stop_condition_type == 'B' # Warunek stopu: błąd
            if error < stop_condition_value:  # Sprawdzenie, czy błąd jest mniejszy niż zadana wartość
                calc_continue = False  # Ustawienie flagi na False, aby zakończyć pętlę
    print("Rozwiązanie: ", matrix_x)  # Wyświetlenie znalezionego rozwiązania

