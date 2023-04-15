import os
import shutil

class Token:
    data = None

    def __init__(d):
        data = d.lower()

def tokenize(TFP):
    with open(TFP, 'r') as f:
        text = f.read()
        text = text.split("\n")
    
    return text

def computeWordFrequencies(word):
    None

def print(mapping):
    None 

if __name__ == "__main__":
    print("pog")
    print("starting program...")


    filepath = "C:/Users/berya/ICS121/testing.txt"
    filepath = filepath.split("/")

    target_file = filepath[-1]
    print(filepath[-1])

    tokenize(target_file)    
