import string

letters = input("Введите диапазон букв, например, a-c: ")
all_letters = string.ascii_letters

start_char = letters[0]
end_char = letters[-1]

start_index = all_letters.index(start_char)
end_index = all_letters.index(end_char)

cut_letters = all_letters[start_index:end_index + 1]

print(cut_letters)
