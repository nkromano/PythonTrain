import string
def checkio(text):

#    text = text.lower()
#    return max(string.ascii_lowercase, key=text.count)
	
    #replace this for solution
    countW = 0
    UnicWord = set(text.lower())
    MaxWord = 'z'
    for i in UnicWord:
      c = text.lower().count(i)
      if i.isalpha():
        if countW < c:
          countW = c
          MaxWord = i
        if countW == c and i < MaxWord:
          countW = c
          MaxWord = i
  print('Max count word in: ', MaxWord)

text = input('Input text: ')
checkio(text)

