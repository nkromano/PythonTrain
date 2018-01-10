import re
#def checkio(password):
#  return(re.match('[0-9]'))
    
#  return x

checkio = lambda p: len(p) >= 10 and bool(re.search('[0-9]',p)) and bool(re.search('[a-z]',p)) and bool(re.search('[A-Z]',p)) and bool(re.search('![0-9,a-z,A-Z]',p)) == False

print(checkio('A1213pokl'))# == False
print(checkio('bAse730onE'))# == True
print(checkio('asasasasasasasaas'))# == False
print(checkio('QWERTYqwerty'))# == False
print(checkio('123456123456'))# == False
print(checkio('QwErTy911poqqqq'))# == True

