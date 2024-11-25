import string

def popular_words(text: str, words: list):
   text = text.lower()
   text = ''.join(char for char in text if char not in string.punctuation)

   counting_words = {word: 0 for word in words}

   for word in text.split():
       if word in counting_words:
           counting_words[word] += 1

   return counting_words

print(popular_words("He said she said that we said everything was said already.",['he', 'she', 'said', 'was']))