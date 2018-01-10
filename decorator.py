def logger(func):
  def wrapped(*args, **kwargs):
    result = func(*args, **kwargs)
    with open('log.txt', 'w') as f:
      f.write(str(result))
    return result
  return wrapped
  
@logger
def summator(num_list):
  return(sum(num_list))
  
print(summator(range(5)))