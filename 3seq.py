str_number = input("ВВедите числа через запятую: ")

numbers = str_number.split(',')

str_number = input("ВВедите числа через запятую: ")

second_numbers = str_number.split(',')

for number in numbers[:]:
    if number in second_numbers:
        numbers.remove(number)

print(numbers)