
def binary_to_text(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'


def string_to_byte_word(s):
    b = bin(s)[2:]
    b = "0"*(8-len(b))+b
    b = b[len(b) - 8:len(b)]
    return b


def string_to_binary(text, encoding='utf-8', errors='surrogatepass'):
    text=str(text)
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))
