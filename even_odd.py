answers = ['y', 'yes', 'n', 'no', '', 'quit', 'exit', 'done']


def leave_check(usr_input):
    if usr_input.lower() in answers[5:8]:
        quit()


while True:
    low = input("Lower limit: ")
    leave_check(low)
    high = input("Higher Limit: ")
    leave_check(high)
    ans_sum = input("Calculate sum of integers?: ")
    leave_check(ans_sum)
    ans_num = input("Count the number of even and odd numbers?: ")
    leave_check(ans_num)
    if (
        low.isnumeric()
        and high.isnumeric()
        and ans_sum.lower() in answers[0:5]
        and ans_num.lower() in answers[0:5]
    ):
        if int(low) >= int(high):
            print("\nInvalid range, please try again.\n")
        else:
            break
    else:
        print("\nInvalid input, please try again.\n")
l, h = (int(low), int(high))
rng = range(l, h+1)


def calc(even_odd):
    found = []
    if even_odd == 'even':
        for n in rng:
            if n != 0:
                if n % 2 == 0:
                    found.append(n)
    elif even_odd == 'odd':
        for n in rng:
            if n != 0:
                if not n % 2 == 0:
                    found.append(n)
    return found


def sum_num(even_odd):
    if ans_sum.lower() in answers[0:2]:
        total = 0
        for n in calc(even_odd):
            total += n
        print("\nThe sum of ", even_odd, " numbers is", total)
    if ans_num.lower() in answers[0:2]:
        print("\nThe number of", even_odd, "numbers is", len(calc(even_odd)))


def main(even_odd):
    print("\n-The", even_odd, "numbers are", calc(even_odd))
    sum_num(even_odd)


main('even')
main('odd')
