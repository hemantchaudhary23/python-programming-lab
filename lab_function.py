def ArmN(x):
 sum=0
 t=x
 while(t>0):
  d=t%10
  sum+=d**3
  t=t//10
 if sum==x:
  return'Armstrong Number'
 else:
  return'Not Armstrong Numbr'
x=int(input())
print(ArmN(x))

