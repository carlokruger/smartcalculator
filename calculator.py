# write your code here
import collections

running_total = 0
nums = 0
variables = {}
equal_count = 0
text_in = []

op_stack = collections.deque()
post_stack = collections.deque()
calc_stack = collections.deque()
mem_stack = collections.deque()


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
        for idx1, item in enumerate(text):
            text[idx1] = item.replace("=", "")
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

    elif len(text_in) == 3 and text_in[1] == "=":  # deal with assignment

        if not text_in[0].isalpha():  # well formed variable assignment
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

    elif len(text_in) > 3 and text_in.count("=") > 1:  # catch special case of multi equals
        print("Invalid assignment")

    elif len(text_in) >= 3:

        for el in text_in:  # separate into expressions and operations
            if el.lstrip("-+").isdigit():
                post_stack.append(int(el))

            elif el.isalpha() and el in variables:
                post_stack.append(variables[el])

            elif el.isalpha() and el not in variables:
                print("Unknown variable")

            elif el in "-+":
                if len(op_stack) == 0:
                    op_stack.append(el)
                    print("opstack1", op_stack)

                elif len(op_stack) > 0:
                    post_stack.append(op_stack.pop())
                    op_stack.append(el)
                    print("opstack2", op_stack)

            elif el in "*/":
                if len(op_stack) == 0:
                    op_stack.append(el)

                elif len(op_stack) > 0:
                    if op_stack[0] in "+-":
                        op_stack.append(el)

                    elif op_stack[0] in "*/":
                        post_stack.append(op_stack.pop())
                        op_stack.append(el)

            elif el == "(":
                    op_stack.append(el)

            elif el == ")":
                for j in range(len(op_stack)):
                    if op_stack[j] != "(":
                        post_stack.append((op_stack.pop()))
                    elif op_stack[j] == "(":
                        op_stack.pop()

        for _i in range(len(op_stack)):
            post_stack.append(op_stack.pop())
        print("postfix0", post_stack)
        print("opstack0", op_stack)

# calculate using the postfix queue
        for r in post_stack:
            if str(r).lstrip("-+").isdigit():
                calc_stack.append(r)
                print("calc1", calc_stack)

            elif r in "+-/*":
                if r == "+":
                    calc_stack.append(calc_stack.pop() + calc_stack.pop())
                    print("calcstack+", calc_stack)

                elif r == "-":
                    calc_stack.append(calc_stack.pop() - calc_stack.pop())
                    print("calcstack-", calc_stack)

                elif r == "*":
                    calc_stack.append(calc_stack.pop() * calc_stack.pop())
                    print("calcstack*", calc_stack)

                elif r == "/":
                    calc_stack.append(calc_stack.pop() / calc_stack.pop())
                    print("calcstack/", calc_stack)



        # calc_stack.append(op_stack.pop())
        print("result", calc_stack[0])

