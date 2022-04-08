def collatz(number):
    if number % 2:
        number = (3 * number) + 1

    else:
        number = number // 2

    print(number)
    return number

def get_input(count):
    try:
        if count == 1:
            number = int(input('Enter number: \n'))
        else:
            number = int(input())
        return number
    except ValueError:
        print('Please enter a number: ')

count = 0
while True:
    count += 1
    number = get_input(count)
    if number != None:
        break

while number != 1:
    number = collatz(number)
