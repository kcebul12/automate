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

print('Chance of streak: %s%%' % ((numStreaks/(100*10000))))
                
        
           
  
            
