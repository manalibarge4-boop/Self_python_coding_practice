def multiply(a= 10, b= 20):
    return a * b

print(multiply(10, 10))
result = multiply(5, 10)
print(result)

#To print the square of a number
def square(num = 10):
    return num ** 2
print(square(3))

#Write a function that takes a string and returns the count of vowels and consonant separately.
def countVowConso(userInput):

    #define vowels
    vowels = "aeiouAEIOU"
    countVowel = 0
    countConsonant = 0

    #MANALI
    for eachChar in userInput:
        if eachChar.isalpha():
            if eachChar in vowels:
                countVowel += 1
            else:
                countConsonant += 1
    return countVowel, countConsonant

vowels, consonants = countVowConso("Manali")
print(vowels, consonants)