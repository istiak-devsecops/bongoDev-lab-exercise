import string

user_input = input("Write more than 2 words.").lower().split()

split_word = []

for word in user_input:
    clean_word = ""
    for char in word:
        if char not in string.punctuation and not char.isspace():
            clean_word += char
    if clean_word:
        split_word.append(clean_word)

anagram_dict = {}

def anagram_check(words):
    for word in words:
        key = "".join(sorted(word))
        if key in anagram_dict:
            anagram_dict[key].append(word)
        else:
            anagram_dict[key] = [word]
    
    return list(anagram_dict.values())

print(anagram_check(split_word))