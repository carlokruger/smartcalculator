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
num_str = ""
strings = ""
plus = []
minus = []


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
    global text_in
    try:
        running_total += int(text[0])

    except ValueError:
        print("Invalid identifier")

    else:
        print(running_total)
        running_total = 0
        text_in = []


def single_variable_assignment_malformed(text):
    if text[0][-1] == "=" or text[1][0] == "=":
        for idx1, item in enumerate(text):
            text[idx1] = item.replace("=", "")
    if text[1] in variables:
        variables.update({text[0]: variables[text[1]]})
    else:
        variables.update({text[0]: text[1]})


while True:
    text_in = []
    text = "".join(input().split())  # concatenate into a single string
    len_text = len(text) - 1
    print("txt", text)

    # parse string into list
    for t in text:
        if len(text) == 0:
            pass

        elif "**" in text or "//" in text:
            print("Invalid expression")
            text = ""
            pass

        # deal with command initialisation
        elif t == "/" and text.index(t) == 0:
            strings += t

        # deal with unary minus
        elif t == "-" and text.index(t) == 0:
            num_str += t

        # deal with last character
        elif text.index(t) == text.index(text[-1]):
            if t == ")":
                if len(num_str) > 0:
                    text_in.append(num_str)
                    text_in.append(t)
                    num_str = ""
                elif len(strings) > 0:
                    text_in.append(strings)
                    text_in.append(t)
                    strings = ""
                else:
                    text_in.append(t)

            # if final alpha
            elif t.isalpha():
                if len(plus) > 0:
                    text_in.append("+")
                    plus = []
                    strings += t
                    text_in.append(strings)
                    strings = ""
                elif len(minus) % 2 == 0 and len(minus) != 0:
                    text_in.append("+")
                    minus = []
                    strings += t
                    text_in.append(strings)
                    strings = ""
                elif len(minus) % 2 != 0:
                    text_in.append("-")
                    minus = []
                    strings += t
                    text_in.append(strings)
                    strings = ""
                elif len(plus) == 0 or len(minus) == 0:
                    strings += t
                    text_in.append(strings)
                    strings = ""

            # if final digit
            elif t.isdigit:
                print("T", t)
                print("+", plus)
                print("-", minus)
                if len(plus) > 0:
                    text_in.append("+")
                    plus = []
                    num_str += t
                    text_in.append(num_str)
                    num_str = ""
                elif len(minus) % 2 == 0 and len(minus) != 0:
                    text_in.append("+")
                    minus = []
                    num_str += t
                    text_in.append(num_str)
                    num_str = ""
                elif len(minus) % 2 != 0:
                    text_in.append("-")
                    minus = []
                    num_str += t
                    text_in.append(num_str)
                    num_str = ""
                elif len(plus) == 0 or len(minus) == 0:
                    num_str += t
                    text_in.append(num_str)
                    num_str = ""

        elif t.isdigit():
            if len(plus) > 0:
                text_in.append("+")
                num_str += t
                plus = []
            elif len(minus) % 2 == 0 and len(minus) != 0:
                text_in.append("+")
                minus = []
                num_str += t
            elif len(minus) % 2 != 0:
                text_in.append("-")
                minus = []
                num_str += t
            elif len(plus) == 0 or len(minus) == 0:
                num_str += t

        elif t.isalpha():
            if len(plus) > 0:
                text_in.append("+")
                plus = []
                strings += t
            elif len(minus) % 2 == 0 and len(minus) != 0:
                text_in.append("+")
                minus = []
                num_str += t
            elif len(minus) % 2 != 0:
                text_in.append("-")
                minus = []
                num_str += t
            elif len(plus) == 0 or len(minus) == 0:
                strings += t

        elif t in "+":
            print("here")
            print("+", plus)
            print("-", minus)
            if len(num_str) > 0:
                text_in.append(num_str)
                num_str = ""
                plus.append(t)
            elif len(strings) > 0:
                text_in.append(strings)
                strings = ""
                plus.append(t)
            elif len(num_str) == 0 or len(strings) == 0:
                plus.append(t)

        elif t in "-":
            if len(num_str) > 0:
                text_in.append(num_str)
                num_str = ""
                minus.append(t)
            elif len(strings) > 0:
                text_in.append(strings)
                strings = ""
                minus.append(t)
            elif len(num_str) == 0 or len(strings) == 0:
                minus.append(t)

        elif t in "/*=)^":
            if len(num_str) > 0:
                text_in.append(num_str)
                num_str = ""
                text_in.append(t)
            elif len(strings) > 0:
                text_in.append(strings)
                strings = ""
                text_in.append(t)
            elif len(num_str) == 0 or len(strings) == 0:
                text_in.append(t)

        elif t in "(":
            text_in.append(t)

    #print("text_in", text_in)


    if len(text_in) == 0:
        pass
    elif text_in.count("(") != text_in.count(")"):
        print("Invalid expression")

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

    # parse into postfix and opstack
    elif len(text_in) >= 3:

        for el in text_in:  # separate into expressions and operations

            if el.lstrip("-+").isdigit():

                post_stack.append(int(el))

            elif el.isalpha() and el in variables:
                post_stack.append(variables[el])

            elif el.isalpha() and el not in variables:
                print("Unknown variable")

            elif el == "(":
                op_stack.append(el)

            elif el == "^":
                while True:
                    if len(op_stack) == 0:
                        op_stack.append(el)
                        break

                    elif op_stack[-1] == "^":
                        post_stack.append(op_stack.pop())

                    elif op_stack[-1] in "/+-*":
                        op_stack.append(el)
                        break

                    elif op_stack[-1] == "(":
                        op_stack.append(el)
                        break

            elif el in "/*":
                while True:
                    if len(op_stack) == 0:
                        op_stack.append(el)
                        break
                    elif op_stack[-1] == "^":
                        post_stack.append(op_stack.pop())

                    elif op_stack[-1] in "*/":
                        post_stack.append(op_stack.pop())

                    elif op_stack[-1] in "+-":
                        op_stack.append(el)
                        break

                    elif op_stack[-1] == "(":
                        op_stack.append(el)
                        break

            elif el in "-+":
                while True:
                    if len(op_stack) == 0:
                        op_stack.append((el))
                        break

                    elif op_stack[-1] in "*/^":
                        post_stack.append(op_stack.pop())

                    elif op_stack[-1] in "+-":
                        post_stack.append(op_stack.pop())

                    elif op_stack[-1] == "(":
                        op_stack.append(el)
                        break

            elif el == ")":
                while True:
                    if len(op_stack) == 0:
                        break
                    if op_stack[-1] in "+-/*^":
                        post_stack.append(op_stack.pop())
                    elif op_stack[-1] == "(":
                        op_stack.pop()
                        break


        while len(op_stack) > 0:
            temp1 = op_stack.pop()
            if temp1 is None:
                break
            elif temp1 in "/-+*^":
                post_stack.append(temp1)
            elif temp1 in "()":
                print("Invalid expression")

        print("postfix0", post_stack)

# calculate using the postfix queue
        for r in post_stack:
            if str(r).lstrip("-+").isdigit():
                calc_stack.append(r)
                #print("calc1", calc_stack)

            elif r in "+-/*^":
                if r == "+":
                    calc_stack.append(calc_stack.pop() + calc_stack.pop())
                    #print("calcstack+", calc_stack)

                elif r == "-":
                    calc_stack.append(-calc_stack.pop() + calc_stack.pop())
                    #print("calcstack-", calc_stack)

                elif r == "*":
                    calc_stack.append(calc_stack.pop() * calc_stack.pop())
                    #print("calcstack*", calc_stack)

                elif r == "/":
                    calc_stack.append(int(1 / (calc_stack.pop() / calc_stack.pop())))
                    #print("calcstack/", calc_stack)

                elif r == "^":
                    termb = calc_stack.pop()
                    terma = calc_stack.pop()
                    calc_stack.append(int((terma ** termb)))
                    #print("calcstack^", calc_stack)


        # return results and clean up
        print(calc_stack[0])
        post_stack = collections.deque()
        calc_stack = collections.deque()


