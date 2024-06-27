#!/usr/bin/env python
# coding: utf-8

# In[16]:


def bin_to_dec(binary_string):

    length_of_integer = len(binary_string)
    base_ten_interpretation = 0

    for i in range(0, length_of_integer):
        base_ten_interpretation += (int(binary_string[i])) * (2 ** (length_of_integer - 1 - i))
    
    return base_ten_interpretation

bin_to_dec("1011")


# In[18]:


def dec_to_bin(number): 

    result = ""

    while number != 0:
        remainder = number % 2
        if remainder == 1:
            result += "1"
        elif remainder == 0:
            result += "0"
        number = (number // 2)

    return result[::-1]

dec_to_bin(2555)


# In[20]:


def telephone_cipher (message):

    encoder_dict = {
        " ":"0",
        "A":"2",
        "B":"22",
        "C":"222",
        "D":"3",
        "E":"33",
        "F":"333",
        "G":"4",
        "H":"44",
        "I":"444",
        "J":"5",
        "K":"55",
        "L":"555",
        "M":"6",
        "N":"66",
        "O":"666",
        "P":"7",
        "Q":"77",
        "R":"777",
        "S":"7777",
        "T":"8",
        "U":"88",
        "V":"888",
        "W":"9",
        "X":"99",
        "Y":"999",
        "Z":"9999"
    }

    result = ""

    for i in message:
        if i in encoder_dict:
            corresponding_code = encoder_dict[i]
            # if result exists and if last number of result is equal to first number of code
            if result and result[-1] == corresponding_code[0]:
                result += "_"
                result += corresponding_code
            else:
                result += corresponding_code

    return result

telephone_cipher("HELLO")


# In[22]:


def telephone_decipher(telephone_string):
    decipher_dict = {
        "0":" ",
        '2': 'A',
        '22': 'B',
        '222': 'C',
        '3': 'D',
        '33': 'E',
        '333': 'F',
        '4': 'G',
        '44': 'H',
        '444': 'I',
        '5': 'J',
        '55': 'K',
        '555': 'L',
        '6': 'M',
        '66': 'N',
        '666': 'O',
        '7': 'P',
        '77': 'Q',
        '777': 'R',
        '7777': 'S',
        '8': 'T',
        '88': 'U',
        '888': 'V',
        '9': 'W',
        '99': 'X',
        '999': 'Y',
        '9999': 'Z'
    }

    
    result = ""
    length_of_message = len(telephone_string)
    i = 0

    while i < length_of_message:
        if telephone_string[i] == "_":
            i += 1
            continue

        next_index = i
        while next_index < length_of_message and telephone_string[i] == telephone_string[next_index]:
            next_index += 1


        new_string = telephone_string[i:next_index]
        if new_string in decipher_dict:
            result += decipher_dict[new_string]
        elif new_string not in decipher_dict:
            result += ""


        i = next_index

    return result
        
telephone_decipher("4433555_555666096667775553")

