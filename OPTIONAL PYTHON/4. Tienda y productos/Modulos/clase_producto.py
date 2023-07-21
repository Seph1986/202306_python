class Producto:
    def __init__(self,nombre,precio,categoria,id):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.id = id

    def actualizar_precio(self,cambio_porcentaje, está_elevado):
        
        if está_elevado == True:
            temp = self.precio
            self.precio *= (1 + (cambio_porcentaje / 100))
            int(self.precio)
            print(f"Se actualizo el precio de {temp} a {self.precio}")
            return self
        else:
            temp = self.precio
            self.precio *= (1 - (cambio_porcentaje / 100))
            int(self.precio)
            print(f"Descuento realializado, precio paso de {temp} a {self.precio}")
            return self

    def print_info(self):
        print(f"*Nombre:    {self.nombre}\n*Categoria: {self.categoria}\n*Precio:    {self.precio}")
        print("-*"*23)
        return self