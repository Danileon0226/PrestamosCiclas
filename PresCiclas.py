class Cicla:
    def __init__(self, id_cicla, origen, destino):
        self.id_cicla = id_cicla
        self.origen = origen
        self.destino = destino

class Usuario:
    def __init__(self, nombre, numero_tarjeta):
        self.nombre = nombre
        self.numero_tarjeta = numero_tarjeta
        self.prestamos = []

    def tomar_cicla(self, id_cicla, origen, destino):
        prestamo = Cicla(id_cicla, origen, destino)
        self.prestamos.append(prestamo)

class SistemaPrestamos:
    def __init__(self):
        self.usuarios = []
        self.prestamos = []

    def registrar_usuario(self, nombre, numero_tarjeta):
        usuario = Usuario(nombre, numero_tarjeta)
        self.usuarios.append(usuario)

    def listar_usuarios(self):
        for usuario in self.usuarios:
            print(f"Nombre: {usuario.nombre}, Número de Tarjeta: {usuario.numero_tarjeta}")

    def listar_prestamos(self):
        for prestamo in self.prestamos:
            print(f"ID de Cicla: {prestamo.id_cicla}, Origen: {prestamo.origen}, Destino: {prestamo.destino}")



sistema_prestamos = SistemaPrestamos()

while True:
    print("\nMenú de Opciones:")
    print("1. Registrar Usuario")
    print("2. Tomar Cicla")
    print("3. Listar Usuarios")
    print("4. Listar Préstamos")
    print("5. Salir")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del usuario: ")
        numero_tarjeta = input("Ingrese el número de tarjeta: ")
        sistema_prestamos.registrar_usuario(nombre, numero_tarjeta)
        print("Usuario registrado exitosamente.")

    elif opcion == "2":
        if not sistema_prestamos.usuarios:
            print("No hay usuarios registrados. Registre un usuario primero.")
        else:
            print("Usuarios registrados:")
            sistema_prestamos.listar_usuarios()
            usuario_index = int(input("Elija el número de usuario: "))
            if usuario_index < 1 or usuario_index > len(sistema_prestamos.usuarios):
                print("Número de usuario inválido.")
            else:
                id_cicla = int(input("Ingrese el ID de la cicla: "))
                origen = input("Ingrese el origen del viaje: ")
                destino = input("Ingrese el destino del viaje: ")
                sistema_prestamos.usuarios[usuario_index - 1].tomar_cicla(id_cicla, origen, destino)
                sistema_prestamos.prestamos.append(Cicla(id_cicla, origen, destino))
                print("Cicla tomada exitosamente.")

    elif opcion == "3":
        print("\nListado de Usuarios:")
        sistema_prestamos.listar_usuarios()

    elif opcion == "4":
        print("\nListado de Préstamos:")
        sistema_prestamos.listar_prestamos()

    elif opcion == "5":
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, elija una opción válida del menú.")
