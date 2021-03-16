# Created by flow :>
# This is the third version of calculator. The new things added can be found below.
"""
1- Changed the colors, and added more colors. (Please don't kill me if it's too rainbow)
2- Changed the variables names, and thus looks more friendlier.
3- Added big ASCII texts that should make it look good :)
4- You can declare the variable {Status_of_calculator} off and on, like a power switch. (Line 18)
5- Other minor changes.
"""
def main():
    import os
    import time

    os.system("title Flow's calculator!")
    from colorama import init, Fore, Style
    init(convert=True, autoreset=True)
    #Variables stored here that are defined not by the user.
    Status_of_calculator = True
    Avogadronumber = 6.0221409 * 10 ** 23
    nolist = ['no', 'n', 'nope']
    yeslist = ['yes', 'y', 'yea', 'yeah']
    # If status is set to False, the program will close after 200 seconds ( 4 minutes ).
    if Status_of_calculator == False:
        os.system("title :(")
        print(f"""{Fore.RED}
                                    ███████╗████████╗ █████╗ ████████╗██╗   ██╗███████╗    ██████╗  ██████╗ ██╗    ██╗███╗   ██╗
                                    ██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║   ██║██╔════╝    ██╔══██╗██╔═══██╗██║    ██║████╗  ██║
                                    ███████╗   ██║   ███████║   ██║   ██║   ██║███████╗    ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║
                                    ╚════██║   ██║   ██╔══██║   ██║   ██║   ██║╚════██║    ██║  ██║██║   ██║██║███╗██║██║╚██╗██║
                                    ███████║   ██║   ██║  ██║   ██║   ╚██████╔╝███████║    ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║
                                    ╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝    ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝

        
        """)
    elif Status_of_calculator == True:
        def formatNumber(num):
            if num % 1 == 0:
                return int(num)
            else:
                return num


        os.system("title Loading calculator. Please wait..")
                                                        # Title down below that will get deleted after 3 seconds.
        print(f"""{Fore.GREEN}
                                ███████╗████████╗ █████╗ ████████╗██╗   ██╗███████╗     ██████╗ ███╗   ██╗    
                                ██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║   ██║██╔════╝    ██╔═══██╗████╗  ██║    
                                ███████╗   ██║   ███████║   ██║   ██║   ██║███████╗    ██║   ██║██╔██╗ ██║    
                                ╚════██║   ██║   ██╔══██║   ██║   ██║   ██║╚════██║    ██║   ██║██║╚██╗██║    
                                ███████║   ██║   ██║  ██║   ██║   ╚██████╔╝███████║    ╚██████╔╝██║ ╚████║    
                                ╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝     ╚═════╝ ╚═╝  ╚═══╝    
        """)
        time.sleep(3)
        
        os.system("cls")
        os.system("title Flow's calculator. Running...")
                    
        print(f""" {Fore.LIGHTMAGENTA_EX}
                                     ______           __                   __            __                       
                                    /      \         |  \                 |  \          |  \                      
                                   |  ▓▓▓▓▓▓\ ______ | ▓▓ _______ __    __| ▓▓ ______  _| ▓▓_    ______   ______  
                                   | ▓▓   \▓▓|      \| ▓▓/       \  \  |  \ ▓▓|      \|   ▓▓ \  /      \ /      \ 
                                   | ▓▓       \▓▓▓▓▓▓\ ▓▓  ▓▓▓▓▓▓▓ ▓▓  | ▓▓ ▓▓ \▓▓▓▓▓▓ \▓▓▓▓▓▓ |  ▓▓▓▓▓▓\  ▓▓▓▓▓▓
                                   | ▓▓   __ /      ▓▓ ▓▓ ▓▓     | ▓▓  | ▓▓ ▓▓/      ▓▓ | ▓▓ __| ▓▓  | ▓▓ ▓▓   \▓▓
                                   | ▓▓__/  \  ▓▓▓▓▓▓▓ ▓▓ ▓▓_____| ▓▓__/ ▓▓ ▓▓  ▓▓▓▓▓▓▓ | ▓▓|  \ ▓▓__/ ▓▓ ▓▓      
                                    \▓▓    ▓▓\▓▓    ▓▓ ▓▓\▓▓     \ ▓▓    ▓▓ ▓▓\▓▓    ▓▓  \▓▓  ▓▓\▓▓    ▓▓ ▓▓      
                                     \▓▓▓▓▓▓  \▓▓▓▓▓▓▓\▓▓ \▓▓▓▓▓▓▓ \▓▓▓▓▓▓ \▓▓ \▓▓▓▓▓▓▓   \▓▓▓▓  \▓▓▓▓▓▓ \▓▓      
                                                                                
                                                                                
                                                                                

        """)   
        
        
        print(f"{Fore.GREEN}You have opened up a calculator.\nWhat makes this calculator different is that it already has Avogadro's number integrated to it!\n")
        print(f"{Fore.RED}1 to 4 is normal calculation, 5 to 8 is the same but with Avogadro's number.{Fore.RESET}\n\n1 = add, 2 = subtract, 3 = multiply, 4 = divide\n\n5 = add + Avogadro's number, 6 = subtract - Avogadro's number\n7 = multiply * Avogadro's number, 8 = divide /  Avogadro's number")
        A = int(input(f"{Fore.MAGENTA}\nPlease type your choice:  {Style.RESET_ALL}{Fore.BLUE}")) 
                                                # Calculation down below
                                                # will unquote the floatToString function when I understand how to remove trailing zeros for floats. Ofcourse other than the way of rounding which does remove it :p                
        if A == 1:
            print(f"\n{Fore.RESET}You have chosen {Fore.LIGHTRED_EX}addition!{Style.RESET_ALL} \n \nWhat is the {Fore.LIGHTMAGENTA_EX}first {Style.RESET_ALL}number?")
            firstnum = float(input(f"{Fore.MAGENTA}\nPlease type your first desired number:  {Style.RESET_ALL}{Fore.BLUE}"))
            print(f"\n{Fore.RESET}What is the {Fore.LIGHTMAGENTA_EX}second {Style.RESET_ALL}number?")
            secondnum = float(input(f"{Fore.MAGENTA}\nPlease type your second desired number:  {Style.RESET_ALL}{Fore.BLUE}"))
            total = firstnum + secondnum 
            rounded = round(total)
                                    #Will add when I understand it

            print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Fore.MAGENTA} {firstnum}{Style.RESET_ALL}{Style.BRIGHT} +{Style.RESET_ALL} {Fore.MAGENTA}{secondnum}{Style.RESET_ALL} = {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
            print(f"\nThe {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} answer is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")        
            """
            print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Fore.MAGENTA} {firstnum}{Style.RESET_ALL}{Style.BRIGHT} +{Style.RESET_ALL} {Fore.MAGENTA}{secondnum}{Style.RESET_ALL} = {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")

            print(f"\nThe {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} answer is {Fore.RED}{total}{Style.RESET_ALL}, and the {Fore.LIGHTGREEN_EX}rounded{Style.RESET_ALL}anwser is {rounded}{Style.BRIGHT}.")
            """
        elif A == 2:
            print(f"\n{Fore.RESET}You have chosen {Fore.LIGHTRED_EX} subtraction!{Style.RESET_ALL} \n \nThis will subtract the first number by the second number.")
            print(f"\nWhat is the {Fore.LIGHTMAGENTA_EX}first {Style.RESET_ALL}number?")
            firstnum = float(input(f"{Fore.MAGENTA}\nPlease type your first desired number:  {Style.RESET_ALL}{Fore.BLUE}"))
            print(f"\n{Fore.RESET}What is the {Fore.LIGHTMAGENTA_EX}second {Style.RESET_ALL}number?")
            secondnum = float(input(f"{Fore.MAGENTA}\nPlease type your second desired number:  {Style.RESET_ALL}{Fore.BLUE}"))
            total = firstnum - secondnum
            print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Fore.MAGENTA} {firstnum}{Style.RESET_ALL}{Style.BRIGHT} - {Style.RESET_ALL}{Fore.MAGENTA}{secondnum}{Style.RESET_ALL} = {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
            print(f"\nThe {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} answer is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
        elif A == 3:
            print(f"\n{Fore.RESET}You have chosen {Fore.LIGHTRED_EX}multiplication!{Style.RESET_ALL} \n \nWhat is the {Fore.LIGHTMAGENTA_EX}first {Style.RESET_ALL}number?")
            firstnum = float(input(f"{Fore.MAGENTA}\nPlease type your first desired number:  {Style.RESET_ALL}{Fore.BLUE}"))
            print(f"\n{Fore.RESET}What is the {Fore.LIGHTMAGENTA_EX}second {Style.RESET_ALL}number?")
            secondnum = float(input(f"{Fore.MAGENTA}\nPlease type your second desired number:  {Style.RESET_ALL}{Fore.BLUE}"))
            total = firstnum * secondnum
            print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Fore.MAGENTA} {firstnum}{Style.RESET_ALL}{Style.BRIGHT} * {Style.RESET_ALL}{Fore.MAGENTA}{secondnum}{Style.RESET_ALL} = {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
            print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} answer is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
        elif A == 4:
            print(f"\n{Fore.RESET}You have chosen {Fore.LIGHTRED_EX}division!{Style.RESET_ALL} \n{Fore.YELLOW}Please note:{Style.RESET_ALL} This will divide the first number over the second number.\n \nWhat is the {Fore.LIGHTMAGENTA_EX}first {Style.RESET_ALL}number?")
            firstnum = float(input(f"{Fore.MAGENTA}\nPlease type your first desired number:  {Style.RESET_ALL}{Fore.BLUE}"))
            print(f"\n{Fore.RESET}What is the {Fore.LIGHTMAGENTA_EX}second {Style.RESET_ALL}number?")
            secondnum = float(input(f"{Fore.MAGENTA}\nPlease type your second desired number:  {Style.RESET_ALL}{Fore.BLUE}"))
            if secondnum == 0:
                print(f" \n \n{Fore.RED}Division{Style.RESET_ALL} by {Style.BRIGHT}0{Style.RESET_ALL} is {Style.BRIGHT}impossible.\n\n")
            else:
                total = firstnum / secondnum
                print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Fore.MAGENTA} {firstnum}{Style.RESET_ALL}{Style.BRIGHT} / {Style.RESET_ALL}{Fore.MAGENTA}{secondnum}{Style.RESET_ALL} = {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
                print(f"\nThe {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} answer is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
        elif A == 5:
            print(f"\n{Fore.RESET}You have chosen {Fore.LIGHTRED_EX}addition!{Style.RESET_ALL} \n \nWhat's the {Fore.LIGHTMAGENTA_EX}first {Style.RESET_ALL}number?")
            firstnum = float(input(f"{Fore.MAGENTA}\nPlease type your first desired number:  {Style.RESET_ALL}{Fore.BLUE}"))
            print(f"\n{Fore.RESET}Do you want a second number? 1 = no, 2 = yes")
            choice = int(input(f"{Fore.MAGENTA}\nPlease type your desired choice:  {Style.RESET_ALL}{Fore.RED}"))
            if choice == 1:
                total = firstnum + Avogadronumber
                print(f"{Fore.RESET}\nThe {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Fore.MAGENTA} {firstnum}{Style.RESET_ALL}{Style.BRIGHT} + {Style.RESET_ALL}{Fore.MAGENTA}{Avogadronumber}{Style.RESET_ALL} = {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
                print(f"\nThe {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} answer is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
            else:
                print(f"\n{Fore.RESET}What is the {Fore.LIGHTMAGENTA_EX}second {Style.RESET_ALL}number then?")
                secondnum = float(input(f"{Fore.MAGENTA}\nPlease type your second desired number:  {Style.RESET_ALL}{Fore.BLUE}"))
                total = firstnum + secondnum + Avogadronumber
                print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Fore.MAGENTA} {firstnum}{Style.RESET_ALL}{Style.BRIGHT} + {Style.RESET_ALL}{Fore.MAGENTA}{secondnum}{Style.RESET_ALL}{Style.BRIGHT} +{Style.RESET_ALL} {Fore.MAGENTA}{Avogadronumber}{Style.RESET_ALL} = {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
                print(f"\nThe {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} answer is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
        elif A == 6:
            print(f"\n{Fore.RESET}You have chosen {Fore.LIGHTRED_EX}subtraction!{Style.RESET_ALL} \n{Fore.YELLOW}Please note:{Style.RESET_ALL}This will subtract the first number to the second number (if you choose one) to Avogadro's number.")
            print(f"\nWhat's the {Fore.LIGHTMAGENTA_EX}first {Style.RESET_ALL}number?")
            firstnum = float(input(f"{Fore.MAGENTA}\nPlease type your first desired number:  {Style.RESET_ALL}{Fore.BLUE}"))
            print(f"\n{Fore.RESET}{Style.BRIGHT}Do you want a second number? 1 = no, 2 = yes")
            choice = int(input(f"{Fore.MAGENTA}\nPlease type your desired choice:  {Style.RESET_ALL}{Fore.RED}"))
            if choice == 1:
                total = firstnum - Avogadronumber
                print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Fore.MAGENTA} {firstnum}{Style.RESET_ALL}{Style.BRIGHT} - {Style.RESET_ALL}{Fore.MAGENTA}{Avogadronumber}{Style.RESET_ALL} = {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
                print(f"\nThe {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} answer is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
            else:
                print(f"\n{Fore.RESET}What is the {Fore.LIGHTMAGENTA_EX}second {Style.RESET_ALL}number then?")
                secondnum = float(input(f"{Fore.MAGENTA}\nPlease type your second desired number:  {Style.RESET_ALL}{Fore.BLUE}"))
                total = (firstnum - secondnum) - Avogadronumber
                print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Style.BRIGHT}({Style.RESET_ALL}{Fore.MAGENTA}{firstnum}{Style.RESET_ALL}{Style.BRIGHT} - {Style.RESET_ALL}{Fore.MAGENTA}{secondnum}{Style.RESET_ALL}{Style.BRIGHT}) - {Fore.MAGENTA}{Avogadronumber}{Style.RESET_ALL} = {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
                print(f"\nThe {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} answer is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
        elif A == 7:
            print(f"\n{Fore.RESET}You have chosen {Fore.LIGHTRED_EX}multiplication!{Style.RESET_ALL} \n \nWhat's the {Fore.LIGHTMAGENTA_EX}first {Style.RESET_ALL}number?")
            firstnum = float(input(f"{Fore.MAGENTA}\nPlease type your first desired number:  {Style.RESET_ALL}{Fore.BLUE}"))
            print("\n{Fore.RESET}Do you want a second number? 1 = no, 2 = yes")
            choice = int(input(f"{Fore.MAGENTA}\nPlease type your desired choice:  {Style.RESET_ALL}{Fore.RED}"))
            if choice == 1:
                total = firstnum * Avogadronumber
                print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Fore.MAGENTA} {firstnum}{Style.RESET_ALL}{Style.BRIGHT} * {Style.RESET_ALL}{Fore.MAGENTA}{Avogadronumber}{Style.RESET_ALL} = {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
                print(f"\nThe {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} answer is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
            else:
                print(f"\n{Fore.RESET}What is the {Fore.LIGHTMAGENTA_EX}second {Style.RESET_ALL}number then?")
                secondnum = float(input(f"{Fore.MAGENTA}\nPlease type your second desired number:  {Style.RESET_ALL}{Fore.BLUE}"))
                total = firstnum * secondnum * Avogadronumber
                print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Fore.MAGENTA} {firstnum}{Style.RESET_ALL}{Style.BRIGHT} * {Style.RESET_ALL}{Fore.MAGENTA}{secondnum}{Style.RESET_ALL}{Style.BRIGHT} * {Style.RESET_ALL}{Fore.MAGENTA}{Avogadronumber}{Style.RESET_ALL} = {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
                print(f"\nThe {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} answer is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
        elif A == 8:
            print(f"\n{Fore.RESET}You have chosen {Fore.LIGHTRED_EX}division!{Style.RESET_ALL} \n{Fore.YELLOW}Please note:{Style.RESET_ALL} This will divide the first number over the second number (If you choose a second number) over Avogadro's number.\n \nWhat's the {Fore.LIGHTMAGENTA_EX}first {Style.RESET_ALL}number?")
            firstnum = float(input(f"{Fore.MAGENTA}\nPlease type your first desired number:  {Style.RESET_ALL}{Fore.BLUE}"))
            print(f"\n{Fore.RESET}{Style.BRIGHT}Do you want a second number? 1 = no, 2 = yes")
            choice = int(input(f"{Fore.MAGENTA}\nPlease type your desired choice:  {Style.RESET_ALL}{Fore.RED}"))
            if choice == 1:
                total = firstnum / Avogadronumber 
                print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Fore.MAGENTA} {firstnum}{Style.RESET_ALL}{Style.BRIGHT} / {Style.RESET_ALL}{Fore.MAGENTA}{Avogadronumber}{Style.RESET_ALL} = {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} answer is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
            else:
                print(f"\n{Fore.RESET}What is the {Fore.LIGHTMAGENTA_EX}second {Style.RESET_ALL}number then?")
                secondnum = float(input(f"{Fore.MAGENTA}\nPlease type your second desired number:  {Style.RESET_ALL}{Fore.BLUE}"))
                if secondnum == 0:
                    del secondnum
                try:
                    secondnum
                except NameError:
                    print(f" \n \n{Fore.RED}Division{Style.RESET_ALL} by {Style.BRIGHT}0{Style.RESET_ALL} is {Style.BRIGHT}impossible.\n\n")
                else:
                    total = (firstnum / secondnum) / Avogadronumber
                    print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Style.BRIGHT}({Style.RESET_ALL}{Fore.MAGENTA}{firstnum}{Style.RESET_ALL}{Style.BRIGHT} / {Style.RESET_ALL}{Fore.MAGENTA}{secondnum}{Style.RESET_ALL}{Style.BRIGHT} / {Style.RESET_ALL}{Fore.MAGENTA}{Avogadronumber}{Style.RESET_ALL}{Style.BRIGHT}{Style.RESET_ALL} = {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
                    print(f"\nThe {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} answer is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.\n\n")
        else:
            print(f"\n\n{Fore.RESET}You have not chosen {Fore.LIGHTMAGENTA_EX}any {Style.RESET_ALL}of the choices, which is why you have been prompted to the end of this program. \n\n{Fore.YELLOW}Please close the program and reopen it again if you want to use it.")
            

        print(f"{Fore.LIGHTCYAN_EX}\n\n\nIf you have any questions please contact me on my github(https://github.com/Flowgonnarap/calculator){Style.RESET_ALL}{Style.BRIGHT}.\n\n")
        Repeat = input(f"{Fore.CYAN}Do you wish to restart the program?{Style.RESET_ALL}   {Fore.LIGHTBLUE_EX}").lower()
        if Repeat in yeslist:
            os.system("cls")
            main()
        elif Repeat == "":
            exit()
        elif Repeat in nolist:
            exit()
            #Where the code starts
main()
