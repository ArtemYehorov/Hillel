number = input("Введите любое целое число: ")
sum = 1

while len(number) > 1:
    for num in number:
        sum *= int(num)
    number = str(sum)
    sum = 1
print(number)