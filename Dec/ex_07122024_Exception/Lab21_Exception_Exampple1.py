import os
from csv import excel
from sys import excepthook

try:
    full_path = os.getcwd()
    print(full_path)

    full_path_file = full_path + "/example.txt"
    print(full_path_file)

    print(os.name)  # "nt for window"

# Steps to read the file:-

# 1. Read a file

    file = open(full_path_file)  # FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\Admin\\PycharmProjects\\pyATB5XLearning\\Dec\\ex_07122024_Exception/example.txt'
except Exception as e:
    print("file not found, fix the path and create a file")
finally:
    print("This code will be executed ")



