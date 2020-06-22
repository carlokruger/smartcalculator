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
        variables.update({text[0]: text[1]})
        print(variables)

while True:
    text_in = input().split()

    if len(text_in) == 0:
        pass

    elif len(text_in) == 1 and text_in[0][0] == "/":  #commands
        if text_in[0] == "/exit":
            print("Bye!")
            break

        elif text_in[0] == "/help":
            print("The program calculates the output of an expression")

        else:
            print("Unknown command")

    elif len(text_in) == 1 and text_in[0][0].isalpha():  # variable return
        return_variable(text_in)

    elif len(text_in) == 1 and text_in[0][0] != "/":  # return single digit
        return_single_digit(text_in)

    elif len(text_in) == 2:  # malformed variable assignment
        for x in text_in:
            if "=" in x:
                equal_count += 1
        if equal_count == 1:
            single_variable_assignment_malformed(text_in)
            equal_count = 0
        else:
            print("Invalid expression2")

    elif len(text_in) == 3 and text_in[1] == "=":  # well formed variable assignment
        try:
            text_in[2] = int(text_in[2])
            variables.update({text_in[0]: text_in[2]})
        except ValueError:
            variables.update({text_in[0]: text_in[2]})

    else:  # number operations
        try:
            for x in range(0, len(text_in), 2):
                nums += int(text_in[x])

        except ValueError:
            print("Invalid expression3")

        else:
            running_total += int(text_in[0])

            for i in range(1, len(text_in), 2):
                if "-" in text_in[i] and len(text_in[i]) % 2 != 0:
                        running_total -= int(text_in[i + 1])
                else:
                    running_total += int(text_in[i + 1])

            print(running_total)

    running_total = 0
