number = int(input("Give me a number! "))
result = ""
for i in range(1, number + 1):
    for j in range(1, number + 1):
        result = result + f"{i*j}\t"
    result = result + "\n"
    
print(result) 
