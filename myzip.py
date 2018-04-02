def myzip1(*seqs):
  seqs = [list(S) for S in seqs]
  res = []
  while all(seqs):
    res.append(tuple(S.pop(0) for S in seqs))
  return res
#    yield tuple(S.pop(0) for S in seqs)

def mymapPad(*seqs, pad=None):
  seqs = [list(S) for S in seqs]
  res = []
  while any(seqs):
    res.append(tuple(S.pop(0) if S else pan) for S in seqs)
  return res
#    yield tuple(S.pop(0) if S else pan) for S in seqs

def myzip2(*args):
#  print(next(iter(args[0])))
  iters = list(map(iter,args))
  while iters:
    res = [next(i) for i in iters]
    yield tuple(res)

	
S1, S2 = 'abc', 'xyz123'
print(next(myzip2(S1,S2)))
#print(myzip(S1,S2))
#print(mymapPad(S1,S2))
#print(mymapPad(S1,S2,pad=99))