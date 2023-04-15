import os
import shutil

# O(N) runtime, Linear Time relative to text file, since the function places
# each word into a list and calls lower() to standaraize each word
def tokenize(TFP):
    #FTP is assumed the filepath including the target file 
    #ex: filepath = "C:/Users/berya/ICS121/testing.txt"
    #ICS121 being project folder
    #testing.txt being the target folder
    filepath = TFP.split("/")
    #isolates target folder name
    target_file = filepath[-1]

    #opens and auto closes file, reads then places each word (seperated by newline) into a list
    with open(target_file, 'r') as f:
        text = f.read()
        text = text.split("\n")
    
    #standarizes each word in list, making every word lowercase
    Tokened = [x.lower() for x in text]

    #returns list of tokenized words
    return Tokened

# O(N) runtime, iterates through each word in the list to add to a dict
# then iterates throught he list again to increment the frequency
def computeWordFrequencies(words):
    #declare dictionary variable
    retMap = dict()
    
    #initialize each dictionary key
    for x in words:
        retMap[x] = 0

    #increment the value of each key for every time it appears in the list
    for x in words:
        retMap[x]+=1
    
    #returns dict (map in c++)
    return retMap

# O(N) runtime, 
def printout(mapping):
    #sorted items based on their frequency
    sortedmap = sorted(mapping.items(), key=lambda item:item[1], reverse=True)

    #iterates through and prints out each word in order
    for x in sortedmap:
        print(x[0] + " = " + str(x[1]))





if __name__ == "__main__":
    print("...starting program...")

    file = input("\nEnter file path (ex: C:/Users/berya/ICS121/testing.txt): ")  
    #file = "C:/Users/berya/ICS121/testing.txt"
    list = tokenize(file)
    print("\ncounting word frequency...")
    map = computeWordFrequencies(list)

    print("\nprinting out map...")
    print("----------------------------------------------")
    printout(map)
    print("----------------------------------------------")
    print("finished printing map...")
