import os


def is_contains_signature(file_address: str, signature: str):
    file = open(file_address, "rb").read(32)
    hex_bytes = " ".join(['{:02X}'.format(byte) for byte in file])
    return hex_bytes.find(signature) != -1


def check_files_for_signature(directory: str, signature: str):
    for x in next(os.walk(directory))[2]:
        if is_contains_signature(directory+'/'+x, signature):
            print('Signature match on '+directory+'/'+x+'!')
    for x in next(os.walk(directory))[1]:
        check_files_for_signature(directory+'/'+x,signature)