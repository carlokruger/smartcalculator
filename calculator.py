# write your code here

running_total = 0
nums = 0
variables = {}
equal_count = 0
text_in = []


def return_variable(text):
    global variables

    if not text[0].isalpha():
        print("Invalid identifier")

    elif text[0] in variables:
        print(variables[text[0]])

    else:
        print("Unknown variable")


def return_single_digit(text):
    global running_total
    try:
        running_total += int(text[0])

    except ValueError:
        print("Invalid identifier")

    else:
        print(running_total)


def single_variable_assignment_malformed(text):
    if text[0][-1] == "=" or text[1][0] == "=":
        for idx, item in enumerate(text):
            text[idx] = item.replace("=", "")
    if text[1] in variables:
        variables.update({text[0]: variables[text[1]]})
    else:
        variables.update({text[0]: text[1]})


while True:
    text_in = input().split()

    if len(text_in) == 0:
        pass

    elif len(text_in) == 1 and text_in[0][0] == "/":  # deal with commands
        if text_in[0] == "/exit":
            print("Bye!")
            break

        elif text_in[0] == "/help":
            print("The program calculates the output of an expression")

        else:
            print("Unknown command")

    elif len(text_in) == 1:

        if text_in[0].isalpha():  # well formed variable return
            return_variable(text_in)

        elif "=" == text_in[0][1]:  # another malformed variable assignment of form "a=b"
            try:
                y = int(text_in[0][2])
                variables.update({text_in[0][0]: y})
            except ValueError:
                if text_in[0][2] in variables:
                    variables.update({text_in[0][0]: variables[text_in[0][2]]})
                else:
                    if not text_in[0][2].isalpha():
                        print("Invalid identifier")
                    else:
                        print("Unknown variable")

        elif text_in[0].lstrip("-+").isdigit():  # return single digit
            return_single_digit(text_in)
        else:
            print("Invalid identifier")

    elif len(text_in) == 2:  # malformed variable assignment of form "a= b" or "a =b"
        for x in text_in:
            if "=" in x:
                equal_count += 1
        if equal_count == 1:
            single_variable_assignment_malformed(text_in)
            equal_count = 0
        elif equal_count > 1:
            print("Invalid assignment")  # too many equal signs

    elif len(text_in) == 3:
        if text_in[1] == "=":  # well formed variable assignment
            if not text_in[0].isalpha():
                print("Invalid identifier")
            else:
                try:
                    z = int(text_in[2])
                    variables.update({text_in[0]: z})  # assign numerical value

                except ValueError:
                    if text_in[2] in variables:  # if variable already exists set assignment to value
                        variables.update({text_in[0]: variables[text_in[2]]})
                    else:
                        if not text_in[2].isalpha():
                            print("Invalid identifier")
                        else:
                            print("Unknown variable")

        if text_in[1] == "+":  # dealing with simple addition
            if not text_in[0].isalpha() or not text_in[2].isalpha():
                print("Invalid identifier")
            else:
                if text_in[0] in variables:
                    running_total += variables[text_in[0]]
                else:
                    try:
                        a = int(text_in[0])
                        running_total += a
                    except ValueError:
                        print("Unknown variable")

                if text_in[2] in variables:
                    running_total += variables[text_in[2]]
                    print(running_total)

                else:
                    try:
                        a = int(text_in[2])
                        running_total += a
                        print(running_total)
                    except ValueError:
                        print("Unknown variable")

        if text_in[1] == "-":  # dealing with simple subtraction
            if not text_in[0].isalpha() or not text_in[2].isalpha():
                print("Invalid identifier")
            else:
                if text_in[0] in variables:
                    running_total += variables[text_in[0]]
                else:
                    try:
                        a = int(text_in[0])
                        running_total += a
                    except ValueError:
                        print("Unknown variable")

                if text_in[2] in variables:
                    running_total -= variables[text_in[2]]
                    print(running_total)
                else:
                    try:
                        a = int(text_in[2])
                        running_total -= a
                        print(running_total)
                    except ValueError:
                        print("Unknown variable")

    elif len(text_in) > 3 and text_in[1] != "=":
        for var in range(0, len(text_in), 2):  # parse for variables
            if not text_in[var].isalpha() and not text_in[var].lstrip("=+-").isdigit():
                print("Invalid identifier")
            elif text_in[var] not in variables and not text_in[var].lstrip("=+-").isdigit():
                print("Unknown variable")
            try:
                b = int(text_in[var])
                text_in[var] = b  # assign number to variable spot
            except ValueError:
                if text_in[var] in variables:
                    text_in[var] = variables[text_in[var]]  # set spot = value of key variable
                else:
                    print("Invalid identifier")

        for ops in range(1, len(text_in), 2):  # parsing operators
            if "+" in text_in[ops]:
                text_in[ops] = "+"
            elif "-" in text_in[ops] and len(text_in[ops]) % 2 == 0:
                text_in[ops] = "+"
            elif "-" in text_in[ops] and len(text_in[ops]) % 2 == 1:
                text_in[ops] = "-"
            else:
                print("Invalid operator")

        running_total += text_in[0]

        for idx in range(2, len(text_in), 2):
            if text_in[idx - 1] == "+":
                running_total += text_in[idx]

            elif text_in[idx - 1] == "-":
                running_total -= text_in[idx]

            elif text_in[idx - 1] == "=":
                print("Invalid assignment")

        print(running_total)



    '''else:  # number operations
        try:
            for x in range(0, len(text_in), 2):
                nums += int(text_in[x])

        except ValueError:
            print("Invalid expression3")

        else:
            running_total += int(text_in[0])

            for i in range(1, len(text_in), 2):
                if "-" in text_in[i] and len(text_in[i]) % 2 != 0:  # dealing with multiple minus signs
                    running_total -= int(text_in[i + 1])
                else:
                    running_total += int(text_in[i + 1])

            print(running_total)'''

    running_total = 0
