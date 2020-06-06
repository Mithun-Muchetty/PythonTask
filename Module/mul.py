#3 - multiplication 

def mul():
 num1 = int(input("enter first number : "))
 num2 = int(input("enter second number : "))
 a=input("Press the for arithemetic operation 1, 2, 3, 4 : ")
 if(a == '3'):
   result = num1 * num2
   print(result)
 else:
  print("Invalid operation")

mul()