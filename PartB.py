import os
import shutil
import re

# O(N) linear run time, we iterate through each word of both files, and as we iterate we
# add the word to a set, which ignores duplicates saving time
# then calls intersect instead of a double for loop to avoid a quadratic run time
def compare(TFP1, TFP2):
    #FTP is assumed the filepath including the target file 
    #ex: filepath = "C:/Users/berya/ICS121/testing.txt"
    #ICS121 being project folder
    #testing.txt being the target folder
    filepath1 = TFP1.split("/")
    filepath2 = TFP2.split("/")

    target_file1 = filepath1[-1]
    target_file2 = filepath2[-1]

    #opens and auto closes file, reads then places each word (seperated by newline) into a set
    #set auto counts unique words
    Tokened1 = set()
    with open(target_file1, encoding="utf8") as f:
        for line in f:
            try:
                for word in line.split(" "):
                    word = word.lower()
                    wordFix = re.sub(r'[^a-z0-9]','', word)
                    Tokened1.append(wordFix)
            except:
                pass
    f.close()


    Tokened2 = set()
    with open(target_file2, encoding="utf8") as f:
        for line in f:
            try:
                for word in line.split(" "):
                    word = word.lower()
                    wordFix = re.sub(r'[^a-z0-9]','', word)
                    Tokened2.append(wordFix)
            except:
                pass
    f.close()

    #output intersecting words and number of words
    intersect = Tokened1.intersection(Tokened2)
    print("intersecting words: ")
    print(intersect)

    print(len(intersect))



if __name__ == "__main__":
    print("...starting program...")
    file1 = input("\nEnter file1 path (ex: C:/Users/berya/ICS121/testing.txt): ")  
    file2 = input("\nEnter file2 path (ex: C:/Users/berya/ICS121/testing.txt): ")
    compare(file1 ,file2)
