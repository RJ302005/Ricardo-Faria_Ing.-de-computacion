print("Calculadora de salario")  #Este es el mensaje de bienvenida que informa al usuario sobre la calculadora de salarios.

print("Ingrese su tipo de salario (A, B o C): ") #Aquí solicitamos al usuario que ingrese el tipo de salario (A, B o C).
TS = input()  #Guardamos la elección del usuario en la variable TS (Tipo de Salario).

print("Ingrese las horas que ha trabajado esta semana: ")#Ahora pedimos al usuario que ingrese las horas trabajadas esta semana.
Horas_Trabajadas = float(input())  #Convertimos la entrada del usuario a un número decimal para poder realizar cálculos.

#Verificamos el tipo de salario ingresado por el usuario.
if TS[0] == "A" or TS[0] == "a":
    #Si el tipo de salario es A, definimos la tarifa por hora.
    print("Salario tipo A, valor bs. 60")
    salario_A = 60  # Valor del salario por hora para el tipo A.
    Salario = Horas_Trabajadas * salario_A  # Calculamos el salario total sin horas extra.
    print(f"Su salario semanal es de bs. {Salario}")
    #Si el usuario trabajó más de 40 horas, calculamos el salario extra.
    if Horas_Trabajadas > 40:
        Salario_Extra = (Horas_Trabajadas - 40) * (salario_A * 1.5)  # Cálculo del pago por horas extra al 1.5 del salario por hora.
        print("Usted ha trabajado horas extra")
        print("Las horas extra se pagan al 1.5 del salario por hora")
        print(f"Sus horas extra son de bs. {Salario_Extra}")
    #Si el usuario trabajó más de 50 horas, se añade un bono especial.
    if Horas_Trabajadas > 50:
        print("Usted ha trabajado más de 50 horas semanales")
        print("Ha recibido un bono de bs. 200")
        Bono_Esp = Salario + 200  # Calculamos el salario total con el bono.
        print(f"Su salario más el bono es de bs. {Bono_Esp}")
    #Calculamos y mostramos el salario total incluyendo bono y horas extra.
    print(f"Su salario total (Bono + Horas extra) es de bs. {Bono_Esp + Salario_Extra}")

elif TS[0] == "B" or TS[0] == "b":
    #Si el tipo de salario es B, definimos la tarifa por hora.
    print("Salario tipo B, valor bs. 70")
    salario_B = 70  # Valor del salario por hora para el tipo B.
    Salario = Horas_Trabajadas * salario_B  # Calculamos el salario total sin horas extra.
    print(f"Su salario semanal es de bs. {Salario}")
    #Si el usuario trabajó más de 40 horas, calculamos el salario extra.
    if Horas_Trabajadas > 40:
       Salario_Extra = (Horas_Trabajadas - 40) * (salario_B * 1.5)  # Cálculo del pago por horas extra al 1.5 del salario por hora.
       print("Usted ha trabajado horas extra")
       print("Las horas extra se pagan al 1.5 del salario por hora")
       print(f"Sus horas extra son de bs. {Salario_Extra}")
    #Si el usuario trabajó más de 50 horas, se añade un bono especial.
    if Horas_Trabajadas > 50:
        print("Usted ha trabajado más de 50 horas semanales")
        print("Ha recibido un bono de bs. 200")
        Bono_Esp = Salario + 200  # Calculamos el salario total con el bono.
        print(f"Su salario más el bono es de bs. {Bono_Esp}")
    #Calculamos y mostramos el salario total incluyendo bono y horas extra.
    print(f"Su salario total (Bono + Horas extra) es de bs. {Bono_Esp + Salario_Extra}")

elif TS[0] == "C" or TS[0] == "c":
    #Si el tipo de salario es C, definimos la tarifa por hora.
    print("Salario tipo C, valor bs. 120")
    Salario_C = 120  # Valor del salario por hora para el tipo C.
    Salario = Horas_Trabajadas * Salario_C  # Calculamos el salario total sin horas extra.
    print(f"Su salario semanal es de bs. {Salario}")
    #Si el usuario trabajó más de 40 horas, calculamos el salario extra.
    if Horas_Trabajadas > 40:
         Salario_Extra = (Horas_Trabajadas - 40) * (Salario_C * 1.5)  # Cálculo del pago por horas extra al 1.5 del salario por hora.
         print("Usted ha trabajado horas extra")
         print("Las horas extra se pagan al 1.5 del salario por hora")
         print(f"Sus horas extra son de bs. {Salario_Extra}")
    #Calculamos y mostramos el salario total incluyendo horas extra.
    print(f"Su salario total (Salario normal + Horas extra) es de bs. {Salario + Salario_Extra}")

else:
    #Si el tipo de salario ingresado no es válido, mostramos un mensaje de error y salimos del programa.
    print("Entrada inválida, expulsando")
    exit()