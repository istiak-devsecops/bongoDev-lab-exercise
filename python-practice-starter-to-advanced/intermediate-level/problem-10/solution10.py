import re
from collections import Counter

blog = """
Docker is a powerful tool for containerization. Docker simplifies deployment, scaling, and management.
With Docker, developers can package applications with all dependencies.
"""

# Common stopwords to exclude
stopwords = {"is", "a", "for", "and", "with", "can", "all", "the", "of", "to", "in", "on", "at", "by", "an", "be", "this", "that"}

words = re.findall(r'\b\w+\b', blog.lower())

# Filter out stopwords
filtered = [word for word in words if word not in stopwords]

# Count frequency
freq = Counter(filtered)

# Get most common word
most_common = freq.most_common(1)[0]
print(f"Most frequent word: '{most_common[0]}' (appears {most_common[1]} times)")