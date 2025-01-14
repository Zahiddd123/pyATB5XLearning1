# File creation
import os

file_name= "zahid.py"
content= "This file is of Zahid"

with open(file_name, "w") as file:
    file.write(content)

with open(file_name, "r") as file:
    content2= file.read()
    print(content2)

# os.chdir("Desktop") Used to move the file to other location

### File Reading with Python

# File reading is a fundamental operation in Python that allows you to access and manipulate data stored in text files

# file.open("path or name of the file"), "mode")

# path or name of the file ->

# mode -> r, w, x

# ```
# 'r'       open for reading (default)
# 'w'       open for writing, truncating the file first
# 'x'       create a new file and open it for writing
# 'a'       open for writing, appending to the end of the file if it exists
# 'b'       binary mode
# 't'       text mode (default)
# '+'       open a disk file for updating (reading and writing)
# ```