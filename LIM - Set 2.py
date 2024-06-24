#!/usr/bin/env python
# coding: utf-8

# In[89]:


def shift_letter (letter, shift):

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if letter == " ":
        new_letter = " "
        
    elif alphabet.index(letter) + shift <= 25:
        new_letter = alphabet[alphabet.index(letter) + shift]
        
    else:
        new_index = alphabet.index(letter) + shift - 26
        while new_index > 25:  
            new_index = new_index - 26
        new_letter = alphabet[new_index]
            
    return (new_letter)

shift_letter ("Z", 100)


# In[91]:


def caesar_cipher (message, shift):
   
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message_length = len(message)
    message_index = 0
    new_word = ""
   
    while message_length != message_index:
        letter = message[message_index]
        message_index += 1
         
        if letter == " ":
            new_word += " "
        
        elif alphabet.index(letter) + shift <= 25:
            new_word += alphabet[alphabet.index(letter) + shift]
        
        else:
            new_index = alphabet.index(letter) + shift - 26
            while new_index > 25:  
                new_index = new_index - 26
            new_word += alphabet[new_index]

    return new_word
            
caesar_cipher ("HELLO WORLD", 2)


# In[93]:


def shift_by_letter (letter, letter_shift):

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if letter == " ":
        shifted_letter = " "
    
    elif alphabet.index(letter) + alphabet.index(letter_shift) <= 25:
        shifted_letter = alphabet[alphabet.index(letter) + alphabet.index(letter_shift)]
    
    else:
        new_index = alphabet.index(letter) + alphabet.index(letter_shift) - 26
        while new_index > 25:
            new_index = new_index - 26
        shifted_letter = alphabet[new_index]

    return(shifted_letter)

shift_by_letter ("Z", "C")


# In[95]:


def vigenere_cipher (message, key):

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message_length = len(message)
    message_index = 0
    key_index = 0
    new_word = ""
    
    if len(message) <= len(key):
        while message_length != message_index:
            message_letter = message[message_index]
            key_letter = key[key_index]
            message_index += 1
            key_index += 1

            if message_letter == " ":
                new_word += " "
            elif alphabet.index(message_letter) + alphabet.index(key_letter) <= 25:
                new_word += alphabet[alphabet.index(message_letter) + alphabet.index(key_letter)]

            else:
                new_index = alphabet.index(message_letter) + alphabet.index(key_letter) - 26
                while new_index > 25:  
                    new_index = new_index - 26
                new_word += alphabet[new_index]
    
    else:    
        key = (((len(message) // len(key))+1) * key)
        while message_length != message_index:
            message_letter = message[message_index]
            key_letter = key[key_index]
            message_index += 1
            key_index += 1

            if message_letter == " ":
                new_word += " "
            elif alphabet.index(message_letter) + alphabet.index(key_letter) <= 25:
                new_word += alphabet[alphabet.index(message_letter) + alphabet.index(key_letter)]

            else:
                new_index = alphabet.index(message_letter) + alphabet.index(key_letter) - 26
                while new_index > 25:  
                    new_index = new_index - 26
                new_word += alphabet[new_index]
    
    return new_word

vigenere_cipher ("A C", "KEY")


# In[97]:


def scytale_cipher(message, shift):
    
    while len(message) % shift != 0:
        message += "_"
    
    encoded_message = []
    message_length = len(message)
    
    for i in range(message_length):
        new_index = (i // shift) + (message_length // shift) * (i % shift)
        encoded_message += (message[new_index])
    
    return "".join(encoded_message)

scytale_cipher ("INFORMATION_AGE", 3)


# In[99]:


def scytale_decipher (message, shift):
    
    message_length = len(message)
    decoded_message = ""

    for i in range(message_length):
        original_index = (i // (message_length // shift)) + (shift * (i % (message_length // shift)))
        decoded_message += message[original_index]

    return "".join(decoded_message)

scytale_decipher ("IMNNA_FTAOIGROE", 3)

