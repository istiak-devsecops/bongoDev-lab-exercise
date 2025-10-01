text = "python for web developers"
capitalized_words = []

for word in text.split():
    new_word = word[0].upper() + word[1:]
    capitalized_words.append(new_word)

new_sentence = " ".join(capitalized_words)
print(new_sentence)  
