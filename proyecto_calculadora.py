import math

# Diccionario seguro de funciones permitidas
funciones = {
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'sqrt': math.sqrt,
    'log': math.log,     # log(x) = ln(x)
    'log10': math.log10, # log base 10
    'exp': math.exp,
    'pi': math.pi,
    'e': math.e,
    'abs': abs,
    'pow': pow
}

def calcular(expresion):
    try:
        resultado = eval(expresion, {"__builtins__": None}, funciones)
        return resultado
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("🔢 Calculadora científica en Python")
    print("Funciones disponibles: sin, cos, tan, sqrt, log, log10, exp, pi, e, abs, pow")
    print("Ejemplos: sin(pi/2), log(e), sqrt(25), pow(2,3), 2+3*4")

    while True:
        expresion = input("\nIngresa una expresión (o 'salir'): ")
        if expresion.lower() in ["salir", "exit", "quit"]:
            print("¡Hasta luego!")
            break
        resultado = calcular(expresion)
        print("Resultado:", resultado)

if __name__ == "__main__":
    main()
