import random
#global var
symbols = ("`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=",
           "+", "[", "{", "]", "}", ";", ":", "'", '"', ",", "<", ".", ">", "/", "?", "|", "")
letters = ("asdfghjklzxcvbnmqwertyuiop")

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

def askLength():
    global passLength
    print("Enter the passphrase Length")
    passLength = input()
    while passLength.isnumeric() == False:
        print("Please enter a valid number")
        passLength = input()
    else: passLength = int(passLength)
    while passLength <= 0 :
        print("Please enter a valid number")
        passLength = input()

def incNumber():
     # numbers
    print("Include Numbers? (y/n)")
    includeNumber = input()
    while includeNumber != "y" and includeNumber != "n":
        print("please enter y for yes and n for no")
        print("Include Numbers? (y/n)")
        includeNumber = input()
    if includeNumber == "y":
        functions.append(addNumber)
        global noCharacter
        noCharacter = True
def incUpper():
    # upper case
    print("Include Upper Case? (y/n)")
    includeUpperCase = input()
    while includeUpperCase != "y" and includeUpperCase != "n":
        print("please enter y for yes and n for no")
        print("Include Upper Case? (y/n)")
        includeupperCase = input()
    if includeUpperCase == "y":
        functions.append(addUpperCase)
        global noCharacter
        noCharacter = True
def incLower():
    print("Include Lower Case? (y/n)")
    includeLowerCase = input()
    while includeLowerCase != "y" and includeLowerCase != "n":
        print("please enter y for yes and n for no")
        print("Include Lower Case? (y/n)")
        includeLowerCase = input()
    if includeLowerCase == "y":
        functions.append(addLowerCase)
        global noCharacter
        noCharacter = True
def incSymbol():
    print("Include Symbols? (y/n)")
    includeSymbol = input()
    while includeSymbol != "y" and includeSymbol != "n":
        print("please enter y for yes and n for no")
        print("Include Symbols? (y/n)")
        includeSymbol = input()
    if includeSymbol == "y":
        functions.append(addSymbol)
        global noCharacter
        noCharacter = True

    

# generator loop
while True:
    changeConfig = "y"
    while changeConfig == "y":
        functions = []
        passLength = 0
        noCharacter = False
        askLength()
        incLower()
        incUpper()
        incNumber()
        incSymbol()
        while noCharacter == False:
            print("You need to at least allow one type of chracater")
            incLower()
            incUpper()
            incNumber()
            incSymbol()
        again = "y"
        while again == "y":
            print(generate(passLength))
            print("Generate a New Passphrase?(y/n)")
            again = input()
            while again != "y" and again != "n":
                print("Please Enter y for Yes and n for No")
                again == input()
        print("Would you like to chagne the configuration?(y/n)")
        changeConfig = input()
        while changeConfig != "n" and changeConfig != "y":
            print("Please enter y for yes and n for no")
            changeConfig = input()
    else: print("Thanks")
    break