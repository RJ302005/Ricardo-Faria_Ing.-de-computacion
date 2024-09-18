print("What is the base of your rectangle?")  # Pedimos al usuario que ingrese la base del rectángulo.
b=int( input())  # Guardamos el valor de la base en la variable b, convirtiendo la entrada a un número entero.
print("What is the height of your rectangle")  # Solicitamos al usuario la altura del rectángulo.
h=int( input())  # Guardamos el valor de la altura en la variable h, convirtiendo la entrada a un número entero.
print("We are calculating the area of the polygon")  # Informamos al usuario que estamos calculando el área del rectángulo.
a = b*h  # Calculamos el área del rectángulo usando la fórmula área = base * altura.
print(f"The area of your polygon is: {a}")  # Mostramos el área calculada al usuario.

# Verificamos si el área es mayor a 40 y la altura es mayor a 10.
if a > 40 and h > 10:
    print("Your polygon has an area more than 40")  # Mensaje si el área es mayor a 40.
    print("Your polygon has a height more than 10")  # Mensaje si la altura es mayor a 10.
else:
    # Si la condición no se cumple, no mostramos ningún mensaje (vacío).
    print('')
