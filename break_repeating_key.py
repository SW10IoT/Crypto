from base64 import b64decode
import hamming_distance
from binascii import hexlify

def load_file():
    r = ''
    with open('blocks.txt', 'r') as f:
        for line in f:
            r += line.rstrip('\n')
    return r

def split_hex_string(hex_string):
    return [hex_string[i:i+2] for i in range(0, len(hex_string), 2)]

def make_blocks(hex_array, key_size):
    return [hex_array[i:i+key_size] for i in range(0, len(hex_array), key_size)]


# For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes, and find the edit distance between them. Normalize this result by dividing by KEYSIZE.
def block_distance(block_1, block_2, key_size):
    return hamming_distance.calculate_hex(block_1, block_2) / key_size

KEY_RANGE = 40

# TEST
s = load_file()
h = hexlify(b64decode(s))
splittet_h =  split_hex_string(h)
blocks = make_blocks(splittet_h, 10)



for x in range(1, KEY_RANGE):
    b = make_blocks(splittet_h, x)
    print(block_distance(b[0], b[1], x))


#hamming distance test
#print(hamming_distance.calculate('this is a test', 'wokka wokka!!!'))







