from servicio import Servicio
class MaquinaSnacks:
    def __init__(self):
        self.servicio_snacks = Servicio()
        self.productos = []
    
    def maquina_snacks(self):
        salir = False
        print('---Bienvenido a la máquina de snacks---')
        self.servicio_snacks.mostrar_snacks()
        while not salir:
            try:
                opcion = self.mostrar_menu()
                salir = self.ejecutar_opcion(opcion)
            except Exception as e:
                print(f'Ocurrió un error: {e}')
    def mostrar_menu(self):
        print('1. Comprar snack')
        print('2. Mostrar ticket')
        print('3. Agregar nuevo snack')
        print('4. Inventario de snacks')
        print('5. Salir')
        return int(input('Seleccione una opción: '))
    def ejecutar_opcion(self,opcion):
        if opcion == 1:
            self.comprar_snack()
        elif opcion == 2:
            self.mostrar_ticket()
        elif opcion == 3:
            self.agregar_snack()
        elif opcion == 4:
            self.servicio_snacks.mostrar_snacks()
        elif opcion == 5:
            print('Gracias por usar la máquina de snacks')
            return True
        else:
            print(f'Opción {opcion} no válida, intente nuevamente')    
    
    def comprar_snack(self):
        id_snack = int(input('Ingrese el ID del snack que desea comprar: '))
        next()
        self.servicio_snacks.get_snacks() 
    
        