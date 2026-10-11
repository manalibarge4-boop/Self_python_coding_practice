"""
Write a Python program that prints the numbers 1 to 10, one number on each line.
"""
for i in range(1, 11):
    print(i)

"""
A security system needs to display the valid locker numbers in a building.
The lockers are numbered from 1 through 10.
Write a Python program that displays each locker number on a separate line.
"""
for locker_number in range(1, 11):
    print(locker_number)    

"""
A school has 20 students, numbered from 1 to 20.
The teacher wants to display only the students with even roll numbers.
"""
for students in range(1, 21):
    if students % 2 == 0:
        print(students)

"""
Ask the user to enter a number n.
Then print all the numbers from 1 to n.
"""
n = int(input("Enter a number: "))
for i in range(1, n+1):
    print(i) 
       
"""
It should return a list containing all numbers from 1 to n.
Test cases
Input: 5
Output: [1, 2, 3, 4, 5]

Input: 3
Output: [1, 2, 3]

Input: 1
Output: [1]
"""

def print_numbers(n):
    numbers = [] #first created an empty list to store the numbers
    for i in range(1, n + 1): 
        numbers.append(i) #need to add that number to the list
    return numbers #return the list of numbers

"""
A school has n students standing in a line. The teacher wants 
to create a list containing only the odd-numbered positions 
from 1 to n.
n = 10 → [1, 3, 5, 7, 9]
n = 6  → [1, 3, 5]
n = 1  → [1]
"""
def odd_positions(n):
    odd_list = [] #first created an empty list to store the odd numbers
    for i in range(1, n + 1):
        if i % 2 != 0: 
            odd_list.append(i) #need to add that number to the list
    return odd_list        


