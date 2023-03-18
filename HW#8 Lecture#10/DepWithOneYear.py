
#!/usr/bin/env python3


USAGE = """USAGE: {script} initial_sum percent fixed_period set_period

\tCalculate deposit yield. See script source for more details.
"""
USAGE = USAGE.strip()


def deposit(initial_sum, percent, fixed_period, set_period):
    """Calculate deposit yield."""
    per = percent / 100
    one_year = (1 + per)
    growth_five = one_year ** 5
    growth_ten = one_year ** 10
    growth_set = one_year ** (set_period / fixed_period)
    res = f"One month yield: {'%.2f' % (initial_sum * one_year / 12)}\n" \
           f"One year yield: {'%.2f' % (initial_sum * one_year)}\n" \
           f"Five year yield: {'%.2f' % (initial_sum * growth_five)}\n" \
           f"Ten year yield: {'%.2f' % (initial_sum * growth_ten)}\n" \
           f"Set period yield: {'%.2f' % (initial_sum * growth_set)}"
    write_deposit(res)


    return res

def read_deposit():
    initial_sum, percent, fixed_period, set_period = None, None, None, None
    try:
        with open('DepositArgs.txt', 'r', encoding='cp1251') as file:
            lines = file.readlines()

            try:
                initial_sum = float(lines[0].split('=')[1])
                percent = float(lines[1].split('=')[1])
                fixed_period = float(lines[2].split('=')[1])
                set_period = float(lines[3].split('=')[1])
            except:
                print('Something goes wrong, check file data')
            res = deposit(initial_sum, percent, fixed_period, set_period)
            write_deposit(res)
            print(res)
            return res
    except FileNotFoundError:
        print('File is missing')

def write_deposit(res):
    with open('DepositArgs.txt', 'a')as file:
        file.write(f'\n{res}')




def main(args):
    """Gets called when run as a script."""
    if len(args) != 4 + 1:
        exit(USAGE.format(script=args[0]))

    args = args[1:]
    initial_sum, percent, fixed_period, set_period = map(float, args)

    # same as
    # initial_sum = float(args[0])
    # percent = float(args[1])
    # ...

    res = deposit(initial_sum, percent, fixed_period, set_period)
    print(res)

read_deposit()

# if __name__ == '__main__':
#     import sys
#
#     main(sys.argv)

