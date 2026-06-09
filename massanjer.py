while True:
    print("which one do you want ")
    print("\t*NUMBER 1 : Input\n\t*NUMBER 2 : Output\n\t*NUMBER 3 : Exit app ")
    x = input("choose one: ")

    if x == "1":
        enter = ""
        ent = input("enter text: ")
        for char in ent:
            luck = (ord(char) * 5 + 7 - 3)
            enter += chr(luck)
        print("*" * 40)
        print(enter)
        print("*" * 40)
    elif x == "2":
        exting = input("enter output: ")
        exit = ""
        for ex in exting:
            unluck = (ord(ex) + 3 - 7) // 5
            exit += chr(unluck)
        print("*" * 40)
        print(exit)
        print("*" * 40)

    elif x == "3":
        print("are you want exit")
        e = input("yes or no").lower()
        if e == "yes: ":
            break
        else:
            print("waring and again")
    else:
        print("waring and again")