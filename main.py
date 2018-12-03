
#Reads in the File and sorts it into the dictionary. then counts the frequency 
def readInFile():
    #text_file = open("dataFiles/test/new_test.txt", 'r') #Opens text file in read only
    text_file = open("dataFiles/test/testPos.txt", 'r') 
    read_file = text_file.read() #Variable holding the full unedited tweets
    word_list = read_file.split() #Splits up each word seperately
    uniquewords = set(word_list) #Creates a set of just unique words from the list of words

    #Does it again for the 2nd file
    #text_file2 = open("dataFiles/test/new_test2.txt", 'r')
    text_file2 = open("dataFiles/test/testNeg.txt", 'r') 
    read_file2 = text_file2.read() 
    word_list2 = read_file2.split()
    uniquewords2 = set(word_list2) 
    
    #Makes a full list of words from Positive and Negative
    fullList = uniquewords2|uniquewords

    #Creates a dictionary setting the key of each fullList to 0 for counting
    posDictionary = dict.fromkeys(fullList, 0) 
    negDictionary = dict.fromkeys(fullList, 0)
    fullDictionary = dict.fromkeys(fullList, 0)
    
    #Calls on the wordCounter
    wordCounter(word_list, word_list2,fullList, posDictionary, negDictionary, fullDictionary) 

#Goes through the positive, negative and whole word list and counts the occurance of each word in each
def wordCounter(word_list, word_list2, fullList, posDictionary, negDictionary, fullDictionary):
    #Positive wordcount
    for word in word_list: #For each word in word_list 
        posDictionary[word] = posDictionary[word]+1 #Increments key by one  
    print("The positive dictionary:\n" , posDictionary) #Prints the dictionary and its occurances 

    #Negative wordcount
    for word in word_list2: #For each word in word_list 
        negDictionary[word] = negDictionary[word]+1 #Increments key by one  
    print("The negative dictionary:\n" , negDictionary) #Prints the dictionary and its occurances 

    #Combined wordcount
    for word in word_list: #For each word in word_list 
        fullDictionary[word] = fullDictionary[word]+1 #Increments key by one
    for word in word_list2:    
        fullDictionary[word] = fullDictionary[word]+1
    print("The whole dictionary:\n" , fullDictionary) #Prints the dictionary and its occurances 


    #Probability workout  
    #Postive
    for word in posDictionary.keys():
        probability =  (posDictionary[word] / len(word_list))
        print(f"The probablility of the word {word} appearing in the positive list is : {probability}")
    
    #Negative
    print("")
    for word in negDictionary.keys():
        probability =  (negDictionary[word] / len(word_list2))
        print(f"The probablility of the word {word} appearing in the negative list is : {probability}")
    
    #Full List
    print("")
    for word in fullDictionary.keys():
        probability =  (fullDictionary[word] / (len(word_list) + len(word_list2) ) )
        print(f"The probablility of the word {word} appearing in the full list is : {probability}")

def main():
    readInFile() #Calls in readInFile

main()
