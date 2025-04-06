from menu import menu, load_file, get_data_from_user
from jacobian_method import jacobian_method, is_diagonal_dominance, matrix_m_n_calculation, generate_x_matrix, is_irreducible, is_weakly_diagonally_dominant_with_strict_one, is_zero_on_diagonal


# Funkcja przeprowadzająca obliczenia metodą Jacobiego na podstawie danych wejściowych.
def run_calculation(matrix_coefficients, matrix_b, stop_condition_value, stop_condition_type):
    # Obliczenie macierzy M i N na podstawie macierzy współczynników.
    matrix_m, matrix_n = matrix_m_n_calculation(matrix_coefficients)

    # Wygenerowanie początkowej macierzy x o odpowiednim rozmiarze.
    matrix_x = generate_x_matrix(len(matrix_coefficients))

    # Wywołanie metody Jacobiego z odpowiednimi parametrami.
    jacobian_method(matrix_x, matrix_b, matrix_m, matrix_n, stop_condition_value, stop_condition_type)


# Funkcja główna programu
def main():

    # Pobranie danych wejściowych od użytkownika za pomocą menu
    number_of_equations, get_data_option , stop_condition_value, stop_condition_type = menu()
    # Sprawdzenie, czy dane mają być wczytane z pliku
    if get_data_option == 'file':
        # Wczytanie macierzy współczynników i wektora wyrazów wolnych z pliku
        matrix_coefficients, matrix_b = load_file(number_of_equations)
        # Wyświetlenie wczytanych danych
        print("Wczytano macierz: \n" + str(matrix_coefficients) + "\n\n oraz wektor b: \n" + str(matrix_b))
    else:
        # Pobranie macierzy współczynników i wektora wyrazów wolnych od użytkownika
        matrix_coefficients, matrix_b = get_data_from_user(number_of_equations)


    if is_zero_on_diagonal(matrix_coefficients):
    # Sprawdzenie, czy macierz współczynników jest diagonalnie dominująca
        if is_diagonal_dominance(matrix_coefficients):

            # Jeśli macierz jest diagonalnie dominująca, istnieje gwarancja rozwiązania
            run_calculation(matrix_coefficients, matrix_b, stop_condition_value, stop_condition_type)
        else:
            # Jeśli macierz nie jest diagonalnie dominująca, wyświetlenie ostrzeżenia
            print("\nOstrzeżenie: Macierz NIE JEST ściśle diagonalnie dominująca.")
            # Wyświetlenie informacji o rozpatrywanym warunku nieredukowalności
            print("ZOSTANIE ROZPATRZONY WARUNEK NIEREDUKOWALNOŚCI.")

            # Sprawdzenie warunku nieredukowalności i słabej dominacji diagonalnej z jednym wierszem ściśle dominującym
            if is_irreducible(matrix_coefficients) and is_weakly_diagonally_dominant_with_strict_one(matrix_coefficients):
                # Jeśli warunek nieredukowalności jest spełniony, istnieje gwarancja rozwiązania
                run_calculation(matrix_coefficients, matrix_b, stop_condition_value, stop_condition_type)

            else:

                # Jeśli warunek nieredukowalności nie jest spełniony, brak gwarancji rozwiązania
                print("\nOstrzeżenie: Macierz NIE JEST nieredukowalna i nie jest ściśle diagonalnie dominująca.")
                # Wyświetlenie informacji o braku gwarancji znalezienia dobrego rozwiązania
                print("Nie można zagwarantować, że metoda Jacobiego znajdzie dobre rozwiązanie.")
                # Wyświetlenie informacji o podjęciu próby rozwiązania z zabezpieczeniem przed nieskończoną pętlą
                print("Zostanie podjęta próba rozwiązania. Zabezpieczenie przed nieskończoną pętlą to 100 iteracji.")

                # Uruchomienie obliczeń z maksymalną liczbą iteracji ustawioną na 100
                run_calculation(matrix_coefficients, matrix_b, 100, 'M')

                # Zakończenie funkcji main
                return
    else:
        # Jeśli na diagonali znajdują się zera, wyświetlenie ostrzeżenia
        print("\nOstrzeżenie: Macierz współczynników zawiera zera na przekątnej diagonalnej.")
        print("Popraw macierz współczynników, aby uniknąć problemów z obliczeniami.")
        return

# Uruchomienie programu
if __name__ == "__main__":
    main()
