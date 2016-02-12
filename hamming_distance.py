def hamming(string1, string2):
    r = 0;
    for x,y in zip(string1,string2):
        r += bitLenCount(ord(x) ^ ord(y))
    return r


def bitLenCount(int_type):
    count = 0
    while (int_type):
        count += (int_type & 1)
        int_type >>= 1
    return(count)

#print(hamming("this is a test","wokka wokka!!!"))
