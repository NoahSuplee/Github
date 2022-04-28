"""
This is simple code for my class
Noah Suplee 2021
"""

def only_ints(x,y):
  '''
  Logs if arguments are ints
  '''
  if isinstance(x, int) == True and isinstance(y, int) == True:
    print ("Both variables are integers")

  elif isinstance(x, int) == True and isinstance(y, int) == False:
    print("The first varible is an integers and the second on isn't")

  elif isinstance(x, int) == False and isinstance(y, int) == True:
    print("The first varible isn't an integers and the second on is an integer ")

  else:
    print("They are both not varible")

def main():
  only_ints(5,6)
  only_ints("a",6)
  only_ints(5, "a")
  only_ints("a","b")

if __name__ == '__main__':
  main()
