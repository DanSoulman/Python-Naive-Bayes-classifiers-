#Reads in the File and sorts it into the dictionary. then counts the frequency 
def readInFile():
    text_file = open("dataFiles/test/new_test.txt", 'r') #Opens text file in read only
    read_file = text_file.read() #Variable holding the full unedited tweets
    word_list = read_file.split() #Splits up each word seperately
    uniquewords = set(word_list) #Creates a set of just unique words from the list of words

    #Does it again for the 2nd 
    text_file2 = open("dataFiles/test/new_test2.txt", 'r')
    read_file2 = text_file2.read() 
    word_list2 = read_file2.split()
    uniquewords2 = set(word_list2) 
    
    fullList = uniquewords|uniquewords2

    #print(uniquewords) #Prints the unique words for testing 



    positiveDictionary = dict.fromkeys(fullList, 0) #Creates a dictionary
    negativeDictionary = dict.fromkeys(fullList, 0) 
    #print(dictionary)

    #Positive wordcount
    for word in word_list: #For each word in word_list 
        positiveDictionary[word] = positiveDictionary[word]+1 #Increments key by one  
    print("The positive dictionary:\n" , positiveDictionary) #Prints the dictionary and its occurances 

    #Negative wordcount
    for word in word_list2: #For each word in word_list 
        negativeDictionary[word] = negativeDictionary[word]+1 #Increments key by one  
    print("The negative dictionary:\n" , negativeDictionary) #Prints the dictionary and its occurances 

def main():
    readInFile() #Calls in readInFile
    
main()