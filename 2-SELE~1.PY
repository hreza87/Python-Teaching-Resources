#basic selection-Matrix 
pill=input ("Red or Blue pill?")
if pill=="Red":
  print ("You stay in woderland and se how far the rabit hole gos")
elif pill=="Blue":
  print ("You will wake up and foget everythng")
else:
  print("that is not an option for you!")

#Basic selection-Car collision
person=input("is there a person right infront of the car yes/no?")
if person=="yes":
  print("Keep the car on stop mode")
elif person=="no":
  print("enable car to go forward")
else:
  print("you dont make much sense, please say yes or no")

#Basic Selection Program- Quiz 
q1=input("what is the capital of france? \n 1. Paris \n 2. UK \n 3. Cyprus")
if q1=="paris":
  print("Welldone that is the correct answer")
else:
  print("I'm afraid the correct answer was paris!")

#Medium Selection- Hot/Cold
answer=input("is the window open? yes/no")
if answer=="yes":
  print("its pretty chilly in here")
elif answer=="no":
  print("its boiling hot in here")
else:
  print("Meh!!, not sure what you mean!")

#Basic Selection-Guests hotel room suggestion
guests=int(input("enter the number of guests to determine room size"))
if guests==1:
  print("you are booked in for single room")
elif guests==2:
  print("you are booked in for a double room")
elif guests>=3:
  print("you are booked in for a family room")

#Basic selection-Ticket Price
passengers=int(input("enter the amount of passengers"))
if passengers==1:
  print("cost per journey would be £2.50")
elif passengers==2:
  print("cost per journey would be £3.00")
elif passengers==3:
  print("cost per journey would be £3.50")
elif passengers==4:
  print("cost per journey would be £4.00")
elif passengers>=5:
  print("cost per jounry would be £5.00")
else:
  print("You have entered an invalid amount.")

#Basic selection-GCSE grades and uni admission
gcses=int(input("enter gcses that are A* to a C"))
if gcses>=5:
  print("You can enter your chosen university choice")
elif gcses>=3:
  print("you will need to go for an interview")
else:
  print("sorry im afraid you cant go university")

#Basic selection Program-Driving License
age=int(input("enter your age to check if you are eligible for driving license"))
if age>18:
  print("you can apply for a UK driving license")
if age>17:
  print("you can apply for a provisional license")
else:
  print("Go to smyths toys, and get a car.")

# Basic Selection Program- Larger number 
number1=int(input("enter number1"))
number2=int(input("enter number2"))

if number1>number2:
  print("the largest number is",number1)
else:
  print("the larger number is",number2)

#Basic selection-Hot/Cold
temp=float(input("please enter the temp"))
if temp>=23:
  print("turn off heating")
else:
  print("turn on the heating")

#There are three 
#kinds of logical
#operators known as :
#and
  
#or
  
#not

#Write a program which accepts userinputs :
#username & password.
#if both username & password are correct, it grants access.
#else it says invalid entry.

username=input("enter username")
password=input("enter password")
if username=="potatohead" and password=="potato":
  print("welcome kind sir")
else:
  print("invalid entry")

#Medium Selection -Larger number
number1=int(input("enter number1"))
number2=int(input("enter number2"))
number3=int(input("enter number3"))
if number1>number2 and number1>number3:
  print("the largest number is",number1)
elif number2>number3 and number2>number1:
  print("the largest number is", number2)
else:
  print("the largest number is", number3)
  
#write a program for RAF recruitment which only accepts candidates age 21-49, and prompts them , whether they are eligible for entry else rejects them. 

age=int(input("enter your age to check if you are eligible for entry on the RAF!"))
if age >=21 and age<=49:
  print("you are eligible ")
else:
  print("sorry , good bye. ")

#Write a program , which outputs A if the score is more then 50, if its 50 only then its a pass, otherwise it would be a fail.

marks=int(input("enter the score to find out the grade?"))
if marks>=50 and marks<=100:
  print("Passed this test")
elif marks<50:
  print("you have failed") 

#Basic selection program Or operator-Vowels
letter=input("enter a letter: ")
if letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u":
  print("you have entered a vowel")
else:
  print("you have entered consonant")

#Basic selection Program with Logical operators-Quiz
total=0
q1=input("what is the capital of france? \n 1. Paris \n 2. UK \n 3. Cyprus")
if q1=="paris" or q1=="Paris" or q1==" Paris" or q1==" paris":
  print("Welldone that is the correct answer")
  total=total+1
