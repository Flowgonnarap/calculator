import os
import time
os.system("title Flow's calculator!")
from colorama import init, Fore, Style
init(convert=True, autoreset=True)
#Variables stored here that are defined not by the user.
Status_of_calculator = False
Avogadronumber = 6.0221409 * 10 ** 23
# If status is set to False, the program will close after 200 seconds ( 4 minutes ).
if Status_of_calculator == False:
    os.system("title :(")
    print(f"{Fore.RED}Status of calculator is down right now.")
    time.sleep(100)
    exit()
    
print(f"{Fore.GREEN}You have opened up a calculator. What makes this calculator different is that it already has Avogadro's number integrated to it!")
print(f"{Fore.LIGHTYELLOW_EX}Do you want to multiply, divde, add, or subtract numbers?\n1 = add, 2 = multiply, 3 = Subtract, 4 = divide\n5 = add + Avogadro's number, 6 = multiply * Avogadro's number, 7 = Subtract - Avogadro's number, 8 = divide /  Avogadro's number")
A = int(input())
                                        # Calculation down below 
if A == 1:
    print(f"You have chosen {Fore.LIGHTRED_EX}addition!{Style.RESET_ALL} \n \nWhat is the {Fore.LIGHTMAGENTA_EX}first {Style.RESET_ALL}number?")
    firstnum = float(input())
    print(f"What is the {Fore.LIGHTMAGENTA_EX}second {Style.RESET_ALL}number?")
    secondnum = float(input())
    total = firstnum + secondnum 
    print(f"The answer is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
elif A == 2:
    print(f"You have chosen {Fore.LIGHTRED_EX}multiplication!{Style.RESET_ALL} \n \nWhat is the {Fore.LIGHTMAGENTA_EX}first {Style.RESET_ALL}number?")
    firstnum = float(input())
    print(f"What is the {Fore.LIGHTMAGENTA_EX}second {Style.RESET_ALL}number?")
    secondnum = float(input())
    total = firstnum * secondnum
    print(f"The answer is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
elif A == 3:
    print(f"You have chosen {Fore.LIGHTRED_EX} subtraction!{Style.RESET_ALL} \n \nThis will subtract the first number by the second number.")
    print(f"What is the {Fore.LIGHTMAGENTA_EX}first {Style.RESET_ALL}number?")
    firstnum = float(input())
    print(f"What is the {Fore.LIGHTMAGENTA_EX}second {Style.RESET_ALL}number?")
    secondnum = float(input())
    total = firstnum - secondnum
    print(f"The answer is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
elif A == 4:
    print(f"You have chosen {Fore.LIGHTRED_EX}division!{Style.RESET_ALL} \n{Fore.YELLOW}Please note:{Style.RESET_ALL} This will divide the first number over the second number.\n \nWhat is the {Fore.LIGHTMAGENTA_EX}first {Style.RESET_ALL}number?")
    firstnum = float(input())
    print(f"What is the {Fore.LIGHTMAGENTA_EX}second {Style.RESET_ALL}number?")
    secondnum = float(input())
    total = firstnum / secondnum
    print(f"The answer is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
elif A == 5:
    print(f"You have chosen {Fore.LIGHTRED_EX}addition!{Style.RESET_ALL} \n \nWhat's the {Fore.LIGHTMAGENTA_EX}first {Style.RESET_ALL}number?")
    firstnum = float(input())
    print("Do you want a second number? 1 = no, 2 = yes")
    choice = int(input())
    if choice == 1:
        print(f"The answer is {Fore.RED}{ firstnum + Avogadronumber}{Style.RESET_ALL}{Style.BRIGHT}.")
    else:
        print(f"What is the {Fore.LIGHTMAGENTA_EX}second {Style.RESET_ALL}number then?")
        secondnum = float(input())
        print(f"The answer is {Fore.RED}{ firstnum + secondnum + Avogadronumber}{Style.RESET_ALL}{Style.BRIGHT}.")
elif A == 6:
    print(f"You have chosen {Fore.LIGHTRED_EX}multiplication!{Style.RESET_ALL} \n \nWhat's the {Fore.LIGHTMAGENTA_EX}first {Style.RESET_ALL}number?")
    firstnum = float(input())
    print("Do you want a second number? 1 = no, 2 = yes")
    choice = int(input())
    if choice == 1:
        print(f"The answer is {Fore.RED}{firstnum * Avogadronumber}{Style.RESET_ALL}{Style.BRIGHT}.")
    else:
        print(f"What is the {Fore.LIGHTMAGENTA_EX}second {Style.RESET_ALL}number then?")
        secondnum = float(input())
        print(f"The answer is {Fore.RED}{firstnum * secondnum * Avogadronumber}{Style.RESET_ALL}{Style.BRIGHT}.")
elif A == 7:
    print(f"You have chosen {Fore.LIGHTRED_EX}subtraction!{Style.RESET_ALL} \nThis will subtract the first number to the avogadro's number. But if you chose to have a second number, it will subtract the first number to the second number to Avogadro's number.")
    print(f"What's the {Fore.LIGHTMAGENTA_EX}first {Style.RESET_ALL}number?")
    firstnum = float(input())
    print("Do you want a second number? 1 = no, 2 = yes")
    choice = int(input())
    if choice == 1:
        print(f"The answer is {Fore.RED}{firstnum - Avogadronumber}{Style.RESET_ALL}{Style.BRIGHT}.")
    else:
        print(f"What is the {Fore.LIGHTMAGENTA_EX}second {Style.RESET_ALL}number then?")
        secondnum = float(input())
        print(f"The answer is {Fore.RED}{(firstnum - secondnum) - Avogadronumber}{Style.RESET_ALL}{Style.BRIGHT}.")
elif A == 8:
    print(f"You have chosen {Fore.LIGHTRED_EX}division!{Style.RESET_ALL} \n{Fore.YELLOW}Please note:{Style.RESET_ALL} This will divide the first number over the second number (If you choose a second number) over Avogadro's number.\n \nWhat's the {Fore.LIGHTMAGENTA_EX}first {Style.RESET_ALL}number?")
    firstnum = float(input())
    print("Do you want a second number? 1 = no, 2 = yes")
    choice = int(input())
    if choice == 1:
        print(f"The answer is {Fore.RED}{firstnum * Avogadronumber}{Style.RESET_ALL}{Style.BRIGHT}.")
    else:
        print(f"What is the {Fore.LIGHTMAGENTA_EX}second {Style.RESET_ALL}number then?")
        secondnum = float(input())
        print(f"The answer is {Fore.RED}{((firstnum / secondnum) / Avogadronumber)}{Style.RESET_ALL}{Style.BRIGHT}. \n \n")
else:
    print(f"\n\nYou have not chosen {Fore.LIGHTMAGENTA_EX}any {Style.RESET_ALL}of the choices, which is why you have been prompted to the end of this program. \n\n{Fore.YELLOW}Please close the program and reopen it again if you want to use it.")
    
print(f"{Fore.LIGHTCYAN_EX}\n\n\nIf the program didn't work as intended please dm Flow#0002 on discord. \nBut judging how you've seen this message, it probably worked!!\nWell anyways, until next time. see ya later!!!{Style.RESET_ALL}{Style.BRIGHT}\n\nPress enter to terminate the program.")
exit = input()
