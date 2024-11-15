import requests
import os
import shutil
from datetime import datetime

if os.path.exists('jimmy_essel'):
    try:
        shutil.rmtree('jimmy_essel')
        print(f"Directory 'jimmy_essel' has been removed successfully")
    except Exception as e:
        print(f"Error: {e}")


download_folder = 'jimmy_essel'
if not os.path.exists(download_folder):
    os.mkdir(download_folder)
    print(f"Directory '{download_folder}' created")


local_file_path = os.path.join(download_folder, 'jimmy_essel.txt')
url = "https://raw.githubusercontent.com/sdg000/pydevops_intro_lab/main/change_me.txt"

response = requests.get(url)

if response.status_code == 200:
    print(f"File successfully downloaded")

    with open(local_file_path, 'wb') as f:
        f.write(response.content)
        print("File saved successfully")
else:
    print(f"Failed to download file. Status code: {response.status_code}")


user_input = input("What have you learned so far in a sentence: ")
now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

with open(local_file_path, 'w') as file:
    file.write(user_input+ '\n')
    file.write(f"Last modified on: {current_time}")
    print("File succesffully modified")


with open(local_file_path, 'r') as file:
    print("\nYou Entered: ", end='')
    print(file.read())