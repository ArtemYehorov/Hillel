def second_index(text, some_str):
    first_index = text.find(some_str)
    if first_index == -1:
        return None
    second_index = text.find(some_str, first_index + 1)

    return second_index if second_index != -1 else None

print(second_index("sims", "s"))
print(second_index("find the river", "e"))
print(second_index("hi", "h"))
print(second_index("Hello, hello", "lo"))
