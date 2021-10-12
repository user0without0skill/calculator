def math():
   
   """Regular calculator, that do simple math operation .
   This function don't use argument and return result.
   """

   

   x = input("Put the first number: ")

   y = input("Put the second number: ")

   oper = input("What we do with number?: ")

   if oper == '+':
     return float(x) + float(y)
     

   elif oper == '-':
     c = float(x) - float(y)
     print(str(c))

   elif oper == '*':
     c = float(x) * float(y)
     print(str(c))

   elif oper == '**':
     c = float(x) ** float(y)
     print(str(c))


   elif oper == '/':
     c = float(x) / float(y)
     print(str(c))

   elif oper == '//':
     c = float(x) // float(y)
     print(str(c))

   elif oper == '%':
     c = float(x) % float(y)
     print(str(c))
   
   elif oper == '/' and x == 0 and y == 0:
    print("Function can't divide 0 to 0")

   else:
      print("Error, something go wrong ")
   
print(math.__doc__)   
print(math())
