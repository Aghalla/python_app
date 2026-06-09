import string
import random

lw = (string.ascii_lowercase)
up = (string.ascii_uppercase)
number = "1234567890"
nomad = "!@#$%^&*()_-+=|\\}{[]:;<,.>?/"
all = lw + up + number + nomad
while True:
    print("witch one :\n\t (1) for create password.\n\t (2) for Exit ")
    choose = int(input("chose one: "))
    if choose == 1:
        tol = int(input("Ente tool password: "))
        SEED = int(input("seed your password: "))
        random.seed(SEED)
        RANDOM = ("".join(random.sample(all, tol)))
        print("*" * 40)
        print(RANDOM)
        print("*" * 40)
    elif choose == 2:
        break
    else:
        print("*" * 40)
        print("worrying your text please agine")
        print("*" * 40)
