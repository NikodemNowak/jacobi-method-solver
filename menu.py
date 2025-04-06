import numpy as np

# Funkcja do pobierania od użytkownika informacji o liczbie równań i sposobie wprowadzania danych.
def get_number_of_equations():
    number_of_equations = 0  # Inicjalizacja zmiennej przechowującej liczbę równań.
    get_data_option = ''  # Inicjalizacja zmiennej przechowującej informację o sposobie wprowadzania danych.
    valid_number = False  # Inicjalizacja flagi sprawdzającej poprawność wprowadzonej liczby.

    # Pętla while, która trwa dopóki użytkownik nie wprowadzi poprawnej liczby równań.
    while not valid_number:
        try:
            print("Wybierz opcję:")
            print("1. Wczytaj macierz z pliku")
            print("2. Wprowadź własne dane")
            choice = int(input())  # Pobranie od użytkownika informacji o wyborze opcji.

            # Sprawdzenie, czy użytkownik wybrał opcję wczytania macierzy z pliku.
            if choice == 1:
                print("Podaj numer macierzy do wczytania z pliku (max 10): ")
                number_of_equations = int(input())  # Pobranie od użytkownika numeru macierzy do wczytania.

                # Sprawdzenie, czy numer macierzy jest z przedziału 1-10.
                if 1 <= number_of_equations <= 10:
                    valid_number = True  # Ustawienie flagi na True, ponieważ wprowadzona liczba jest poprawna.
                    get_data_option = 'file'  # Ustawienie opcji pobierania danych na 'file'.
                else:
                    print("Liczba równań musi być z przedziału 1-10")

            # Sprawdzenie, czy użytkownik wybrał opcję wprowadzenia własnych danych.
            elif choice == 2:
                print("Podaj rozmiar macierzy do wprowadzenia (max 10): ")
                number_of_equations = int(input())  # Pobranie od użytkownika rozmiaru macierzy do wprowadzenia.

                # Sprawdzenie, czy rozmiar macierzy jest z przedziału 2-10.
                if 2 <= number_of_equations <= 10:
                    valid_number = True  # Ustawienie flagi na True, ponieważ wprowadzona liczba jest poprawna.
                    get_data_option = 'manual'  # Ustawienie opcji pobierania danych na 'manual'.
                else:
                    print("Liczba równań musi być z przedziału 1-10")
            else:
                print("Nieprawidłowa opcja. Wybierz 1 lub 2.")

        # Obsługa wyjątku ValueError, który jest zgłaszany, gdy użytkownik wprowadzi niepoprawną wartość.
        except ValueError:
            print("Niepoprawna wartość. Podaj liczbę całkowitą.")

    # Zwrócenie liczby równań i opcji pobierania danych.
    return number_of_equations, get_data_option

# Funkcja do pobierania od użytkownika informacji o typie warunku stopu (maksymalna liczba iteracji lub błąd).
def get_stop_condition_type():
    valid_choice = False  # Inicjalizacja flagi sprawdzającej poprawność wyboru.
    user = ''  # Inicjalizacja zmiennej przechowującej wybór użytkownika.
    while not valid_choice:  # Pętla while, która trwa dopóki użytkownik nie wprowadzi poprawnego wyboru.
        print("Maksymalna liczba iteracji/Błąd [M/B]:")  # Wyświetlenie pytania o typ warunku stopu.
        user = input().upper()  # Pobranie od użytkownika informacji o wyborze i zamiana na wielkie litery.
        if user in ['M', 'B']:  # Sprawdzenie, czy użytkownik wybrał 'M' (maksymalna liczba iteracji) lub 'B' (błąd).
            valid_choice = True  # Ustawienie flagi na True, ponieważ wprowadzony wybór jest poprawny.
        else:
            print("Niepoprawny wybór. Wybierz M lub B")  # Wyświetlenie komunikatu o błędzie.
    return user  # Zwrócenie wyboru użytkownika.

