def ArmN(x):#function for armstrong number
 sum=0
 t=x
 while(t>0):#condition statement
  d=t%10    #extarct last digit
  sum+=d**3 #adds the cube
  t=t//10   #removes remaining digits aside
 if sum==x: #checks sum with initial numbers
  return'Armstrong Number'#prints if condition is true
 else:
  return'Not Armstrong Numbr'#prints if condition is false
x=int(input())#accept number from user
print(ArmN(x))#prints statement

