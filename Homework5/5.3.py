import string
userInput = input()

userInput = userInput.title()
for char in string.punctuation + ' ':
        userInput = userInput.replace(char, '')
userInput = '#' + userInput
if len(userInput) > 140:
    userInput = userInput[:140]
print(userInput)

