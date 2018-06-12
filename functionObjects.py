def square(number):
    return number * number

num = 2
squareNumber = square(num)
print(squareNumber)

numbers = [1,2,3,4]

numbersSquared = list(map(square, numbers))
print(numbersSquared)
