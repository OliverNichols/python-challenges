def times_tables(number):
    result = ""
    for i in range(1, number + 1):
        for j in range(1, number + 1):
            result = result + f"{i*j}\t"
        result = result + "\n"
        
    return result

number = int(input("Give me a number! "))
print(times_tables(number))
