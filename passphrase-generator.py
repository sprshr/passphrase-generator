import random
symbols = ("`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=",
           "+", "[", "{", "]", "}", ";", ":", "'", '"', ",", "<", ".", ">", "/", "?", "|", "")
letters = ("asdfghjklzxcvbnmqwertyuiop")

print(len(letters))
print("Passphrase Generator")
print("By Sepehr Sahraian")
print("AP CSP Class")


def selectLetter(case):
    letterSelected = letters[random.randint(0, 25)]
    if case == "upper":
        return letterSelected.upper()
    else:
        return letterSelected


# generator loop
while True:
    functions = []

    # lower case
    print("Include Lower Case? (y/n)")
    includeLowerCase = input()
    while includeLowerCase != "y" and includeLowerCase != "n":
        print("please enter y for yes and n for no")
        print("Include Lower Case? (y/n)")
        includeLowerCase = input()
    # upper case
    print("Include Upper Case? (y/n)")
    includeupperCase = input()
    while includeupperCase != "y" and includeupperCase != "n":
        print("please enter y for yes and n for no")
        print("Include Upper Case? (y/n)")
        includeupperCase = input()
    # symbols
    print("Include Symbols? (y/n)")
    includeSymbol = input()
    while includeSymbol != "y" and includeSymbol != "n":
        print("please enter y for yes and n for no")
        print("Include Symbols? (y/n)")
        includeSymbol = input()
    # numbers
    print("Include Numbers? (y/n)")
    includeNumber = input()
    while includeNumber != "y" and includeNumber != "n":
        print("please enter y for yes and n for no")
        print("Include Numbers? (y/n)")
        includeNumber = input()
