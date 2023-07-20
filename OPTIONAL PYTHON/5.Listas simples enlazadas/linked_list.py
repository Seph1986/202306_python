class Lista:
    def __init__(self):
        self.head = None

    def agregar_adelante(self,val):
        nuevo_nodo = Nodo(val)
        cabeza_actual = self.head
        nuevo_nodo.next = cabeza_actual
        self.head = nuevo_nodo

        return self
    
    def agregar_atras(self,val):
        if (self.head == None):
            self.agregar_adelante(val)
            return self
            
        nuevo_nodo = Nodo(val)
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = nuevo_nodo

        return self

    def recorrer_lista(self):
        runner = self.head
        while(runner != None):
            print(runner.valor)

            runner = runner.next
        
        return self


class Nodo:
    
    def __init__(self,val):
        self.valor = val
        self.next = None


mi_lista = Lista()

mi_lista.agregar_adelante('Probando').agregar_atras(123).agregar_atras('ajjaja').recorrer_lista()