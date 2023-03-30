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
    pass
def rps():
    pass
def mario_wins():
    pass

print("Which function would you like to run?")
print("0. Modulo Calculator")
print("1. Integer Division Calculator")
print("2. Float & Integer Calculator")
print("3. For Loop Counter")
print("4. Print ASCII values of letters in a string")
print("5. Change Machine")
print("6. Rock Paper Scissors")
print("7. Mario wins a level")

fun_selec = int(input("Enter the number of a function: "))

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