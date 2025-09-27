## Beginner Level Problems
### Problem-1: Reverse a String Without Slicing
You are building a simple text utility tool for your web app. 
    One of the requirements is to reverse a string input by a user.

-   **Input**: `"bongodev"`
    
-   **Output**: `"vedognob"`
    
-   **Hint**: Use a loop to read the string from end to start.


### Problem-2: Count Vowels in a Sentence

    
As part of a data-cleaning pipeline, count how many vowels are in a string to later analyze readability.

-   **Input**: `"Data Science is awesome"`
    
-   **Output**: `9`
    
-   **Hint**: Convert string to lowercase and check each character.


### Problem-3: Find Duplicates in a List

You’re given a user-uploaded list of tags. Identify duplicates for suggestion cleanup.

-   **Input**: `["ai", "ml", "python", "ml", "dl", "ai"]`
    
-   **Output**: `["ml", "ai"]`
    
-   **Hint**: Use a dictionary or set to track seen elements.



### Problem-4: Check if a Word is a Palindrome
Write a function that checks if a word or phrase is the same when reversed, ignoring spaces and punctuation.

-   **Input**: `"Madam"`
    
-   **Output**: `True`
    
-   **Hint**: Normalize the string and compare it to its reverse.



### Problem-5: Flatten a Nested List
You are given a nested list of elements (e.g., UI config data). Flatten it into a single-level list.
    
    -   **Input**: `[1, [2, 3], [4, [5]]]`
        
    -   **Output**: `[1, 2, 3, 4, 5]`
        
    -   **Hint**: Use recursion to handle sublists.



### Problem-6: Capitalize First Letter of Each Word
Build a custom title formatter that capitalizes the first letter of each word without using `.title()`.

-   **Input**: `"python for web developers"`
    
-   **Output**: `"Python For Web Developers"`
    
-   **Hint**: Use `.split()` and loop through each word.



### Problem-7: Find Missing Number in a Sequence
You received log files indexed from 1 to n. One log is missing. Find it.

-   **Input**: `[1, 2, 4, 5]`
    
-   **Output**: `3`
    
-   **Hint**: Use arithmetic formula for sum of n numbers.



### Problem-8: Factorial Using Recursion
Write a function to return the factorial of a number, used in data science combinations calculation.

-   **Input**: `5`
    
-   **Output**: `120`
    
-   **Hint**: Base case is `0! = 1`, then recurse.



### Problem-9: Sum of Digits of an Integer
For a gamification feature, sum the digits of a user’s ID to generate a unique color code.

-   **Input**: `9875`
    
-   **Output**: `29`
    
-   **Hint**: Use `//` and `%` or string conversion.



### Problem-10: Check if a Number is Prime
Write a function to check if a number is prime, useful in some encryption schemes.
    
-   **Input**: `29`
    
-   **Output**: `True`
    
-   **Hint**: Check divisibility from 2 to `sqrt(n)`.
