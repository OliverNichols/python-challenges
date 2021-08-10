def seven_five(start, stop):
    result = []
    for i in range(start, stop+1):
        if i % 7 == 0 and i % 5 != 0:
            result.append(str(i))
    return ",".join(result)

print(seven_five(2000, 3200))