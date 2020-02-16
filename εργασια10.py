import random
values=[ '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , 'J' , 'Q' , 'K' , 'A']
figures=[ 'S' , 'H' , 'D', 'C']
p1=[["",""] , ["",""] , ["",""] , ["",""] , ["",""] ]
p2=[["",""] , ["",""] , ["",""] , ["",""] , ["",""] ]
p3=[["",""] , ["",""] , ["",""] , ["",""] , ["",""] ]

def settleties (a,b):
       for i in range (5):
              if (a[i][0]=="K") or (a[i][0]=="J") or (a[i][0]=="Q"):
                     value=10
              elif (a[i][0]=="A"):
                     value=11
              else:
                     value=int(a[i][0])
       amax=value
       for i in range (5):
              if (b[i][0]=="K") or (b[i][0]=="J") or (b[i][0]=="Q"):
                     value=10
              elif (b[i][0]=="A"):
                     value=11
              else:
                     value=int(b[i][0])
       bmax=value
       if amax>bmax:
              return "lower"
       elif bmax>amax:
              return "higher"
       else:
              return "tie"
                     
def deal ():
       global p1,p2,p3
       for x in range (5):
              v=random.randrange(0,12)
              f=random.randrange(0,3)
              p1[x][0]=values[v]
              p1[x][1]=figures[f]
       for x in range (5):
              v=random.randrange(0,12)
              f=random.randrange(0,3)
              p2[x][0]=values[v]
              p2[x][1]=figures[f]
       for x in range (5):
              v=random.randrange(0,12)
              f=random.randrange(0,3)
              p3[x][0]=values[v]
              p3[x][1]=figures[f]
              
def checkflush(p):
       test=p[0][1]
       if (p[1][1]==test) and (p[2][1]==test) and (p[3][1]==test) and (p[4][1]==test):
              return True
       else:
              return False


def checkstraightflush (p):
       combinations=["A2345", "23456", "34567", "45678", "56789","678910","78910J","8910JQ","910JQK","10JQKA"]
       combination=""
       for i in range (5):
              combination=combination+p[i][0]
       test=p[0][1]
       if (p[1][1]==test) and (p[2][1]==test) and (p[3][1]==test) and (p[4][1]==test):
              if combination in combinations:
                     return True
              else:
                     return False
       else:
              return False

def checkfourofakind (p):
       for i in range (0,5):
              counter=0
              for j in range (0,5):
                     if (p[i][0]==p[j][0]) and (i!=j):
                            counter=counter+1
              if counter==3:
                     return True
       return False

def checkthreeofakind (p):
       for i in range (0,5):
              counter=0
              for j in range (0,5):
                     if (p[i][0]==p[j][0]) and (i!=j):
                            counter=counter+1
              if counter==2:
                     return True
       return False

def checktwoofakind (p):
       for i in range (0,5):
              counter=0
              for j in range (0,5):
                     if (p[i][0]==p[j][0]) and (i!=j):
                            counter=counter+1
              if counter==1:
                     return True
       return False


def checktwopairs (p):
       pairs=0
       key=0
       for i in range (5):
              counter=0
              for j in range (5):
                     if (p[i][0]==p[j][0]) and (i!=j):
                            counter=counter+1
                            key=i
              if counter==1:
                     pairs=pairs+1
                     break
       for i in range (5):
              counter=0
              for j in range (5):
                     if (p[i][0]==p[j][0]) and (i!=j) and (p[j][0]!=p[key][0]):
                            counter=counter+1
                            
              if counter==1:
                     pairs=pairs+1
                     break
       if pairs==2:
              return True
       else:
              return False
                     
                     
                     

def checkstraight (p):
       combinations=["A2345", "23456", "34567", "45678", "56789","678910","78910J","8910JQ","910JQK","10JQKA"]
       combination=""
       for i in range (5):
              combination=combination+p[i][0]
       if combination in combinations:
              return True
       else:
              return False


def checkfullhouse(p):
       k1=p[0][0]
       i=1
       while True:
              if k1==p[i][0]:
                     i=i+1
                     continue
              else:
                     k2=p[i][0]
                     key=i
                     break     
       c1=0
       c2=0
       for i in range (1,5):
              if p[i][0]==k1:
                     c1=c1+1
              elif (p[i][0]==k2) and (i!=key):
                     c2=c2+1
       if ( (c1==1) and (c2==2) ) or ( (c1==2) and (c2==1)):
              return True
       else:
              return False
              


deal()
print ("Player 1 has: ", p1)
print ("Player 2 has: ", p2)
print ("Player 3 has: ", p3)
players = [p1 , p2, p3]
values= [0,0,0]
for i in range (3):
       if checkstraightflush(players[i]):
              print ("Player ", i+1 , " has a straight flush")
              values[i]=8
       elif checkfourofakind(players[i]):
              print ("Player ", i+1 , " has four of a kind ")
              values[i]=7
       elif checkfullhouse(players[i]):
              print ("Player ", i+1 , " has a full house")
              values[i]=6
       elif checkflush(players[i]):
              print ("Player ", i+1 , " has a plain flush")
              values[i]=5
       elif checkstraight(players[i]):
              print ("Player ", i+1 , " has a straight")
              values[i]=4
       elif checkthreeofakind(players[i]):
              print ("Player ", i+1 , " has three of a kind")
              values[i]=3
       elif checktwopairs(players[i]):
              print ("Player ", i+1 , " has two pairs")
              values[i]=2
       elif checktwoofakind(players[i]):
              print ("Player ", i+1 , " has a pair")
              values[i]=1
       else:
              print ("No valid combinations for player ", i+1)
if (values[0]>values[1]) and (values[0]>values[2]):
       print ("Player 1 wins")
elif (values[1]>values[0]) and (values[1]>values[2]):
       print ("Player 2 wins")
elif (values[2]>values[1]) and (values[2]>values[0]):
       print ("Player 3 wins")
elif (values[1]==values[0]) and (values[1]>values[2]):
       if settleties (p1,p2)== "lower":
              print ("Player 1 wins")
       elif settleties(p1,p2)=="higher":
              print ("Player 2 wins")
       else:
              print ("Tie between player 1 and 2")
              
elif (values[1]==values[2]) and (values[1]>values[0]):
       if settleties (p2,p3)== "lower":
              print ("Player 2 wins")
       elif settleties(p2,p3)=="higher":
              print ("Player 3 wins")
       else:
              print ("Tie between player 2 and 3")
elif (values[2]==values[0]) and (values[2]>values[1]):
       if settleties (p1,p3)== "lower":
              print ("Player 1 wins")
       elif settleties(p1,p2)=="higher":
              print ("Player 3 wins")
       else:
              print ("Tie between player 1 and 3")

       



       

                     
                                          
                           
                                   
                     
       
                     
                     
                     
                     
                     
              

       


       
       
       
