def while_print(i):
    '''Takes an integer argument and prints up to it from 1'''
    start = 1
    while start < i+1:
        print(start)
        start += 1

def for_print(i):
    '''Takes an integer argument and prints up to it from 1'''
    for x in range(1,i+1):
        print(x)

def spam_greet(spam):
    '''Prints 'Hello' if spam is 1
    Prints 'Howdy' if spam is 2
    Prints 'Greetings!' if spam is 3'''    

    if spam == 1:
        print('Hello')
    elif spam == 2:
        print('Howdy')
    elif spam == 3:
        print('Greetings')
    else:
        print('Invalid input')




while_print(5)
for_print(3*2)
spam = 2
spam_greet(spam)

for i in range(1,4):
    spam = i
    spam_greet(spam)


    

    
