#Basico
for i in range(150):
    print(i)


#Multiplos de cinco
for i in range(5,150,5):
    print(i)

#Contar, a la manera del Dojo
for i in range(100):
    if i % 10 == 0:
        print("Coding Dojo")
    if i % 5 == 0:
        print("Coding")
    else:
        print(i)

#Whoa. Es un gran idiota
suma = 0;

for i in range(500000):
    if i % 2 == 1:
        suma += i

print(suma)

#Cuenta regresiva de a 4
for i in range(2018,0,-4):
    print(i)

#Contador flixible
lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum,highNum+1):
    if i % mult == 0:
        print(i)

