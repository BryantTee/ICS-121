import os
import shutil


global wordList

class Token:
    data = None

    def __init__(init, d):
        data = d.lower()

def tokenize(TFP):
    with open(TFP, 'r') as f:
        text = f.read()
        text = text.split("\n")
    
    Tokened = [Token(x) for x in text]
    WordList = Tokened
    return Tokened

def computeWordFrequencies(words):
    retMap = {}
    for x in words:
        retMap[x] = 0

    for x in words:
        retMap[x]+=1
    
    return retMap

def print(mapping):
    None 

if __name__ == "__main__":
    print("pog")
    print("starting program...")


    filepath = "C:/Users/berya/ICS121/testing.txt"
    filepath = filepath.split("/")

    target_file = filepath[-1]
    print(filepath[-1])

    list = tokenize(target_file)
    computeWordFrequencies(list)    
