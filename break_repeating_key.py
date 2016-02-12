from base64 import b64decode
import hamming_distance
from binascii import hexlify
from single_byte_xor import brute_force_split
from repeating_key_xor_encrypt import decrypt

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

def make_blocks_with_padding(hex_array, key_size, padding_value):
    blocks = make_blocks(hex_array, key_size)
    last_block_index = len(blocks)-1
    last_block_length = len(blocks[last_block_index])
    if last_block_length is not key_size:
        for x in range(last_block_length, key_size):
            blocks[last_block_index].append(padding_value)
    return blocks

def block_distance_normalized(block_1, block_2, key_size):
    return hamming_distance.calculate_hex(block_1, block_2) / key_size

def get_key_score(hex_array, key_range_max, return_sorted=False):
    r = dict()
    for x in range(1, KEY_RANGE):
        b = make_blocks(hex_array, x)
        r[x]=block_distance_normalized(b[0], b[1], x)
    if return_sorted:
        return sorted(r.items(), key = lambda p: p[1])
    return r

def transpose(blocks):
    return list(zip(*blocks))

def examine_keys(matrix):
    for v in matrix:
        results = brute_force_split(v)
        results = sorted(results.items(), key = lambda p: p[1])
        for r in results:
            print(r)
        input('Press any key to continue..')

        
KEY_RANGE = 40

s = load_file()
h = hexlify(b64decode(s))
hex_array =  split_hex_string(h)

#print(get_key_score(hex_array, KEY_RANGE, return_sorted=True))

KEY_SIZE = 5
PADDING_VALUE = b'ff'

blocks = make_blocks_with_padding(hex_array, KEY_SIZE, PADDING_VALUE)
transposed_matrix = transpose(blocks)
#examine_keys(transposed_matrix)
#KEY: ionio

print(decrypt(s, 'ionio'))

#hamming distance test
#print(hamming_distance.calculate('this is a test', 'wokka wokka!!!'))







