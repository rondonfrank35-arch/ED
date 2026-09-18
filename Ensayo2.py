cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))

for estudiante in range(cantidad_estudiantes):
    notas = []

    print(f"\nEstudiante {estudiante + 1}")

    for i in range(3):
        nota = float(input(f"Ingrese la nota {i + 1}: "))
        notas.append(nota)

    while True:
        respuesta = input("¿Desea ingresar más notas? (si/no): ").lower()

        if respuesta == "si":
            nota = float(input("Ingrese la nota adicional: "))
            notas.append(nota)
        elif respuesta == "no":
            break
        else:
            print("Respuesta inválida. Escriba si o no.")

    promedio = sum(notas) / len(notas)

    print("Notas:", notas)
    print(f"Promedio: {promedio:.2f}")