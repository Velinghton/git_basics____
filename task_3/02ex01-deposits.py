#!/usr/bin/env python3

"""Calculate deposit percent yield based on time period.

Imagine your friend wants to put money on a deposit.
He has got many offers from different banks:
- First bank declares +A% each day;
- Second bank promises +B% each month;
- Third bank offers +C% by the end of the year;
- The 4th bank promotes +D% in a 10-year term;
- ... and so on ...

Your friend gets a terrible headache calculating all this stuff,
and asks you to help checking everything. You quickly realize
it is a common task and having a simple script is a great idea.

Let's implement this.

A simplified task:
Given the SUM amount of money, and PERCENT yield promised in a
FIXED_PERIOD of time, calculate the TOTAL equivalent of money
in a SET_PERIOD of time.

Math formula:
p = PERCENT / 100
TOTAL = SUM * ((1 + p) ** (SET_PERIOD / FIXED_PERIOD))
"""


# TODO: add lines to calculate yields for some common periods
#       of time (e.g. 1 month, 1 year, 5 years, 10 years)
# TODO: change the script to output the 1-year percent yield
#       as well
# TODO: (extra) Output only percents if the initial SUM is
#       not known at the moment the script is run


USAGE = """USAGE: {script} initial_sum percent fixed_period set_period

\tCalculate deposit yield. See script source for more details.
"""
USAGE = USAGE.strip()

MONTH = 30
YEAR = 365
FIVE_YEAR = 1826
TEN_YEAR = 3652


def deposit(initial_sum, percent, fixed_period, set_period):
    """Calculate deposit yield."""
    
    per = percent / 100
    growth = [(1 + per) ** (set_period / fixed_period),
    	      (1 + per) ** (MONTH / fixed_period),
    	      (1 + per) ** (YEAR / fixed_period),
              (1 + per) ** (FIVE_YEAR / fixed_period),
    	      (1 + per) ** (TEN_YEAR / fixed_period)]
    grow = [initial_sum * g for g in growth] if initial_sum else [100 * g for g in growth]
    year_per = round((growth[2] - 1) * 100, 2)
    return grow, year_per

def main(args):
    """Gets called when run as a script."""
    if len(args) != 4 + 1:

        exit(USAGE.format(script=args[0]))

    args = args[1:]
    initial_sum , percent, fixed_period, set_period= map(float, args)


    result, onlly_per = deposit(initial_sum, percent, fixed_period, set_period)
    periods_of_time = ['Set period', '1 month', '1 year', '5 years', '10 years']

    [(print(f"{periods_of_time[i]} = {result[i]}")) for i in range(len(result))]
    print(f"Only percents = {onlly_per}")
    


if __name__ == '__main__':
    import sys

    main(sys.argv)


