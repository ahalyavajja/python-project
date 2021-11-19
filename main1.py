'''from * import math
n=int(input())
r=math.sqrt(n)
if(r**2 == n):
	print("It is perfect square")
else:
	print("It is not a perfect square")'''
n=int(input())
for i in range(1,1+n//2): #(1,2)
 if (n==i*i):
   print('perfect square')
   break
else:
 print('not a perfect square')