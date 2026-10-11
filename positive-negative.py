"""
Write a Python program that accepts a number from the user and checks whether the number is:
- Positive
- Negative
- Zero
"""
num = int(input("Enter number:"))
if num == 0:
    print("Zero")
elif num > 0:
    print("Positive")
else:
    print("Negative")

"""
A temperature-monitoring system receives a temperature value.
- If the temperature is above 0, display "Above Freezing".
- If the temperature is below 0, display "Below Freezing".
- If the temperature is exactly 0, display "Freezing Point".
"""
temp = int(input("Enter temperature:"))
if temp == 0:
    print("Freezing Point")
elif temp > 0:
    print("Above Freezing")
else:
    print("Below Freezing") 

"""
A weather station classifies temperature like this:
- If temperature is below 0 → "Freezing"
- If temperature is 0 → "Freezing Point"
- If temperature is above 0 but below 20 → "Cold"
- If temperature is 20 or above → "Warm"
"""
temp2 = int(input("Enter temperature:"))
if temp2 == 0:
    print("Freezing Point")
elif temp2 < 0:
    print("Freezing")
elif temp2 > 0 and temp2 < 20:
    print("Cold")
elif temp2 >= 20:
    print("Warm") 
else:
    print("Invalid temperature") 

"""
A student's marks are entered by the user.
Classify the result:
- 90 or above → "Excellent"
- 75 to 89 → "Very Good"
- 50 to 74 → "Pass"
- Below 50 → "Fail"
"""
marks = int(input("Enter marks:"))
if marks >= 90:
    print("Excellent")
elif marks >= 75 and marks <90:
    print("Very Good")
elif marks >=50 and marks <= 74:
    print("Pass")
else: 
    print("Fail") 

"""

| Input | Expected output |
|---:|---|
| `95` | `"Excellent"` |
| `82` | `"Very Good"` |
| `67` | `"Pass"` |
| `45` | `"Fail"` |
| `90` | `"Excellent"` |
| `75` | `"Very Good"` |
| `50` | `"Pass"` |               
"""

def grade(marks):
    if marks >= 90:
        return "Excellent"
    elif marks >= 75 and marks < 90:
        return "Very Good"
    elif marks >= 50 and marks < 75:
        return "Pass"
    else:
        return "Fail" 

"""
A competition awards a result based on a participant's score:
- A score of 90 or more → "Gold"
- A score from 75 up to but not including 90 → "Silver"
- A score from 50 up to but not including 75 → "Bronze"
- Any score below 50 → "Not Qualified"
95 → Gold
90 → Gold
89 → Silver
75 → Silver
74 → Bronze
50 → Bronze
49 → Not Qualified
10 → Not Qualified
"""
def classify_score(score):
    if score >= 90:
        return "Gold"
    elif score >= 75 and score < 90:
        return "Silver" 
    elif score >= 50 and score < 75:
        return "Bronze" 
    else:
        return "Not Qualified"    