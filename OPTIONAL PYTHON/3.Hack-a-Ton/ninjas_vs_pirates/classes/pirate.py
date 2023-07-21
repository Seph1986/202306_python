class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Nombre: {self.name}\nFuerza: {self.strength}\nVelocidad: {self.speed}\nSalud: {self.health}\n")

    def attack ( self , ninja ):
        ninja.health -= self.strength
        return self
    

