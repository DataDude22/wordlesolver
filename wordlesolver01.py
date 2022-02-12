#this is going to be a version of the program that i comment along the way, to help focus my workflow.
#opening the initial text file full of potential wordle guesses, naming the raw
with open('wordle list.txt', 'r') as filedata:
    #assign the string of wordle answers to the variable wordle raw
    wordleraw = filedata.read()
    wordlerawlist = wordleraw.split()
    #create empty lists to store user feedback of
    absentletters = []
    presentletters = []
    correctletters = []
    removedwords = []
    possiblewords = []
    #we also need a way to track how many letters have been entered, as well as a way to track the positional relationship of guess count and letter.
    lettercount = 0
    correctletterdict = {}
#now to create a function that takes user input and uses it to generate absent letters, present letters, and correct letters.
    def guesser():
        #set count to 0
        count = 0
        #user inputs their guess
        userinput = input("GUESS:").lower()
        ##we iterate on the individual characters in userinput by passing it to a list
        for letter in list(userinput):
            #increase lettercount to track which character represents which place on the WORDLE matrix.
            count = count + 1
            #Now we need to user to input the status of their guess after submission, and assign it to lettercheck
            lettercheck = int(input('Is ' + letter + ' 1. Absent 2. Present 3. Correct'))
            if lettercheck == 1:
                absentletters.append(letter)
                print(letter + ' added to absent letters list')
            elif lettercheck == 2:
                absentletters.append(letter)
                print(letter + 'added to present letters list')
            elif lettercheck == 3:
                correctletterdict.update({letter: lettercount})
                correctletters.append(letter)
                print(letter + 'added to the correct letters dictionary')
            else:
                print("wtf?")


    #we need a way to narrow down the list of possible results based off which letters are absent, present and correct.
    def deducer():
        for words in wordlerawlist:
            for letters in words:
                if letters in absentletters:
                    removedwords.append(words)







    guesser()
    deducer()
    for entries in wordlerawlist:
        if entries in removedwords:
            print("ignoring removed word.." + entries)
            continue
        else:
            print("Possible word found:" + entries)
            possiblewords.append(entries)

    print(possiblewords)





