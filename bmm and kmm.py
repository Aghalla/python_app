#با این برنامه شما میتوانید  ب م م  و  ک م م دو عدد را بدست  بیاورید

while True:
    X = int(input("choose number\n1 = bmm: \n2 = kmm: "))
    if X == 1:
        x = int(input("number 1: "))
        y = int(input("number 2: "))

        li1 = []
        li2 = []
        for i in range(1, x + 1):
            if x % i == 0:
                li1.append(i)

        for j in range(1, y + 1):
            if y % j == 0:
                li2.append(j)

        for i in li1[::-1]:
            for j in li2[::-1]:
                if i == j:
                    print(i)
                    break
            else:
                continue
            break

    elif X == 2:
        x = int(input("number 1: "))
        y = int(input("number 2: "))
        l1 = []
        l2 = []
        for i in range(1, 100):
            l1.append(x * i)

        for i in range(1, 100):
            l2.append(y * i)

        for i in l1:
            for j in l2:
                if i == j:
                    print(i)
                    break
            else:
                continue

            break

