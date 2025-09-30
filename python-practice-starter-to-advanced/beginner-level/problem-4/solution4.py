import string

def palindrom_checker(word):
    normalized = "".join(char.lower() for char in word if char not in string.punctuation)   # removed space, punctation from the word
    return normalized == normalized[::-1]

word = "madam"
print(palindrom_checker(word))


