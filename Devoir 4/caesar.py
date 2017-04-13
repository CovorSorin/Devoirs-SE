# Caesar cipher and decipher
def caesar(plainText, shift): 
        cipherText = ""
        for ch in plainText:
                ch = ch.lower()
                if ch == ' ':
                    cipherText += ' '
                if ch.isalpha():
                        stayInAlphabet = ord(ch) + shift 
                        if stayInAlphabet > ord('z'):
                                stayInAlphabet -= 26
                        finalLetter = chr(stayInAlphabet)
                        cipherText += finalLetter
        print "Shift:", shift, cipherText
        return cipherText

def decaesar(plainText, shift): 
        cipherText = ""
        for ch in plainText:
                ch = ch.lower()
                if ch == ' ':
                    cipherText += ' '
                if ch.isalpha():
                        stayInAlphabet = ord(ch) - shift
                        print stayInAlphabet
                        if stayInAlphabet < ord('a'):
                                diff = stayInAlphabet + shift - ord('a')
                                stayInAlphabet = diff + ord('a') + 26 - shift 
                        if stayInAlphabet > ord('z'):
                                stayInAlphabet -= 26                   
                        finalLetter = chr(stayInAlphabet)
                        cipherText += finalLetter
        print "Shift:", shift, cipherText
        return cipherText
