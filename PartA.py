import os
import shutil

class Token:
    data = None

    def __init__(d):
        data = d.lower()

if __name__ == "__main__":
    print("pog")
    
    filepath = "C:/Users/berya/ICS121/testing.txt"
    filepath = filepath.split("/")

    target_file = filepath[-1]
    print(filepath[-1])

    with open(target_file, 'r') as f:
        text = f.read()
        text = text.split("\n")

    print(text)