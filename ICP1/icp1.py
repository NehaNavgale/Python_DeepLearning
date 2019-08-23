# function to delete last two char
def deletechar(s):
    if len(s) == 0:
        return s
    else:
        return s[:-2]

# function to reverse the string
def reversestring(s):
    if len(s) == 0:
        return s
    else:
        return s[::-1]

# function to add two numbers
def addNumbers(num1, num2):
    return num1+num2

# function to replace python word with pythons
def replaceWord(s):
    if len(s) == 0:
        return s
    else:
        return s.replace('python', 'pythons')


# creating an empty list
lst = []

# number of elemetns as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    inputStr = input()

    lst.append(inputStr)  # adding the element

print(lst)

# code to get the input and delete first two character
# inputString = input("Enter Input String: ")
deletedString = deletechar(lst)
print('Input String with 2 char deleted: ', deletedString)

# code to reverse the new string
reverseOutput = reversestring(deletedString)
print('Reverse input string: ', reverseOutput)

# code to join list
joiningString = ""

for x in reverseOutput:
    joiningString += x

print(joiningString)

# code to get two numbers and add it
print('Add two numbers: ')
inputNumberOne = int(input("Enter first number: "))
inputNumberTwo = int(input("Enter second number: "))
additionOutput = addNumbers(inputNumberOne, inputNumberTwo)
print('addition of two number: ', additionOutput)

# code to replace word with another one
print('Replace input string')
inputStringToReplace = input("Enter String: ")
replaceOutput = replaceWord(inputStringToReplace)
print('Replace String: ', replaceOutput)








