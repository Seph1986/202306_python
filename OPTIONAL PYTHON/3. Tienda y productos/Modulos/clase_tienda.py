from .clase_producto import Producto

class Tienda:
    def __init__(self,nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self,nuevo_producto):
        self.productos.append(nuevo_producto)  
        return self      

    def vender_producto(self, index):
        self.productos.pop(index)
        return self

    def inflacion(self, porcentaje_aumento):
        for producto in self.productos:
            producto.actualizar_precio(porcentaje_aumento, True)
        return self

    def hacer_liquidacion(self, category, porcentaje_descuento):
        for producto in self.productos:
            if producto.categoria == category:
                producto.actualizar_precio(porcentaje_descuento,False)

        return self  
            
    def consultar_productos(self):
        for lista in self.productos:
            lista.print_info()
        return self
