"""
This is simple code for my class
Noah Suplee 2021
"""


def only_ints(*args, log=False):
  '''
  Recursively logs if the arguments are integers if not found returns false
  '''
  nonIntCount = 0

  for arg in args:

    if type(arg) is int:
      pass

    elif type(arg) is str:
      nonIntCount+=1
      
    elif hasattr(arg, '__iter__'):
      if not only_ints(arg):
        nonIntCount+=1

    else:
      nonIntCount+=1
  
  if log:
    log_statements = {
      nonIntCount == 0 : "all variables are integers",
      nonIntCount > 0 : "one or more are not integers",
      nonIntCount == len(args) : "they are all not integers" 
    }

    print(log_statements[True])

  return nonIntCount == 0

def __test_only_ints():
  '''
  tests the only_ints function
  '''

  for arg_a in ['a', 6]:
    for arg_b in ['b', 5]:
      print(f'({arg_a}, {arg_b}) : ', end='')
      only_ints(arg_a, arg_b, log=True)

def main():
  __test_only_ints()


if __name__ == '__main__':
  main()
