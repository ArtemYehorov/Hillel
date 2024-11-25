import string

def popular_words(text: str, words: list):
   text = text.lower()
   text = ''.join(char for char in text if char not in string.punctuation)

   counting_words = {word: 0 for word in words}

   for word in text.split():
       if word in counting_words:
           counting_words[word] += 1

   return counting_words

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')