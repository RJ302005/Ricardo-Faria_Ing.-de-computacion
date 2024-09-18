print("Ingresa tu nombre")  # Solicitamos al usuario que ingrese su nombre.
nombre = input()  # Guardamos el nombre ingresado en la variable 'nombre'.
print("Introduce tu género (Mujer/Hombre): ")  # Pedimos al usuario que ingrese su género.
genero = input()  # Guardamos el género ingresado en la variable 'genero'.

# Evaluamos el género ingresado para determinar el grupo al que pertenece el usuario.
if genero == "Mujer":
    # Si el género es "Mujer", comprobamos la primera letra del nombre para asignar el grupo.
    if nombre[0] < "M":  # Si la primera letra del nombre es menor que "M" en orden alfabético.
        grupo = "A"  # Asignamos el grupo "A".
    else:
        grupo = "B"  # Si la primera letra del nombre es igual o mayor que "M", asignamos el grupo "B".
elif genero == "Hombre":
    # Si el género es "Hombre", comprobamos la primera letra del nombre para asignar el grupo.
    if nombre[0] > "N":  # Si la primera letra del nombre es mayor que "N" en orden alfabético.
        grupo = "A"  # Asignamos el grupo "A".
    else:
        grupo = "B"  # Si la primera letra del nombre es igual o menor que "N", asignamos el grupo "B".
else:
    print("Sexo no válido.")  # Mensaje en caso de que el género ingresado no sea válido.
    exit()  # Terminamos la ejecución del programa si el género no es válido.

print(f"Perteneces al grupo: {grupo}")  # Mostramos al usuario el grupo al que pertenece.
