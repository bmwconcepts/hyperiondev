#╠══Calculator With Advanced Error Handling══╣
#└──Allows user to enter numbers and operators and performs calculations with try, except handling

#├──Import Modules──┤
import operator

#├──Calculator Function──┤
#└──Used with user inputs to do actual operations
def calculation():
    valid_operators = ["+", "-", "*", "/"]
    #└──Set operators that are allowed
    while True:
        try:
            a = int(input("Enter a number: "))
            if type(a) == int:
                break
        except ValueError:
            print("ERROR: Please enter an integer.")
            continue
        #└──Get first integer, error check for non integers
    while True:
        try:
            b = int(input("Enter a second number: "))
            if type(b) == int:
                break
        except ValueError:
            print("ERROR: Please enter an integer.")
            continue
        #└──Get second integer, error check for non integers
    while True:
        try:
            o = str(input("Enter an operator (+, -, *, /): "))
            if b == 0 and o == "/":
                print("ERROR: Cannot divide by zero.")
                #└──Check that second number is not zero before allowing divide
                continue
            elif o in valid_operators:
                break
            elif o not in valid_operators:
                print("Invalid operator.")
        except ValueError:
            print("ERROR: Please enter a string type operator.")
            continue
        #└──Get operator, error check to confirm type is string and in valid operators
    if o == "+":
        answer = operator.add(a, b)
    elif o == "-":
        answer = operator.sub(a, b)
    elif o == "/":
        answer = operator.truediv(a, b)
    elif o == "*":
        answer = operator.mul(a, b)
    #└──Perform operation and store answer in variable
    with open("answers.txt", "a") as answer_file:
        answer_file.write(f"{a} {o} {b} = {answer}\n")
        #└──Write the full equation to an external file
    return answer
    #└──Provide the answer for quick terminal print confirmation

#├──File Opener Function──┤
#└──Option that allows user to open and read from a file if it exists
def file_opener():
    while True:
        try:
            filename = str(input("Please enter filename: "))
        except ValueError:
            print("ERROR: Please enter a *string* filename\n")
            continue
        #└──Get's a file name input and checks type is string
        try:
            file = open(f"{filename}.txt", "r")
            print("╠══Answers File══╣\n")
            for line in file.readlines():
                print(line)
            print("╠════════════════╣\n")
            break
            #└──Opens file, reads and prints lines to terminal
        except:
            print("ERROR: File not found\n")
            #└──Error catch if file doesn't exist
            break

#├──Main Menu──┤
#└──Loops over menu options until exited and performs functions when number is chosen
while True:
    try:
        print("╠══Calculator Main Menu══╣")
        menu = int(input("""0 - exit the program
1 - begin a new operation
2 - open file
Your selection: """))
        if menu == 0:
            print("Goodbye!")
            exit()
            #└──Exit program code
        elif menu == 1:
            print("╠══Calculatron 9000══╣")
            print(f"Your answer is {calculation()}")
            print("├──Answer File Updated──┤\n")
            #└──Runs calculator function
        elif menu == 2:
            file_opener()
        else:
            print("Menu option out of range, please choose again.\n")
            #└──If entry is integer, but not valid option
    except ValueError:
        print("ERROR: Please enter an integer.\n")
        #└──If entry is not an integer