# write your code here

running_total = 0

def subtract(a, b):
    return int(a) - int(b)


def add(a, b):
    return int(a) + int(b)


while True:
    text_in = input().split()

    if len(text_in) == 1 and text_in[0] == "/exit":
        print("Bye!")
        break

    elif len(text_in) == 1 and text_in[0] == "/help":
        print("The program calculates the sum of numbers")

    elif len(text_in) == 0:
        pass

    else:
        for i in range(len(text_in)):
            if i == 0:
                running_total += int(text_in[i])
            elif "-" in text_in[i]:
                if len(text_in[i]) % 2 != 0:
                    running_total -= int(text_in[i])
            else:
                running_total += int(text_in[i])

        print(running_total)
        running_total = 0
