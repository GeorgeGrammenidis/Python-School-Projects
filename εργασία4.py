def ASCII (x):
       if x=="A":
              return "65"
       elif x=="B":
              return "66"
       elif x=="C":
              return "67"
       elif x=="D":
              return "68"
       elif x=="E":
              return "69"
       elif x=="F":
              return "70"
       elif x=="G":
              return "71"
       elif x=="H":
              return "72"
       elif x=="I":
              return "73"
       elif x=="J":
              return "74"
       elif x=="K":
              return "75"
       elif x=="L":
              return "76"
       elif x=="M":
              return "77"
       elif x=="N":
              return "78"
       elif x=="O":
              return "79"
       elif x=="P":
              return "80"
       elif x=="Q":
              return "81"
       elif x=="R":
              return "82"
       elif x=="S":
              return "83"
       elif x=="T":
              return "84"
       elif x=="U":
              return "85"
       elif x=="V":
              return "86"
       elif x=="W":
              return "87"
       elif x=="X":
              return "88"
       elif x=="Y":
              return "89"
       elif x=="Z":
              return "90"
       elif x=="a":
              return "97"
       elif x=="b":
              return "98"
       elif x=="c":
              return "99"
       elif x=="d":
              return "100"
       elif x=="e":
              return "101"
       elif x=="f":
              return "102"
       elif x=="g":
              return "103"
       elif x=="h":
              return "104"
       elif x=="i":
              return "105"
       elif x=="j":
              return "106"
       elif x=="k":
              return "107"
       elif x=="l":
              return "108"
       elif x=="m":
              return "109"
       elif x=="n":
              return "110"
       elif x=="o":
              return "111"
       elif x=="p":
              return "112"
       elif x=="q":
              return "113"
       elif x=="r":
              return "114"
       elif x=="s":
              return "115"
       elif x=="t":
              return "116"
       elif x=="u":
              return "117"
       elif x=="v":
              return "118"
       elif x=="w":
              return "119"
       elif x=="x":
              return "120"
       elif x=="y":
              return "121"
       elif x=="z":
              return "122"
       elif x=="[":
              return "91"
       elif x=="\\" :
              return "92"
       elif x=="]":
              return "93"
       elif x=="^":
              return "94"
       elif x=="_":
              return "95"
       elif x==":":
              return "58"
       elif x==";":
              return "59"
       elif x=="<":
              return "60"
       elif x=="=":
              return "61"
       elif x==">":
              return "62"
       elif x=="?":
              return "63"
       elif x=="{":
              return "123"
       elif x=="|":
              return "124"
       elif x=="}":
              return "125"
       elif x=="~":
              return "126"
       elif x==" ":
              return "32"
       elif x=="!":
              return "33"
       elif x=='"':
              return "34"
       elif x=="#":
              return "35"
       elif x=="$":
              return "36"
       elif x=="%":
              return "37"
       elif x=="&":
              return "38"
       elif x=="'":
              return "39"
       elif x=="(":
              return "40"
       elif x==")":
              return "41"
       elif x=="*":
              return "42"
       elif x=="+":
              return "43"
       elif x=="-":
              return "43"
       elif x==".":
              return "44"
       elif x=="/":
              return "45"
       elif x=="0":
              return "46"
       elif x=="1":
              return "47"
       elif x=="2":
              return "48"
       elif x=="3":
              return "49"
       elif x=="4":
              return "50"
       elif x=="5":
              return "51"
       elif x=="6":
              return "52"
       elif x=="7":
              return "53"
       elif x=="8":
              return "54"
       elif x=="9":
              return "55"
       elif x=="@":
              return "64"
       elif x=="`":
              return "96"
       


chars=set('0123456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm!@#$%^&*()-+{[}]:;,.<>?/\\\'|`~ \\"')
print ("Acceptable characters:")
print (chars)
word=input("Type a string using the acceptable characters listed above ")
while any((a not in chars) for a in word):
       print ("Your string contains one or more characters not listed above. Please try again.")
       word=input("Type a string ")
num=""
for i in word:
       num= num + ASCII(i)
print ("Your string converted to a number through ASCII: ",num)
num=int(num)
status="This is a prime number"
for i in range (2,num):
       if num%i==0:
              status="This is NOT a prime number"
              break
print (status)
              
