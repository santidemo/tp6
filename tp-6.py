class Alumno:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = ""
        self.notas = []
        self.faltas = 0
        self.amonestaciones = 0

    def ingrese_nota(self, nueva_nota):
        self.notas.append(float(nueva_nota))

    def asignar_falta(self):
        self.faltas += 1

    def asignar_amonestacion(self):
        self.amonestaciones += 1

    def cambiar_domicilio(self, nueva_direccion):
        self.direccion = nueva_direccion

    def obtener_promedio(self):
        if not self.notas:
            return "No hay notas registradas."
        cantidad_notas = len(self.notas)
        suma_notas = sum(self.notas)
        return suma_notas / cantidad_notas if cantidad_notas else 0


def ingresar_datos_alumno():
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input("Ingrese el apellido del alumno: ")
    dni = input("Ingrese el DNI del alumno: ")

    alumno_nuevo = Alumno(nombre, apellido, dni)

    direccion = input("Ingrese la dirección del alumno: ")
    alumno_nuevo.cambiar_domicilio(direccion)

    notas = input("Ingrese las notas del alumno separadas por comas (ejemplo: 7,8,9): ")
    notas_lista = notas.split(',')
    for nota in notas_lista:
        alumno_nuevo.ingrese_nota()

    return alumno_nuevo


def modificar_datos_alumno(alumno):
    print(f"\nDatos actuales del alumno: {alumno}")
    print(f"Dirección actual: {alumno.direccion}")
    print(f"Notas actuales: {alumno.notas}")
    
    opcion = input("\nSeleccione una opción para modificar:\n"
                   "1. Modificar dirección\n"
                   "2. Modificar notas\n"
                   "3. Volver al menú principal\n"
                   "Ingrese el número de la opción: ")

    if opcion == "1":
        nueva_direccion = input("Ingrese la nueva dirección: ")
        alumno.cambiar_domicilio(nueva_direccion)
        print("Dirección modificada con éxito.")
    elif opcion == "2":
        nuevas_notas = input("Ingrese las nuevas notas separadas por comas: ")
        alumno.notas = []
        for nota in nuevas_notas.split(','):
            alumno.ingrese_nota(nota.strip())
        print("Notas modificadas con éxito.")
    elif opcion == "3":
        return
    else:
        print("Opción no válida. Intente nuevamente.")


alumno1 = ingresar_datos_alumno()

alumno1.asignar_falta()
alumno1.asignar_amonestacion()


print(alumno1)
print(f"Dirección: {alumno1.direccion}")
print(f"Faltas: {alumno1.faltas}")
print(f"Amonestaciones: {alumno1.amonestaciones}")
print(f"Promedio de notas: {alumno1.obtener_promedio()}")


modificar_datos_alumno(alumno1)


print("\nInformación actualizada del alumno:")
print(alumno1)
print(f"Dirección: {alumno1.direccion}")
print(f"Faltas: {alumno1.faltas}")
print(f"Amonestaciones: {alumno1.amonestaciones}")
print(f"Promedio de notas: {alumno1.obtener_promedio()}")

