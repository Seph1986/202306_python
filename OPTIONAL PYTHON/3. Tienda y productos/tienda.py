from Modulos.clase_tienda import Tienda
from Modulos.clase_producto import Producto


des_Apolo = Tienda("Despensa Apolo")

tomate = Producto("Tomate",7000,"Verdura")
lechuga = Producto("Lechuga",3000,"Verdura")
morron = Producto("Morron",16000,"Verdura")
leche = Producto('Leche',7000,'Lacteo')
queso = Producto("Queso",18000,'Lacteo')
crema = Producto('Crema de leche', 9000,'Lacteo')

des_Apolo.agregar_producto(tomate).agregar_producto(lechuga).agregar_producto(morron).agregar_producto(leche).agregar_producto(queso).agregar_producto(crema)


des_Apolo.consultar_productos().vender_producto(0).consultar_productos() #quitamos tomate de la lista de productos

des_Apolo.inflacion(5).consultar_productos() #actualizar los precios a la inflacion

des_Apolo.hacer_liquidacion('Verdura',15).consultar_productos() #descuento en base a categoria


