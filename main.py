
def only_ints(x,y):
  if isinstance(x, int) == True and isinstance(y, int) == True:
    print ("Both variables are integers")
    # The function will print the two input values
    
  elif isinstance(x, int) == True and isinstance(y, int) == False:
    print("The first varible is an integers and the second on isn't")
    # This part of the function compares the integer input from the orginal statement 
    
  elif isinstance(x, int) == False and isinstance(y, int) == True:
    print("The first varible isn't an integers and the second on is an integer ")
    
  else:
    print("They are both not varible")
    # if the function gets input that is considered an integer the statement would be true
only_ints(5,6)
only_ints("a",6)
only_ints(5, "a")
only_ints("a","b")
