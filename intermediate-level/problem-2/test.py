import string

user_input = input("write at least 2 character to check if they are anagram. ").lower().split()

clean_word = []

for word in user_input:
    if word not in string.punctuation and not word.isspace():
        clean_word.append(word)

if sorted(clean_word[0]) == sorted(clean_word[1]):
    print(f"They are anagram: {clean_word[0]} : {clean_word[1]}")

else:
    print("not a anagram")