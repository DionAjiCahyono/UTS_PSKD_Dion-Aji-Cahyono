import math
print('Nama  : Dion Aji Cahyono')
print('Nim   : V3920018')
print('kelas : TI D')
print('-----------------------------------')
plaintext = input("Plaintext : ")
key, keyA, keyB = input("Kunci Alphabet : "), int(
    input("kunci 1 : ")), int(input("kunci 2 : "))

def keyakses(Plaintext, key):
    key = list(key)
    if len(key) == len(Plaintext):
        return key
    else:
        for x in range(len(Plaintext)-len(key)):
            key.append(key[x % len(key)])
        key = ''.join(key)
        return key
def ENvignere(plaintext, key):
    key = keyakses(plaintext, key)
    plaintext = list(plaintext)
    enkripsi = []
    for x in range(len(plaintext)):
        if plaintext[x].isalpha():
            if plaintext[x].isupper():
                first_alph = ord("A")
                convert = (ord(plaintext[x]) - first_alph) + \
                    (ord(key[x].upper()) - first_alph)
                hasil = convert % 26
                hasil = chr(hasil + first_alph)
                enkripsi.append(hasil)
            if plaintext[x].islower():
                first_alph = ord("a")
                convert = (ord(plaintext[x]) - first_alph) + \
                    (ord(key[x].lower()) - first_alph)
                hasil = convert % 26
                hasil = chr(hasil + first_alph)
                enkripsi.append(hasil)
        else:
            enkripsi.append(plaintext[x])

    return "".join(enkripsi)
def DEKvignere(chipertext, key):
    key = keyakses(chipertext, key)
    plaintext = list(chipertext)
    dekripsi = []
    for x in range(len(plaintext)):
        if plaintext[x].isalpha():
            if plaintext[x].isupper():
                first_alpha = ord("A")
                convert = (ord(plaintext[x]) - first_alpha) - \
                    (ord(key[x].upper()) - first_alpha)
                hasil = convert % 26
                hasil = chr(hasil + first_alpha)
                dekripsi.append(hasil)
            if plaintext[x].islower():
                first_alpha = ord("a")
                convert = (ord(plaintext[x]) - first_alpha) - \
                    (ord(key[x].lower()) - first_alpha)
                hasil = convert % 26
                hasil = chr(hasil + first_alpha)
                dekripsi.append(hasil)
        else:
            dekripsi.append(plaintext[x])

    return "".join(dekripsi)
# +++++++++++++++++++ Proses pada  Affine Cipher
def CheckMMI(keyA):
    n = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    for i in n:
        looping = (keyA * i) % 26
        if looping == 1:
            return i
def EnkripsiAffine(plaintext, keyA, keyB):
    hasil = []
    for x in plaintext:
        if x.isalpha():
            if x.isupper():
                Tipe = ord("A")
                perkata = ord(x)
                sistem = perkata - Tipe
                sistemKU = keyA*sistem+keyB
                mod = sistemKU % 26
                finals = chr(mod + Tipe)
                hasil.append(finals)
            else:
                Tipe = ord("a")
                perkata = ord(x)
                sistem = perkata - Tipe
                sistemKU = keyA*sistem+keyB
                mod = sistemKU% 26
                finals= chr(mod + Tipe)
                hasil.append(finals)
        else:
            hasil.append(x)
    return ''.join(hasil)

def DeskripsiAffine(plaintext, keyA, keyB):
    hasil = []
    y = CheckMMI(keyA)
    for x in plaintext:
        if x.isalpha():
            if x.isupper():
                Tipe = ord("A")
                perkata = ord(x)
                sistem = perkata - Tipe
                sistemKU = y*(sistem-keyB)
                mod = sistemKU % 26
                finals = chr(mod + Tipe)
                hasil.append(finals)
            else:
                Tipe = ord("a")
                perkata = ord(x)
                sistem= perkata - Tipe
                sistemKU = y*(sistem-keyB)
                mod = sistemKU % 26
                finals = chr(mod + Tipe)
                hasil.append(finals)
        else:
            hasil.append(x)
    return ''.join(hasil)


if math.gcd(keyA, 26) == 1:
    print("Vigenere Chiper --------------------------------------")
    print("Plaintext : " + plaintext)
    print("Key : " + key)
    vignereEN = ENvignere(plaintext, key)
    affineEN = EnkripsiAffine(vignereEN, keyA, keyB)
    print("Kombinasi Vignere and affine: " + affineEN)

    print("Affine Chiper ----------------------------------------")
    print("Key A : " + str(keyA))
    print("Key B : " + str(keyB))
    affinelove = DeskripsiAffine(affineEN, keyA, keyB)
    vignerelove = DEKvignere(affinelove, key)
    print("Deskripsi : " + vignerelove)
    print("--------------------------------------------")
    print("Alhamdullilah")

else:
    print("Kunci A Tidak valid Bung")
