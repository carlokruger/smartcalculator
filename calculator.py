# write your code here

running_total = 0

while True:
    text_in = input().split()

    if len(text_in) == 0:
        pass

    elif len(text_in) == 1:
        if text_in[0] == "/exit":
            print("Bye!")
            break

        elif text_in[0] == "/help":
            print("The program calculates the sum of numbers")

        elif text_in[0][0] == "/":
            print("Unknown command")

        elif text_in[0][0] in ("+", "-"):
            running_total += int(text_in[0])
            print(running_total)

        elif text_in[0].isdigit():
            running_total += int(text_in[0])
            print(running_total)

        elif not text_in[0].isdigit():
                print("Invalid expression")

    elif len(text_in) > 1 and len(text_in) % 2 == 0:
        print("Invalid expression")

    else:
        running_total += int(text_in[0])

        for i in range(1, len(text_in), 2):
            if "-" in text_in[i] and len(text_in[i]) % 2 != 0:
                    running_total -= int(text_in[i + 1])
            else:
                running_total += int(text_in[i + 1])

    if len(text_in) == 0:
        pass

    elif len(text_in) == 1 and not text_in[0].isdigit():
        pass
    elif len(text_in) == 1 and text_in[0].isdigit():
        pass
    else:
        print(running_total)
    running_total = 0
