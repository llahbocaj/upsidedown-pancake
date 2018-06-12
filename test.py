"""

def square(number):
    return number * number
"""

def numVowels(string):
    string = string.lower()
    count = 0
    for i in range(len(string)):
        if isVowel(string[i]):
            count += 1
    return count

def isVowel(letter):
    if letter == "a" or letter == "e" or letter == "i" \
    or letter == "o" or letter == "u":
        return True
    else:
        return False

"""
print("Enter a number: ")
num = int(input())
numSquared = square(num)
print(str(num) + " squared = " + str(numSquared))
"""
print("Enter a string: ")
input = input()
print("There are " + str(numVowels(input)) + " vowels in the string " + str(input))
