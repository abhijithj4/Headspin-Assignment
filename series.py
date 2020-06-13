def fun(num):
     res = 0
     fact = 1
     for i in range(1, num+1):
         fact *= i
         res = res + (i/ fact)
     return res

n=int(input("Enter the value for n "))
print(fun(n))