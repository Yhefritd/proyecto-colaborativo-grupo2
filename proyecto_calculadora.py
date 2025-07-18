def calculadora():
    """
    Realiza operaciones matemáticas básicas: suma, resta, multiplicación y división.
    """
    print("--- Calculadora Simple ---")
    print("Operaciones disponibles:")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")
    print("------------------------")

    while True:
        try:
            num1 = float(input("Ingresa el primer número: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")

    while True:
        operador = input("Ingresa la operación (+, -, *, /): ")
        if operador in ('+', '-', '*', '/'):
            break
        else:
            print("Operación inválida. Por favor, elige +, -, * o /.")

    while True:
        try:
            num2 = float(input("Ingresa el segundo número: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")

    if operador == '+':
        resultado = num1 + num2
        print(f"El resultado de la suma es: {resultado}")
    elif operador == '-':
        resultado = num1 - num2
        print(f"El resultado de la resta es: {resultado}")
    elif operador == '*':
        resultado = num1 * num2
        print(f"El resultado de la multiplicación es: {resultado}")
    elif operador == '/':
        if num2 != 0:
            resultado = num1 / num2
            print(f"El resultado de la división es: {resultado}")
        else:
            print("Error: No se puede dividir por cero.")
    else:
        print("Ha ocurrido un error inesperado con el operador.")

    print("------------------------")

# Llama a la función de la calculadora para ejecutarla
calculadora()