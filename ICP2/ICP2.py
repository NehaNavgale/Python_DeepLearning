def main():
    print("Task to convert LBs to KGs")
    convertLBToKG()
    input("Press enter")
    print("Task to return alternate char from string")
    string_alternative()
    input("Press enter")
    print("Task to find word count in a file")
    wordCount()

# function to convert LB to KG
def convertLBToKG():
    studentNo = int(input("Enter number of students = "))
    weightInLB = [(int(input("Enter weight for student :"))) for x in range(studentNo)]
    print(weightInLB);
    weightInKG = [("{: .2f}".format(float(weightInLB[i]*0.453592))) for i in range(studentNo)]
    print(weightInKG)

# function to return alternate char from string
def string_alternative():
    strInput = input("Enter string: ")
    strOutput = strInput[::2]
    print(strOutput)

# function to find wordcount in a file
def wordCount():
    inputFile = open("wordCountInOut.txt", "r")
    data = inputFile.read()
    data = data.split()
    print(data)
    wordList = {}
    for word in data:
        word = word.casefold()
        if word not in wordList:
            wordList[word] = 0
        wordList[word] += 1
    print(wordList)

    with open('wordCountInOut.txt', 'a') as file:
        for key in wordList:
            file.write(str(key) + " : " + str(wordList[key]) + "\r\n")


if __name__ == "__main__":
    main()