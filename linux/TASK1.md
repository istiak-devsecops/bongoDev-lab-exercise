# Log File Filtering Task

## Problem Statement
You are working as a **DevOps engineer** and need to analyze application logs for errors.  

### Task
1. Create a log file named **`app.log`** and add at least **10 lines** of mixed log messages.  
   - Include different log levels such as `INFO`, `DEBUG`, and at least **3 lines** with the keyword `ERROR`.  
   - Example log lines:
     ```
     2025-09-16 10:10:23 INFO User logged in
     2025-09-16 10:11:05 ERROR Database connection failed
     2025-09-16 10:11:45 DEBUG Cache refreshed
     2025-09-16 10:12:10 ERROR Service unavailable
     ```

2. Write a **bash script** named **`find_errors.sh`** that:
   - Reads from `app.log`.  
   - Extracts and displays only the lines that contain the keyword `ERROR`.

3. Run the script and show the output.



## Expected Output
    2025-09-16 10:11:05 ERROR Database connection failed
    2025-09-16 10:12:10 ERROR Service unavailable
