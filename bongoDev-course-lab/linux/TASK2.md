# Linux Task: File Permissions and Ownership

## Problem Statement
As a **Linux user**, controlling access to files is an important skill.  
In this task, you will practice creating files, modifying permissions, and changing ownership.  

---

## Task Instructions

1. **Create a Directory**
   - Create a directory called `project`.

2. **Create a File**
   - Inside the `project` directory, create a file named `notes.txt`.
   - Add some sample text to the file using `echo` or `nano`.

3. **Check File Permissions**
   - Use the `ls -l` command to check the default permissions of `notes.txt`.

4. **Modify File Permissions**
   - Remove the **write permission** for the group.
   - Add **execute permission** for the owner.

5. **Change Ownership**
   - Change the owner of `notes.txt` to the `root` user (use `sudo`).
   - Verify the ownership change.

6. **Show Final Result**
   - Display the final permissions and ownership using:
     ```bash
     ls -l project/notes.txt
     ```

## Expected Output
    -r-xr--r-- 1 root user 25 Sep 16 12:00 notes.txt