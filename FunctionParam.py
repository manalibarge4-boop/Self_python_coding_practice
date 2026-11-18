"""
#Function Definition with parameters
def average(a, b):
    averageValue = (a + b) / 2
    print(averageValue)

#Function calling with Arguments
average(5, 10)
average(7, 10)
average(80, 98)
average(2, 4)


def average(a = 10, b = 20):
    averageValue = (a + b) / 2
    print(averageValue)

average(5, 10)
average(7, 10)
average(80, 98)
average()  #default function calling with default values.
"""

def show_age(name = "Atharva", age = 24):
    print(f"{name} is {age} years old.")
show_age("Manali", 23)
show_age()