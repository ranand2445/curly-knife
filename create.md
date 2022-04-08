{% include navigation.html %}
# Riya Create Task: Typing Game Tester!!!!
## [Video](https://drive.google.com/file/d/1V4CgI6JvoveDZCwnLKqA1N90FTXYzUBP/view)
## [Raw Code](https://github.com/sarayu-pr11/team-narks/commit/cb4b6fc1b84277353f8a67be44492de83cc2e2c2)

# Written Response:
**3a:**
- This program is intended to test the user’s typing ability, by having the user type out a given phrase, and scoring them based on the time taken and accuracy of their entry. The video demonstrates a randomized quote being provided to the user, and the user typing it to the best of their ability. When they hit enter to check, the program provides the correct score percentage and the error score percentage, and which words they missed.The input of the program is the user entry, as they try to type out the quote provided. The output of the program is the scoring of the user’s ability because it displays the users’ accuracy percentages and words they missed. 

**3b:** (i) 
  ```
def splitStringsIntoList(userString):

 .....

    # get the global list of words in user string using space as tokenizer
    global userList
    userList = userString.split(" ")
    # User entered string =  Oprah Winfrey : Be thankful for what you have; you'l end up having more.
    # userString =  ['Oprah', 'Winfrey', ':', 'Be', 'thankful', 'for', 'what', 'you', 'have;', "you'l", 'end', 'up', 'having', 'more.']

    #assign global variable to the user  string word count
    global userCount
    userCount = len(userList)

    #get the minumum of word count between quote provided and User entry
    minWordCount = quoteCount

    #check if minCount is greater than userCount and if so, assign userCount to minCount
    if minWordCount > userCount:
        minWordCount = userCount

    return minWordCount
  ```
**3b:** (ii) 
  ```
def compareQuoteToUserString(userInputString, metricChoice):
....
    else:
        while loopIndex < minCount:
            if quoteList[loopIndex] == userList[loopIndex]:
                correctList.append(userList[loopIndex])
            else:
                print("Error! : ", userList[loopIndex], " : at word# =>", loopIndex)
                errorScore = errorScore + 1
                errorList.append(userList[loopIndex])
            loopIndex += 1
        return errorScore
   ```
- The name of the list being used is called “userList”, and the list/array contains the tokenized words from the user typed back entry string, based on the randomized reference quote provided. When the program is executed, the users’ entry string is tokenized into a list (“userList”) of words using space as a delimiter. This list is then compared to the tokenized quote list (“quoteList”). The number of words in the “userList” is dependent on the length of the reference quote string. This word count is used as the exit condition for the loop that compares the individual words in the “userList” and the “quoteList”. Essentially, these new tokenized lists are compared and used to measure the users’ input string correctness. Without these tokenized lists, we would have to parse through the individual characters for the entire input string, and do a character by character comparison.

**3c**(i)
  ```
    def compareQuoteToUserString(userInputString, metricChoice):

    # call procedure to split strings based on space tokens
    global minCount
    minCount = splitStringsIntoList(userInputString)

    # loop through quoteSplit list and userSplit list and compare each word in it
    # loopIndex is the incremental counter to execute the loop
    # compare words in quoteList to user list to check for errors,  using the loopIndex as the array element index
    #after comparison, we go to the second word by increasing loopIndex
    #we stop the loop when loopIndex == minCount

    #global variables accessed in function
    global correctList
    global errorList
    global typingSpeed
    global userCount
    global quoteCount

    #local variables
    loopIndex = 0
    errorScore = 0

    if metricChoice == 'T':
        #calculate time it took for user input
        timeTaken = endTime - startTime
        return timeTaken
    else:
        while loopIndex < minCount:
            if quoteList[loopIndex] == userList[loopIndex]:
                correctList.append(userList[loopIndex])
            else:
                print("Error! : ", userList[loopIndex], " : at word# =>", loopIndex)
                errorScore = errorScore + 1
                errorList.append(userList[loopIndex])
            loopIndex += 1
        return errorScore
    
 ```
**3c**(ii) 
  ```
  while True:
    ....
**    userScore = compareQuoteToUserString(userString, metricChoice)**

    #Based on user's choice of what to measure, display the appropriate scores.

    if metricChoice == 'A':
        # 3. display error score
        displayErrorList(userScore)
        calculatePercentages(userScore, False)

        # 4. display correct score
        correctCount = displayCorrectScore(userScore)
        calculatePercentages(correctCount, True)
    else:
        #calculate the speed of typing - total words in reference quote over user time taken
        wordsPerMinute = quoteCount/userScore
        print("\n" + "Time Taken = ", userScore, "Words/Minute = ", wordsPerMinute)
   ```
- Depending on if the user chooses time or accuracy, the procedure will run differently. If the user picks a test time, the procedure will compare the initial time to final time. If the user picks accuracy, this procedure loops through the reference quote tokenized word list and through the users’ tokenized word list and compares the word in the respective position for an exact match. Upon match, correct words are collected in one list, and incorrect in another. Another feature of this procedure is that it tracks the error score based on the incorrect words detected. 

- When the user selects ‘T ' for time, the procedure calculates the time taken by subtracting final and initial time. If the user selects ‘A’ for accuracy, the procedure, “compareQuoteToUserString” takes “userInputString” as an input parameter. This parameter contains the user typed entry string. One of the first things “compareQuoteToUserString” does is call the function“splitStringsIntoList(userInputString)” which splits the “userInputString” into its individual words using space as a delimiter. The individual words are stored in another list called “userList”. The “splitStringsIntoList” also tokenizes the reference quote string into its individual words using space as a delimiter. The individual words are stored in “quoteList”. The “splitStringsIntoList” returns the minimum word count between the two tokenized lists. Next, we loop through the two lists until the minimum word count is reached. At each iteration, using the ‘loopIndex’ as the word index in the lists, we compare the words in the ‘quoteList’ and the ‘userList’. This allows us to check for errors on a per word basis in the user string. The matched and unmatched words are stored in separate lists and displayed to the user for feedback. The procedure also calculates the error count to measure user accuracy percentage.

**3d:** 
- The first call is in the while true loop, and the first run through, the user may select 'A', and the "_compareQuoteString_" gets called. The next run through they may choose 'T' and then the while true loop executes again, "_compareQuoteString_" is called again, and executes the a different portion of code. In the case that the user selects 'A', the code of comparing the user's tokenized word list to the quote's tokenized word list, is executed, and displays the error and correct score percentages, and is also checking the conditions of the User's metric choice. In the user's second call, if they select 'T' a different portion of the  "_compareQuoteString_"  is executed, as it checks the time taken to type out the entry.
