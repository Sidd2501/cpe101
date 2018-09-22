from funcs import *


def main():
    string = userInput()
    words = userWord()
    print()
    print()
    printMatrix(string)
    print()
    print()
    split_words = words.split()
    for word in split_words:
        if checkForward(string, word) is not None:
            print(checkForward(string, word))
        elif checkBackward(string, word) is not None:
            print(checkBackward(string, word))
        elif checkDown(string, word) is not None:
            print(checkDown(string, word))
        elif checkUp(string, word) is not None:
            print(checkUp(string, word))
        else:
            print(word, ": word not found")


if __name__ == "__main__":
    main()
