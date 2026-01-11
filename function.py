# functions without | with para

def fun_b():
    print("hello python")


fun_b()


def fun_s(para_X):
    return para_X


print(fun_s("hello mr alise"))


# --------------------------------------------------
# give to the user to give you the input


# nameUser = input("give me your name: ")

# def fun_name(para_x):
#     return f"hi! are you Mr|Mss: {para_x}"

# print(fun_name(nameUser))


# use function with tupel

arrNums = (1,2,3,4,5,6)

def fun_useTuple(*tpl):
    return sum(tpl)

print(fun_useTuple(arrNums))