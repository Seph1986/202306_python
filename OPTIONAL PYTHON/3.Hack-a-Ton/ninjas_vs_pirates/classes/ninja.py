class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Nombre: {self.name}\nFuerza: {self.strength}\nVelocidad: {self.speed}\nSalud: {self.health}\n")

    def attack( self , pirate ):
        pirate.health -= self.strength
        return self
    
 