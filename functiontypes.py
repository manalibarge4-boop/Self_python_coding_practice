#Basic Function Syntax
#Write a function to calculate and return the square of a number.
"""
def square(number):
    print(number ** 2)

square(4) 
"""
"""
def square(number):
    print(number ** 2)
result = square(4)
print(result) #This will print None because the function does not return a value 
"""
def square(number):
    return number ** 2
result = square(4)
print(result) #This will print 16 because the function returns a value

#Function with multiple parameters
#Create a function that takes two numbers as a parameter and return their sum.
def add(num1, num2):
    return num1 + num2
print(add(5, 10)) #This will print 15 because the function returns the sum of the two numbers

#Polymorphism in Functions
#polymorphism is the ability of a function to take different types of arguments and perform different operations based on the type of arguments passed to it.
#Write a function multiply that multiplies two numbers, but can also accept and multiply strings.
def multiply(p1, p2):
    return p1 * p2
print(multiply(8, 5)) #This will print 40 because the function multiplies two numbers 
print(multiply("a", 5)) #This will print aaaaa because the function multiplies a string with a number
print(multiply(5, 'a')) #This will print aaaaa

#Function Returning Multiple Values
#Create a function that returns both the area and circumference of a circle given its radius.
"""
import math
def circle_stats(radius):
    return math.pi * radius ** 2
    print("Hi") #This line will not be executed because it is after the return statement.
print(circle_stats(5)) #This will print 78.5398163399 
"""
import math
def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference
a, c = circle_stats(2) 
print("Area:", a, "Circumference:", c) 

#Default Parameter value
#Write a function that greets a user. if no name is provided, it should greet with a default name.
def greet(name):
    return "Hello, " + name + "!"
print(greet("Manali")) 

def greet1(name = "User"):
    return "Hello, " + name + "!"
print(greet1()) #This will print Hello, User! because the function uses the default parameter value.
print(greet1("Manali")) #This will print Hello, Manali! because the function uses the provided parameter value.

#Function with *args
#Write a function that takes variable number of arguments and returns their sum. 
#*args is used when we want to pass multiple arguments to a function 
# without deciding in advance how many arguments will be passed.
def sum_all(*args):
    return sum(args)
print(sum_all(1, 2)) #Print 3 
print(sum_all(1, 2, 3, 4, 5)) #Print 15
print(sum_all(1, 2, 3, 4, 5, 6, 7, 8)) #Print 36

def sum_all1(*args):
    print(*args) #Print all the arguments passed to the function
    #print(args) Print the arguments as a tuple
    return sum(args)
print(sum_all1(1, 2)) 
print(sum_all1(1, 2, 3, 4, 5)) 
print(sum_all1(1, 2, 3, 4, 5, 6, 7, 8)) 

def sum_all2(*args):
    print(args)
    for i in args:  
        print(i * 2)
    return sum(args)
print(sum_all2(1, 2, 3)) 

#Function with **kwargs
#Create a function that accepts any number of keyword arguments and prints them in the format "key: value".
#**kwargs is used when we want to pass multiple keyword arguments to a function 
#without deciding in advance how many keyword argument will be passed.
"""
def print_kwargs(name, power):
    print("Name:", name, "Power:", power)
print_kwargs(name = "Superman", power = "Flight") #Prints Name: Superman Power: Flight
print_kwargs(name = "Batman") #Prints Name: Batman Power: None because the power parameter is not provided and it has no default value.
print_kwargs(name = "Spiderman", power = "Web-slinging", enemy = "Green Goblin") #The enemy parameter is not defined in the function and it will be ignored.
"""
def print_kwargs(**kwargs):
    for key, value in kwargs.items(): #Iterate through the key-value pairs in the kwargs dictionary
        print(f"{key}: {value}") #Print the key and value in the format "key: value"
print_kwargs(name = "Spiderman", power = "web-slinging", enemy = "Green Goblin") #Prints name: Spiderman power: web-slinging enemy: Green Goblin

#Generator Function with yield
#Write a generator function that yields even numbers upto specified limit.
#return = Give the answer and finish your work.yield = Give one answer, pause, and continue your work when asked again.

def even_generator(limit):
    for i in range(2, limit + 1, 2): 
        return i  #if we use print(i) instead, this will print all even numbers upto limit, but using return will exit the function after the first even number is returned.
print(even_generator(10)) #prints 2 because the function returns the first even number and exits the function.

def even_generator1(limit):
    li = []
    for i in range(2, limit + 1, 2):
        li.append(i)
    return li 
print(even_generator1(10)) #prints [2, 4, 6, 8, 10] because the function returns a list of even numbers upto limit.

def even_generator2(limit):
    for i in range(2, limit + 1, 2):
        yield i #yield is used to return a value from a generator function and pause the function's execution, allowing it to be resumed later.
for num in even_generator2(10):
    print(num) #prints 2 4 6 8 10 because the function yields even numbers upto limit and the for loop iterates the generator function to print each even number.

#Recursive Function
#Create a Recursive function to calculate the factorial of a number.
