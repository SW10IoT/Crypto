import binascii

h = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
jokes = b'ETAOIN SHRDLU'

jokes_hex = binascii.hexlify(jokes)

def brute_force(some_input):
    splittet = [some_input[i:i+2] for i in range(0, len(some_input), 2)]
    print(splittet)
    for x in range(0, 127):
        s = list()
        for v in splittet:
            s.append(chr(int(v,16) ^ x))
        print(str(x) + ':' + chr(x) + '  :  ' + ''.join(s))
        print('')

brute_force(jokes_hex)
