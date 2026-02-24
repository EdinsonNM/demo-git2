def multiplicar(a,b):
    return a * b


def dividir(a,b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir por cero"
    
def potencia(a,b):
    return a ** b


multiplicacion = multiplicar(3, 8)
print("La multiplicacion es:", multiplicacion)

division = dividir(10, 2)
print("La division es:", division)

potencia = potencia(2, 3)
print("La potencia es:", potencia)