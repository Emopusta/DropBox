"""daha fazla yapılabilir"""
maximumAsciiValue=127 
"""ascii yani decimal bir sayıyı binary sayıya çevirme fonksiyonu"""
def AsciiToBinary(asciiNum):
    binNumber = ""
    while asciiNum>0:
        if asciiNum%2==1:
            binNumber+="1"
        else:
            binNumber+="0"
        asciiNum //=2
    while len(binNumber)%4 != 0:
        binNumber+="0"
    return binNumber [::-1]

    """XORFunc adından da anlaşılacağı üzere string binary sayıyı alır ve XORlanmış halini geri döndürür
örnek: XORFunc("101010101010") returns "010101010101" """
def XORFunc(BinaryNum):
    xoredBinaryNum = ""
    for i in BinaryNum:
        if i=="0":
            xoredBinaryNum += "1"
        else:
            xoredBinaryNum += "0"
    return xoredBinaryNum

"""binary bir sayıyı decimal sayıya çevirme fonksiyonu"""
def BinaryToAscii(binaryNum):
    counter = 0
    total=0
    for i in binaryNum[::-1]:
        if i == "1":
            total += pow(2,counter)
        counter+=1
    return total

"""Brut Force XOR ve girilen key ile çarpma kullanılarak yaptığım encryption algoritması"""
"""Algoritma düzenlenebilir ancak Big(O) = 4n olduğu için henüz düzenlemeye öncelik vermedim."""
def EmopEncryption(text,key):
    temp = []
    bin_lst = []
    xor_lst = []
    asci_lst = []
    chr_lst = []
    emopText = ""
    for i in text:
        temp.append(ord(i))
        bin_lst.append(AsciiToBinary((ord(i)*key)))
    for i in bin_lst:
        xor_lst.append(XORFunc(i))
    for i in xor_lst:
        asci_lst.append(hex(BinaryToAscii(i)))
    for i in asci_lst:
        chr_lst.append(i)
        emopText += str(i) + " "
    return emopText

"""EmopEncryption algoritmasının Decryption algoritması"""
"""Algoritma düzenlenebilir ancak Big(O) = 5n olduğu için henüz düzenlemeye öncelik vermedim."""
def EmopDecryption(cryptedText,key):
    bin_lst = []
    xor_lst = []
    asci_lst = []
    chr_lst = []
    emopText = ""
    counter=0
    hexanum = ""
    x=0
    deneme_lst = cryptedText.split(" ")
    deneme_lst.pop() 
    for i in deneme_lst:
        a = str(i)
        base16INT = int(a, 16)
        bin_lst.append(base16INT)
    for i in bin_lst:
        xor_lst.append(XORFunc(AsciiToBinary(i)))
    for i in xor_lst:
        asci_lst.append(BinaryToAscii(i))
    for i in asci_lst:
        chr_lst.append(int(i/key))
    for i in chr_lst:
        if i!=0:
            emopText += chr(i)
        else:
            emopText += " "
    
    return emopText


def EncrpytFile(fileAddress,key):
    with open(fileAddress,"r") as f:
        text = f.read()
    encryptedText = EmopEncryption(text,key)
    with open(fileAddress,"w") as f:
        f.write(encryptedText)


def DecryptFile(fileAddress,key):
    with open(fileAddress,"r") as f:
        encryptedText = f.read()
    text = EmopDecryption(encryptedText,key)
    with open(fileAddress,"w") as f:
        f.write(text)

def EncryptFileName(fileName,key):
    increaseVar = (key%3)+1
    newName = ""
    for i in fileName:
        newName+= chr(ord(i)+increaseVar)
        
    return newName

#text = "Merhaba Ben Emre."
key = 123

#EncrpytFile(key)
#DecryptFile(key)



