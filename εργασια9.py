while True:
       try:
              number=input("Please type an integer ")
              number=int(number)
              break
       except:
              print ("Error. Try again.")

while number>9:
       print ("Now", number, "is tripled:", number*3, "and is increased by 1: ", 3*number+1)      
       number=number*3+1
       number=str(number)
       sum=0
       for x in number:
              y=int(x)
              sum=sum+y
       print ("The sum of its digits is", sum )
       if sum>9:
              print ("The sum has more than one digit so let's repeat the process")
       else:
              print ("The sum has a single digit so the process is terminated")
       number=sum
