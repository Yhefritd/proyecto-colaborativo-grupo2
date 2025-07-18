def calculadora():
    print("--- Calculadora Simple ---")
    ops = {'+': 'suma', '-': 'resta', '*': 'multiplicación', '/': 'división'}
    print("Operaciones disponibles:", ', '.join([f"{k} ({v})" for k, v in ops.items()]))

    while True:
        try:
            num1 = float(input("Ingresa el primer número: "))
            operador = input("Ingresa la operación (+, -, *, /): ")
            num2 = float(input("Ingresa el segundo número: "))
            if operador not in ops:
                raise ValueError("Operación inválida.")
            if operador == '/' and num2 == 0:
                raise ZeroDivisionError("No se puede dividir por cero.")
            resultado = eval(f"{num1}{operador}{num2}")
            print(f"El resultado de la {ops[operador]} es: {resultado}")
            break
        except ValueError as e:
            print(f"Error: {e}")
        except ZeroDivisionError as e:
            print(f"Error: {e}")
    print("------------------------")

calculadora()