# Funkcja do pobierania od użytkownika wartości warunku stopu (liczba iteracji lub wartość błędu).
def get_stop_condition_value(stop_condition_type):
    valid_value = False  # Inicjalizacja flagi sprawdzającej poprawność wprowadzonej wartości.
    stop_condition_value = 0  # Inicjalizacja zmiennej przechowującej wartość warunku stopu.
    while not valid_value:  # Pętla while, która trwa dopóki użytkownik nie wprowadzi poprawnej wartości.
        try:
            if stop_condition_type == 'M':  # Sprawdzenie, czy warunkiem stopu jest maksymalna liczba iteracji.
                print("Podaj maksymalną liczbę iteracji: ")  # Wyświetlenie prośby o podanie maksymalnej liczby iteracji.
                stop_condition_value = int(input())  # Pobranie od użytkownika maksymalnej liczby iteracji.
                if stop_condition_value > 0:  # Sprawdzenie, czy wprowadzona liczba iteracji jest dodatnia.
                    valid_value = True  # Ustawienie flagi na True, ponieważ wprowadzona wartość jest poprawna.
                else:
                    print("Liczba iteracji musi być dodatnia.")  # Wyświetlenie komunikatu o błędzie.
            else:  # stop_condition_type == 'B' - Warunkiem stopu jest błąd.
                print("Podaj błąd: ")  # Wyświetlenie prośby o podanie wartości błędu.
                stop_condition_value = float(input())  # Pobranie od użytkownika wartości błędu.
                if stop_condition_value > 0:  # Sprawdzenie, czy wprowadzona wartość błędu jest dodatnia.
                    valid_value = True  # Ustawienie flagi na True, ponieważ wprowadzona wartość jest poprawna.
                else:
                    print("Wartość błędu musi być dodatnia.")  # Wyświetlenie komunikatu o błędzie.
        except ValueError:  # Obsługa wyjątku ValueError, który jest zgłaszany, gdy użytkownik wprowadzi niepoprawną wartość.
            print("Niepoprawna wartość. Podaj odpowiednią liczbę.")  # Wyświetlenie komunikatu o błędzie.
    return stop_condition_value  # Zwrócenie wartości warunku stopu.

# Funkcja menu, która zbiera od użytkownika wszystkie potrzebne dane do uruchomienia obliczeń.
def menu():
    number_of_equations, get_data_option = get_number_of_equations()  # Pobranie informacji o liczbie równań i sposobie wprowadzania danych.
    stop_condition_type = get_stop_condition_type()  # Pobranie informacji o typie warunku stopu.
    stop_condition_value = get_stop_condition_value(stop_condition_type)  # Pobranie wartości warunku stopu.
    return number_of_equations, get_data_option, stop_condition_value, stop_condition_type  # Zwrócenie wszystkich zebranych danych.


# Funkcja do wczytywania danych z pliku o podanej nazwie.
def load_file(file_number):
    # Funkcja wczytuje dane z pliku tekstowego, tworząc oddzielne macierze dla współczynników i wektora wyrazów wolnych.
    # Przykład formatu pliku:
    # 3 3 1 12
    # 2 5 7 33
    # 1 2 1 8

    try:
        # Otwarcie pliku o nazwie 'file_number.txt' w katalogu 'coefficients' w trybie do odczytu ('r').
        with open(f'coefficients/{file_number}.txt', 'r') as f:
            # Wczytanie wszystkich linii z pliku do listy 'lines'.
            lines = f.readlines()

            # Filtrowanie pustych linii z listy 'lines'.
            lines = [line.strip() for line in lines if line.strip()]

            # Sprawdzenie, czy plik jest pusty.
            if not lines:
                print("Plik jest pusty.")
                return None, None

            # Parsowanie linii do postaci macierzy.
            data = []
            # Iteracja po każdej linii w liście 'lines'.
            for line in lines:
                # Konwersja wartości w linii na liczby zmiennoprzecinkowe i umieszczenie ich w liście 'values'.
                values = list(map(float, line.strip().split()))
                # Sprawdzenie, czy w linii jest co najmniej jeden współczynnik i wyraz wolny.
                if len(values) < 2:
                    print(f"Błąd w linii: '{line}' - za mało wartości.")
                    continue
                data.append(values)

            # Sprawdzenie, czy dane zostały poprawnie wczytane.
            if not data:
                print("Brak poprawnych danych w pliku.")
                return None, None

            # Sprawdzenie, czy wszystkie wiersze mają taką samą długość.
            row_lengths = [len(row) for row in data]
            if len(set(row_lengths)) > 1:
                print("Błąd: Niezgodna liczba wartości w wierszach.")
                return None, None

            # Tworzenie macierzy współczynników poprzez wyodrębnienie wszystkich kolumn oprócz ostatniej.
            coefficient_matrix = np.array([row[:-1] for row in data])
            # Tworzenie wektora wyrazów wolnych poprzez wyodrębnienie ostatniej kolumny z każdej linii.
            matrix_b = np.array([row[-1] for row in data])

            # Zwrócenie macierzy współczynników i wektora wyrazów wolnych.
            return coefficient_matrix, matrix_b

    # Obsługa wyjątku FileNotFoundError, gdy plik nie zostanie znaleziony.
    except FileNotFoundError:
        print(f"Nie znaleziono pliku dla {file_number} równań.")
        return None, None


