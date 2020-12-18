import random

#put file datas into a list
myFile = open("words.txt", "r+")
data = myFile.read()
wordsLibrary = data.split()

#choose a random word in the list
wordNumber = random.randint(0, len(wordsLibrary)-1)
word = wordsLibrary[wordNumber]
emptyWord = ["_"]*len(word)

#nbr of tries (allowing 6 wrong guesses)
tryCount = 7

#---------------------- FUNCTION ----------------------#

#request the user to put a letter
def guess():
    try:
        while True:
            inputLetter = input("Choose a letter : ").upper()
            if inputLetter.isalpha() and len(inputLetter) == 1: #single+letter
                break
            else:
                print("You didn't write a single letter, don't you ?")
                
        return inputLetter

    except Exception as e:
            print("Error :", e)
            guess()

#search if letter is in the word
def match(word, letter):
    indexPos = []
    for index, char in enumerate(word):
        if char == letter:
            indexPos.append(index)
    if len(indexPos) >= 1:
        return True, letter, indexPos
    else:
        return False, letter, indexPos

#replace letters at the right position
def replaceLetter(emptyWord, letter, pos):
    index = 0
    while index < len(pos):
        emptyWord[pos[index]] = letter
        index += 1
    return emptyWord


#------------------------ CORE ------------------------#

#uncomment if you want to test with the word written
print(word)

print("Hangman is starting...")
print(' '.join(map(str, emptyWord)))

while tryCount > 0:
    inputLetter_ = guess()
    #print(inputLetter_)
    
    match_ = match(word, inputLetter_)
    #print(match_)
    
    if match_[0] == True:
        fetch = replaceLetter(emptyWord, match_[1], match_[2])
        print(' '.join(map(str, fetch)))

        if "_" not in fetch:
            print("c'est gagné !")
            break
    else:
        tryCount -= 1
        print(tryCount)
        if tryCount == 0:
            print("C'est grillé !")
            break

print("Partie terminée !")



