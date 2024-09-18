#Primeramente quiero avisar que sé que esto no está en el progrma de estudios 
#Lo que sucede es que tuve que investigar aparte y buscar ejemplos con todas las herramientas a disposición
#Por lo cual entiendo bién la lógica del programa y como este funciona
#En dado caso primero tenemos que declarar las variables que contendrán a todos los perfiles y calibres
#De tubos que hay en la empresa de tubrimeca, para ello es mejor usar una variable en función de diccionario
#Esto funciona igual que hacer una función o una sección de tipo void en C la cual componga todas las variables
perfiles = {
    #colocamos los nombres de los pefiles par separarlos cada uno
    #Después incluimos en todos las medidas de los perfiles de acuerdo a sus calibres
    #Por lo cual los separamos primero por calibre, dentro del calibre ponemos las medidas
    #Y tambien ponemos los valores de los pesos por metro de tubo y por pieza de tubo.
    #Todo ello siguiendo la imagen de referencia de la presentción de power point
    "C-050": {18: ('1/2"x1/2" (13mm)', 0.5, 3.0), 20: ('1/2"x1/2" (13mm)', 0.4, 2.4)},
    "C-075": {18: ('3/4"x3/4" (19mm)', 0.75, 4.5), 20: ('3/4"x3/4" (19mm)', 0.6, 3.6)},
    "C-100": {18: ('1"x1" (25mm)', 1.0, 6.0), 20: ('1"x1" (25mm)', 0.8, 4.8)},
    "C-125": {18: ('1 1/4"x1 1/4" (32mm)', 1.25, 7.5), 20: ('1 1/4"x1 1/4" (32mm)', 1.0, 6.0)},
    "C-150": {18: ('1 1/2"x1 1/2" (38mm)', 1.5, 9.0), 20: ('1 1/2"x1 1/2" (38mm)', 1.2, 7.2)},
    "C-200": {18: ('2"x2" (50mm)', 2.0, 12.0)}
}

#Ahora tenemos que solicitarle al usuario el modelo y calibre del tubo necesitado por la empresa.
print("Ingrese el modelo del perfil (C-050, C-075, C-100, C-125, C-150, C-200): ")
modelo = input()
print("Ingrese el calibre del perfil (18, 20): ")
print("Aviso: El perfil C-200 no tiene calibre 20 en existencia")
calibre = int( input())
#Por lo cual guardamos las entradas de teclado del usuario en dos variables para cada objeto necesatio.
#Seguidamente mostramos los datos del perfil si existe dentro del diccionario
if modelo in perfiles and calibre in perfiles[modelo]:
    medidas, peso_metro, peso_pieza = perfiles[modelo][calibre]
#En la linea de arriba declaramos el formato que se usa para los objetos de modelo y calibre del programa
#Los cuales estan designados y contenidos dentro del diccionario de perfiles
#Al haberlos escrito y declarado con la misma estructura el programa puede encontrar estos datos de forma lineal
    print(f"Datos del perfil {modelo} calibre {calibre}: {medidas}")
    print(f"Peso por metro: {peso_metro} Kg")
    print(f"Peso por pieza: {peso_pieza} Kg")
else:
    #Por ultimo si no existe el perfil presentamos un mensaje de error
    print("Error Error Error Error Error Error Error Error Error Error Error Error Error Error Error Error Error Error Error")
    print("ERROR: El perfil indicado no existe.")
