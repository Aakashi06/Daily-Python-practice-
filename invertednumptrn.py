n = 5 #this will set the number of rows in ptrn
for i in range(n,0, -1): #outer loop for rows
  for j in range(1,i+1):
    print(j, end=" ") 
  print()