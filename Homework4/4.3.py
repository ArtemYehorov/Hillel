import random
my_list = [random.randint(1,20) for i in range(random.randint(3,10))]
print(my_list)

small_list = [my_list[0], my_list[2], my_list[-2]]
print(small_list)

print("Я угадаю ваше число от 1 до 100! За 5 или меньше попыток!!!")
low = 1
high = 100

while low <= high:
    guess = (low + high) // 2
    print(f'Это ваше число? {guess}')

    user_input = input("Ответьте 'Да' (+), 'Меньше' (<), или 'Больше' (>): ")

    if user_input == '+':
        print(f"Ура! Я угадал ваше число: {guess}")
        break
    elif user_input == '<':
        high = guess - 1
    elif user_input == '>':
        low = guess + 1
    else:
        print("Пожалуйста, введите '+', '<' или '>'.")

if low > high:
    print("Число не найдено. Возможно, была ошибка ввода.")