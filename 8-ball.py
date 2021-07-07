import time
import random
print("Hello I'am the Magic 8 ball....")
time.sleep(2)
question=input("Ask me a question:")
list1=[1,2,3,4,5,6,7,8]
answer=random.choice(list1)
if answer==1:
    print("It is certain")
elif answer==2:
    print("Outlook good!")
elif answer==3:
    print("You may rely on it!")
elif answer==4:
    print("Ask again later!")
elif answer==5:
    print("Concentrate and ask again!")
elif answer==6:
    print("reply hazy,try again ")
elif answer==7:
    print("My reply is no")
elif answer==8:
    print("My sources say no") 
    
