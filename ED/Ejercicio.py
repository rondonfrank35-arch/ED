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


def Ejercicio3():
    print("--- Del 1 al 100 ---")
    for i in range(1, 101):
        print(i, end=" ")
    print("\n")

    print("--- Números Pares ---")
    for i in range(1, 101):
        if i % 2 == 0:
            print(i, end=" ")
    print("\n")

    print("--- Números Impares ---")
    for i in range(1, 101):
        if i % 2 != 0:
            print(i, end=" ")
    print("\n")

    print("--- Múltiplos de 5 ---")
    for i in range(1, 101):
        if i % 5 == 0:
            print(i, end=" ")
    print("\n")

    print("--- Suma del 1 al 100 ---")
    suma = 0
    for i in range(1, 101):
        suma += i
    print(f"La suma total es: {suma}")


def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def Ejercicio4():
    while True:
        print("\n=========================")
        print("       CALCULADORA       ")
        print("=========================")
        print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir")
        
        opcion = input("Seleccione: ")
        
        if opcion == "5":
            print("Saliendo de la calculadora...")
            break
            
        if opcion in ["1", "2", "3", "4"]:
            num1 = float(input("Ingrese primer número: "))
            num2 = float(input("Ingrese segundo número: "))
            
            if opcion == "1":
                print("Resultado:", sumar(num1, num2))
            elif opcion == "2":
                print("Resultado:", restar(num1, num2))
            elif opcion == "3":
                print("Resultado:", multiplicar(num1, num2))
            elif opcion == "4":
                print("Resultado:", dividir(num1, num2))
        else:
            print("Opción inválida. Intente de nuevo.")

def Ejercicio5():
    nota1 = 3.5
    nota2 = 4.2
    nota3 = 2.8
    nota4 = 4.5
    nota5 = 3.9

    promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
    mayor = max(nota1, nota2, nota3, nota4, nota5)
    menor = min(nota1, nota2, nota3, nota4, nota5)
    
    aprobados = 0
    for nota in [nota1, nota2, nota3, nota4, nota5]:
        if nota >= 3.0:
            aprobados += 1

    print(f"Promedio: {promedio}")
    print(f"Mayor nota: {mayor}")
    print(f"Menor nota: {menor}")
    print(f"Aprobados: {aprobados}")

# Respuesta a la pregunta:
# Si fueran 100 estudiantes, crear 100 variables individuales (nota1, nota2... nota100)
# haría el código imposible de mantener, propenso a errores y repetitivo.

def Ejercicio6():
    estudiantes = ["Carlos", "María", "Juan", "Ana", "Luis", "Sofia", "Pedro", "Laura", "Diego", "Elena"]
    
    # 1. Mostrar todos
    print("Estudiantes:", estudiantes)
    # 2. Primer estudiante
    print("Primer estudiante:", estudiantes[0])
    # 3. Último estudiante
    print("Último estudiante:", estudiantes[-1])
    # 4. Cantidad
    print("Total estudiantes:", len(estudiantes))
    # 5. Agregar
    estudiantes.append("Camilo")
    # 6. Eliminar
    estudiantes.remove("Juan")
    # 7. Buscar
    nombre_buscar = "Ana"
    if nombre_buscar in estudiantes:
        print(f"{nombre_buscar} se encuentra en la lista.")

# Pregunta: ¿Qué diferencia existe entre tener estudiante1, estudiante2... y una lista?
# Con variables separadas no puedes iterar sobre ellas ni redimensionarlas. La lista las agrupa 
# bajo un único nombre y permite manipularlas dinámicamente con ciclos y métodos.

