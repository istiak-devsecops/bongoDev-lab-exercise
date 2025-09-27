user_input = input("Write down a sentence. ").split()

def long_word_finder(words):
    max_word = ""
    for word in words:
        if len(word) > len(max_word):
            max_word = word
    return max_word

print(long_word_finder(user_input))
