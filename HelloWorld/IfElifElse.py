TextInput = input()
Output = 'true' if TextInput else 'false'
print(Output)

if TextInput == 'aaa':
  print(TextInput)
elif TextInput:
  print('true')
else:
  print('false')
