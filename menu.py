import numpy as np

def get_number_of_equations():
    number_of_equations = 0
    get_data_option = ''
    valid_number = False
    while not valid_number:
        try:
            print("Wybierz opcję:")
            print("1. Wczytaj macierz z pliku")
            print("2. Wprowadź własne dane")
            choice = int(input())

            if choice == 1:
                print("Podaj numer macierzy do wczytania z pliku (max 10): ")
                number_of_equations = int(input())
                if 1 <= number_of_equations <= 10:
                    valid_number = True
                    get_data_option = 'file'
                else:
                    print("Liczba równań musi być z przedziału 1-10")
            elif choice == 2:
                print("Podaj rozmiar macierzy do wprowadzenia (max 10): ")
                number_of_equations = int(input())
                if 1 <= number_of_equations <= 10:
                    valid_number = True
                    get_data_option = 'manual'
                else:
                    print("Liczba równań musi być z przedziału 1-10")
            else:
                print("Nieprawidłowa opcja. Wybierz 1 lub 2.")
        except ValueError:
            print("Niepoprawna wartość. Podaj liczbę całkowitą.")
    return number_of_equations, get_data_option

def get_stop_condition_type():
    valid_choice = False
    user = ''
    while not valid_choice:
        print("Maksymalna liczba iteracji/Błąd [M/B]:")
        user = input().upper()
        if user in ['M', 'B']:
            valid_choice = True
        else:
            print("Niepoprawny wybór. Wybierz M lub B")
    return user

def get_stop_condition_value(stop_condition_type):
    valid_value = False
    stop_condition_value = 0
    while not valid_value:
        try:
            if stop_condition_type == 'M':
                print("Podaj maksymalną liczbę iteracji: ")
                stop_condition_value = int(input())
                if stop_condition_value > 0:
                    valid_value = True
                else:
                    print("Liczba iteracji musi być dodatnia.")
            else:  # stop_condition_type == 'B'
                print("Podaj błąd: ")
                stop_condition_value = float(input())
                if stop_condition_value > 0:
                    valid_value = True
                else:
                    print("Wartość błędu musi być dodatnia.")
        except ValueError:
            print("Niepoprawna wartość. Podaj odpowiednią liczbę.")
    return stop_condition_value

def menu():
    number_of_equations, get_data_option = get_number_of_equations()
    stop_condition_type = get_stop_condition_type()
    stop_condition_value = get_stop_condition_value(stop_condition_type)
    return number_of_equations, get_data_option, stop_condition_value, stop_condition_type

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


def get_data_from_user(number_of_equations):
    # Create separate matrices for coefficients and constants
    coefficient_matrix = np.zeros((number_of_equations, number_of_equations))
    matrix_b = np.zeros(number_of_equations)

    print(f"Wprowadź macierz {number_of_equations}x{number_of_equations} oraz wyrazy wolne.")
    print("Format: dla każdego wiersza podaj współczynniki oddzielone spacją, a na końcu wyraz wolny.")
    print("Przykład dla 2 równań: 2 1 5 (gdzie 2 i 1 to współczynniki, 5 to wyraz wolny)")

    for i in range(number_of_equations):
        valid_input = False
        while not valid_input:
            try:
                print(f"Wiersz {i + 1}: ", end="")
                values = list(map(float, input().strip().split()))

                if len(values) != number_of_equations + 1:
                    print(f"Błąd: Podaj dokładnie {number_of_equations} współczynniki oraz 1 wyraz wolny.")
                else:
                    # Przypisz współczynniki
                    for j in range(number_of_equations):
                        coefficient_matrix[i][j] = values[j]

                    # Ostatnia wartość to wyraz wolny
                    matrix_b[i] = values[number_of_equations]
                    valid_input = True

            except ValueError:
                print("Błąd: Podaj poprawne wartości liczbowe oddzielone spacjami.")

    print("\nWprowadzona macierz współczynników:")
    print(coefficient_matrix)
    print("\nWprowadzone wyrazy wolne:")
    print(matrix_b)

    return coefficient_matrix, matrix_b