def Ejercicio7():
    notas = [3.5, 4.2, 2.8, 4.5, 3.9, 2.5, 4.0, 4.7]
    
    total_estudiantes = 0
    suma_notas = 0
    mayor = notas[0]
    menor = notas[0]
    aprobados = 0
    reprobados = 0

    for nota in notas:
        total_estudiantes += 1
        suma_notas += nota
        
        if nota > mayor:
            mayor = nota
        if nota < menor:
            menor = nota
            
        if nota >= 3.0:
            aprobados += 1
        else:
            reprobados += 1

    promedio = suma_notas / total_estudiantes
    
    notas_mayores_promedio = []
    for nota in notas:
        if nota > promedio:
            notas_mayores_promedio.append(nota)

    print(f"Total estudiantes: {total_estudiantes}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Nota mayor: {mayor}")
    print(f"Nota menor: {menor}")
    print(f"Aprobados: {aprobados}")
    print(f"Reprobados: {reprobados}")
    print(f"Notas mayores al promedio: {notas_mayores_promedio}")

def Ejercicio8():
    productos = ["Teclado", "Mouse", "Monitor", "Impresora", "Memoria RAM", "Disco SSD"]
    busqueda = input("Ingrese el producto a buscar: ")
    
    encontrado = False
    for prod in productos:
        if prod.lower() == busqueda.lower():
            encontrado = True
            break
            
    if encontrado:
        print(f"El producto '{busqueda}' fue encontrado.")
    else:
        print(f"El producto '{busqueda}' NO fue encontrado.")

# Explicación:
# El programa realiza una búsqueda secuencial. Recorre elemento por elemento la lista mediante
# un ciclo 'for' y compara cada texto con lo ingresado por el usuario.

def Ejercicio9():
    notas = [
        [4.0, 3.5, 4.2],
        [3.0, 4.1, 3.7],
        [4.5, 3.8, 4.0],
        [2.8, 3.2, 3.5],
        [3.9, 4.5, 4.2]
    ]

    # 1. Promedio de cada estudiante (filas)
    for i in range(len(notas)):
        prom = sum(notas[i]) / len(notas[i])
        print(f"Promedio estudiante {i+1}: {prom:.2f}")
        
    # 2. Promedio de cada asignatura (columnas)
    asignaturas = ["Programación", "Matemáticas", "Inglés"]
    for j in range(3):
        suma_col = sum(notas[i][j] for i in range(len(notas)))
        print(f"Promedio {asignaturas[j]}: {suma_col / len(notas):.2f}")
        
    # 3. Mayor y Menor nota global
    todas_las_notas = [nota for fila in notas for nota in fila]
    print("Nota mayor global:", max(todas_las_notas))
    print("Nota menor global:", min(todas_las_notas))

def Ejercicio10():
    estudiantes = []
    
    while True:
        print("\n=============================")
        print("   SISTEMA DE ESTUDIANTES    ")
        print("=============================")
        print("1. Registrar estudiante\n2. Mostrar estudiantes\n3. Buscar estudiante")
        print("4. Mostrar promedio\n5. Mostrar mayor nota\n6. Mostrar menor nota")
        print("7. Mostrar aprobados\n8. Salir")
        
        opc = input("Seleccione una opción: ")
        
        if opc == "8":
            break
        elif opc == "1":
            nom = input("Nombre: ")
            edad = int(input("Edad: "))
            nota = float(input("Nota: "))
            estudiantes.append([nom, edad, nota])
        elif opc == "2":
            for est in estudiantes:
                print(f"Nombre: {est[0]} | Edad: {est[1]} | Nota: {est[2]}")
        elif opc == "3":
            nom_b = input("Ingrese el nombre a buscar: ")
            hallado = [e for e in estudiantes if e[0].lower() == nom_b.lower()]
            print("Encontrado:", hallado if hallado else "No existe")
        elif opc == "4" and estudiantes:
            prom = sum(e[2] for e in estudiantes) / len(estudiantes)
            print(f"Promedio general: {prom:.2f}")
        elif opc == "5" and estudiantes:
            m = max(estudiantes, key=lambda x: x[2])
            print(f"Mayor nota: {m[0]} ({m[2]})")
        elif opc == "6" and estudiantes:
            m = min(estudiantes, key=lambda x: x[2])
            print(f"Menor nota: {m[0]} ({m[2]})")
        elif opc == "7" and estudiantes:
            aprobados = [e for e in estudiantes if e[2] >= 3.0]
            print("Aprobados:", aprobados)

#prueba 11
