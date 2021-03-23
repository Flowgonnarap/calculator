def main():
    import os
    import time
    from math import sqrt
    os.system("title Flow's calculator!")
    from colorama import init, Fore, Style
    init(convert=True, autoreset=True)
    #Variables stored here that are defined not by the user.
    Status_of_calculator = True
    Avogadronumber = 6.0221409 * 10 ** 23
    nolist = ['no', 'n', 'nope', 'nop']
    yeslist = ['yes', 'y', 'yea', 'yeah']
    exitlist = ['q', 'quit', 'exit', 'die', 'exit()', 'leave', ' ']
    add = ['add', 'addition']
    multiply = ['multiply', 'time', 'x']
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
        os.system("title Flow's calculator -Running...")
                    
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
        
        
        print(f"{Fore.GREEN}You have opened up a calculator.\n")
        print(f"{Fore.RED}1 to 4 is basic math, 5 to 8 has more options to choose.{Fore.RESET}\n\n1 = add, 2 = subtract, 3 = multiply, 4 = divide\n\n5 = square root")
        A = input(f"{Fore.MAGENTA}\nPlease type your choice:  {Style.RESET_ALL}{Fore.BLUE}")
        def quit_progam_any_time(check_input):
            if check_input in exitlist: 
                return True
            return False

        def is_digit(check_input):
            '''
            function checking if your string is a pure digit, int
            return : bool
            '''
            if check_input.isdigit():
                return True
            return False

        def is_string_only(check_input):
            '''
            function checking if your string is all letters
            return : bool
            '''    
            if check_input.isalpha():
                return True
            return False

        def is_string_with_space(check_input):
            '''
            function checking if your string is all letters, but including space(s)
            return : bool
            '''   
            valid = False
            if ' ' in check_input:
                for char in check_input:
                    if char.isdigit():
                        valid = False
                    elif char.isalpha() or char.isspace():
                        valid = True
            return valid

        def is_string_or_num(check_input):
            '''
            function checking if your string is all letters or numbers
            return : bool
            '''       
            if check_input.isalnum():
                return True
            return False

        def is_float(check_input):
            '''
            function checking if your string is a floating point
            return : bool
            '''   
            if '.' in check_input:
                split_number = check_input.split('.')
                if len(split_number) == 2 and split_number[0].isdigit() and split_number[1].isdigit():
                        return True
            return False
        
        while A not in exitlist and not is_digit(A):
            print(f"{Style.RESET_ALL}{Fore.RED}\nInvalid Input, Integers are the only values accepted.")
            A = input(f"{Fore.MAGENTA}\nPlease repick your choise from the list above:{Style.RESET_ALL}{Fore.RED}   ")
        if quit_progam_any_time(A) == True: #We add this part incase the user wants to exit while inputting a choice
            print(f"{Style.BRIGHT}{Fore.YELLOW}\nGoodbye!")
            time.sleep(2)
            exit() 

        if A !=is_digit(A):
            A = int(A)

                                                # Calculation down below
        if A == 1:
            print(f"\n{Fore.RESET}You have chosen {Fore.LIGHTRED_EX}addition!{Style.RESET_ALL} \n \nWhat is the {Fore.LIGHTMAGENTA_EX}first {Style.RESET_ALL}number?")
            firstnum = input(f"{Fore.MAGENTA}\nPlease type your first desired number:  {Style.RESET_ALL}{Fore.BLUE}")
 
            while firstnum not in exitlist and not is_float(firstnum) and not is_digit(firstnum): #Loops if user inputs a letter and special characters, or actuall anything else rather than a decimal or an integer
                print(f"{Fore.RED}\nInvalid entry. Only decimals and integers are accepted.")
                firstnum = input(f"{Fore.MAGENTA}\nPlease retype your first desired number:  {Style.RESET_ALL}{Fore.BLUE}")
            if quit_progam_any_time(firstnum) == True: #We add this part incase the user wants to exit while inputting
                print(f"{Style.BRIGHT}{Fore.YELLOW}Goodbye!")
                time.sleep(2)
                exit()  
            print(f"\n{Fore.RESET}What is the {Fore.LIGHTMAGENTA_EX}second {Style.RESET_ALL}number?")
            secondnum = input(f"{Fore.MAGENTA}\nPlease type your second desired number:  {Style.RESET_ALL}{Fore.BLUE}")
            while secondnum not in exitlist and not is_float(secondnum) and not is_digit(secondnum):
                print(f"{Fore.RED}\nInvalid entry. Only decimals and integers are accepted.")
                secondnum = input(f"{Fore.MAGENTA}\nPlease retype your second desired number:  {Style.RESET_ALL}{Fore.BLUE}")
            if quit_progam_any_time(secondnum) == True: #We add this part incase the user wants to exit while inputting
                print(f"{Style.BRIGHT}{Fore.YELLOW}Goodbye!")
                time.sleep(2)
                exit()  


            if firstnum or secondnum not in exitlist and is_digit(secondnum, firstnum) or is_float(secondnum, firstnum): #If user passes the while loop, then he is checked 1 more time and then converted to a float(decimal) as it has been set to as a string(letter)
                firstnum = float(firstnum)
                secondnum = float(secondnum)
                total = firstnum + secondnum


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
            firstnum = input(f"{Fore.MAGENTA}\nPlease type your first desired number:  {Style.RESET_ALL}{Fore.BLUE}")
            while firstnum not in exitlist and not is_float(firstnum) and not is_digit(firstnum): #Loops if user inputs a letter and special characters, or actuall anything else rather than a decimal or an integer
                print(f"{Fore.RED}\nInvalid entry. Only decimals and integers are accepted.")
                firstnum = input(f"{Fore.MAGENTA}\nPlease retype your first desired number:  {Style.RESET_ALL}{Fore.BLUE}")
            if quit_progam_any_time(firstnum) == True: #We add this part incase the user wants to exit while inputting
                print(f"{Style.BRIGHT}{Fore.YELLOW}Goodbye!")
                time.sleep(2)
                exit()  
            print(f"\n{Fore.RESET}What is the {Fore.LIGHTMAGENTA_EX}second {Style.RESET_ALL}number?")
            secondnum = input(f"{Fore.MAGENTA}\nPlease type your second desired number:  {Style.RESET_ALL}{Fore.BLUE}")
            while secondnum not in exitlist and not is_float(secondnum) and not is_digit(secondnum):
                print(f"{Fore.RED}\nInvalid entry. Only decimals and integers are accepted.")
                secondnum = input(f"{Fore.MAGENTA}\nPlease retype your second desired number:  {Style.RESET_ALL}{Fore.BLUE}")
            if quit_progam_any_time(secondnum) == True: #We add this part incase the user wants to exit while inputting
                print(f"{Style.BRIGHT}{Fore.YELLOW}Goodbye!")
                time.sleep(2)
                exit()  

            if firstnum or secondnum not in exitlist and is_digit(secondnum, firstnum) or is_float(secondnum, firstnum): #If user passes the while loop, then he is checked 1 more time and then converted to a float(decimal) as it has been set to as a string(letter)
                firstnum = float(firstnum)
                secondnum = float(secondnum)
                total = firstnum - secondnum
                print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Fore.MAGENTA} {firstnum}{Style.RESET_ALL}{Style.BRIGHT} +{Style.RESET_ALL} {Fore.MAGENTA}{secondnum}{Style.RESET_ALL} = {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
                print(f"\nThe {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} answer is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")       
        elif A == 3:
            print(f"\n{Fore.RESET}You have chosen {Fore.LIGHTRED_EX}multiplication!{Style.RESET_ALL} \n \nWhat is the {Fore.LIGHTMAGENTA_EX}first {Style.RESET_ALL}number?")
            firstnum = input(f"{Fore.MAGENTA}\nPlease type your first desired number:  {Style.RESET_ALL}{Fore.BLUE}")
            while firstnum not in exitlist and not is_float(firstnum) and not is_digit(firstnum): #Loops if user inputs a letter and special characters, or actuall anything else rather than a decimal or an integer
                print(f"{Fore.RED}\nInvalid entry. Only decimals and integers are accepted.")
                firstnum = input(f"{Fore.MAGENTA}\nPlease retype your first desired number:  {Style.RESET_ALL}{Fore.BLUE}")
            if quit_progam_any_time(firstnum) == True: #We add this part incase the user wants to exit while inputting
                print(f"{Style.BRIGHT}{Fore.YELLOW}Goodbye!")
                time.sleep(2)
                exit()  
            print(f"\n{Fore.RESET}What is the {Fore.LIGHTMAGENTA_EX}second {Style.RESET_ALL}number?")
            secondnum = input(f"{Fore.MAGENTA}\nPlease type your second desired number:  {Style.RESET_ALL}{Fore.BLUE}")
            while secondnum not in exitlist and not is_float(secondnum) and not is_digit(secondnum):
                print(f"{Fore.RED}\nInvalid entry. Only decimals and integers are accepted.")
                secondnum = input(f"{Fore.MAGENTA}\nPlease retype your second desired number:  {Style.RESET_ALL}{Fore.BLUE}")
            if quit_progam_any_time(secondnum) == True: #We add this part incase the user wants to exit while inputting
                print(f"{Style.BRIGHT}{Fore.YELLOW}Goodbye!")
                time.sleep(2)
                exit()  


            if firstnum or secondnum not in exitlist and is_digit(secondnum, firstnum) or is_float(secondnum, firstnum): #If user passes the while loop, then he is checked 1 more time and then converted to a float(decimal) as it has been set to as a string(letter)
                firstnum = float(firstnum)
                secondnum = float(secondnum)
                total = firstnum * secondnum
                print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Fore.MAGENTA} {firstnum}{Style.RESET_ALL}{Style.BRIGHT} * {Style.RESET_ALL}{Fore.MAGENTA}{secondnum}{Style.RESET_ALL} = {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
                print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} answer is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
        elif A == 4:
            print(f"\n{Fore.RESET}You have chosen {Fore.LIGHTRED_EX}division!{Style.RESET_ALL} \n{Fore.YELLOW}Please note:{Style.RESET_ALL} This will divide the first number over the second number.\n \nWhat is the {Fore.LIGHTMAGENTA_EX}first {Style.RESET_ALL}number?")
            firstnum = input(f"{Fore.MAGENTA}\nPlease type your first desired number:  {Style.RESET_ALL}{Fore.BLUE}")
            while firstnum not in exitlist and not is_float(firstnum) and not is_digit(firstnum): #Loops if user inputs a letter and special characters, or actuall anything else rather than a decimal or an integer
                print(f"{Fore.RED}\nInvalid entry. Only decimals and integers are accepted.")
                firstnum = input(f"{Fore.MAGENTA}\nPlease retype your first desired number:  {Style.RESET_ALL}{Fore.BLUE}")

            if quit_progam_any_time(firstnum) == True: #We add this part incase the user wants to exit while inputting
                print(f"{Style.BRIGHT}{Fore.YELLOW}Goodbye!")
                time.sleep(2)
                exit()  
            
            print(f"\n{Fore.RESET}What is the {Fore.LIGHTMAGENTA_EX}second {Style.RESET_ALL}number?")
            secondnum = input(f"{Fore.MAGENTA}\nPlease type your second desired number:  {Style.RESET_ALL}{Fore.BLUE}")
            if quit_progam_any_time(secondnum) == True: #We add this part incase the user wants to exit while inputting
                print(f"{Style.BRIGHT}{Fore.YELLOW}Goodbye!")
                time.sleep(2)
                exit()  
            while secondnum not in exitlist and not is_float(secondnum) and not is_digit(secondnum):
                print(f"{Fore.RED}\nInvalid entry. Only decimals and integers are accepted.")
                secondnum = input(f"{Fore.MAGENTA}\nPlease retype your second desired number:  {Style.RESET_ALL}{Fore.BLUE}")


            if firstnum or secondnum not in exitlist and is_digit(secondnum, firstnum) or is_float(secondnum, firstnum): #If user passes the while loop, then he is checked 1 more time and then converted to a float(decimal) as it has been set to as a string(letter)
                firstnum = float(firstnum)
                secondnum = float(secondnum)
                total = firstnum / secondnum

            print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Fore.MAGENTA} {firstnum}{Style.RESET_ALL}{Style.BRIGHT} / {Style.RESET_ALL}{Fore.MAGENTA}{secondnum}{Style.RESET_ALL} = {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
            print(f"\nThe {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} answer is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
        elif A == 5:
            print(f"\n{Fore.RESET}You have chosen {Fore.LIGHTRED_EX}square root!{Style.RESET_ALL}")
            firstnum = input(f"{Fore.MAGENTA}\nPlease type your first desired number:  {Style.RESET_ALL}{Fore.BLUE}")
            while firstnum not in exitlist and not is_float(firstnum) and not is_digit(firstnum): #Loops if user inputs a letter and special characters, or actuall anything else rather than a decimal or an integer
                print(f"{Fore.RED}\nInvalid entry. Only decimals and integers are accepted.")
                firstnum = input(f"{Fore.MAGENTA}\nPlease retype your first desired number:  {Style.RESET_ALL}{Fore.BLUE}")

            if quit_progam_any_time(firstnum) == True: #We add this part incase the user wants to exit while inputting
                print(f"{Style.BRIGHT}{Fore.YELLOW}Goodbye!")
                time.sleep(2)
                exit()  



            if firstnum not in exitlist and is_digit(firstnum) or is_float(firstnum): #If user passes the while loop, then he is checked 1 more time and then converted to a float(decimal) as it has been set to as a string(letter)
                firstnum = float(firstnum)
                result = sqrt(firstnum)
            print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Fore.MAGENTA} √ {Style.RESET_ALL}{Fore.YELLOW}{firstnum}{Style.RESET_ALL} = {Fore.RED}{result}{Style.RESET_ALL}{Style.BRIGHT}.")            
            print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} answer is {Fore.RED}{result}{Style.RESET_ALL}{Style.BRIGHT}.")

  
      
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
