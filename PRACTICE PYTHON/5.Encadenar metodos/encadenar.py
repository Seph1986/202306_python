class Usuario:
    nombre_banco = "Coding Bank"

    def __init__(self,nombre,email,saldo_cuenta):
        self.nombre = nombre
        self.email = email
        self.saldo_cuenta = saldo_cuenta

    def hacer_deposito(self,monto):
        self.saldo_cuenta += monto
        print(f'Se ha depositado con exito: {monto}')
        print(f'Su saldo disponible es de: {self.saldo_cuenta}')
        print('-'*40)

        return self

    def hacer_retiro(self,monto):
        self.saldo_cuenta -= monto
        print(f'Se ha retirado con exito: {monto}')
        print(f'Su saldo disponible es de: {self.saldo_cuenta}')
        print('-'*40)

        return self

    def mostrar_balance_usuario(self):
        print(f"El saldo de su cuenta es de: {self.saldo_cuenta}")
        print('-'*40)

        return self

    def transfer_dinero(self, otra_cuenta,monto):
        self.saldo_cuenta -= monto
        otra_cuenta.saldo_cuenta += monto
        print(f'Transferencia a {otra_cuenta.nombre} de {monto} con exito')
        print('*-'*20)

        return self


usuario1 = Usuario("Micaela","schmickler@gmail.com",5000)
usuario2 = Usuario("Jose","weber@gmail.com",5000)
usuario3 = Usuario("Enzo","sch@gmail.com",5000)

usuario1.hacer_deposito(200).hacer_deposito(100).hacer_retiro(500).mostrar_balance_usuario()

usuario2.hacer_deposito(300).hacer_deposito(200).hacer_retiro(600).hacer_retiro(100).mostrar_balance_usuario()

usuario3.hacer_deposito(600).hacer_retiro(100).hacer_retiro(100).mostrar_balance_usuario()



usuario1.transfer_dinero(usuario2, 600)

usuario1.mostrar_balance_usuario()
usuario2.mostrar_balance_usuario()
