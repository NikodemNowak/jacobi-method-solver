from menu import menu, load_file, get_data_from_user
from jacobian_method import jacobian_method, is_matrix_convergent, matrix_m_n_calculation, generate_x_matrix

def main():

    number_of_equations, get_data_option , stop_condition_value, stop_condition_type = menu()
    if get_data_option == 'file':
        matrix_coefficients, matrix_b = load_file(number_of_equations)
        print("Wczytano macierz: \n" + str(matrix_coefficients) + "\n i wektor b: " + str(matrix_b))
    else:
        matrix_coefficients, matrix_b = get_data_from_user(number_of_equations)


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
