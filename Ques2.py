#2. Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line.
for j in range(5,11):
 fact=1
 for i in range(1,j+1):
  fact=fact*i
 print(fact,end=",")