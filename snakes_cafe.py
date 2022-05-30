import sys

print(
    """ **************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
    """   )

print("""Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears""")




print("""******************************""")






list=[]
while True:
     user_input=input("** What would you like to order? **"+"\n"+("""******************************""")+"\n")


     list.append(user_input)
     #print(list)

     output= str(list.count(user_input) )+ " order of " + user_input + " have been added to your meal "



     if user_input == "quit":
              break
     print(output)





