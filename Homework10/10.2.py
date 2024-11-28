import string

def first_word(text):
    text = ''.join(char if char not in string.punctuation or char == "'" else ' ' for char in text).split()[0]
    return text




assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
assert first_word(" Hello.World") == "Hello", 'Test7'
assert first_word("     Hello.World") == "Hello", 'Test8'
print('OK')