# Funkcja do pobierania danych od użytkownika: macierzy współczynników i wektora wyrazów wolnych.
def get_data_from_user(number_of_equations):
    # Inicjalizacja macierzy współczynników jako macierzy zer o wymiarach number_of_equations x number_of_equations.
    coefficient_matrix = np.zeros((number_of_equations, number_of_equations))
    # Inicjalizacja wektora wyrazów wolnych jako wektora zer o długości number_of_equations.
    matrix_b = np.zeros(number_of_equations)

    # Wyświetlenie instrukcji dla użytkownika, jak wprowadzić dane.
    print(f"Wprowadź macierz {number_of_equations}x{number_of_equations} oraz wyrazy wolne.")
    print("Format: dla każdego wiersza podaj współczynniki oddzielone spacją, a na końcu wyraz wolny.")
    # Pętla iterująca po każdym wierszu macierzy.
    for i in range(number_of_equations):
        valid_input = False
        # Pętla while zapewniająca, że użytkownik wprowadzi poprawne dane dla danego wiersza.
        while not valid_input:
            try:
                # Wyświetlenie numeru wiersza, o który prosi się użytkownika.
                print(f"Wiersz {i + 1}: ", end="")
                # Pobranie danych od użytkownika, podzielenie ich na wartości i przekształcenie na liczby zmiennoprzecinkowe.
                values = list(map(float, input().strip().split()))

                # Sprawdzenie, czy liczba wprowadzonych wartości jest zgodna z oczekiwaną liczbą współczynników i wyrazem wolnym.
                if len(values) != number_of_equations + 1:
                    print(f"Błąd: Podaj dokładnie {number_of_equations} współczynniki oraz 1 wyraz wolny.")
                else:
                    # Przypisanie wprowadzonych wartości do macierzy współczynników.
                    for j in range(number_of_equations):
                        coefficient_matrix[i][j] = values[j]

                    # Przypisanie ostatniej wartości do wektora wyrazów wolnych.
                    matrix_b[i] = values[number_of_equations]
                    # Ustawienie flagi valid_input na True, co oznacza, że dane zostały wprowadzone poprawnie.
                    valid_input = True

            # Obsługa wyjątku ValueError, który występuje, gdy użytkownik wprowadzi niepoprawne dane (np. tekst zamiast liczby).
            except ValueError:
                print("Błąd: Podaj poprawne wartości liczbowe oddzielone spacjami.")

    # Wyświetlenie wprowadzonej macierzy współczynników.
    print("\nWprowadzona macierz współczynników:")
    print(coefficient_matrix)
    # Wyświetlenie wprowadzonego wektora wyrazów wolnych.
    print("\nWprowadzone wyrazy wolne:")
    print(matrix_b)

    # Zwrócenie macierzy współczynników i wektora wyrazów wolnych.
    return coefficient_matrix, matrix_b
