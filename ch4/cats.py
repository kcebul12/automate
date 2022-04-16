def get_cats():
    '''Gets cat name and returns it'''
    cat = input('Enter cat\'s name or hit \'q\' when finished: ')
    
    return cat

cats = []

while True:
    cat = get_cats().capitalize()

    if cat != 'Q':
        if cat in cats:
            answer = input('You already have a cat by that name, are you sure? Y/N')
            if answer.capitalize() == 'N':
                continue
        cats.append(cat)
    else:
        break

for cat in cats:
    print(cat)

for index,cat in enumerate(cats):
    print(f'Cat #{index} is {cat}')

if 'Mike' in cats:
    print(f"Mike is cat # {cats.index('Mike')}")

else:
    print('No Mike here')

cats.sort()

for cat in cats:
    print(cat)

