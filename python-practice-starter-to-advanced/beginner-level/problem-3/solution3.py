from collections import defaultdict

def freq_counter(tags):
    count = defaultdict(int)
    for tag in tags:
        count[tag] += 1
    return [tag for tag, freq in count.items() if freq > 1]

duplicate_tags = ["ai", "ml", "python", "ml", "dl", "ai"]

print(freq_counter(duplicate_tags))

