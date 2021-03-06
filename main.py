import random
#global var
symbols = ("`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-",
           "_", "=", "+", "[", "{", "]", "}", ";", ":", "'", '"', ",", "<",
           ".", ">", "/", "?", "|", "")
letters = ("asdfghjklzxcvbnmqwertyuiop")

print("Passphrase Generator")
print("By Sepehr Sahraian")
print("AP CSP Class")


# This function asks for the length of the passphrase
def askLength():
    global passLength
    print("Enter the passphrase Length")
    passLength = input()
    while passLength.isnumeric() == False:
        print("Please enter a valid number")
        passLength = input()
    else:
        passLength = int(passLength)
    while passLength <= 0:
        print("Please enter a valid number")
        passLength = input()


# Whehter or not include lower case letters
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
        noCharacter = False


# Whehter or not include upper case letters
def incUpper():
    print("Include Upper Case? (y/n)")
    includeUpperCase = input()
    while includeUpperCase != "y" and includeUpperCase != "n":
        print("please enter y for yes and n for no")
        print("Include Upper Case? (y/n)")
        includeupperCase = input()
    if includeUpperCase == "y":
        functions.append(addUpperCase)
        global noCharacter
        noCharacter = False


# Whehter or not include numbers
def incNumber():
    print("Include Numbers? (y/n)")
    includeNumber = input()
    while includeNumber != "y" and includeNumber != "n":
        print("please enter y for yes and n for no")
        print("Include Numbers? (y/n)")
        includeNumber = input()
    if includeNumber == "y":
        functions.append(addNumber)
        global noCharacter
        noCharacter = False


# Whehter or not include symbols
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
        noCharacter = False


# generator functions

# This function returns a random upper case letter
def addUpperCase():
    letterSelected = letters[random.randint(0, 25)]
    return letterSelected.upper()


# This function returns a random lower case letter
def addLowerCase():
    letterSelected = letters[random.randint(0, 25)]
    return letterSelected


# This function returns a random one digit number
def addNumber():
    return str(random.randint(0, 9))


# This function returns a random symbol
def addSymbol():
    return random.choice(symbols)


# This function is exectued based on Length and combines all the returned value(s) from function above
def generate(length):
    passphrase = ""
    if length > 1000000:
        print("It might take longer than usual, please wait")
    for n in range(length):
        generated = random.choice(functions)()
        passphrase = passphrase + generated
    return passphrase


# generator loop
while True:
    changeConfig = "y"
    while changeConfig == "y":
        functions = []
        passLength = 0
        noCharacter = True
        askLength()
        incLower()
        incUpper()
        incNumber()
        incSymbol()
        while noCharacter == True:
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
                again = input()
        print("Would you like to chagne the configuration?(y/n)")
        changeConfig = input()
        while changeConfig != "n" and changeConfig != "y":
            print("Please enter y for yes and n for no")
            changeConfig = input()
    else:
        print("Thanks")
    break
