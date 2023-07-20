class Underscore:
   
    def map(self, iterable, callback):
        lista = []

        for i in iterable:
            devolver = callback(i)
            lista.append(devolver)

        return lista


    def find(self, iterable, callback):
        for i in iterable:
            if callback(i) == True:
                return i
                
        

    def filter(self, iterable, callback):
        array = []

        for i in iterable:
            if callback(i) == True:
                array.append(i)

        return array


    def reject(self, iterable, callback):
        array = []

        for i in iterable:
            if callback(i) == False:
                array.append(i)

        return array




_ = Underscore()


maping = _.map([1,2,3], lambda x: x*2)
bigger_than_4 = _.find([1,2,3,4,5,6], lambda x: x>4)
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
not_evens= _.reject([1,2,3,4,5,6], lambda x: x % 2==0)

print(maping)
print(bigger_than_4)
print(evens)
print(not_evens)