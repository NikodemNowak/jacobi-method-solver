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
                if 2 <= number_of_equations <= 10:
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


def load_file(file_number):
    # Create separate matrices for coefficients and constants
    # Example
    # 3 3 1 12
    # 2 5 7 33
    # 1 2 1 8

    try:
        with open(f'coefficients/{file_number}.txt', 'r') as f:
            lines = f.readlines()

            # Filtrowanie pustych linii
            lines = [line.strip() for line in lines if line.strip()]

            if not lines:
                print("Plik jest pusty.")
                return None, None

            # Parsowanie linii do postaci macierzy
            data = []
            for line in lines:
                values = list(map(float, line.strip().split()))
                if len(values) < 2:  # Potrzebujemy co najmniej jeden współczynnik i wyraz wolny
                    print(f"Błąd w linii: '{line}' - za mało wartości.")
                    continue
                data.append(values)

            if not data:
                print("Brak poprawnych danych w pliku.")
                return None, None

            # Sprawdzenie czy wszystkie wiersze mają taką samą długość
            row_lengths = [len(row) for row in data]
            if len(set(row_lengths)) > 1:
                print("Błąd: Niezgodna liczba wartości w wierszach.")
                return None, None

            # Tworzenie macierzy współczynników i wektora wyrazów wolnych
            coefficient_matrix = np.array([row[:-1] for row in data])
            matrix_b = np.array([row[-1] for row in data])

            return coefficient_matrix, matrix_b

    except FileNotFoundError:
        print(f"Nie znaleziono pliku dla {file_number} równań.")
        return None, None


def get_data_from_user(number_of_equations):
    # Create separate matrices for coefficients and constants
    coefficient_matrix = np.zeros((number_of_equations, number_of_equations))
    matrix_b = np.zeros(number_of_equations)

    print(f"Wprowadź macierz {number_of_equations}x{number_of_equations} oraz wyrazy wolne.")
    print("Format: dla każdego wiersza podaj współczynniki oddzielone spacją, a na końcu wyraz wolny.")
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
