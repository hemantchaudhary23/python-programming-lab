from easygui import *
import sys
sum=0
while 1:
   msgbox("Hello, world! welcome to D-Mart")
   msg ="What are the things you seek?"              
   title = "shopping"
   choices = ["shoes", "T-shirts", "Shirts"]
   choice = indexbox(msg, title, choices)
    
   if choice==0:
      msg="which brands you looking for"
      title="Shoes"
      choices=['Converse','Gucci']
      choice=indexbox(msg, title, choices)
      if choice==0:
        sum+=2500
        msgbox(sum,"your total bill is")
      elif choice==1:
        sum+=2000
        msgbox(sum,"your total bill is")
      
   elif choice==1:
      msg="which brands you looking for"
      title="T-shirts"
      choices=['buffelo','Gucci']
      choice=indexbox(msg, title, choices)
      if choice==0:
        sum+=1500
        msgbox(sum,"your total bill is")
      elif choice==1:
        sum+=1000
        msgbox(sum,"your total bill is")
 
   elif choice==2:
      msg="which brands you looking for"
      title="Shirts"
      choices=['crimson club',' Peter England']
      choice=indexbox(msg, title, choices)
      if choice==0:
        sum+=3500
        msgbox(sum,"your total bill is")
      elif choice==1:
        sum+=3000
        msgbox(sum,"your total bill is")
   msg = "Do you want to continue?"
   title = "Please Confirm"
   if ccbox(msg, title):  
        pass 
   else:
        sys.exit(0)  


