input_date = int(input("Введите число от 0 до 8640000: "))
our_date = {"days": 0, "hours": 0, "minutes": 0, "seconds": 0}

if input_date >= 0 and input_date <= 8640000:
    our_date["hours"] = input_date  // 3600
    our_date["minutes"] = (input_date % 3600) // 60
    our_date["seconds"] = input_date % 60

    while our_date["hours"] >= 24:
        our_date["hours"] -= 24
        our_date["days"] += 1

if 11 <= our_date["days"] % 100 <= 14:
    day_word = "дней"
else:
    if our_date["days"] % 10 == 1:
        day_word = "день"
    elif 2 <= our_date["days"] % 10 <= 4:
        day_word = "дня"
    else:
        day_word = "дней"

print(f"{our_date["days"]} {day_word}, {our_date["hours"]:02}:{our_date["minutes"]:02}:{our_date["seconds"]:02}")