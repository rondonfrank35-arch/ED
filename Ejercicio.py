def Ejercicio1():
    Nombre = input("Ingrese su nombre: ")
    Edad = int(input("Ingrese su edad: "))
    Programa = input("Ingrese su programa académico: ")
    Promedio = float(input("Ingrese su promedio academico: "))
    print (Nombre,Edad,Programa,Promedio) 
    print (type(Nombre),type(Edad),type(Programa),type(Promedio))
    print (f"Hola {Nombre}, tienes {Edad} años, estudias {Programa} y tu promedio es {Promedio}.")




def Ejercicio2():
    nota=float(input("Ingrese su nota: "))
    if nota>=3.0:
        print("Aprobado")
    else:
        print("Reprobado")
    if nota < 0.0 or nota > 5.0:
        print("Nota inválida, por favor ingrese un valor entre 0 y 5.")

Ejercicio2()
