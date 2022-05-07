num = int(input("n:"))
new_num = num + 1

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("factorial does not exist")
elif num == 0:
   print("factorial of 0 is 1")
else:
   for i in range(1, new_num):
       factorial = factorial*i
   print("The factorial of" , num , "is" , factorial)