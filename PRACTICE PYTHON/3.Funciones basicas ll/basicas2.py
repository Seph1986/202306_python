# 1. Cuenta regresiva

def count_down(elm):
    lst = []
    for i in range(0,elm+1):
        lst.append(i)
    
    lst.reverse()
    return lst 

print(count_down(5))

# 2. Imprimir y devolver

def imp_dev(elm):
    val1 = elm[0]
    val2 = elm[1]

    print(val1)
    return val2

print(imp_dev([10,20]))

# 3. Primero mas longitud

def prm_mas_lng(elm):
    val1 = elm[0]

    suma = val1 + len(elm)
    return suma

print(prm_mas_lng([1,2,3,4,5]))

# 4. Valores mayores que el segundo

def val_may_2(elm):

    if len(elm) >= 2:
        val_2 = elm.pop(1)
        new_list = []

        for i in elm:
            if i > val_2:
                new_list.append(i)

        print(len(new_list))
        return new_list
    
    else:
        return False

print(val_may_2([5,1]))

# 5. Esta longitud, ese valor

def long_valor(num1,num2):
    lst = []

    for i in range(num1):
        lst.append(num2)

    print(lst)
    return lst

long_valor(10,8)