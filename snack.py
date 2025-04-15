class Snack:
    contador_snacks = 0
    def __init(self, nombre='', precio = 0.0):
        Snack.contador_snacks += 1
        self.id = Snack.contador_snacks
        self.nombre = nombre
        self.precio = precio
    def __str__(self):
        return (f'ID snack: {self.id} Nombre: {self.nombre}, 
                Precio: {self.precio}')
    def escribir_snack(self):
        return f'{self.id}, | {self.nombre}, | {self.precio}\n'