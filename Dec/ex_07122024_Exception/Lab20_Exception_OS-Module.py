import os
from importlib.metadata import files

# OS module: Os module in python is a powerful tool that provides
#            functions for interacting with the operating system.

# key feature of OS module:-

# Operating System Interface: The OS module provides a way to interact with
#                the underlying operating system, whether it's Windows, macOS, or Linux.


# File and Directory Operations: It offers functions for file and directory management,
#                             including creating, removing, and listing directories and files.


# Current Working Directory: The module allows you to get and change
#                 the current working directory using functions like os.getcwd() and os.chdir().


# Platform Independence: The OS module abstracts away platform-specific details,
#                        allowing you to write more portable code.

print(os.getcwd())
# Return current working directory(cwd)

# When ever a file/ direc. name start with . it is a hidden file or direct.

# Listfiles in the current directory
files= os.listdir('/Users/Admin/PycharmProjects/pyATB5XLearning/Dec/ex_07122024_Exception')
print("Files in the current directory",files)

# Create a new directory in current working directory
os.mkdir('Test 1')

# Check if this file exists
file_exist= os.path.exists('Test 1')
print(file_exist)