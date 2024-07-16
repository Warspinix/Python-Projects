# Birthday Paradox


'''

In probability theory, the birthday problem asks for the probability that,
in a set of 'n' randomly chosen people, at least two will share a birthday.

The birthday paradox is that, counterintuitively,
the probability of a shared birthday exceeds 50% in a group of only 23 people.

'''

import random

l = []  # list of birthdays

for i in range(23):  # 23 randomly chosen people
    l.append(random.randint(1, 365))  # birthdays (only DD and MM, not Year)

# If the number is 1, it's January 1
# If the number is 365, it's December 31

length = len(l)
l.sort()
print(l)

i = 0
j = 1
check = 0

while i < length - 1:  # length = 23, so i < 22, i.e. i will go from 0 to 21
    # i can't be 22, because then we can't do i+1 (l[23] doesn't exist)
    if l[i] == l[i + 1]:  # Comparing ith element and (i+1)th element
        print(f"Repetition {j}: {l[i]}, {l[i + 1]}")
        j += 1
        check = 1
    i += 1
if check == 0:
    print('No repetitions identified.')

'''
While this gives us an idea of the paradox and the repetitions,
we still don't know whether the probability is greater than 0.5.

And for that, we have to do a Monte Carlo simulation.
'''
