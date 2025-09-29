import re
sentences = "Data Science is awesome"


vowels = r"[aeiouAEIOU]"
result = len(re.findall(vowels, sentences))

print("Total vowels are in the sentences: ",result)