else:
  print("I'm afraid you need brushing up on your general knowledge")
print("you scored:", total)
#extension
if total==10:
  print("well done you scored full marks")
elif total>=7:
  print("good effort")
else:
  print("that is absolutely horrendous")


#Use the NOT logical operator. 
#Write a program which accepts userinput colour.
#it should compliment only "navyblue" and nothing else.
#the prompt for any other colours should be , bad taste.

colour=input("enter your favourite colour")
if not(colour=="navyblue"):
  print("bad taste")
else:
  print("good choice!")

#Write a program which takes in your lucky number.
#If the lucker number matches 9, it should say , you won, if the lucky number is not 9 , it should say unlucky.

number=int("enter your lucky number")
if not(number==9):
  print("unlucky mate")
else:
  print("well done you won the lottery")

#Write a program which asks for user input and prints it.
#if user input is not between 1-10 , then it asks for it again

number=int(input("enter a number between 1 and 10"))
while not(number>1 and number<10):
  number=int(input("enter a number between 1 and 10"))
print(number)
#Alternative solution
number=int(input("enter a number between 1 and 10"))
while number<1 or number>10:
  number=int(input("enter a number between 1 and 10"))
print(number)

#Nested If Selection-
#Hard Selection- travelling with tea

passengers=0
while passengers<5:
  response=input("are you the correct person?")
  if response=="yes":
    carryingtea=input("are you carrying tea on you")
    if carryingtea=="yes":
      permit=input("are you carrying a tea permit?")
      if permit=="yes":
        print("you are allowed")
        passengers=passengers+1
      elif permit=="no":
        print("you arent allowed sorry")
    elif carryingtea=="no":
      passengers=passangers+1
      print("you are allowed to enter")
    print("you are permitted")
  elif response=="no":
    print("you are not permitted")
    
#Nested If Selection
#Special airservice has a minimum height requirement. To be considered for selection they want minimum height of 160cm, or 150cm if weight is between 100-150 pounds.

#Create an algorithm that:
#  asks the user to input the height of the candidate in cm.
#  if needed , asks for their weight.
#  Outputs whether or not they are eligible for selection. 
height=int(input("How tall are you ?"))
if height>=160:
  print("You are eligible for SAS selection, goodluck!")
if height>=150 and height<160:
  weight=float(input("How much do you weigh?"))
  if weight>=100 and weight<=150:
    print("you are eligible for selection, goodluck")
  else:
    print("you are not eligible for selection")

#Examination Questions
length1=int(input("enter length"))
length2=int(input("enter length"))
length3=int(input("enter length"))

if length1==length2 or length1==length3 or length2==length3:
  print("you have isoleces trignle")
else:
  print("non iso")

#Alternative solution

if length1==length2:
  print("iso")
elif length2==length3:
  print("iso")
elif length1==length3:
  print("iso")
else:
  priont("no iso")

#Examination Questions
passengers=0
while passengers<8:
  height=float(input("enter height to check if you quality for a ride"))
  if height>=140:
    print("you can ride this alone")
    passengers=passengers+1
  elif height>=120 and height<140:
    adult=input("are you with an adult yes/no")
    if adult=="yes":
      print("you are allowed with adult")
      passengers=passengers+2
    elif adult=="no":
      print("you cant ride sorry.")
  else:
    print("you cant go sorry mate!")

#Examination Questions
riders=0
while riders<8:
  height=float(input("enter your height"))
  if height>=140:
    print("you are allowed to ride on your own")
    riders=riders+1
  elif height>=120 and height<140:
    print("you need an adult to travel with you")
    adult=input("travelling with adult yes/no")
    if adult=="yes":
      riders=riders+2
  else:
    print("you cant ride this sorry")

#Examination Questions
teddybears=int(input("enter the number of teddy bears"))
hours=float(input("enter the number of hours"))
wage1=2*teddybears
wage2=hours*5
if wage1>wage2:
  print(wage1)
else:
  print(wage2)

#Examination Questions
#While and selection- Vote Program
a=0
b=0
c=0
vote="weoifjweiofjio"
while vote!="END":
  vote=input("enter a vote , either a/b/c or press END to stop")
  if vote=="a":
    a=a+1
  elif vote=="b":
    b=b+1
  elif vote=="c":
    c=c+1
print(a,"are the number of votes for a")
print(b,"are the number of votes for b")
print(c,"are the number of votes for c")

#Alternative 
"""
while True:
  do something

  if votes=="____"
    break
"""