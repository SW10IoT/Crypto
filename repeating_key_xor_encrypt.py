from binascii import hexlify

def encrypt(plaintext, key):
    s = ''
    keylength = len(key)
    for i in range(len(plaintext)):
        s += chr(ord(plaintext[i]) ^ ord(key[i % keylength]))
    return s

def decrypt(plaintext, key):
    return encrypt(plaintext, key)


def do_stuff():
    l1 = "Burning 'em, if you ain't quick and nimble"
    print(l1)
    s=encrypt(l1,"ICE")
    h= hexlify(s.encode('ascii'))
    print(h)
    print(decrypt(s,'ICE'))
