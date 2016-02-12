def calculate(string1, string2):
    r = 0;
    for x,y in zip(string1,string2):
        r += bit_len_count(ord(x) ^ ord(y))
    return r


def bit_len_count(int_type):
    count = 0
    while (int_type):
        count += (int_type & 1)
        int_type >>= 1
    return(count)
