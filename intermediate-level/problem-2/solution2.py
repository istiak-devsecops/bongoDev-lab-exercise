tags = ["bat", "tab", "cat", "act"]


def group_anagrams(words):
    anagram_dict = {}

    for word in words:
        key = ''.join(sorted(word)) 
        if key in anagram_dict:
            anagram_dict[key].append(word)
        else:
            anagram_dict[key] = [word]

    return list(anagram_dict.values())


grouped = group_anagrams(tags)

print(grouped)