while(True) :
    x = str(input("enter any letter from r,p,s: "))
    myDict1 = {"r":"rock","p":"paper","s":"scissors"}
    option = str(myDict1.get(x))
    print("you chose ",x," which is ",option)

    import random
    myDict2 = {1:"r",2:"p",3:"s"}
    n = random.randint(1,3)
    a = str(myDict2[n])
    option2 = str(myDict1.get(a))
    print("computer option: ",myDict2[n],"which is ",option2)

    if x == "r" :
        if n == 1 :
            print("tie")
        elif n == 2 :
            print("computer wins")
        else :
            print("you win")
    elif x == "p" :
        if n == 1 :
            print("you win")
        elif n == 2 :
            print("tie")
        else :
            print("computer wins")
    else :
        if n == 1 :
            print("computer wins")
        elif n == 2 :
            print("you win")
        else :
            print("tie")
    g = str(input("do you want to continue[y/n]: "))
    if g == "y" :
        continue
    else :
        print("game over")
        break






