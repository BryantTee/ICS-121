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

    #opens and auto closes file
    #iterates through each line of the text file, and iterates through each word of that line
    #for each word change it to all lower case to standarize, then use regular expression to
    #replace any characters that are nonalphanumeric
    #then add words to the set, which cannot contain duplicates, so there is no need to check
    #and remove duplicates after
    Tokened1 = set()
    with open(target_file1, encoding="utf8") as f:
        for line in f:
            try:
                for word in line.split(" "):
                    word = word.lower()
                    wordFix = re.sub(r'[^a-z0-9]','', word)
                    Tokened1.add(wordFix)
            except:
                pass
    f.close()

    #performs exactly the same as the same text file above Tokened1
    Tokened2 = set()
    with open(target_file2, encoding="utf8") as f:
        for line in f:
            try:
                for word in line.split(" "):
                    word = word.lower()
                    wordFix = re.sub(r'[^a-z0-9]','', word)
                    Tokened2.add(wordFix)
            except:
                pass
    f.close()

    #output intersecting words and number of words between Tokened1 and Tokened2 (set1 and set2)
    intersect = Tokened1.intersection(Tokened2)
    print("intersecting words: ")
    print(intersect)

    print(len(intersect))



if __name__ == "__main__":
    print("...starting program...")
    running = True
    while running:
        try:
            file1 = input("\nEnter file1 path (ex: C:/Users/berya/ICS121/testing.txt) (q to quit): ")  
            file2 = input("\nEnter file2 path (ex: C:/Users/berya/ICS121/testing.txt) (q to quit): ")

            if (file1 == "q" or file2 == "q"):
                break

            compare(file1 ,file2)
        except:
            print("\n-------------------------------------------------")
            print("file does not exist or wrong format try again...")
            print("-------------------------------------------------")

    print("\nprogram finished running...\n")
