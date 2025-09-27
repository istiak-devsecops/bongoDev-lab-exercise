# Find the most frequent character in the paragraph

import string

rhyme = 'Twinkle, twinkle, little star. How I wonder what you are!'

lower_string = rhyme.lower()

clean_char = []



for char in lower_string:
    if char not in string.punctuation and not char.isspace():
        clean_char.append(char)

char_freq = {}

for chr in clean_char:
    if chr in char_freq:
        char_freq[chr] += 1
    else:
        char_freq[chr] = 1

max_frq = max(char_freq.keys())

print(f"Most frequently appeared char is: {max_frq} \nand it appeares {max(char_freq.values())} times.")


 