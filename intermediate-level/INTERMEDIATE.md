## Intermediate Level Problems
### Problem-1: Longest Word in a Sentence
   Build a function that extracts the longest word from user-generated content.

-   **Input**: `"Machine learning is fascinating"`
    
-   **Output**: `"fascinating"`
    
-   **Hint**: Split string and use `max()` with `key=len`.


### Problem-2: Group Anagrams Together
Group similar words together in a UI (e.g., tags: `["bat", "tab", "cat", "act"]`).

-   **Output**: `[["bat", "tab"], ["cat", "act"]]`
    
-   **Hint**: Use a dictionary where sorted word is key.


### Problem-3: Implement an LRU Cache (Least Recently Used)
Simulate caching in a backend system. You need to implement a cache with `get()` and `put()` methods.
    

-   **Hint**: Use `OrderedDict` or create a custom class with a doubly linked list.



### Problem-4: Validate Email Format
Write a function that validates emails during user registration.
    

-   **Input**: `"test@domain.com"`
    
-   **Output**: `True`
    
-   **Hint**: Use regular expressions.



### Problem-5: Fibonacci Using Memoization
Optimize a recursive Fibonacci function using caching, useful in DP-based ML solutions.
    

-   **Input**: `50`
    
-   **Output**: `12586269025`
    
-   **Hint**: Use `@lru_cache` from `functools`.



### Problem-6: Flatten a Nested JSON
Flatten a nested dictionary for storage in tabular format or NoSQL DB.
    

-   **Input**: `{"a": {"b": 1}}`
    
-   **Output**: `{"a.b": 1}`
    
-   **Hint**: Use recursion.



### Problem-7: Analyze Access Logs and Count IPs
Parse Apache log and find the top 3 IPs with the most requests.
    

-   **Hint**: Read file line-by-line and count IPs using `collections.Counter`.



### Problem-8: Command-line Calculator
Build a CLI tool that takes command `add 5 7` and returns `12`.
    

-   **Hint**: Parse `input().split()` and use if/elif for commands.



### Problem-9: Password Validator (Security Utility)
Build a validator that checks for minimum length, uppercase, lowercase, number, and special character.
    

-   **Hint**: Use regex or manual checks with `any()`.



### Problem-10: Most Frequent Word (Excluding Stopwords)
Analyze blog content and find the most frequent word, excluding common stopwords.
    

-   **Hint**: Clean punctuations, lowercase all, use `Counter`.
