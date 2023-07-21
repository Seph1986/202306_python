from classes.ninja import Ninja
from classes.pirate import Pirate
import random

dice = random.randint(1,6)

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

def tirar_dado():
    if lambda dice : dice > 6:
        print('hello')
    else:
        print('probando')

tirar_dado()

# jack_sparrow.show_stats()
# michelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()