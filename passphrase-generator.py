import random
#global var
global again
symbols = ("`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=",
           "+", "[", "{", "]", "}", ";", ":", "'", '"', ",", "<", ".", ">", "/", "?", "|", "")
letters = ("asdfghjklzxcvbnmqwertyuiop")

print(len(letters))
print("Passphrase Generator")
print("By Sepehr Sahraian")
print("AP CSP Class")
#generator functions

def addUpperCase():
    letterSelected = letters[random.randint(0, 25)]
    return letterSelected.upper()

def addLowerCase():
    letterSelected = letters[random.randint(0, 25)]
    return letterSelected

def addNumber():
    return str(random.randint(0, 9))

def addSymbol():
    return random.choice(symbols)

def generate(length):
    passphrase = ""
    for n in range(length):
        generated = random.choice(functions)()
        passphrase = passphrase + generated
    return passphrase
        

    

# generator loop
while True:
    functions = []
    passLength = 0
    # lower case
    print("Enter the passphrase Length")
    passLength = int(input())
    while passLength <= 0:
        print("Please enter a valid number")
        passLength == input()
    print("Include Lower Case? (y/n)")
    includeLowerCase = input()
    while includeLowerCase != "y" and includeLowerCase != "n":
        print("please enter y for yes and n for no")
        print("Include Lower Case? (y/n)")
        includeLowerCase = input()
    if includeLowerCase == "y":
        functions.append(addLowerCase)
    # upper case
    print("Include Upper Case? (y/n)")
    includeUpperCase = input()
    while includeUpperCase != "y" and includeUpperCase != "n":
        print("please enter y for yes and n for no")
        print("Include Upper Case? (y/n)")
        includeupperCase = input()
    if includeUpperCase == "y":
        functions.append(addUpperCase)
    # symbols
    print("Include Symbols? (y/n)")
    includeSymbol = input()
    while includeSymbol != "y" and includeSymbol != "n":
        print("please enter y for yes and n for no")
        print("Include Symbols? (y/n)")
        includeSymbol = input()
    if includeSymbol == "y":
        functions.append(addSymbol)
    # numbers
    print("Include Numbers? (y/n)")
    includeNumber = input()
    while includeNumber != "y" and includeNumber != "n":
        print("please enter y for yes and n for no")
        print("Include Numbers? (y/n)")
        includeNumber = input()
    if includeNumber == "y":
        functions.append(addNumber)
    again = "y"
    while again == "y":
        print(generate(passLength))
        print("Generate a New Passphrase?(y/n)")
        again = input()
        if again != "y" and again != "n":
            print("Please Enter y for Yes and n for No")
            again == input()
    break