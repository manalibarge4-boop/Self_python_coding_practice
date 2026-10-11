"""
Write a Python program using a while loop to print numbers
 1 to 5, one per line.
"""

i = 1   #starting value
while i <= 5: #condition
    print(i)
    i = i + 1 #update the variable so the loop eventually stop

"""
A counter starts at 1. A teacher wants to display the seat numbers
 from 1 to 10. Display only the even-numbered seats.
"""
seatno = 1
while seatno <= 10:
    if seatno % 2 == 0:
        print(seatno)
    seatno = seatno + 1

"""
 A cinema has seats numbered from 1 to 20.
Using a while loop:
- If the seat number is even, print "Available"
- If the seat number is odd, print "Occupied"
"""  
seat_number = 1
while seat_number <= 20:
    if seat_number % 2 == 0:
        print(f"Seat {seat_number}: Available")
    else:
        print(f"Seat {seat_number}: Occupied")
    seat_number += 1 

"""
Ask the user to enter the number of seats n.
Then, using a while loop, print all seat numbers from 1 to n.
"""    
n = int(input("Enter the number of seats: "))
seat_num = 1
while seat_num <= n:
    print(seat_num)
    seat_num += 1
