a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))

if a >=b and a >=c:
  print('a is the largest number')
elif b>=a and b>=c:
  print("b is the largest number")
elif c>=a and c>=b:
  print("c is the largest number")
elif a==b and b==c:
  print('all the numbers are equal')
else:
  print("invalid input")