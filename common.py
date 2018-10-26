

def string_to_binary(s):
    b = bin(s)[2:]
    b = "0"*(8-len(b))+b
    b = b[len(b) - 8:len(b)]
    return b
