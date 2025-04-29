#Declaracion de una lista vacia para las calificaciones en ingle
gradesTemp = []
grades = []

#ciclo de ingreso y validacion de las calificaciones
while True:
    errorValue = True
    print("--" * 55)
    gradesTemp = input("Ingresa las calificaciones de los estudiantes separadas por (,): ").split(",")
    try:
        for grade in gradesTemp:
            datoErrado = grade
            if 0 <= float(grade) <= 100:
                grades.append(float(grade))
            else:
                print("--" * 55)
                print(f"ERROR: uno de los valores ingresados ({datoErrado}) esta por fuera del rango valido (0-100).")
                print("Corrige desde tu ultima posicion ingresada.")
                print(f">>{grades}<< ({grades[-1]}).")
                errorValue = False
                break
        if errorValue == True:
            break
    except:
        print("--" * 55)
        print(f"ERROR: la calificacion ({datoErrado}) contiene caracteres por ello es invalida.")
        print("Corrige desde tu ultima posicion ingresada.")
        print(f">>{grades}<< ({grades[-1]}).")