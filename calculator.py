# write your code here

running_total = 0
nums = 0
variables = {}
equal_count = 0

def commands(text):
    if text[0] == "/exit":
        print("Bye!")
        break

    elif text[0] == "/help":
        print("The program calculates the output of an expression")

    elif text[0][0] == "/":
        print("Unknown command")

def return_variable(text):
    if not text.isalpha():
        print("Invalid identifier")

    elif text in variables:
        print(variables[text])

    else:
        print("Unknown variable")

def return_single_digit(text):
    try:
        running_total += int(text[0])

    except ValueError:
        print("Invalid identifier")

    else:
        print(running_total)

def variable_assignment(text):
    pass

while True:
    text_in = input().split()

    if len(text_in) == 0:
        pass

    elif len(text_in) == 1 and text_in[0][0] == "/":
        commands(text_in)

    elif len(text_in) == 1 and text_in[0][0].isalpha():
        return_variable(text_in)

    elif len(text_in) == 1 and text_in[0][0] != "/":
        return_single_digit(text_in)

    elif len(text_in) > 1 and len(text_in) % 2 == 0:
        for x in text_in:
            if "=" in x:
                equal_count += 1
        if equal_count == 1:
            variable_assignment(text_in)
        else:
            print("Invalid expression2")

    else:
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
