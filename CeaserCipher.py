#Caesar cipher encryption program--------------------------------------
print("welcome to Caesar cipher encryption program")
plaintext=input("Enter the plaintext: ")
key=input("Enter the key: ")

#Copenents of the code--------------------------------------------------
AlphabetLower="abcdefghijklmnopqrstuvwxyz"
AlphabetUpper=AlphabetLower.upper()
try: #exception handeling
    key=int(key)
except ValueError:
    key = int(input("Value Error, Enter an integer key: "))
#Upper or lower case function tester------------------------------------
def isLowerUpper(letter):
    if letter in AlphabetLower:
        return 0
    elif letter in AlphabetUpper:
        return 1
    else:
        return 2
#Alphabet position finder-----------------------------------------------
def letterPos(letter, Alphabet):
    for j in range(25):
        if letter==Alphabet[j]:
            return j
#Encryption function----------------------------------------------------
def caesarEncryption(plaintext, key):
    ciphertext=""
    for i in range(len(plaintext)):
        letter=plaintext[i]
        if isLowerUpper(letter)==0:#lowercase
            pos=letterPos(letter, AlphabetLower)
            shift=key+pos
            if shift>=25: #in case we exceeded the index range we go back to the beginning
                shift=shift-25
            ciphertext+=AlphabetLower[shift]
        elif isLowerUpper(letter)==1: #uppercase
            pos=letterPos(letter, AlphabetUpper)
            shift=key+pos
            if shift>=25: #in case we exceeded the index range we go back to the beginning
                shift=shift-25
            ciphertext+=AlphabetUpper[shift]
        else:
            ciphertext+=letter
    return ciphertext
ciphertext=caesarEncryption(plaintext, key)
print("The ciphertext is: " + ciphertext)
