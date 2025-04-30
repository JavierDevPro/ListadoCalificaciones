#Declaracion de una lista vacia para las calificaciones en ingle
gradesTemp = []
grades = []
answersList = ["si","s","no","n"]
referenceValue = 0
validedState = False
sumGrades = 0
iterator = 0
countEquals = 0
countGreater = 0

#Ciclo para validar que el valor entregado como calificacion sea evaluable es decir sea un numero y si esta dentro del rango aceptable (0-100)
def agregarDato(var, phase):
    while True:
        try:
            match phase:
                case 1:                    
                    value = float(input("Ingrese la calificacion del estudiante: "))                    
                case 2:
                    print("--" * 55)
                    value = float(input("Ingresa una calificacion minima para evaluar la(s) calificacion(es): "))
                case 3:
                    print("--" * 55)
                    print("Evaluemos las calificaciones especificas!")
                    value = float(input("Ingresa una calificacion para determinar cuantas son iguales y cuantas son mayores: "))
            
            if value >= 0 and value <= 100:
                match phase:
                    case 1:
                        var.append(value)
                        break
                    case 2 | 3:
                        var = value
                        return var
                    # case 3:
                    #     var = value
                    #     return var
            elif value < 0 or value > 100:
                print("--" * 55)
                print(f"ERROR: La calificacion ({value}) esta por fuera del rango (0-100).")
        except:
            print("--" * 55)
            print("ERROR: La calificacion no debe contener letras ni simbolos especiales.")

#Llamado de la funcion para agregar el primer dato
agregarDato(grades,1)

#Preguntar si se va a implementar mas calificaciones ademas 
#se evalua si se tiene la respuesta en la lista de respuestas
print("--" * 55)
print("Ingresaras nuevas calificaciones? Si/No: ")
answer = input(" ")
while answer.lower() not in answersList:
    print("--" * 55)
    print("Respuesta invalida, Ingresaras nuevas calificaciones? Si/No: ")
    answer = input(" ")

#Ejecutar solo si la respuesta es si
if (answer.lower() == "si" or answer.lower() == "s"):
    #Ciclo de ingreso y validacion de las calificaciones
    while True:
        errorValue = True
        print("--" * 55)
        gradesTemp = input("Ingresa las calificaciones de los estudiantes separadas por (,): ").split(",")
        try:#evalua si hay un error
            #se recorre la lista temporal y se evalua que no existan errores.
            for grade in gradesTemp:
                datoErrado = grade#se almacena el valor de la posicion del recorrido actual de la lista temporal para expresarla como el causante del error
                if 0 <= float(grade) <= 100:
                    grades.append(float(grade))
                else:
                    print("--" * 55)
                    print(f"ERROR: uno de los valores ingresados ({datoErrado}) esta por fuera del rango valido (0-100).")
                    print("Corrige desde tu ultima posicion ingresada.")
                    print(f">>{grades}<< ({grades[-1]}).")#se imprime la ultima posicion valida del programa
                    errorValue = False
                    break
            if errorValue == True:
                break
        except:
            print("--" * 55)
            print(f"ERROR: la calificacion ({datoErrado}) contiene caracteres por ello es invalida.")
            print("Corrige desde tu ultima posicion ingresada.")
            print(f">>{grades}<< ({grades[-1]}).")

referenceValue = agregarDato(referenceValue,2)

for grade in grades:
    sumGrades += grade
averageGrade = sumGrades / len(grades)
if (averageGrade >= referenceValue):
    validedState = True

if (validedState== True):
    print(f"Aprobado! promedio: {averageGrade}. \nnota minima para aprobar: {referenceValue}")
else:
    print(f"Reprobado! promedio: {averageGrade}. \nnota minima para aprobar: {referenceValue}")
#Reutilizamos el referenceValue para una nueva evaluacion
referenceValue = agregarDato(referenceValue,3)

#Ciclo while para encontrar numeros mayores que el numero referencia
while iterator < len(grades):
    if (grades[iterator] > referenceValue):
        countGreater += 1
    iterator+= 1
print("Dentro de la lista: ",grades)
print(f"En total hay ({countGreater}) calificaciones mayores a {referenceValue}")

#Ciclo for para encontrar valores iguales
for i in grades:
    if referenceValue == i:
        countEquals += countEquals

print(f"En total hay ({countEquals}) identicos al valor evaluado {referenceValue}")