def verificar(dato):
    while dato == "":
        print("Error")
        dato = input("Ingrese nuevamente el dato: ")
    return dato

def convertir(valor):
    while valor.isdecimal() == False:
        print("Error. Solo numeros!")
        valor = input("Ingrese nuevamente el valor: ")
    valor = int(valor)
    return valor



######################################

alumnos = {}

while True:
    print("Menu")
    print("1 - Agregar alumno")
    print("2 - Ver alumnos")
    print("3 - Ver los cursos de un alumno")
    print("4 - Salir")
    opcion = input(">>> Ingrese una opcion: ")
    if opcion == "1":
        nombre_alumno = input("Ingrese nombre del alumno: ")
        nombre_alumno = verificar(nombre_alumno)
        cursos = input("Ingrese la cantidad de cursos: ")
        cursos = convertir(cursos)
        alumnos[nombre_alumno] = cursos
        print("Alumno agregado!")
    elif opcion == "2":
        print("Listado de alumnos y cantidad de cursos")
        for nombre in alumnos:
            cursos = alumnos[nombre]
            print(nombre + " - " + str(cursos) + " cursos")
    elif opcion == "3":
        print("Ver la cantidad de cursos de un alumno")
        buscar = input("Ingrese el nombre del alumno: ")
        buscar = verificar(buscar)
        if buscar in alumnos:
            print(buscar + " tiene " + str(alumnos.get(buscar)) + " cursos.")
        else:
            print("Alumno inexistente")
    elif opcion == "4":
        print("Gracias por usar nuestro programa")
        break
    else:
      print("Error esa opcion no existe")