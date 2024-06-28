#!/usr/bin/env python
# coding: utf-8

# In[71]:


def password_checker(password):
    #number of capital letters:
    
    number_of_capital_letters = sum(1 for c in password if c.isupper())
    number_of_numeric_characters = sum(1 for c in password if c.isdigit())
    special_characters = "+" in password or "@" in password or "!" in password or "*" in password

    #strong
    if len(password) >= 8 and number_of_capital_letters >= 1 and number_of_numeric_characters >= 1 and special_characters:
        return "strong"

    #medium
    elif len(password) >= 8 and number_of_capital_letters >= 1 and number_of_numeric_characters >= 1:
        return "medium"

    #weak
    elif len(password) >= 8 and number_of_capital_letters >= 1:
        return "weak"

    #minimum
    elif len(password) >= 8:
        return "minimum"

    #unacceptable
    else: 
        return "unacceptable"

password_checker("X!@1a")


# # 4
# ### 5 points
# ### Context
# Recall the hexadecimal base system, or base-16. There are not enough Arabic numerals to support base-16, so the first few letters of the alphabet are used instead of numbers for higher values:
#    
#     A : 10
#     B : 11
#     C : 12
#     D : 13
#     E : 14
#     F : 15
#     
# Conversion to and from the hexadecimal system relies on the same principle and process as lower bases. For instance: converting the hexadecimal number "1A9" to decimal:
# 
#     # From hexadecimal:
#     # 1A9 == (1 * 16**2) + (A * 16**1) + (9 * 16**0) == 425
#     # 1A9 == (1 * 16**2) + (10 * 16**1) + (9 * 16**0) == 425
#     
# ### Required
# Write a function that takes a single argument, a number in hexadecimal (string). The function should **return** the number in **decimal** (string). You only need to consider decimal to hexadecimal, not the other way around.
# 
# e.g. 
# 
#     dec_to_hex_convert("FF") -> "255"
#     
# ### Constraints
# 1. Do not use the int(x, 16) function. You may still use int() to convert strings to integers.
# 2. For simplicity, input integer strings will always represent positive integers.

# In[154]:


def hexadecimal_base_system(number):

    number_dict = {
        "A" : 10, 
        "B" : 11, 
        "C" : 12,
        "D" : 13, 
        "E" : 14,
        "F" : 15
    }

    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

    number_length = len(number)
    sum = 0

    for i in range(number_length):
        char = number[i]
        if char.isnumeric():
            sum += int(char) * 16 ** (number_length-1-i)
        else:
            value = number_dict[char]
            sum += value * 16 ** (number_length-1-i)

    return sum
        
hexadecimal_base_system("111")


# In[ ]:




