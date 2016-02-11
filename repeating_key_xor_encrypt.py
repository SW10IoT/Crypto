def encrypt(plaintext, key):
    s = ' '
    keylength = len(key)
    for i in range(len(plaintext)):
        s += chr( ord(plaintext[i]) ^ ord(key[i % keylength]))

    print(s)

l1 = "Burning 'em, if you ain't quick and nimble"


encrypt(l1,"ICE")
