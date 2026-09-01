def fact(n):
    if n==0 or n==1:
       return 1
    else:  return n*fact(n-1)
n=int(input("Enter the number: "))
c=fact(n)
print("The Factorial of" , n , "is :" , c)