num1 = 42 #variable declaration, initialize int number
num2 = 2.3 #variable declaration, initialize float number
boolean = True #variable declaration, initialize boolean
string = 'Hello World' #variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, initialize int tuple
print(type(fruit)) #print, data type, tuple
print(pizza_toppings[1]) #print, access value 1
pizza_toppings.append('Mushrooms') #list, add value
print(person['name']) #print, dictionary, acess value
person['name'] = 'George' #dictionary, change value
person['eye_color'] = 'blue' #dictionary, add key, add value
print(fruit[2]) #print, tuple, access value

if num1 > 45:           #conditional, if
    print("It's greater")
else:                    #conditional, else
    print("It's lower") 

if len(string) < 5:           #conditional, if
    print("It's a short word!")
elif len(string) > 15:          #conditional, elif
    print("It's a long word!") 
else:                           #conditional, else
    print("Just right!")

for x in range(5): #for loop, stop 5
    print(x)
for x in range(2,5):    #for loop, start 2, stop 5
    print(x)
for x in range(2,10,3): #for loop, start 2, stop 10, increment 3
    print(x)
x = 0
while(x < 5): #while loop, 
    print(x)
    x += 1 #increment

pizza_toppings.pop() #list, delete value
pizza_toppings.pop(1) #list, delete value on position 1

print(person) #print {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False, 'eye_color' = 'blue'} 
person.pop('eye_color') #list, delete value "eye_color"
print(person) #print {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} 

for topping in pizza_toppings: #for loop in pizza_toppings
    if topping == 'Pepperoni':    
        continue
    print('After 1st if statement')
    if topping == 'Olives':  
        break                       #only prints : After 1st if statement

def print_hello_ten_times():       #function declaration
    for num in range(10):       #for loop, stop(10)
        print('Hello')          

print_hello_ten_times()     #calling function, print Hello 10 times

def print_hello_x_times(x): #function declaration with 1 argument
    for num in range(x):    #for loop stops on argument
        print('Hello')      

print_hello_x_times(4)  #imprime Hello 4 veces

def print_hello_x_or_ten_times(x = 10): #declaracion de funcion con su valor predeterminado
    for num in range(x):    #for loop con el argumento
        print('Hello') 

print_hello_x_or_ten_times()   #imprime hello 10 veces
print_hello_x_or_ten_times(4)   #imprime hello 4 veces


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)