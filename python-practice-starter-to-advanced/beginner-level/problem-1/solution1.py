# ## Beginner Level Problems
# ### Problem-1: Reverse a String Without Slicing
# You are building a simple text utility tool for your web app. 
#     One of the requirements is to reverse a string input by a user.

# -   **Input**: `"bongodev"`
    
# -   **Output**: `"vedognob"`
    
# -   **Hint**: Use a loop to read the string from end to start.

text = "bongodev"

Reverse_text = ""

for char in range(len(text) -1, -1, -1):
    Reverse_text += text[char]

print(Reverse_text)