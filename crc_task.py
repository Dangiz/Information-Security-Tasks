from common import *


def get_control_sum(file_address):
    input_string = string_to_binary(open(file_address).read())
    crc_word = input_string[:8]
    input_string = input_string[8:]
    for c in input_string:
        crc_word = string_to_byte_word(int(crc_word, 2) << 1)
        if crc_word[0] == '1':
            crc_word = string_to_byte_word((int(crc_word, 2) ^ int("10011011", 2)) | int("00000001", 2))
        crc_word = crc_word[:-1] + c
    return int(crc_word, 2)