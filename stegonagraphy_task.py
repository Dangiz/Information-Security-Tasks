from common import *


def steganography_task_encode(coded_file_address, container_file_address):
    input_string=string_to_binary(open(coded_file_address).read())
    container_string_array = list(open(container_file_address).read())
    for i in range(len(container_string_array)):

        if container_string_array[i] == ' ' and input_string[0] == '1':
            container_string_array[i] = ' '
            input_string = input_string[1:]
        elif container_string_array[i] == ' ' and input_string[0] == '0':
            container_string_array[i] = ' '
            input_string = input_string[1:]

        if len(input_string) == 0:
            container_string_array.insert(i, '😃')
            break
    #print(''.join(container_string_array))
    return container_string_array


def steganograpy_uncode(container_string):
    return binary_to_text(''.join(map(lambda x: '1' if x == ' ' else '0', filter(lambda x: x == ' ' or x == ' ', container_string[:container_string.index('😃')+2]))))
