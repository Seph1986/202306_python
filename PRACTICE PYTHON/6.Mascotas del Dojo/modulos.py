class Ninja:

    def __init__(self,nombre,apellido,premio,comida_mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.mascotas = Gato('Chucho', 'Perro', 'Galletas',15,15)
        self.premio = premio
        self.comida_mascota = comida_mascota

    def caminar(self):
        self.mascotas.jugar()
        print(f"Paseando {self.mascotas.name}")
    
    def alimentar(self):
        self.mascotas.comer()
        print(f"Alimentando a {self.mascotas.name}")
    
    def bañar(self):
        self.mascotas.noise()
        print(f"Bañanando a {self.mascotas.name}")

class Mascota:

    def __init__(self,name,tipo,golosinas,salud,energia, sonido):
        self.name = name
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud = salud
        self.energia = energia
        self.sonido = sonido

    def dormir(self):
        self.energia += 25
        return self

    def comer(self):    
        self.energia += 5
        self.salud += 10
        return self

    def jugar(self):
        self.salud += 5

    def noise(self):
        print(self.sonido)

class Perro(Mascota):
    def __init__(self, nombre, tipo, golosinas, salud, energia):
        super().__init__(nombre,tipo,golosinas,salud,energia,"Burf Burf")
    

class Gato(Mascota):
    def __init__(self, nombre, tipo, golosinas, salud, energia):
        super().__init__(nombre,tipo,golosinas,salud,energia,"Miau Miau")