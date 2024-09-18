print("Calculadora de factibilidad de proyectos de Hyserca")
print("Ingrese el presupuesto actual disponible")
#Uso print para mostrar un mensaje de bienvenida y explicar la función del programa.
presupuesto = float(input())  #Almaceno el valor del presupuesto en una variable de tipo float.
#Usamos float para permitir números con decimales, lo cual es importante para presupuestos precisos.

print("Ahora ingrese el valor del coste del proyecto")
coste_proyecto = float(input())  #Almaceno el valor del coste del proyecto en una variable de tipo float.
#Igualmente utilizo float aquí para colocar decimales en el coste del proyecto si llega a hacer falta

lim_factibilidad = presupuesto * 0.75  #Calculo y almaceno en una variable el 75% del presupuesto 
#como límite para la factibilidad del proyecto.
print("El límite para la factibilidad del proyecto es del 75% del presupuesto")
#Le informo al usuario sobre el porcentaje límite establecido.
print(f"El límite actual es de: {lim_factibilidad}")  #Muestro el límite calculado basado en el presupuesto.

if lim_factibilidad > coste_proyecto:
    #Si el coste del proyecto es menor que el 75% del presupuesto, el proyecto es factible.
    print("El coste del proyecto es factible")  #Le informo al usuario que el coste está dentro del límite permitido.
    print("No sobrepasa el 75% del presupuesto")  #Confirmo que el proyecto está dentro del rango de presupuesto.
    sobrante = lim_factibilidad - coste_proyecto  #Calculo el sobrante del presupuesto accesible 
    #después de considerar el coste del proyecto.
    #Muestra el sobrante disponible para otros usos o proyectos.
    print(f"El presupuesto sobrante es de: {sobrante}")  #Informo al usuario cuánto presupuesto queda 
    #después de considerar el coste del proyecto.

elif lim_factibilidad == coste_proyecto:
    #Si el coste del proyecto es exactamente el 75% del presupuesto, el proyecto no es factible.
    print("El coste del proyecto no es factible")  #Le informo al usuario que el coste es igual al límite permitido, pero no es factible.
    print("El coste es igual al 75% del presupuesto")  #Y confirmo que el coste está en el límite exacto pero no es aceptable.

else:
    #Si el coste del proyecto excede el 75% del presupuesto, el proyecto no es factible.
    print("El coste del proyecto no es factible")  #Le informo al usuario que el coste supera el límite permitido.
    print("El coste sobrepasa el 75% del presupuesto")  #Y confirmo que el proyecto excede el presupuesto permitido.
