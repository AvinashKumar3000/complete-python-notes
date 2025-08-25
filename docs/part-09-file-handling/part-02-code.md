# example code 

```python
import os

vales = dir(os)

current_path = os.getcwd()

new_path = os.path.join(current_path, 'new_folder')
new_path = os.path.join(new_path,'hall1')

os.makedirs(new_path)

os.popen()

with os.scandir('./') as entries:
    for entry in entries:
        print(entry.name)
        
# Walking a directory tree and printing the names of the directories 
# and files
for dirpath, dirnames, files in os.walk('.'):
    print(f'Found directory: {dirpath}')
    for file_name in files:
        print(file_name)
        
# File: fileinput-example.py
import fileinput

files = fileinput.input('./sample_file.txt')
for line in files:
    if fileinput.isfirstline():
        print(f'\n--- Reading {fileinput.filename()} ---')
    print(' -> ' + line, end='')
print()
```
