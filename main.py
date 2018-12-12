import re
import matplotlib.pyplot as plt
plt.rcdefaults
import numpy as np

#Reads in data, splits up each word and makes lowercase  
def readFile(src):
    text_file = open(src) 
    read_file = text_file.read() #Variable holding the full unedited tweets
    word_list = read_file.lower().split() #Splits up each word seperately into all lowercase
    return word_list
    

#Filters out the keys that aren't allowed
def formatWords(word_list):

    #sets the allowed keys
    allowedWords = re.compile("[^A-Za-z0-9]+")
    
    #filters through your word list keeping only the allowed words
    return list(filter(lambda cursedWord: not allowedWords.search(cursedWord) ,word_list))  


#Counts the times each word appears, sets it as the value for the dictionary passed in
def wordOccurance(clean_list, dictionary):
    for word in clean_list: #For each word in clean_list 
        dictionary[word] += 1 #Increments key by one  
    #For testing     
    #print("The positive dictionary:\n" , dictionary) #Prints the dictionary and its occurances 
    #input("Hit enter to continue:") #This is to break up information into readable chunks
    return dictionary

#Works out from the full dictionary the probability any given word is positive
def positivityOfTrainingWords(posDictionary, fullDictionary):
    vocabPos = {} #Dictionary that stores the probability that a word is positive as its value
    for word in fullDictionary:
        fOccurance = fullDictionary[word]
        posProbability = (posDictionary[word]/fOccurance)
        #negProbability = (1 - posProbability) #Got negative occurance until I realised I didn't need it 
        vocabPos[word] = posProbability
        #For testing
        #print(f"The probablility that the word {word} is Positive: {vocabPos[word]} Negative: {(1 - vocabPos[word])}") 
    #
    # input("Hit enter to continue:")
    return vocabPos

def predictTweets2(testTweets, fullDictionary, vocabPos, vocabNeg, posOrNegFile):
    finalVerdict = {} #Dictionary that stores if the algorithm thinks the tweet is positive or negative
    #Initialise varibles used to count how many are predicted positive or negative
    postiveTweets, negativeTweets = 0,0

    #Loops through words in the tweet to find any trained to be positive/negative
    for tweet in testTweets:
        tweetWords = re.split(r"[^\w]", tweet) #Should clean up the special characters.
        posCount = 1
        negCount = 1 #Initialise varibles needed foe the loop
        
        #Loops through each word in the tweet, if it appeared in the trainer it goes through and grabs the probability. Then adds that to the total probability and ups counted words
        for word in tweetWords:
            #if vocabPos.__contains__(word):
            if word in vocabPos.keys():
                if fullDictionary[word] > 1: #Ignores any word that appears onceb
                    posCount *= vocabPos[word]
                    negCount *= vocabNeg[word]
                    
        if posCount > negCount: 
            finalVerdict[tweet] = "Positive"
            postiveTweets +=1

        elif posCount == negCount:
            finalVerdict[tweet] = "Undecided"

        else:
            finalVerdict[tweet] = "Negative"
            negativeTweets += 1

    print("Positive Tweets Identified: ",postiveTweets, "Negative:" ,negativeTweets)
    #-----------------------------------------------
    #Getting Accuracy
    #-----------------------------------------------
    #Counts length of the Count
    #count = len(testTweets)
        
    #Works out the accuracy
    accuracyPos = ((postiveTweets/(postiveTweets + negativeTweets))*100)
    accuracyNeg = ((negativeTweets/(postiveTweets + negativeTweets))*100)
    
    if posOrNegFile == True:
        print(f"The positive accuracy is {accuracyPos}")
        return accuracyPos
    else:
        print(f"The negative accuracy is {accuracyNeg}")   
        return accuracyNeg


    

#It reads in the test data we were given, finds each word from our dictionary and works out from that how likey a tweet is to be positive or negative
def predictTweets(posDictionary, negDictionary, fullDictionary, vocabPos):
    #-------------------------------------------
    #Assigning the likelyhood of a word being Positive/Negative
    #-------------------------------------------
    finalVerdict = {} #Dictionary that stores if the algorithm thinks the tweet is positive or negative
   
    #Opens in file seperated by tweets
    tweetsPos = open("dataFiles/test/testPos.txt", 'r').read().lower().split("\n") 
    tweetsNeg = open("dataFiles/test/testNeg.txt", 'r').read().lower().split("\n")
    #Combines full list of tweets
    #tweets = tweetsPos + tweetsNeg 

    #Initialise varibles used to count how many are predicted positive or negative
    postiveTweets, negativeTweets = 0,0

    #Loops through words in the tweet to find any trained to be positive/negative
    for tweet in tweetsPos:
        tweetWords = re.split(r"[^\w]", tweet) #Should clean up the special characters. TODO: Test this is properly fundtioning
        probOfPos,count, posCount, negCount = 1,0,1,1 #Initialise varibles needed foe the loop
           
        #Loops through each word in the tweet, if it appeared in the trainer it goes through and grabs the probability. Then adds that to the total probability and ups counted words
        for word in tweetWords:
            if vocabPos.__contains__(word):
                count +=1 #counts words considered
                
                if vocabPos[word] > 0.5:
                    posCount *= vocabPos[word]
                elif vocabPos[word] == 0.5:
                    skipOver = 0
                else :
                    negCount *= vocabPos[word]

        if posCount > negCount:
            finalVerdict[tweet] = "Positive"
            postiveTweets +=1
        elif posCount == negCount:
            finalVerdict[tweet] = "Undecided"
        else:
            finalVerdict[tweet] = "Negative"
            negativeTweets += 1


            #print(f"{tweet} is positive")

        #print("The probablility that the whole tweet is Positive is" , probability) #for testing 
        
        #Assigns each tweet Positive or Negative
        #if probOfPos > 0.5:
        #    finalVerdict[tweet] = "Positive"
        #    postiveTweets +=1 
            #print(f"{tweet} is positive")
        #elif probOfPos < 0.5:
        #    finalVerdict[tweet] = "Negative"
        #    negativeTweets += 1
            #print(f"{tweet} is negative")
        #else:
        #    finalVerdict[tweet] = "Undecided"
    print("Positive Tweets Identified: ",postiveTweets, "Negative:" ,negativeTweets)

    #-----------------------------------------------
    #Getting Accuracy
    #-----------------------------------------------
    #Counts length of the Count
    positiveCount = len(tweetsPos)
    #negativeCount = len(tweetsNeg)
    #Works out the accuracy
    accuracyPos = ((postiveTweets/(positiveCount))*100)
    accuracyNeg = ((negativeTweets/(positiveCount))*100)
    print(f"The positive accuracy is {accuracyPos} \nThe negative accuracy is {accuracyNeg}")   

    #-------------------------------------
    #DATA VISUALIZATION 
    #------------------------------------
    #plots the graph
    y_pos = [-1, round(accuracyNeg)]
    object = ('Processed +ve Accuracy', 'Processed -ve Accuracy')
    plot = [accuracyPos, accuracyNeg]
    y_pos = np.arange(len(object))
    plt.bar(y_pos, plot, align='center', alpha=0.1)
    plt.xticks(y_pos, object)
    plt.ylabel("Value")
    plt.xlabel("Data")
    plt.title("Data Visualization")
    plt.show() 


