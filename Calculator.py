# Made By Flow#0002




Avogadronumber = 6.02 * 10 ** 23
print("Do you want to multiply, divde, add, or subtract numbers?")
print("1 = add, 2 = multiply, 3 = Subtract, 4 = divide,5 = add + Avogadro's number, 6 = multiply * Avogadro's number, 7 = Subtract - Avogadro's number, 8 = divide /  Avogadro's number . ")
A = int(input())
if A == 1:
    print("What is the first number?")
    B = float(input())
    print("What is the second number?")
    C = float(input())
    D = B + C
    print("The answer is", D)
    
elif A == 2:
    print("What is the first number?")
    B = float(input())
    print("What is the second number?")
    C = float(input())
    D = B * C
    print("The answer is", D)
elif A == 3:
    print("This will subtract the first number by the second number.")
    print("What is the first number?")
    B = float(input())
    print("What is the second number?")
    C = float(input())
    D = B - C
    print("The answer is", D)
elif A == 4:
    print("This will divide the first number over the second number")
    print("What is the first number?")
    B = float(input())
    print("What is the second number?")
    C = float(input())
    D = B / C
    print("The answer is", D)
elif A == 5:
    print("What's the first number?")
    B = float(input())
    print("Do you want a second number? 1 = no, 2 = yes")
    K = int(input())
    if K == 1:
        print( B + Avogadronumber)
    else:
        print("What is the second number then?")
        C = float(input())
        print("The answer is", B + C + Avogadronumber)
elif A == 6:
    print("What's the first number?")
    B = float(input())
    print("Do you want a second number? 1 = no, 2 = yes")
    K = int(input())
    if K == 1:
        print( B * Avogadronumber)
    else:
        print("What is the second number then?")
        C = float(input())
        print("The answer is", B * C * Avogadronumber)
elif A == 7:
    print("This will subtract the first number to the avogadro's number, but if you chose an extra number it will subtract the first number to the secod number to avogadro's number.")
    print("What's the first number?")
    B = float(input())
    print("Do you want a second number? 1 = no, 2 = yes")
    K = int(input())
    if K == 1:
        print( B - Avogadronumber)
    else:
        print("What is the second number then?")
        C = float(input())
        print("The answer is",  (B - C) - Avogadronumber)
elif A == 8:
    print("Please note that this will divide the first number over the second number (If you choose one) over Avogadro's number...")
    print("What's the first number?")
    B = float(input())
    print("Do you want a second number? 1 = no, 2 = yes")
    K = int(input())
    if K == 1:
        print( B * Avogadronumber)
    else:
        print("What is the second number then?")
        C = float(input())
        print("The answer is", ((B / C) / Avogadronumber))
print("If the program didn't work as intended please dm Flow#0002 on discord. \nBut judging how you've seen this message, it probably worked!!\nWell anyways, until next time. see ya later!!!")
exit = input("press Enter to terminate the program.")
