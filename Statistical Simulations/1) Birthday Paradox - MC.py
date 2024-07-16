'''

In probability theory, the birthday problem asks for the probability that,
in a set of 'n' randomly chosen people, at least two will share a birthday.

The birthday paradox is that, counterintuitively,
the probability of a shared birthday exceeds 50% in a group of only 23 people.

'''

import random

b_list = []  # list of birthdays

# Two variables to check probability (no. of successes/total no. of attempts)

repetitions = 0  # no. of successes
total = 1  # total no. of attempts

# While loop variable

j = 0

while total <= 40000: # total number of trials
    for i in range(23):  # 23 randomly chosen people
        b_list.append(random.randint(1, 365))  # date of birth; Jan 1 is 1, Dec 31 is 365...
    b_list.sort()  # Sorted to check for repetitions
    while j < len(b_list)-1:
        if b_list[j] == b_list[j+1]:
            repetitions += 1
            break
        j += 1
    total += 1
    j = 0
    b_list = []

print(f"Probability by Monte Carlo Simulation = {(repetitions/total):.5f}")  # must be above 0.5

''' 
REASON FOR USING break in LINE 31

--> We need at most 1 repetition in one batch of 23 people, so once we find that pair, 
we can stop searching in that batch.
--> Hence break is used if a repetition is found.
--> If we don't use break here, then repetition might get incremented by +2 or even +3.
--> That is, if more than one pair share the same date of birth in the 23 people, repetition can get incremented
by 2 or 3 with each iteration of the uppermost while loop.
--> Meanwhile, total only gets incremented by 1 with each iteration of the same while loop.
--> So repetition might become more than total and probability will become a value more than 1, which is WRONG.
--> So, break is EXTREMELY important.
'''
