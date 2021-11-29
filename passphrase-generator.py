import random
symbols = ("`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=",
           "+", "[", "{", "]", "}", ";", ":", "'", '"', ",", "<", ".", ">", "/", "?", "|", "")
letters = ("asdfghjklzxcvbnmqwertyuiop")

print(len(symbols))
print("Passphrase Generator")
print("By Sepehr Sahraian")
print("AP CSP Class")

while True:
    functions = []

    # lower case
    print("Include Lower Case? (y/n)")
    lowerCase = input()
    while lowerCase != "y" and lowerCase != "n":
        print("please enter y for yes and n for no")
        print("Include Lower Case? (y/n)")
        lowerCase = input()
    # upper case
    print("Include Upper Case? (y/n)")
    upperCase = input()
    while upperCase != "y" and upperCase != "n":
        print("please enter y for yes and n for no")
        print("Include Upper Case? (y/n)")
        upperCase = input()
    # symbols
    print("Include Symbols? (y/n)")
    symbol = input()
    while symbol != "y" and symbol != "n":
        print("please enter y for yes and n for no")
        print("Include Symbols? (y/n)")
        symbol = input()
    # numbers
    print("Include Numbers? (y/n)")
    number = input()
    while number != "y" and number != "n":
        print("please enter y for yes and n for no")
        print("Include Numbers? (y/n)")
        number = input()
