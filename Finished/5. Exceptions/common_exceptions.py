# Example file for Advanced Python by Joe Marini
# Understanding the built-in exception classes in Python

import os

# IndexError occurs when you try to access an index that is out of range
int_list = [0,3,6,1,8,7,3,5]
print(int_list[10])


# KeyError is similar - it is raised when a key is not found in a Dictionary
my_dict = {1: "one", 2: "two", 3: "three"}
print(my_dict[4])


# FileNotFoundError is raised when you try to access a file that doesn't exist
with open("myfile.txt", "r") as my_file:
    print(my_file)


# FileExistsError is raised when a file or directory already exists
os.mkdir("testdir")
# NotADirectoryError is raised when try to perform a dir operation on a non-dir object
os.listdir("myfile.txt")
