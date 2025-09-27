## Advances Level Problems
### Problem-1: Docker Log Analyzer
Build a script that reads a Docker log file and returns error messages with timestamps.
    

-   **Hint**: Look for keywords like `"ERROR"` or `"Exception"` using regex.


### Problem-2: Web Scraper for Blog Titles
Scrape a sample blog page and return all titles within `<h2>` tags.
    

-   **Hint**: Use `BeautifulSoup` and `requests`.


### Problem-3: Validate JSON Against Schema
Validate a dynamic JSON input against a predefined schema before database insertion.
    

-   **Hint**: Use `jsonschema` library or manually check key types.



### Problem-4: Create a Mini REST API with Flask
Build a mini Flask app with `/tasks` endpoint to `GET`, `POST`, and `DELETE` tasks from a list.
    

-   **Hint**: Use `Flask`'s route decorators.



### Problem-5: Calculate Pearson Correlation
Given two lists, calculate the correlation coefficient (e.g., feature correlation in ML).
    

-   **Hint**: Use formula or `scipy.stats.pearsonr()`.



### Problem-6: Read CSV and Return Top Records
Read a CSV of users and return top 5 users by `score`.
    

-   **Hint**: Use `csv.DictReader` or `pandas`.



### Problem-7: Simulate File Watcher in a Directory
Monitor a folder and detect when new `.txt` files are added.
    

-   **Hint**: Use `os.listdir()` in a loop or `watchdog`.



### Problem-8: **Matrix Multiplication for ML**
Multiply two matrices, often needed in neural net computations.
    

-   **Hint**: Use nested loops or `numpy.dot()`.



### Problem-9: Convert Image to Grayscale
Write a function to convert a color image to grayscale and save it.
    

-   **Hint**: Use `Pillow` (`PIL.Image.open().convert("L")`).



### Problem-10: Load Environment Variables from `.env` File
Implement a simple `.env` file loader for config in DevOps.
    

-   **Hint**: Use `dotenv` library or parse lines manually and set in `os.environ`.
