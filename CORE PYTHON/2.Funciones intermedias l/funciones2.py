# 1 Actualizar valores en diccionarios y listas

x = [ [5,2,3], [10,8,9] ] 

estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}

z = [ {'x': 10, 'y': 20} ]


# ========= resultados del 1ro =============
x[1][0] = 15
print(x)

estudiantes[0]['last_name'] = 'Bryant'
print(estudiantes)

directorio_deportes['fútbol'][0] = 'Andrés'
print(directorio_deportes)

z[0]['y'] = 30
print(z)



#2 Iterar a través de una lista de diccionarios

estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


def iterateDictionary(elm):

    for i in elm:
        print(f"first_name - {i['first_name']}, last_name - {i['last_name']}")

iterateDictionary(estudiantes) 

#--------------------------------------------------------------------- #

#3 Obtener valores de una lista de diccionario


def iterateDictionary2(key_name, some_list):
    if key_name == "name":
        for i in some_list:
            print(i['first_name'])
    if key_name == "last_name":
        for i in some_list:
            print(i['last_name'])

iterateDictionary2("last_name",estudiantes)

#--------------------------------------------------------------------- #

# 4 Iterar a traves de un diccionario con valores de lista

dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dict):

    for i in dict:
        print(len(dict[i]),i.upper())
        for j in dict[i]:
            print (j)
   
            
printInfo(dojo)
