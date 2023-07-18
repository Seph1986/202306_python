class CuentaBancaria:


    def __init__(self,balance = 0,tasa_interes = 0.01):
        self.balance = balance
        self.tasa_interes = tasa_interes

    def deposito(self,monto):
        self.balance += monto
        print(f"Deposito de {monto}$ con exito")
        print('*-'*23)

        return self

    def retiro(self,monto):
        if monto > self.balance:
            self.balance -= 5
            print("Fondos insuficientes: cobrando una tarifa de 5$")
            print('*-'*23)

            return self

        else:
            self.balance -= monto
            print(f"Retiro de {monto}$ con exito")
            print('*-'*23)

            return self

    def mostrar_info_cuenta(self):
        print('--'*23)
        print(f"Balance: {self.balance}$")
        print('--'*23)

        return self
    
    def generar_interes(self):
        if self.balance > 0:
            valor1 = self.balance
            self. balance += self.balance * self.tasa_interes
            print(f"Se generaron intereses con el valor de {valor1 * self.tasa_interes}$")
            print('*-'*23)

            return self

        else:
            print("Saldo insuficiente para operacion")
            print('*-'*23)
            
            return self


class Usuario:

    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.cuenta = {'cuenta1' : CuentaBancaria( balance = 0, tasa_interes = 0.02),'cuenta2' : CuentaBancaria( balance = 0, tasa_interes = 0.02)}

    def hacer_deposito(self, monto, nroCuenta):
        self.cuenta[nroCuenta].deposito(monto)

    def hacer_retiro(self,monto, nroCuenta):
        self.cuenta[nroCuenta].retiro(monto)

    def mostar_balance_usuario(self, nroCuenta):
        self.cuenta[nroCuenta].mostrar_info_cuenta()

usuario1 = Usuario("Jose","jw@gmail.com")

usuario1.hacer_deposito(2000, 'cuenta1')
usuario1.hacer_deposito(3000, 'cuenta2')

usuario1.mostar_balance_usuario('cuenta1')
usuario1.mostar_balance_usuario('cuenta2')






        