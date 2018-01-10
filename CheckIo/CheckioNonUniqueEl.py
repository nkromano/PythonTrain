#def checkio(mass):
#  result = []
#  for i in mass:
#    if mass.count(i) != 1:
#      result.append(i)
#  return result


checkio = lambda d:[x for x in d if d.count(x)>1]

print(checkio([1, 2, 3, 1, 3]))# == [1, 3, 1, 3]
print(checkio([1, 2, 3, 4, 5]))# == []
print(checkio([5, 5, 5, 5, 5]))# == [5, 5, 5, 5, 5]
print(checkio([10, 9, 10, 10, 9, 8]))# == [10, 9, 10, 10, 9]

