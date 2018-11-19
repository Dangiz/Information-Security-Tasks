import os

def office_file_determination(file_address: str):
    if(open(file_address,encoding='utf-8', errors='ignore').read().find('word/document')!=-1):
        print('This is the word document')
    if (open(file_address, encoding='utf-8', errors='ignore').read().find('ppt/slides/') != -1):
        print('This is MS office presination')


def is_contains_signature(file_address: str, signature: str):
    file = open(file_address, "rb").read(32)
    hex_bytes = " ".join(['{:02X}'.format(byte) for byte in file])
    return hex_bytes.find(signature) != -1


def check_files_for_signature(directory: str, signature: str):
    for x in next(os.walk(directory))[2]:
        if is_contains_signature(directory+'/'+x, signature):
            print('Signature match on '+directory+'/'+x+'!')
            if(signature=='50 4B 03 04'):office_file_determination(directory+'/'+x)

    for x in next(os.walk(directory))[1]:
        check_files_for_signature(directory+'/'+x,signature)