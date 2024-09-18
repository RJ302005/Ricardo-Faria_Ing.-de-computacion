print(f"What is your age?") #Aquí le preguntamos al usuario cual es su edad
a = int(input()) #Guardamos lo que escriba el ususario en una variable y lo transformamos a entero

if a >= 18: #Si el usuario tiene 18 o más el programa imprimirá un mensaje diciendo si es mayor o menor de edad
    print("You are legaly an adult")
else: print("You are a minor")
