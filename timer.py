import time
reps = 5
repslist = range(reps)

def timer(func, *pargs, **kargs):
  start = time.clock()
  for i in repslist:
    ret = func(*pargs, **kargs)
  elapsed = time.clock() - start
  return (elased, ret)