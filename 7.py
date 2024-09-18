print("Bienvenido al sistema de calificaciones del colegio La Salle de la Grita")
print("Por favor ingrese la calificación asignada por su profesor")
print("Ingrese su calificación abajo") #Estos son unos mensajes de bienvenida e instrucciones para el alumno
calificacion = int(input()) #Aquí guardamos el valor de la calificación en una variable
if calificacion >= 90 and calificacion <= 100: #Esta es una estructura de if y elif para comparar la información
    #con los rangos de calificaciones
    print("Su calificación es de rango A, Increible!")
elif calificacion >= 80 and calificacion <= 89:
    print("Su calificación es de rango B, Felicidades!")
elif calificacion >= 70 and calificacion <= 79:
    print("Su calificación es de rango C, Buen trabajo")
elif calificacion >= 60 and calificacion <= 69:
    print("Su calificación es de rango D, Bien, pero puedes mejorar")
elif calificacion >= 50 and calificacion<= 59:
    print("Su calificación es de rango F, Más esfuerzo para la proxima vez")
else: print("Su calificación no es lo suficientemente alta para ser calificada")
#Coloqué un mensaje al final para cerrar toda la estructura de if-else para un caso que no sea comparable