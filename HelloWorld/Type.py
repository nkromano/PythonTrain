import math
import random
print (math.pi)
print(math.sqrt(2))
print(random.random())
print(random.choice([1,2,3,4]))

S = 'Spam'
print(S.find('p'))
print(S.replace( 'p' , 'Z' ))

line = ' aaa, bbb,ccc,zzz '
line = line.rstrip()
print(line)
print(line.split(','))
print(S.upper())
print(S.isalpha())


print('%s, eggs and %s' % ('spam', 'SPAM'))
print('{0}, eggs and {1}'.format('spam', 'SPAM'))

M = [[1,2,3],[4,5,6],[7,8,9]]
print(M)
col2=[row[1] for row in M]
print(col2)

col3=[row[1] for row in M if row[1] % 2 ==0]
print(col3)