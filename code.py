_name = input("Enter your full name: ")
_year = input("Enter the year you were born: ")
import keyword
keywords=keyword.kwlist
def change_name(full_name, birth_year):
  name=full_name.split()
  name_1=name[1]
  name_2=name_1[0]
  name_3=name[0]
  name_4=name[2]
  hi=name_3+ " " + name_2 + ". " + name_4
  print(hi+ ": " + "living large since "+ _year)
  length=len(name_3)
  length_1=len(name_4)
  length_2=len(name_1)
  total_length=length +length_1 + length_2
  print ("Your full name contains "+ str(total_length) + " characters -excluding spaces.")

  
 


change_name(_name, _year)
