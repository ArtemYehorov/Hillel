import keyword
import string

punct = string.punctuation.replace("_", "")
UserInput= input()
correct = True

if UserInput.strip('_') == '' and len(UserInput) > 1:
    correct = False
elif UserInput[0].isdigit():
    correct = False
elif any(char.isupper() for char in UserInput):
    correct = False
elif any(char in punct or char.isspace() for char in UserInput):
    correct = False
elif UserInput in keyword.kwlist:
    correct = False

print(correct)