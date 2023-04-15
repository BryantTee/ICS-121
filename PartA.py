import os
import shutil
import re

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
    Tokened = list()
    with open(target_file, encoding="utf8") as f:
        for line in f:
            for word in line.split(" "):
                word = word.lower()
                wordFix = re.sub(r'[^a-z0-9]','', word)
                Tokened.append(wordFix)
    
    #standarizes each word in list, making every word lowercase

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

    running = True
    while running:
        try:
            file = input("\nEnter file path (ex: C:/Users/berya/ICS121/testing.txt) (q to quit): ")  
            #file = "C:/Users/berya/ICS121/testing.txt"
            
            if (file == "q"):
                break

            list = tokenize(file)
            print("\ncounting word frequency...")
            map = computeWordFrequencies(list)

            print("\nprinting out map...")
            print("----------------------------------------------")
            printout(map)
            print("----------------------------------------------")
            print("finished printing map...")
        except:
            print("\n-------------------------------------------------")
            print("file does not exist or wrong format try again...")
            print("-------------------------------------------------")\
    
    print("\nprogram finished running...\n")



    
