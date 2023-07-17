class CuentaBancaria:

    cuentas = []

    def __init__(self,balance = 0,tasa_interes = 0.01):
        self.balance = balance
        self.tasa_interes = tasa_interes
        CuentaBancaria.cuentas.append(self)

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



cuenta1 = CuentaBancaria()
cuenta2 = CuentaBancaria()


cuenta1.deposito(700).deposito(500).deposito(1500).retiro(300).generar_interes().mostrar_info_cuenta()
cuenta2.deposito(200).deposito(400).retiro(100).retiro(100).retiro(100).retiro(100).mostrar_info_cuenta()
