from console import *
import os
import platform
import random

trys = 0;
word = None;
memoryArray = [];
allWords = open("words.txt").read().splitlines()

def startGame():
    global trys, word, memoryArray;

    trys = 0
    word = randomWord()
    memoryArray = []

def verifyWord(string):
    global word
    string = string.upper()

    resultString = ""
    checkWord = (string == word)

    if checkWord:
        resultString += f"{bColors.OKGREEN}{word}{bColors.ENDC}"
        return resultString

    for x in range(len(string)):
        char = string[x]
        checkChar = char in word
        
        if checkChar:
            if char == word[x]:
                resultString += f"{bColors.OKGREEN}{char}{bColors.ENDC}"
            else:
                resultString += f"{bColors.WARNING}{char}{bColors.ENDC}"
        else:
            resultString += f"{char}"

    return resultString

def restart():
    incorrectPrompt = True
    while incorrectPrompt:
        restart = input("Do you want to play again? (Y/N) ").upper()
        if restart == "Y" or restart == "N":
            incorrectPrompt = False

    if restart == "Y":
        startGame()
    else: 
        os._exit(os.EX_OK)

def randomWord():
    index = random.randint(0, len(allWords)-1)
    return allWords[index].upper()
    
while True:
    startGame()
    while trys < 6:
        wordInput = input(f"({len(word)}) Enter your guess: ").upper()
        result = verifyWord(wordInput)

        system = platform.system()
        if system == "Windows":
            os.system('cls')
        else:
            os.system('clear')

        memoryArray.append(result)
        for value in memoryArray:
            print(value)
        
        if wordInput.upper() == word:
            print(f"\n{bColors.BOLD}Congrats! You found the word!")
            restart()
        else:
            trys += 1

    print(f"\nThe word was {word}")
    restart()