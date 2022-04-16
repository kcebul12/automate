# easy way using join
def comma1(spam):
    newspam = ', '.join(spam[:len(spam)- 1])
    newspam += ', and ' + spam[-1]
    return newspam

# using loops and concatenation
def comma2(spam):
    newspam = ''

    for item in spam:
        if item == spam[-1]:
            newspam += 'and ' + item
        else:
            newspam += item + ', '
    return newspam
    
spam = ['apples','bananas','tofu','cats']
cheese = ['nice','to','meet','you','hello']

print(comma1(spam))
print(comma1(cheese))

print(comma2(spam))
print(comma2(cheese))



    
