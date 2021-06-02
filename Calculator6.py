#    Made by Flow.
#    version = 6.0
from decimal import * #Using the decimal library to bring extremely accurates FOR FLOATS. {try doing 0.1 + 0.2 without the decimal library to understand what I mean.}
getcontext() 

def main():
    import os # Used for the titles
    import time # Used for a delay at the "status on" part and exiting program.
    from math import sqrt #Used for the square root as python doesn't have squareroot built in.
    from functools import reduce  
    import signal
    import sys
    signal.signal(signal.SIGINT, lambda x, y: sys.exit(0)) # Source for this part is from Stack OverFlow
    import operator
    os.system("title Flow's calculator!")
    from colorama import init, Fore, Style # Used for the colors if it wasn't obvious by the title 
    init(convert=True, autoreset=True)
    #--------------------------------------------DO NOT CHANGE----------------------------------------------------------
    #Variables stored here that are defined not by the user.
    no_choice = "INVALID CHOICE!"
    Status_of_calculator = True
    Avogadronumber = 6.0221409 * 10 ** 23
    avogadro_choices = [1,2,3,4,5,6,7,8]
    yeslist = ['yes', 'y', 'yea', 'yeah']
    exitlist = ['q', 'quit', 'exit', 'die', 'exit()', 'leave', ' ']
    logo_avagadro_number = f"""

                     █████╗ ██╗   ██╗ ██████╗  ██████╗  █████╗ ██████╗ ██████╗  ██████╗    ▄█   ███████╗      
                    ██╔══██╗██║   ██║██╔═══██╗██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔═══██╗   ██   ██╔════╝     
                    ███████║██║   ██║██║   ██║██║  ███╗███████║██║  ██║██████╔╝██║   ██║   ▀▀   ███████╗     
                    ██╔══██║╚██╗ ██╔╝██║   ██║██║   ██║██╔══██║██║  ██║██╔══██╗██║   ██║        ╚════██║     
                    ██║  ██║ ╚████╔╝ ╚██████╔╝╚██████╔╝██║  ██║██████╔╝██║  ██║╚██████╔╝        ███████║      
                    ╚═╝  ╚═╝  ╚═══╝   ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝         ╚══════╝      
                        
                        
                    ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗   
                    ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗   
                    ██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝   
                    ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗   
                    ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║    
                    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝    
                        """
    status_on = f"""{Fore.GREEN}
                                ███████╗████████╗ █████╗ ████████╗██╗   ██╗███████╗     ██████╗ ███╗   ██╗    
                                ██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║   ██║██╔════╝    ██╔═══██╗████╗  ██║    
                                ███████╗   ██║   ███████║   ██║   ██║   ██║███████╗    ██║   ██║██╔██╗ ██║    
                                ╚════██║   ██║   ██╔══██║   ██║   ██║   ██║╚════██║    ██║   ██║██║╚██╗██║    
                                ███████║   ██║   ██║  ██║   ██║   ╚██████╔╝███████║    ╚██████╔╝██║ ╚████║    
                                ╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝     ╚═════╝ ╚═╝  ╚═══╝    
        """
    status_off = f"""{Fore.RED}
                            ███████╗████████╗ █████╗ ████████╗██╗   ██╗███████╗    ██████╗  ██████╗ ██╗    ██╗███╗   ██╗
                            ██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║   ██║██╔════╝    ██╔══██╗██╔═══██╗██║    ██║████╗  ██║
                            ███████╗   ██║   ███████║   ██║   ██║   ██║███████╗    ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║
                            ╚════██║   ██║   ██╔══██║   ██║   ██║   ██║╚════██║    ██║  ██║██║   ██║██║███╗██║██║╚██╗██║
                            ███████║   ██║   ██║  ██║   ██║   ╚██████╔╝███████║    ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║
                            ╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝    ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝

        
        """
    calculator_logo = f"""{Fore.LIGHTMAGENTA_EX}
                                     ______           __                   __            __                       
                                    /      \         |  \                 |  \          |  \                      
                                   |  ▓▓▓▓▓▓\ ______ | ▓▓ _______ __    __| ▓▓ ______  _| ▓▓_    ______   ______  
                                   | ▓▓   \▓▓|      \| ▓▓/       \  \  |  \ ▓▓|      \|   ▓▓ \  /      \ /      \ 
                                   | ▓▓       \▓▓▓▓▓▓\ ▓▓  ▓▓▓▓▓▓▓ ▓▓  | ▓▓ ▓▓ \▓▓▓▓▓▓ \▓▓▓▓▓▓ |  ▓▓▓▓▓▓\  ▓▓▓▓▓▓
                                   | ▓▓   __ /      ▓▓ ▓▓ ▓▓     | ▓▓  | ▓▓ ▓▓/      ▓▓ | ▓▓ __| ▓▓  | ▓▓ ▓▓   \▓▓
                                   | ▓▓__/  \  ▓▓▓▓▓▓▓ ▓▓ ▓▓_____| ▓▓__/ ▓▓ ▓▓  ▓▓▓▓▓▓▓ | ▓▓|  \ ▓▓__/ ▓▓ ▓▓      
                                    \▓▓    ▓▓\▓▓    ▓▓ ▓▓\▓▓     \ ▓▓    ▓▓ ▓▓\▓▓    ▓▓  \▓▓  ▓▓\▓▓    ▓▓ ▓▓      
                                     \▓▓▓▓▓▓  \▓▓▓▓▓▓▓\▓▓ \▓▓▓▓▓▓▓ \▓▓▓▓▓▓ \▓▓ \▓▓▓▓▓▓▓   \▓▓▓▓  \▓▓▓▓▓▓ \▓▓      
                                                                                
                                                                                
                                                                                

        """ 


















    #---------------------------------------FUNCTIONS STORED HERE------------------------------------------------------
    def quit_progam_any_time(check_input):
        if check_input in exitlist: 
            return True
        return False

    def is_digit(check_input):
        
        #function checking if your string is a pure digit, int
        #return : bool
        
     
        try:
            val = int(check_input) 
            return True
        except ValueError:
            return False
    
    def is_float(check_input):

        #function checking if your string is a floating point
        #return : bool

        if '.' in check_input:
            split_number = check_input.split('.')
            split_part = split_number[0]
            split_part_1 = split_number[1]
            if len(split_number) == 2:
                if is_digit(split_part) == True and is_digit(split_part_1) == True:
                    return True
        return False 
   

    def checking_(check_input, sign):    
        try:
            checking_.resonation = [Decimal(idx) for idx in check_input.split(sign)]
            return True
        except:
            return False
    def first_num_check(sign):
        global all_numbers
        global splited
        print(f"{Fore.YELLOW}Please note: {Fore.RESET} You must place a number followed by a {Fore.GREEN}{sign}{Fore.RESET} sign.")
        all_numbers = input(f"\n{Fore.MAGENTA}Please type your desired numbers:  {Style.RESET_ALL}{Fore.BLUE}")
        while f"{sign}" not in all_numbers and not checking_(all_numbers, sign) and not is_list_digit(all_numbers,sign):
            print(f"\n{Fore.RED}Invalid entry. Only decimals, integers, and {sign} are accepted.")
            all_numbers = input(f"\n{Fore.MAGENTA}Please retype your desired numbers:  {Style.RESET_ALL}{Fore.BLUE}")
        splited = all_numbers.split(f"{sign}")

        if quit_progam_any_time(all_numbers) == True: #We add this part incase the user wants to exit while inputting
            print(f"{Style.BRIGHT}{Fore.YELLOW}Goodbye!")
            time.sleep(2)
            exit()

        def trying_alot():
            global all_numbers
            global res
            try:
                res = [Decimal(idx) for idx in all_numbers.split(f'{sign}')]
            except:
                print(f"\n{Fore.RED}Invalid entry. Only decimals, integers, and {sign} are accepted.")
                all_numbers = input(f"\n{Fore.MAGENTA}Please retype your desired numbers:  {Style.RESET_ALL}{Fore.BLUE}")
                try:
                    res = [Decimal(idx) for idx in all_numbers.split(f'{sign}')]
                except:
                    trying_alot()
        trying_alot()   
    def negative_checking(check_input):
        if check_input < 0:
            return True
        return False
    def is_list_digit(check_input, sign):
        try:
            if type(check_input) == list:
                return True
            checking_input = [Decimal(idx) for idx in check_input.split(sign)]
            return True  
        except:
            return False   
    def multiply(check_input) :
     
        # Multiply elements one by one
        result = 1
        for x in check_input:
            result = result * x
        return result 
    def power(check_input):
        # Power elements one by one 
        result = check_input[0]
        for x in check_input[1:]:
            result = result ** x
        return result
    def divide(check_input) :
        lotta = check_input
        # Divide elements one by one
        try:
            result = lotta[0]
            for x in lotta[1:]:
                result = result / x
            return result
        except:
            print(f"\n{Fore.RED}Division by {Fore.RESET}{Style.BRIGHT}0{Fore.RED} is {Fore.RESET}{Style.BRIGHT}impossible.")
            Repeat = input(f"\n\n{Fore.CYAN}Do you wish to restart the program?{Style.RESET_ALL}   {Fore.LIGHTBLUE_EX}").lower()
            if Repeat in yeslist:
                os.system("cls")
                main()
            else:
                exit()  
    def subtract(check_input): 
        result = reduce(operator.sub, check_input)
        return result
    #-GLOBAL VARIABLES STORED DOWN BELOW. DO NOT MODIFY AS THIS MAY BREAK PROGRAM-#
    global res
    global all_numbers
    global secondnum
    global base_number
    global splited
    global exponent
    #------------------------------------------------------------------------------#
    if Status_of_calculator == False:
        os.system("title :(")
        print(status_off)
    elif Status_of_calculator == True:

        os.system("title Loading calculator. Please wait..")
        print(status_on)
        time.sleep(3)
        os.system("cls")
        os.system("title Flow's calculator -Running...")
        print(calculator_logo)   
        print(f"{Fore.GREEN}You have opened up a calculator.")
        print(f"\n{Fore.RED}1 to 4 is basic math, 5 to 8 has more options to choose.")
        print(f"\n{Fore.RESET}1 = add(+), 2 = subtract(-), 3 = multiply(*), 4 = divide(/)")
        print(f"\n5 = square root(√), 6 = power(^), 7 = Avogadro's selection")
        A = input(f"\n{Fore.MAGENTA}Please type your choice:  {Style.RESET_ALL}{Fore.BLUE}")
        A = A.lower()            #We do this incase user inputs something of a capital letter for the exitlist keywords.

        while A not in exitlist and not is_digit(A):
            print(f"{Style.RESET_ALL}{Fore.RED}\nInvalid Input, Integers are the only values accepted.")
            A = input(f"\n{Fore.MAGENTA}Please repick your choise from the list above:{Style.RESET_ALL}{Fore.RED}   ")

        if quit_progam_any_time(A) == True: #We add this part incase the user wants to exit while inputting a choice
            print(f"{Style.BRIGHT}{Fore.YELLOW}\nGoodbye!")
            time.sleep(2)
            exit() 
        if A != is_digit(A):
            A = int(A)

                                                # Calculation down below
        if A == 1:
            print(f"\n{Fore.RESET}You have chosen {Fore.LIGHTRED_EX}addition!{Style.RESET_ALL}")
            first_num_check("+")
            total = sum(res)
            print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")        
        elif A == 2:
            print(f"\n{Fore.RESET}You have chosen {Fore.LIGHTRED_EX}subtraction!{Style.RESET_ALL}")
            
            first_num_check("-")
            total = reduce(operator.sub, res)
            print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")       
        elif A == 3:
            print(f"\n{Fore.RESET}You have chosen {Fore.LIGHTRED_EX}multiplication!{Style.RESET_ALL}")
            first_num_check("*")


            total = multiply(res)
            print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
        elif A == 4:
            print(f"\n{Fore.RESET}You have chosen {Fore.LIGHTRED_EX}division!{Style.RESET_ALL} ")
            first_num_check("/")
            total = divide(res)

            print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
        elif A == 5:
            
            print(f"\n{Fore.RESET}You have chosen {Fore.LIGHTRED_EX}square root!{Style.RESET_ALL}")
            firstnum = input(f"\n{Fore.MAGENTA}Please type your first desired number:  {Style.RESET_ALL}{Fore.BLUE}")
            while firstnum not in exitlist and not is_float(firstnum) and not is_digit(firstnum): #Loops if user inputs a letter and special characters, or actually anything else rather than a decimal or an integer
                print(f"\n{Fore.RED}Invalid entry. Only decimals and integers are accepted.")
                firstnum = input(f"\n{Fore.MAGENTA}Please retype your first desired number:  {Style.RESET_ALL}{Fore.BLUE}")
            
            if quit_progam_any_time(firstnum) == True: #We add this part incase the user wants to exit while inputting
                print(f"{Style.BRIGHT}{Fore.YELLOW}Goodbye!")
                time.sleep(2)
                exit()
            firstnum = Decimal(firstnum)
            if negative_checking(firstnum) == True:
                print(f"\n\n{Fore.YELLOW}Please note: {Fore.RESET}This is an {Fore.CYAN}imaginary number{Fore.RESET} as you inputed a negative number.")
                print(f"\n{Fore.YELLOW}i = √-1")
                firstnum = firstnum * (-1)
                result = sqrt(firstnum)
                print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} is {Fore.RED}{result}{Fore.YELLOW} i{Fore.RESET}{Style.BRIGHT}.")

            else:
                result = sqrt(firstnum)
                print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Fore.MAGENTA} √ {Style.RESET_ALL}{Fore.YELLOW}{firstnum}{Style.RESET_ALL} = {Fore.RED}{result}{Style.RESET_ALL}{Style.BRIGHT}.")            
                print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} is {Fore.RED}{result}{Style.RESET_ALL}{Style.BRIGHT}.")

        elif A == 6:
            print(f"\n{Fore.RESET}You have chosen {Fore.LIGHTRED_EX}power!{Style.RESET_ALL}")
            first_num_check("^")
            total = power(res)    
            print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")

        elif A == 7:
            os.system("cls")
            print(logo_avagadro_number)
            print(f"\n{Fore.RESET}You have chosen {Fore.LIGHTRED_EX}Avagadro's selection!{Style.RESET_ALL}")
            print(f"\n\n{Fore.CYAN}1 = addition + Avogadro's number, 2 = subtraction - Avogadro's number")
            print(f"\n{Fore.CYAN}3 = multiplication * Avogadro's number, 4 = division /  Avogadro's number")
            avogadro_choice = input(f"{Fore.MAGENTA}\nPlease type your choice:  {Style.RESET_ALL}{Fore.BLUE}")
            while avogadro_choice not in exitlist and not is_digit(avogadro_choice):
                print(f"\n{Style.RESET_ALL}{Fore.RED}Invalid Input, Integers are the only values accepted.")
                avogadro_choice = input(f"\n{Fore.MAGENTA}Please repick your choise from the list above:{Style.RESET_ALL}{Fore.RED}   ")

            if quit_progam_any_time(avogadro_choice) == True: #We add this part incase the user wants to exit while inputting a choice
                print(f"{Style.BRIGHT}{Fore.YELLOW}\nGoodbye!")
                time.sleep(2)
                exit() 
            
            if avogadro_choice != is_digit(avogadro_choice):
                avogadro_choice = int(avogadro_choice)
            if avogadro_choice == 1:
                print(f"\n{Fore.RESET}You have chosen {Fore.LIGHTRED_EX}addition with avogadro's number!{Style.RESET_ALL}")
                first_num_check("+")
                total = float(sum(res)) + Avogadronumber 
                print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Fore.MAGENTA} {all_numbers}{Style.RESET_ALL}{Style.BRIGHT} + {Style.RESET_ALL}{Fore.MAGENTA}{Avogadronumber}{Style.RESET_ALL} = {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
                print(f"\nThe {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
            elif avogadro_choice == 2:
                print(f"\n{Fore.RESET}You have chosen {Fore.LIGHTRED_EX}subtraction with avogadro's number!{Style.RESET_ALL}")
                first_num_check("-")
                total = float(subtract(res)) - Avogadronumber 
            
                print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Fore.MAGENTA}( {all_numbers} ){Style.RESET_ALL}{Style.BRIGHT} - {Style.RESET_ALL}{Fore.MAGENTA}{Avogadronumber}{Style.RESET_ALL} = {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
                print(f"\nThe {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
    
            elif avogadro_choice == 3:
                print(f"\n{Fore.RESET}You have chosen {Fore.LIGHTRED_EX}multiplication with avogadro's number!{Style.RESET_ALL}")
                first_num_check("*")
                total = float(multiply(res)) * Avogadronumber
                print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Fore.MAGENTA} {all_numbers}{Style.RESET_ALL}{Style.BRIGHT} * {Style.RESET_ALL}{Fore.MAGENTA}{Avogadronumber}{Style.RESET_ALL} = {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
                print(f"\nThe {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
    
                    
            elif avogadro_choice == 4:
                print(f"\n{Fore.RESET}You have chosen {Fore.LIGHTRED_EX}division with avogadro's number!{Style.RESET_ALL}")
                first_num_check("/")
                total = float(divide(res)) / Avogadronumber
                print(f"\n{Fore.RESET}The {Fore.LIGHTGREEN_EX}calculation{Style.RESET_ALL} is {Fore.MAGENTA} {all_numbers}{Style.RESET_ALL}{Style.BRIGHT} / {Style.RESET_ALL}{Fore.MAGENTA}{Avogadronumber}{Style.RESET_ALL} = {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")
                print(f"\nThe {Fore.LIGHTGREEN_EX}total{Style.RESET_ALL} is {Fore.RED}{total}{Style.RESET_ALL}{Style.BRIGHT}.")                
            else:
                print(f"\n\n{Fore.RED}{no_choice}{Style.BRIGHT}") # Incase the user inputs a number other than 4.
        else:
            print(f"\n\n{Fore.RED}{no_choice}{Style.BRIGHT}") # Incase he doesn't even choose an option

        Repeat = input(f"\n\n{Fore.CYAN}Do you wish to restart the program?{Style.RESET_ALL}   {Fore.LIGHTBLUE_EX}").lower()
        if Repeat in yeslist:
            os.system("cls")
            main()
        else:
            exit()
            #Where the code starts
main() #final product all inside the "main" function.
