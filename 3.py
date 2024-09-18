print("Introduzca la nueva contraseña: ")  # Solicitamos al usuario que ingrese una nueva contraseña.
passcode = input()  # Guardamos la contraseña ingresada en la variable 'passcode'.
print("La contraseña ha sido guardada exitosamente")  # Informamos al usuario que la contraseña se ha guardado con éxito.
print("Introduzca la contraseña: ")  # Pedimos al usuario que ingrese la contraseña para verificarla.

# Comparamos la contraseña ingresada con la que guardamos previamente.
if input() == passcode:
    print("Contraseña aceptada, bienvenido")  # Mensaje si la contraseña ingresada es correcta.
else:
    print("Contraseña incorrecta, ejecutando alarma")  # Mensaje si la contraseña ingresada es incorrecta.
