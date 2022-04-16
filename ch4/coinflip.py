'''Note about this script:
    I was wracking my brain all day trying to figure
    out why I wasn't getting the correct percentage.
    My first attempt is similar to the one below except I was multiplying
    100 * 10000 which was incorrect.  There are really only 95 total possible
    streaks in the way that I programmed it below, i.e. once it gets to coin 96
    there aren't enough coins left to satisfy a streak of 6.  This was only
    skewing the result slightly but I still wasn't satified.  I kept getting a
    little bit over 3% each time, but everything I looked at told me the
    probability of flipping heads 6 times in a row (6 of 6) was about 1.5%.  I
    couldn't figure out why I was getting around 3% until I realized I'm
    testing for heads and tails.  So, 3% is the correct probability of flipping
    either heads or tails 6 out of 6 times.

    In reality, I did this problem all wrong.  Apparently from what I read on
    the internet, the question is really asking how many often in a series of
    100 flips will either heads or tails be flipped 6 times in a row.  So if a
    streak of 6 happens once in the set of 100 flips, that would count as a
    single streak and you would move on to the next set of 100 flips giving a
    probability of about 80%.  That would be a bit more simple to code.
    '''

import random

numStreaks = 0
STREAK = 6

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.

    coinflip = []

    for flip in range(100):
        coinflip.append(random.randint(0,1))

    # Code that checks if there is a streak of 6 heads or tails in a row

    for flip,coin in enumerate(coinflip[:len(coinflip)-STREAK+1]):
        flag = True
        for streak in range(1,STREAK):
            if coin != coinflip[flip+streak]:
                flag = False
                break

        if flag:
            numStreaks += 1

print('Chance of streak: %.2f%%' % ((numStreaks/(95*10000))*100))
