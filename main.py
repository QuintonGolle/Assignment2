import random


def modulo_calc():
    # Get two variables type specified as int from the user
    x = int(input("What is the first number? "))
    y = int(input("What is the second number? "))
    # create new variable to store result of calculation of first number modulo second number
    result = x % y
    # print off a message telling the user the result of their numbers
    print(x, "modulo", y, "equals", result)
def int_div_calc():
    # Get two variables type specified as int from the user
    x = int(input("What is the first number? "))
    y = int(input("What is the second number? "))
    # create new variable to store result of calculation of first number divided by second number
    result = x / y
    # print off a message telling the user the result of their numbers
    print(x, "divided by", y, "equals", int(result))
def fl_int_calc():
    # Get two variables type specified as float from the user
    x = float(input("What is the first number? "))
    y = float(input("What is the second number? "))
    # create new variable to store result of calculation of first number divided by second number
    result = x / y
    #create another varible to store the result as an int
    int_result = int(result)
    # print off a message telling the user the result of their numbers in float and int form
    print(x, "divided by", y, "equals", result, ". Its value as an integer is", int_result)
def for_loop_count():
    # gets an input of type int and stores it in counter 
    counter = int(input("What should the initial value of the counter be? "))

    #gets an input of type int and stores it in loop_count
    loop_count = int(input("How many times should the loop run? "))

    #gets an input of type int and stores it in increment
    increment = int(input("How much should the counter increment by? "))

    #gets a default input (type string) and stores it in in_or_dec
    in_or_dec = input("Should the counter decrement instead of incrementing? (y/n) ")

    #make the increment negative if the user wants to decrement
    if in_or_dec == "y":
        increment = increment * -1

    #loop the amount of times requested, and add the incement to the initial value each iteration
    for i in range(loop_count):
        counter = counter + increment
    #once the for loop is done, print off the end result of the loop
    else:
        print("The final value of the counter is:", counter)        
def ascii_val():
    #ask user for a word to iterate over
    user_str = input("Enter the word you would like to print the ASCII values for: ")

    #create an iterator variable
    i = 0

    #a for loop to run equal times to the number of chars in user_str, and print off the letter,
    #along with its corresponding ASCII value and index number
    for char in user_str:
        print("Letter:", user_str[i], end='')
        print("  ASCII Value:", ord(user_str[i]), end='')
        print("  Index Number:", i)
        i += 1
def change_mach():
    
    #make two arrays, one to store the cent values and one to store the amount of that coin
    coins = [25, 10, 5]
    coin_counts = [0, 0, 0]

    #Requests a payment from the user and stores that in a float
    payment = float(input("Enter the amount that you are paying with: "))
    
    #creates a new variable to store just the dollar value with no cents
    int_payment = int(payment)
    
    #subtracts the int payment from the float payment to get just the cents from the float
    cents = payment - int_payment
    
    #multiply the cents by 100 to get an int from the cents
    int_cents = cents * 100

    #declare a variable to deal with random floating point numbers (when you are checking if greater than 5 but its actually 4.999999999)
    tolerance = 0.001

    #a for loop to add to each element in the coin_counts array
    for i in range(len(coin_counts)):
        #checks if the number is in the correct range for coin value its checking for, also accounting for tolerance
        if (int_cents >= coins[i]) or (coins[i] - int_cents <= tolerance):
            #divides the number and adds the result to the i element of the coin counts, accounts for tolerance
            coin_counts[i] = (int_cents / coins[i]) + tolerance
            #sets currernt cents to the remainder of the operation
            int_cents = int_cents % coins[i]

    #Tells the user what their change is
    print("Your change is:")
    print("Quarters:", int(coin_counts[0]))
    print("Dimes:", int(coin_counts[1]))
    print("Nickels:", int(coin_counts[2]))
def rps():
    #generates a random number between 0 and 1
    ran_num = random.random()
    #make a variable to store the ai's move as a string
    ai_play = ""

    #sets ai_play to a string the corresponds with the random number, rock paper or scissors
    if ran_num <= 0.33:
        ai_play = "rock"
    elif ran_num > 0.33 and ran_num <= 0.66:
        ai_play = "paper"
    elif ran_num > 0.66:
        ai_play = "scissors"

    #asks the user for a number between 1 and 3, and asks for it again if they put something else in
    while True:
        plr_inp = int(input("Welcome to rock paper scissors, which one do you choose? (1/2/3) "))
        if plr_inp == 1 or plr_inp == 2 or plr_inp == 3:
            break
    
    #make a variable to hold the player move as a string
    plr = ""

    #sets the plr variable to the string version of the player choice, so it can easily be read and printed off
    if plr_inp == 1:
        plr = "rock"
    elif plr_inp == 2:
        plr = "paper"
    elif plr_inp == 3:
        plr = "scissors"

    #checks all the combinations of ai and player choices and tells the player if they win or loose depending on the choices
    if plr == "rock" and ai_play == "scissors" or plr == "paper" and ai_play == "rock" or plr == "scissors" and ai_play == "paper":
        print("The computer chose", ai_play, " YOU WIN!!")
    elif plr == "rock" and ai_play == "paper" or plr == "paper" and ai_play == "scissors" or plr == "scissors" and ai_play == "rock":
        print("The computer chose", ai_play, "You lose :(")
    elif plr == ai_play:
        print("The computer chose", ai_play, "Its a tie! :o")
        

def mario_wins():
    
    #a while loop that will run until the user enters a number from 5 to 15, once that number is entered, the if statement will break the loop
    while True:
        st_num = int(input("How high would you like Mario's stairs to be? (5-15)"))
        if st_num >= 5 and st_num <= 15:
            break 
    
    #runs the number of times the user requested
    for i in range(st_num + 2):
        #checks if the loop is on the right iteration to cut off the top single step
        if i > 1:
            #two loops to print off decrementing spaces, and incrementing hashtags
            for j in range(st_num - i + 1, 0, -1):
                print(end=" ")
            for j in range(i):
                print(end="#")
        #prints the flag on the same level as the top step
        if i == 2:
            print(end="    <|")
        #prints the flag pole on every level except the top level
        elif i > 2:
            print(end="     |")
        #makes a new line
        print("")

#prints off the initial opens when the program is run
print("Which function would you like to run?")
print("0. Modulo Calculator")
print("1. Integer Division Calculator")
print("2. Float & Integer Calculator")
print("3. For Loop Counter")
print("4. Print ASCII values of letters in a string")
print("5. Change Machine")
print("6. Rock Paper Scissors")
print("7. Mario wins a level")

#asks the user to input which function they want to run, stored as an int
fun_selec = int(input("Enter the number of a function: "))

#checks the input number to see which function the number matches up with
if fun_selec == 0:
    modulo_calc()
elif fun_selec == 1:
    int_div_calc()
elif fun_selec == 2:
    fl_int_calc()
elif fun_selec == 3:
    for_loop_count()
elif fun_selec == 4:
    ascii_val()
elif fun_selec == 5:    
    change_mach()
elif fun_selec == 6:
    rps()
elif fun_selec == 7:
    mario_wins()