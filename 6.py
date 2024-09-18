#Primeramente definimos el precio base de cada zapato y los porcentajes de descuento.
zapatos_precio = int(80) #Guardamos el precio base de cada zapato en una variable de tipo entero
descuento0 = float(0.1)  #En esta colocamos el descuento del 10% como un número decimal
descuento1 = float(0.2)  #Hacemos lo mismo aquí para el descuento del 20%.
descuento2 = float(0.4)  #Y exactamente igual para el descuento del 40%.

print("El precio base de los zapatos es de 80$") #Imprimimos un mensaje que informa al usuario sobre el precio base.
print("Por favor ingrese la cantidad de zapatos que desea comprar")  #Aquí le pedimos al usuario que ingrese la cantidad de zapatos.
cantidad = int(input())  #Con esto convertimos la cantidad que el usuario escriba a un número entero.

subtotal = zapatos_precio * cantidad  #Con esto calculamos el subtotal multiplicando el precio por la cantidad de zapatos.

#Aquí aplicamos el descuento basado en la cantidad de zapatos comprados.
if cantidad > 10 and cantidad <= 20:
    descontado = subtotal * descuento0  #Con esto Calculamos el descuento del 10% para cantidades entre 11 y 20.
    total_zapatos = subtotal - int(descontado)  #Le Restamos el descuento del subtotal para obtener el total.
    print(f"El subtotal del precio de compra asciende a: {subtotal}$")  #Mostramos el subtotal.
    print("Se le ha aplicado un descuento a su compra")  #Informamos al usuario que se ha aplicado un descuento.
    print("El descuento es del 10%")  #Especificamos el porcentaje de descuento.
    print(f"El total de su compra actualmente es de: {total_zapatos}$")  #Mostramos el total con el descuento aplicado.

elif cantidad > 20 and cantidad <= 30:
    descontado = subtotal * descuento1  #En esta función calculamos el descuento del 20% para cantidades entre 21 y 30.
    total_zapatos = subtotal - int(descontado)  #Le restamos el descuento del subtotal para obtener el total.
    print(f"El subtotal del precio de compra asciende a: {subtotal}$")  #Mostramos el subtotal.
    print("Se le ha aplicado un descuento a su compra")  #Informamos al usuario que se ha aplicado un descuento.
    print("El descuento es del 20%")  #Especificamos el porcentaje de descuento.
    print(f"El total de su compra actualmente es de: {total_zapatos}$")  #Mostramos el total con el descuento aplicado.

elif cantidad > 30:
    descontado = subtotal * descuento2  #Calculamos el descuento del 40% para cantidades mayores a 30.
    total_zapatos = subtotal - int(descontado)  #Le restamos el descuento del subtotal para obtener el total.
    print(f"El subtotal del precio de compra asciende a: {subtotal}$")  #Mostramos el subtotal.
    print("Se le ha aplicado un descuento a su compra")  #Informamos al usuario que se ha aplicado un descuento.
    print("El descuento es del 40%")  #Especificamos el porcentaje de descuento.
    print(f"El total de su compra actualmente es de: {total_zapatos}$")  #Mostramos el total con el descuento aplicado.

else:
    #Y por último caso si la cantidad de zapatos no califica para ningún descuento, mostramos el subtotal sin descuento.
    print(f"El total del precio de su compra asciende a: {subtotal}$")
