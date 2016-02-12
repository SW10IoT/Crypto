import binascii

h = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
jokes = b'ETAOIN SHRDLU'

jokes_hex = binascii.hexlify(jokes)


def load_file():
    with open('encrypted.txt') as f:
        hex_values = list()
        for line in f:
            hex_values.append(line.rstrip('\n'))
    return hex_values

def evaluate_decryption(decryptet_message):
    score = 0
    for c in decryptet_message:
        x = ord(c)
        if x < 32:
            score -= 5
        if x == 32:
            score += 10
        elif (x > 32 and x < 65) or (x > 90 and x < 97) or (x > 122):
            score += 1
        elif (x > 64 and x < 91) or (x > 96 and x < 123):
            score += 10
    return score


def brute_force(some_input):
    result = dict()
    splittet = [some_input[i:i+2] for i in range(0, len(some_input), 2)]
    for x in range(0, 127):
        s = list()
        for v in splittet:
            s.append(chr(int(v,16) ^ x))
        r = ''.join(s)
        s = evaluate_decryption(r)
        result[r] = s;
        #print(str(x) + ':' + chr(x) + '  :  ' + r)
        #print('Score: ' + str(s))
        #print('')
    return result

def brute_force_split(split_input):
    result = dict()
    for x in range(0, 127):
        s = list()
        for v in split_input:
            s.append(chr(int(v,16) ^ x))
        r = ''.join(s)
        s = evaluate_decryption(r)
        result[(r,x,chr(x))] = s;
        #print(str(x) + ':' + chr(x) + '  :  ' + r)
        #print('Score: ' + str(s))
        #print('')
    return result

def brute_force_file():
    hex_values = load_file()
    results = dict()
    for h in hex_values:
        results.update(brute_force(h))
    return results

def do_stuff():
    import operator
    results = brute_force_file()
    results = sorted(results.items(), key=operator.itemgetter(1))
    for r in results:
        print(r)
