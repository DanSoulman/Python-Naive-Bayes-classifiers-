import re

#Filters out the keys that aren't allowed
def formatWords(word_list):

    #sets the allowed keys
    allowedWords = re.compile("[^A-Za-z0-9]+")
    
    #filters through your word list keeping only the allowed words
    return list(filter(lambda cursedWord: not allowedWords.search(cursedWord) ,word_list))  


#Goes through the positive, negative and whole word list and counts the occurance of each word in each
def wordCounter(clean_list, clean_list2, fullList, posDictionary, negDictionary, fullDictionary):
    
    #--------------------------------------------------------
    #G E T T I N G  O C C U R A N C E  O F  E A C H  W O R D
    #--------------------------------------------------------

    #Positive wordcount
    for word in clean_list: #For each word in clean_list 
        posDictionary[word] = posDictionary[word]+1 #Increments key by one  
    #For testing     
    #print("The positive dictionary:\n" , posDictionary) #Prints the dictionary and its occurances 
    #input("Hit enter to continue:") #This is to break up information into readable chunks

    #Negative wordcount
    for word in clean_list2: 
        negDictionary[word] = negDictionary[word]+1  
    #For testing
    #print("The negative dictionary:\n" , negDictionary)  
    #input("Hit enter to continue:") 

    #Combined wordcount
    for word in clean_list: #For each word in clean_list 
        fullDictionary[word] = fullDictionary[word]+1 
    for word in clean_list2: #Then also adds in clean_list2
        fullDictionary[word] = fullDictionary[word]+1
    #For Testing
    #print("The whole dictionary:\n" , fullDictionary)  
    #input("Hit enter to continue:") 

   
    #----------------------------------------------------------------------------------------------------
    #G E T T I N G  P R O B A B I L I T Y  O F  A  W O R D  B E I N G  P O S I T I V E / N E G A T I V E
    #----------------------------------------------------------------------------------------------------
    vocabPos = {} #Dictionary that stores the probability that a word is positive as its value
    for word in fullDictionary:
        fOccurance = fullDictionary[word]
        posProbability = (posDictionary[word]/fOccurance)
        #negProbability = (1 - posProbability) #Got negative occurance until I realised I didn't need it 
        vocabPos[word] = posProbability

        #For testing
        #print(f"The probablility that the word {word} is Positive: {vocabPos[word]} Negative: {(1 - vocabPos[word])}") 
    #input("Hit enter to continue:")
   
    #----------------------------------------------------------------------------------------------------
    #G E T T I N G  P R O B A B I L I T Y  O F  A  W O R D  A P P E A R I N G  I N  A  G I V E N  L I S T 
    #----------------------------------------------------------------------------------------------------
    #NOTE: this wasn't needed but I misread the spec and wrote the code for it before I realized so I kept it in
    
    #Postive
    #for word in posDictionary.keys(): #Loops through each word in the dictionary
    #    probability =  (posDictionary[word] / len(clean_list)) #Works out the probability of the word
    #    print(f"The probablility of the word {word} appearing in the positive list is : {probability}") #Prints word and probability
    #input("Hit enter to continue:")

    #Negative
    #print("")
    #for word in negDictionary.keys():
    #    probability =  (negDictionary[word] / len(clean_list2))
    #    print(f"The probablility of the word {word} appearing in the negative list is : {probability}")
    #input("Hit enter to continue:")

    #Full List
    #print("")
    #for word in fullDictionary.keys():
    #    probability =  (fullDictionary[word] / (len(clean_list) + len(clean_list2) ) )
    #    print(f"The probablility of the word {word} appearing in the full list is : {probability}")
    #input("Hit enter to continue:")




    #-------------------------------------------
    #Assigning the likelyhood of a word being Positive/Negative
    #-------------------------------------------
    tweets = open("dataFiles/test/testPos.txt", 'r').read().lower().split("@") #Opens in file seperated by tweets
    #Loops through words in the tweet to find any trained to be positive/negative
    for tweet in tweets:
        tweetWords = re.split(r"[^\w]", tweet) #Should clean up the special characters. TODO: Test this is properly fundtioning

        probOfPos, count, probabiltiy = 0,0,0 #Initialise varibles needed foe the loop
        
        #Loops through each word in the tweet, if it appeared in the trainer it goes through and grabs the probability. Then adds that to the total probability and ups counted words
        for word in tweetWords:
            if vocabPos.__contains__(word):
                count +=1 #counts words considered 
                probOfPos += vocabPos[word] #total probability 
                probability =(probOfPos/count) #works out average probability 
                #print("The probablility that the whole tweet is Positive is" , probability) #for testing 
                    
        if probability > 0.5:
            print(f"{tweet} is positive")
        elif probability < 0.5:
            print(f"{tweet} is negative")
        else:
            print("Tweet fifty fifty.")

#Reads in the File and sorts it into the dictionary. 
def main():
    #-------------------------------------------
    #READING IN DATA & SETTING UP DICTIONARY : 
    #TODO: If there is more time make this a fuction
    #-------------------------------------------
    #Opens text file in read only
    #text_file = open("dataFiles/test/new_test.txt", 'r')  
    text_file = open("dataFiles/train/trainPos.txt", 'r') 
    
    read_file = text_file.read() #Variable holding the full unedited tweets
    word_list = read_file.lower().split() #Splits up each word seperately into all lowercase
    clean_list = formatWords(word_list) #Gets rid of special characters
    uniquewords = set(clean_list) #Creates a set of just unique words from the list of words

    #Does it again for the 2nd file
    #text_file2 = open("dataFiles/test/new_test2.txt", 'r')
    #text_file2 = open("dataFiles/test/testNeg.txt", 'r') 
    text_file2 = open("dataFiles/train/trainNeg.txt", 'r') 
    read_file2 = text_file2.read() 
    word_list2 = read_file2.lower().split()
    clean_list2 = formatWords(word_list2) 
    uniquewords2 = set(clean_list2) 
    
    #Makes a full list of words from Positive and Negative
    fullList = uniquewords2|uniquewords

    #Creates a dictionary setting the value of each fullList to 0 for counting
    posDictionary = dict.fromkeys(fullList, 0) 
    negDictionary = dict.fromkeys(fullList, 0)
    fullDictionary = dict.fromkeys(fullList, 0)
    
    #Calls on the wordCounter
    wordCounter(clean_list, clean_list2 ,fullList, posDictionary, negDictionary, fullDictionary) 

main()