#Reads in the File and sorts it into the dictionary. 
def main():
    #-------------------------------------------
    #READING IN DATA & SETTING UP DICTIONARY : 
    #-------------------------------------------
    #Opens text file in read only  
    posList = readFile("dataFiles/train/trainPos.txt")
    negList = readFile("dataFiles/train/trainNeg.txt")
    
    #Gets rid of special characters
    cleanPosList = formatWords(negList) 
    cleanNegList = formatWords(posList)
    
    #Creates a set of just unique words from the list of words
    uniquePos = set(cleanPosList) 
    uniqueNeg = set(cleanNegList)
    
    #Makes a full list of words from Positive and Negative
    fullSet = uniquePos|uniqueNeg

    #Creates a dictionary setting the value of each fullList to 0 for counting
    posDictionary = dict.fromkeys(fullSet, 0) 
    negDictionary = dict.fromkeys(fullSet, 0)
    fullDictionary = dict.fromkeys(fullSet, 0)
    
    #--------------------------------------------------------
    #GETTING OCCURANCE OF EACH WORD
    #--------------------------------------------------------
    posDictionary = wordOccurance(cleanPosList, posDictionary)
    negDictionary = wordOccurance(cleanNegList, negDictionary)
    #Combined wordcount
    for word in cleanPosList: #For each word in clean_list 
        fullDictionary[word] += 1 
    for word in cleanNegList: #Then also adds in clean_list2
        fullDictionary[word] += 1

    #Printouts for report
    #print(f"The Positive dictionary frequency is {posDictionary}")
    #input("Hit enter to continue")
    #print(f"The Negative dictionary frequency is {negDictionary}")
    #input("Hit enter to continue")
    #print("Full Dictionary is", fullDictionary)

    #----------------------------------------------------------------------------------------------------
    #GETTING PROBABILITY OF A WORD BEING POSITIVE / NEGATIVE
    #----------------------------------------------------------------------------------------------------
    vocabPos = positivityOfTrainingWords(posDictionary, fullDictionary)
    vocabNeg = positivityOfTrainingWords(negDictionary, fullDictionary)
    #print(vocabNeg)
    #-----------------------------------------------------------------------------------
    #PREDICT IF TWEETS ARE POSITIVE OR NEGATIVE & Data Visualization
    #-----------------------------------------------------------------------------------
   
    #Opens in file seperated by tweets
    tweetsPos = open("dataFiles/test/testPos.txt", 'r').read().lower().split("\n") 
    tweetsNeg = open("dataFiles/test/testNeg.txt", 'r').read().lower().split("\n")

    posAccuracy = predictTweets2(tweetsPos, fullDictionary, vocabPos, vocabNeg, True)
    negAccuracy = predictTweets2(tweetsNeg, fullDictionary, vocabPos, vocabNeg, False)
    totalAccuracy = (posAccuracy + negAccuracy/2)
    print(f"The total Accuracy is {totalAccuracy}")
    #predictTweets(posDictionary, negDictionary, fullDictionary, vocabPos) 
    #-------------------------------------
    #DATA VISUALIZATION 
    #------------------------------------
    #plots the graph
    y_pos = [-1, round(negAccuracy)]
    object = ('Processed +ve Accuracy', 'Processed -ve Accuracy')
    plot = [posAccuracy, negAccuracy]
    y_pos = np.arange(len(object))
    plt.bar(y_pos, plot, align='center', alpha=0.1)
    plt.xticks(y_pos, object)
    plt.ylabel("Value")
    plt.xlabel("Data")
    plt.title("Data Visualization")
    plt.show() 


main()




    #----------------------------------------------------------------------------------------------------
    #G E T T I N G  P R O B A B I L I T Y  O F  A  W O R D  A P P E A R I N G  I N  A  G I V E N  L I S T 
    #----------------------------------------------------------------------------------------------------
    #NOTE: this wasn't needed but I misread the spec and wrote the code for it before I realized so I kept it in cause I though it was interesting. 
    #To get it to work just insert it into wordCounter
    
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



