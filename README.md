# Basic Python Scripting Lab

## Introduction
This lab teaches students how to use essential Python modules (os, requests, shutil) and perform basic file handling operations to download and modify a file hosted on GitHub. The lab also introduces learners to other Python modules such as datetime.

## Lab Objectives
At the end of this lab, learners will know how to:
1. Perform basic file handling in Python.
2. Use Python's requests module to download content.
3. Use the os module to create directories and paths.

## Task Overview
1. Create a Python environment and install required libraries (requests).
2. Create a custom directory using the os module.
3. Download a file named "change_me.txt" from a specified GitHub repository using the requests module.
4. Save the downloaded file in the custom directory, renaming it to "<firstname_lastname>.txt".
5. Modify the file content by replacing it with user input and appending the current date and time.
6. Verify the changes in the file content.

## Step 1: Import Required Modules
```python
import requests
import os
import shutil
from datetime import datetime
```

## Step 2: Clean Up Previous Directory
```python
if os.path.exists('john_doe'):
    try:
        shutil.rmtree('john_doe')
        print(f"Directory 'john_doe' has been removed successfully.")
    except Exception as e:
        print(f"Error: {e}")
```

## Step 3: Create a New Directory
```python
download_folder = 'john_doe'
if not os.path.exists(download_folder):
    os.makedirs(download_folder)
    print(f"Directory: {download_folder} created.")
```

## Step 4: Define the Local File Path
```python
local_file_path = os.path.join(download_folder, "john_doe.txt")
```

## Step 5: Download the File
```python
url = "https://raw.githubusercontent.com/sdg000/pydevops_intro_lab/main/change_me.txt"
response = requests.get(url)

if response.status_code == 200:
    print(f"File successfully downloaded.")
    with open(local_file_path, "wb") as file:
        file.write(response.content)
    print('File saved successfully.')
else:
    print(f"Failed to download file. Status code: {response.status_code}")
```

## Step 6: Overwrite File Content
```python
user_input = input("Describe what you have learned so far in a sentence: ")
now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

with open(local_file_path, "w") as file:
    file.write(user_input + "\n")
    file.write(f"Last modified on: {current_time}")
print("File successfully modified.")
```

## Step 7: Display the Updated File Content
```python
with open(local_file_path, "r") as file:
    print("\nYou Entered: ", end='')
    print(file.read())
```

Lab Complete.
