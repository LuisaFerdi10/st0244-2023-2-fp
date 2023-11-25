# Importar todas las funciones definidas en el archivo 'main'
from main import *

# Definir una función para verificar una operación específica con casos de prueba
def verify_operation(operation, func, test_cases):
    # Se utiliza un try except para poder manejar los errores de manera mas clara, y no tener que parar la ejecucion del codigo en su totalidad
    try:
        # Iterar sobre los casos de prueba
        for i, (inputs, expected) in enumerate(test_cases, 1):
            # Verificar que el resultado de la función coincide con el resultado esperado
            assert func(*inputs) == expected, f'Test case {i} failed. \n case: {operation}{inputs}.\n Expected {expected}, got {func(*inputs)}'
        # Si todas las aserciones pasan, imprimir un mensaje indicando que todas las pruebas para la operación han pasado
        print(f"All test cases for {operation} passed.")
    except (AssertionError) as e:
        # Si hay un error de aserción o un ValueError, imprimir el mensaje de error
        print(e)
        print(f"Test case for {operation} failed.")

# Definir una función que verifica todas las operaciones con sus respectivos casos de prueba
def verify_all_methods():
    # Definir casos de prueba para la suma
    sum_test_cases = [
        ((2, 2), 4),
        ((-4, -4), -8),
        ((0, 0), 0),
        ((3, 8), 11),
        ((-7, -2), -9),
        ((5, -5), 0),
        ((7, -3), 4),
        ((-7, 3), -4)
    ]

    # Definir casos de prueba para la resta
    substraction_test_cases = [
        ((2, 2), 0),
        ((-4, -4), 0),
        ((0, 0), 0),
        ((3, 8), -5),
        ((-7, -2), -5),
        ((5, -5), 10),
        ((7, -3), 10),
        ((-7, 3), -10)
    ]

    # Definir casos de prueba para la multiplicación
    multiplication_test_cases = [
        ((2, 2), 4),
        ((-4, -4), 16),
        ((0, 0), 0),
        ((3, 8), 24),
        ((-7, -2), 14),
        ((5, -5), -25),
        ((7, -3), -21),
        ((-7, 3), -21)
    ]

    # Definir casos de prueba para la división
    division_test_cases = [
        ((2, 2), 1),
        ((-4, -4), 1),
        ((3, 8), 0.375),
        ((-7, -2), 3.5),
        ((5, -5), -1),
        ((7, -3), -2.3333333333333335),
        ((-7, 3), -2.3333333333333335),
        ((7, 0), "Cannot divide by zero")
    ]

    # Verificar todas las operaciones con sus respectivos casos de prueba
    verify_operation("sum", sum, sum_test_cases)
    verify_operation("substraction", substraction, substraction_test_cases)
    verify_operation("multiplication", multiplication, multiplication_test_cases)
    verify_operation("division", division, division_test_cases)

# Ejecutar todas las verificaciones
verify_all_methods()