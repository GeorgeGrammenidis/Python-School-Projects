import random
def Max (l1,l2,l3):
       if (l1>l2) and (l1>l3):
              return "Light1"
       elif (l2>l1) and (l2>l3):
              return "Light2"
       elif (l3>l2) and (l3>l1):
              return "Light3"
       elif (l3==l2) and (l3>l1):
              x=random.randrange(2,3)
              if x==2:
                     return "Light2"
              else:
                     return "Light3"
       elif (l2==l1) and (l1>l3):
              x=random.randrange (1,2)
              if x==1:
                     return "Light1"
              else:
                     return "Light2"
       elif (l1==l3) and (l1>l2):
              x=random.randrange(1,2)
              if x==2:
                     return "Light3"
              else:
                     return "Light1"              

              
print ("This program simulates 3 smart traffic lights, where the light with the most cars is the only green one")
l1=random.randrange(0,50)
l2=random.randrange(0,50)
l3=random.randrange(0,50)
print ("Light 1 starts with: ", l1 , "cars, Light 2 starts with: ", l2 , "cars, Light 3 starts with: ", l3, " cars")
green=Max(l1,l2,l3)
loss=random.randrange(5,10)
add1=random.randrange(0,5)
add2=random.randrange(0,5)
if green=="Light1":
       l1=l1-loss
       l2=l2+add1
       l3=l3+add2
elif green=="Light2":
       l2=l2-loss
       l1=l1+add1
       l3=l3+add2
elif green=="Light3":
       l3=l3-loss
       l1=l1+add1
       l2=l2+add2
print (green, " is the only green one, so it losses " , loss, "cars, while the others gain ", add1, " and ", add2, " respectively")
print ("Amount of cars: Light 1: ", l1," Light 2: ",l2," Light 3: ", l3)        
key=input ("To terminate the loop type END or type anything  else to continue ")
while key!="END":
       green=Max(l1,l2,l3)
       loss=random.randrange(5,10)
       add1=random.randrange(0,5)
       add2=random.randrange(0,5)
       if green=="Light1":
              l1=l1-loss
              l2=l2+add1
              l3=l3+add2
       elif green=="Light2":
              l2=l2-loss
              l1=l1+add1
              l3=l3+add2
       elif green=="Light3":
              l3=l3-loss
              l1=l1+add1
              l2=l2+add2
       print (green, " has the most cars, so it losses " , loss, "cars, while the others gain ", add1, " and ", add2, " respectively")      
       print ("Amount of cars: Light 1: ", l1," Light 2: ",l2," Light 3: ", l3)        
       key=input ("To terminate the loop type END or type anything  else to continue ")
