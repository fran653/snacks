import os
class Servicio:
    NOMBRE_ARCHIVO = 'snacks.txt'
    def __init__(self):
        self.snacks = []
        if os.path.isfile(self.NOMBRE_ARCHIVO):
            self.cargar_snacks()
        else:
            self.cargar_snacks_iniciales()
            
    def cargar_snacks(self):
        print('Cargando snacks desde el archivo...')
        snacks = []
        try:
            with open(self.NOMBRE_ARCHIVO, 'r') as archivo:
                for linea in archivo:
                    #se separa por cada coma, si las líneas viene 'Papas', 70.0
                    id, nombre, precio = linea.strip().split(',') #estamos desempaquetando en estas 3 var
                    snack = Snack(nombre, float(precio))
                    snacks.append(snack)
        except Exception as e:
            print(f'Error al abrir el archivo de snacks, error tipo {e}')
        return snacks
                
    def cargar_snacks_iniciales(self):
        print('Cargando snacks iniciales...')
        snacks_iniciales = [('patatas de gordo', 10.5),
        ('chocolate de morsa', 20.5),
        ('gusanitos de la muerte', 30.5)
        ('chicles de la suerte', 40.5)
        ('vergas de goma', 50.5)
        ]
        self.snacks.extend(snacks_iniciales)
        self.guardar_snacks_archivo(snacks_iniciales)
        
    def guardar_snacks_archivo(self, snacks):
        try:
            with open(self.NOMBRE_ARCHIVO, 'a') as archivo:
                for snack in snacks:
                    archivo.write(f' {snack.escribir_snack()}\n')
        except Exception as e:
            print(f'Error al guardar los snacks en el archivo: {e}')
    def agregar_snack(self,snack):
        self.snacks.append(snack)
        self.guardar_snacks_archivo([snack])
    def mostrar_snacks(self):
        print('---En el inventario hay los siguientes snacks---')
        for snack in self.snacks:
            print(snack)
    def get_snacks(self):
        return self.snacks
    
        