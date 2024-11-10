while True:
    first_num = float(input("Введите первое число:"))
    operation = str(input("Введите нужную операцию (+ , - , / , *):"))
    second_num = float(input("Введите второе число:"))

    if operation == "-":
        print(first_num - second_num)
    elif operation == "+":
        print(first_num + second_num)
    elif operation == "*":
        print(first_num * second_num)
    elif operation == "/":
        if second_num == 0:
            print("Делить на 0 нельзя!")
        else:
            print(first_num / second_num)
    else:
        print("Оператор введён некорректно!")

    print("Хотите продолжить? Да- Y Нет - Любой символ")
    if input() != "Y":
        break

