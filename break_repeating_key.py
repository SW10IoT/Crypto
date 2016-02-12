import base64

def load_file():
    r = ''
    with open('blocks.txt', 'r') as f:
        for line in f:
            r += line.rstrip('\n')
    return r

def decode_base64(s):
    return base64.b64decode(s)

def split_hex_string(hex_string):
    return [hex_string[i:i+2] for i in range(0, len(hex_string), 2)]

def make_blocks(hex_array, key_size):
    return [hex_array[i:i+key_size] for i in range(0, len(hex_array), key_size)]


s = load_file()
h = decode_base64(s)
splittet_h =  split_hex_string(h)
blocks = make_blocks(splittet_h, 10)
print(blocks)







