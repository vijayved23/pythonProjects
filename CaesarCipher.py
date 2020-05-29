
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

newText = []

play = True

def getText():
    text = input("Please enter some text in lowercase: ")
    return text
    
def getStep():
    step = input("Please enter a step: ")
    return step

def cipherEncrypt(text,step):
    newStr = ""
    for char in str(text):
        if char in lowercase:
            index = lowercase.index(char)
            cryptingPos = (int(index) + int(step)) % 26
            cryptingLetter = lowercase[cryptingPos]
            newText.append(cryptingLetter)
            newStr += cryptingLetter
    print(newStr)
    return newText  

def cipherDecrypt(text ,step):
    newStr = ""
    for char in str(text):
        if char in lowercase:
            index = lowercase.index(char)
            cryptingPos = (int(index) - int(step)) % 26
            cryptingLetter = lowercase[cryptingPos]
            newText.append(cryptingLetter)
            newStr += cryptingLetter
    print(newStr)
    return newText  


def main():
    q = input("Type 'D' to decrpyt or 'E' to encrypt: ")
    if q == "d" or q =="D":
        cipherDecrypt(getText(), getStep())
    elif  q == "e" or q =="E":
            cipherEncrypt(getText(), getStep())
    playAgain = input("Type 'Y' to use again: ")
    if playAgain == "y" or playAgain == "Y":
        play = True
    else:
        play = False
    while play == True:
        main()
main()

  
