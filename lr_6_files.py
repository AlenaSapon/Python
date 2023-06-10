#5 Скопировать из файла F1 в файл F2 строки,
# начиная с четвертой по порядку.
# Подсчитать количество символов в последнем слове F2.

import os
import regex
try:
    inputFile = "file1.txt"
    readFile = open(inputFile, "r")
    outputFile = "file2.txt"
    writeFile = open(outputFile, "w")
    ReadFileLines = readFile.readlines()
    for line in range(3, len(ReadFileLines)):
            writeFile.write(ReadFileLines[line])
            print(ReadFileLines[line])

    writeFile.close()

    word = open(inputFile, "r")
    last = word.read().split()[-1]
    print("The last word is: " + last +
          ". The count of chars is " + str(len(last)))
    word.close()
except Exception as e:
    print(e)