from servicio import Servicio
from snack import Snack
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
        snacks = self.servicio_snacks.get_snacks()
        snack = next((snack for snack in snacks if snack.id == id_snack), None)
        if snack:
            self.productos.append(snack)
            print(f'Snack encontrado: {snack}')
        else:
            print(f'Snack con ID {id_snack} no encontrado')
    def mostrar_ticket(self):
        if not self.productos:
            print('No hay productos en el ticket')
            return
        total = sum(snack.precio for snack in self.productos)   
        print('---Ticket de compra---')
        for producto in self.productos:
            print(f'\t- {producto.nombre} - ${producto.precio:.2f}')
        print(f'\t Total: ${total:.2f}')   
    def agregar_snack(self):
        nombre = input('Ingrese el nombre del snack: ')
        precio = float(input('Ingrese el precio del snack: '))
        nuevo_snack = Snack(nombre, precio)
        self.servicio_snacks.agregar_snack(nuevo_snack)
        print(f'Snack {nuevo_snack.nombre} agregado con éxito')  
        
#programa principal, que inicia toda la aplicación       
if __name__ == '__main__':
    maquina = MaquinaSnacks()
    maquina.maquina_snacks()