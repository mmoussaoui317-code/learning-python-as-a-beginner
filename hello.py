# print('hello python i am mounaim')

# print('hello')
# print('python')
# print('by!!')


# #**************************** --------------------- **********************
# ## if you the multy ststment in one line without semi colon (;)
# ### python will give you syntax Error 

# # print("hello ")  print("  good by!!")
# print("hello ") ; print("  good by!!")


def fake_bin(x):
    pass
    newStr = ''
    for num in x:
        if int(num) < 5:
            newStr += '0'
        else:
            newStr += '1'
    
    return newStr

def fake_bin_two(x):
    pass
    return ''.join('0' if c < '5' else '1' for c in x)


# "100111001111", "800857237867"
print(fake_bin("800857237867"))

print('-----------------++++++++++++-----------------')

print(fake_bin_two("800857237867"))

