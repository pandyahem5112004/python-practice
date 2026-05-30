num1 = float(input("Enter first number: "))
operator  = input("Enter operators like +,-,*,/8: ")
num2 = float(input("Enter first number: "))

if operator == "+":
  print("Result : ", num1 + num2)
elif operator == "-" :
    print("Result : ", num1 - num2)
elif operator == "*":
  print("Result : ", num1 + num2)
elif operator == "/" :
    if num2 != 0 :
        print("Result : ", num1 / num2)
    else:
       print("Cannot divide by zero ")
else:
   print("Invalid operator")
