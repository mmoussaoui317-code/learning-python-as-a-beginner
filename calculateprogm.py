def calculate():
    # for i in range(1, 5):
    #     print(f"{i}")
        print("1 - addition")
        print("2 - multiplication")
        print("3 - substraction")
        print("4 - division")
        opera = int(input())
        if opera > 0 and opera < 5:
            frNum = float(input("give me the first number: "))
            scNum = float(input("give me the second number: "))
            if opera == 1: 
                return frNum + scNum
            elif opera == 2:
                return frNum * scNum
            elif opera == 3:
                return frNum - scNum
            elif opera == 4:
                if scNum > 0:
                    return frNum / scNum
                else:
                    print("I can't divide to you by zero")
        else:
            print("you're don't need this calculate")


print(f"{calculate()}")