import re

#Filters out the keys that aren't allowed
def formatWords(word_list):
    allowedWords = re.compile("[^A-Za-z0-9]+") #sets the allowed keys
    #filters through your word list keeping only the allowed words
    return list(filter(lambda cursedWord: not allowedWords.search(cursedWord) ,word_list))  
    
#Goes through the positive, negative and whole word list and counts the occurance of each word in each
def wordCounter(clean_list, clean_list2, fullList, posDictionary, negDictionary, fullDictionary):
    #Positive wordcount
    for word in clean_list: #For each word in word_list 
        posDictionary[word] = posDictionary[word]+1 #Increments key by one  
    print("The positive dictionary:\n" , posDictionary) #Prints the dictionary and its occurances 
    input("Hit enter to continue:")

    #Negative wordcount
    for word in clean_list2: #For each word in word_list 
        negDictionary[word] = negDictionary[word]+1 #Increments key by one  
    print("The negative dictionary:\n" , negDictionary) #Prints the dictionary and its occurances 
    input("Hit enter to continue:")

    #Combined wordcount
    for word in clean_list: #For each word in word_list 
        fullDictionary[word] = fullDictionary[word]+1 #Increments key by one
    for word in clean_list2:    
        fullDictionary[word] = fullDictionary[word]+1
    print("The whole dictionary:\n" , fullDictionary) #Prints the dictionary and its occurances 
    input("Hit enter to continue:")

    #Probability workout  
    #Postive
    for word in posDictionary.keys():
        probability =  (posDictionary[word] / len(clean_list))
        print(f"The probablility of the word {word} appearing in the positive list is : {probability}")
    input("Hit enter to continue:")

    #Negative
    print("")
    for word in negDictionary.keys():
        probability =  (negDictionary[word] / len(clean_list2))
        print(f"The probablility of the word {word} appearing in the negative list is : {probability}")
    input("Hit enter to continue:")

    #Full List
    print("")
    for word in fullDictionary.keys():
        probability =  (fullDictionary[word] / (len(clean_list) + len(clean_list2) ) )
        print(f"The probablility of the word {word} appearing in the full list is : {probability}")
    input("Hit enter to continue:")



#Reads in the File and sorts it into the dictionary. 
def main():
    #text_file = open("dataFiles/test/new_test.txt", 'r') #Opens text file in read only
    text_file = open("dataFiles/test/testPos.txt", 'r') 
    read_file = text_file.read() #Variable holding the full unedited tweets
    word_list = read_file.lower().split() #Splits up each word seperately into all lowercase
    clean_list = formatWords(word_list) #Gets rid of special characters
    #print(clean_list)
    uniquewords = set(clean_list) #Creates a set of just unique words from the list of words

    #Does it again for the 2nd file
    #text_file2 = open("dataFiles/test/new_test2.txt", 'r')
    text_file2 = open("dataFiles/test/testNeg.txt", 'r') 
    read_file2 = text_file2.read() 
    word_list2 = read_file2.lower().split()
    clean_list2 = formatWords(word_list2) #Gets rid of special characters
    uniquewords2 = set(clean_list2) 
    
    #Makes a full list of words from Positive and Negative
    fullList = uniquewords2|uniquewords

    #Creates a dictionary setting the key of each fullList to 0 for counting
    posDictionary = dict.fromkeys(fullList, 0) 
    negDictionary = dict.fromkeys(fullList, 0)
    fullDictionary = dict.fromkeys(fullList, 0)
    
    #Calls on the wordCounter
    wordCounter(clean_list, clean_list2 ,fullList, posDictionary, negDictionary, fullDictionary) 

main()