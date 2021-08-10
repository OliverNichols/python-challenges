
def factorial(number):
    for x in range(2, number):
        number = number * x
    return number

number = int(input("Give me a number! "))
print(factorial(number))
