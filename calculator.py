# write your code here

running_total = 0
nums = 0

while True:
    text_in = input().split()

    if len(text_in) == 0:
        pass

    elif len(text_in) == 1:
        if text_in[0] == "/exit":
            print("Bye!")
            break

        elif text_in[0] == "/help":
            print("The program calculates the output of an expression")

        elif text_in[0][0] == "/":
            print("Unknown command")

        elif text_in[0][0] != "/":
            try:
                running_total += int(text_in[0])

            except ValueError:
                print("Invalid expression1")

            else:
                print(running_total)

    elif len(text_in) > 1 and len(text_in) % 2 == 0:
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
