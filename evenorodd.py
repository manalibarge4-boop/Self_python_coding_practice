num = int(input("enter number: "))
if num % 2 == 0:
    print("number is even")
elif num % 2 != 0:
    print("number is odd")
else:
    print("number is not defined")   

"""
A program accepts an integer representing the number of items 
purchased by a customer.
- If the number of items can be divided into two equal groups 
with no item left over, print "Equal Groups".
- Otherwise, print "Unequal Groups".
"""
number = int(input("Enter the number of items purchased:"))
if number % 2 == 0:
    print("Equal Groups")
else:
    print("Unequal Groups")

"""
A shop gives a special discount based on the number of items purchased.
- If the customer purchases an even number of items, print "Discount Applied".
- If the customer purchases an odd number of items, print "No Discount".
- However, if the customer purchases 0 items, print "Invalid Purchase".    
"""
num = int(input("Enter the number of i tems purchased: "))
if num == 0:
    print("Invalid purchase")
elif num % 2 == 0:
    print("Discount Applied")
else:
    print("No Discount")   

"""
def check_number(num):
    # write your code here 
| Test case | Expected |
|---|---|
| `5` | `"Odd"` |
| `8` | `"Even"` |
| `13` | `"Odd"` |
| `20` | `"Even"` |
| `0` | `"Even"` |
"""
def check_number(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"  

"""
A shop divides purchased items into two equal groups.
- If all items can be divided equally into two groups, return "Equal Groups".
- Otherwise, return "Unequal Groups".
- If items is 0, return "Invalid Purchase".
Test cases:
8  → Equal Groups
7  → Unequal Groups
0  → Invalid Purchase
14 → Equal Groups
9  → Unequal Groups
"""
def check_purchase(items):
    if items == 0:
        return "Invalid Purchase"
    elif items % 2 == 0:
        return "Equal Groups"
    else:
        return "Unequal Groups"
