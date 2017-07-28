InputText = input('Input text please: ')
InputCharacter = input('Input character please: ')

for i in InputText:
    if i == InputCharacter:
        print('Got caught!')
        break
else:
    print('In line haven\'t character')
