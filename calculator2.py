import os
import time
os.system("title Flow's calculator!")
from colorama import init, Fore, Style
from colorama.ansi import Back
init(convert=True, autoreset=True)
#Variables stored here that are defined not by the user.
Status_of_calculator = False
Avogadronumber = 6.0221409 * 10 ** 23
if Status_of_calculator == False:
    print(f"{Fore.RED}Status of calculator is down right now.")
    time.sleep(60)
    exit()
    
# Created by Flow :3
print(f"{Fore.GREEN} You have opened up a calculator. What makes this calculator different is that it already has Avogadro's number integrated to it!")
print(f"{Fore.LIGHTYELLOW_EX}Do you want to multiply, divde, add, or subtract numbers?\n1 = add, 2 = multiply, 3 = Subtract, 4 = divide\n5 = add + Avogadro's number, 6 = multiply * Avogadro's number, 7 = Subtract - Avogadro's number, 8 = divide /  Avogadro's number")
A = int(input())
                                        # Calculation down below 
if A == 1:
    print(f"You have chosen {Fore.LIGHTRED_EX}addition!{Style.RESET_ALL} \n \nWhat is the {Fore.LIGHTMAGENTA_EX}first {Style.RESET_ALL}number?")
    B = float(input())
    print(f"What is the {Fore.LIGHTMAGENTA_EX}second {Style.RESET_ALL}number?")
    C = float(input())
    D = B + C
    print(f"The answer is {Fore.RED}{D}{Style.RESET_ALL}{Style.BRIGHT}.")
elif A == 2:
    print(f"You have chosen {Fore.LIGHTRED_EX}multiplication!{Style.RESET_ALL} \n \nWhat is the {Fore.LIGHTMAGENTA_EX}first {Style.RESET_ALL}number?")
    B = float(input())
    print(f"What is the {Fore.LIGHTMAGENTA_EX}second {Style.RESET_ALL}number?")
    C = float(input())
    D = B * C
    print(f"The answer is {Fore.RED}{D}{Style.RESET_ALL}{Style.BRIGHT}.")
elif A == 3:
    print(f"You have chosen {Fore.LIGHTRED_EX} subtraction!{Style.RESET_ALL} \n \nThis will subtract the first number by the second number.")
    print(f"What is the {Fore.LIGHTMAGENTA_EX}first {Style.RESET_ALL}number?")
    B = float(input())
    print(f"What is the {Fore.LIGHTMAGENTA_EX}second {Style.RESET_ALL}number?")
    C = float(input())
    D = B - C
    print(f"The answer is {Fore.RED}{D}{Style.RESET_ALL}{Style.BRIGHT}.")
                                                            # Division
elif A == 4:
    print(f"You have chosen {Fore.LIGHTRED_EX}division!{Style.RESET_ALL} \n{Fore.YELLOW}Please note:{Style.RESET_ALL} This will divide the first number over the second number.\n \nWhat is the {Fore.LIGHTMAGENTA_EX}first {Style.RESET_ALL}number?")
    B = float(input())
    print(f"What is the {Fore.LIGHTMAGENTA_EX}second {Style.RESET_ALL}number?")
    C = float(input())
    if C == 0:
        print(f" \n \n{Fore.RED}Division{Style.RESET_ALL} by {Style.BRIGHT}0{Style.RESET_ALL} is impossible.\n\n")
    else:    
        D = B / C
        print(f"The answer is {Fore.RED}{D}{Style.RESET_ALL}{Style.BRIGHT}.")
        
elif A == 5:
    print(f"You have chosen {Fore.LIGHTRED_EX}addition!{Style.RESET_ALL} \n \nWhat's the {Fore.LIGHTMAGENTA_EX}first {Style.RESET_ALL}number?")
    B = float(input())
    print("Do you want a second number? 1 = no, 2 = yes")
    K = int(input())
    if K == 1:
        print(f"The answer is {Fore.RED}{ B + Avogadronumber}{Style.RESET_ALL}{Style.BRIGHT}.")
    else:
        print(f"What is the {Fore.LIGHTMAGENTA_EX}second {Style.RESET_ALL}number then?")
        C = float(input())
        print(f"The answer is {Fore.RED}{ B + C + Avogadronumber}{Style.RESET_ALL}{Style.BRIGHT}.")
elif A == 6:
    print(f"You have chosen {Fore.LIGHTRED_EX}multiplication!{Style.RESET_ALL} \n \nWhat's the {Fore.LIGHTMAGENTA_EX}first {Style.RESET_ALL}number?")
    B = float(input())
    print("Do you want a second number? 1 = no, 2 = yes")
    K = int(input())
    if K == 1:
        print(f"The answer is {Fore.RED}{B * Avogadronumber}{Style.RESET_ALL}{Style.BRIGHT}.")
    else:
        print(f"What is the {Fore.LIGHTMAGENTA_EX}second {Style.RESET_ALL}number then?")
        C = float(input())
        print(f"The answer is {Fore.RED}{B * C * Avogadronumber}{Style.RESET_ALL}{Style.BRIGHT}.")
elif A == 7:
    print(f"You have chosen {Fore.LIGHTRED_EX}subtraction!{Style.RESET_ALL} \nThis will subtract the first number to the avogadro's number. But if you chose to have a second number, it will subtract the first number to the second number to Avogadro's number.")
    print(f"What's the {Fore.LIGHTMAGENTA_EX}first {Style.RESET_ALL}number?")
    B = float(input())
    print("Do you want a second number? 1 = no, 2 = yes")
    K = int(input())
    if K == 1:
        print(f"The answer is {Fore.RED}{B - Avogadronumber}{Style.RESET_ALL}{Style.BRIGHT}.")
    else:
        print(f"What is the {Fore.LIGHTMAGENTA_EX}second {Style.RESET_ALL}number then?")
        C = float(input())
        print(f"The answer is {Fore.RED}{(B - C) - Avogadronumber}{Style.RESET_ALL}{Style.BRIGHT}.")
elif A == 8:
    print(f"You have chosen {Fore.LIGHTRED_EX}division!{Style.RESET_ALL} \n{Fore.YELLOW}Please note:{Style.RESET_ALL} This will divide the first number over the second number (If you choose a second number) over Avogadro's number.\n \nWhat's the {Fore.LIGHTMAGENTA_EX}first {Style.RESET_ALL}number?")
    B = float(input())
    if B == 0:
        print(f" \n \n{Fore.RED}Division{Style.RESET_ALL} by {Style.BRIGHT}0{Style.RESET_ALL} is impossible.\n\n")
    else:    
        print("Do you want a second number? 1 = no, 2 = yes")
        K = int(input())
        if K == 1:
            print(f"The answer is {Fore.RED}{B * Avogadronumber}{Style.RESET_ALL}{Style.BRIGHT}.")
        else:
            print(f"What is the {Fore.LIGHTMAGENTA_EX}second {Style.RESET_ALL}number then?")
            C = float(input())
            print(f"The answer is {Fore.RED}{((B / C) / Avogadronumber)}{Style.RESET_ALL}{Style.BRIGHT}. \n \n")
print(f"{Fore.LIGHTCYAN_EX}If the program didn't work as intended please dm Flow#0002 on discord. \nBut judging how you've seen this message, it probably worked!!\nWell anyways, until next time. see ya later!!!{Style.RESET_ALL}{Style.BRIGHT} \n \nPress enter to terminate the program.")
exit = input()