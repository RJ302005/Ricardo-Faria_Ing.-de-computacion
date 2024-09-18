print("Introduce tu puntuación (0.0, 0.4, 0.6 o más): ")  #Pedimos al usuario que introduzca su puntuación.
puntuacion = float(input())  #Convertimos la entrada del usuario a un número decimal (float) y la almacenamos en la variable 'puntuacion'.
salario_base = 2400  #Definimos el salario base, que es constante para el cálculo de la bonificación.

# Determinamos el rendimiento basado en la puntuación introducida.
if puntuacion == 0.0:
    rendimiento = "Inaceptable"  #Si la puntuación es 0.0, el rendimiento es "Inaceptable".
elif puntuacion == 0.4:
    rendimiento = "Aceptable"  #Si la puntuación es 0.4, el rendimiento es "Aceptable".
elif puntuacion >= 0.6:
    rendimiento = "Meritorio"  #Si la puntuación es 0.6 o mayor, el rendimiento es "Meritorio".
else:
    print("Puntuación no válida.")  #Mensaje en caso de que la puntuación no sea válida.
    exit()  #Terminamos la ejecución del programa si la puntuación no es válida.

#Calculamos la bonificación como un porcentaje del salario base basado en la puntuación introducida.
bonificacion = salario_base*puntuacion

#Mostramos al usuario el rendimiento y la bonificación calculada.
print(f"Rendimiento: {rendimiento}")
print(f"Bonificación: {bonificacion} €")
