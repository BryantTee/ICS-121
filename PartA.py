import os
import shutil


def tokenize(TFP):
    with open(TFP, 'r') as f:
        text = f.read()
        text = text.split("\n")
    
    Tokened = [x.lower() for x in text]
    WordList = Tokened
    return Tokened

def computeWordFrequencies(words):
    retMap = dict()
    for x in words:
        retMap[x] = 0

    for x in words:
        retMap[x]+=1
    
    return retMap

def printout(mapping):
    sortedmap = sorted(mapping.items(), key=lambda item:item[1], reverse=True)

    for x in sortedmap:
        print(x[0] + " = " + str(x[1]))





if __name__ == "__main__":
    print("pog")
    print("starting program...")


    filepath = "C:/Users/berya/ICS121/testing.txt"
    filepath = filepath.split("/")

    target_file = filepath[-1]
    print(filepath[-1])

    list = tokenize(target_file)
    map = computeWordFrequencies(list)
    printout(map)
