
count = int(input("ВВедите количество элементов: "))

result = []

for i in range(count):
    number = int(input("ВВедите число: "))
    result.append(number)

result.sort()
print(result)
