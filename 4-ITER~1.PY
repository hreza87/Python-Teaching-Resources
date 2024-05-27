#Preliminary knowledge:
#You are required to use the following operators in order to create conditions which the while loop can use to iterate particular task. 

# >
# <
# >=
# <=
# !=
# ==
# and,or,not 



#Introduction to a while loop
#a While Iteration is a condition controlled loop, unlike a for loop it relies on a condition being true to repeat a block of code.  

#Example 1 The following while loop will repeat line7, because it checks if the value stored inside the variable "x" equals to the given value , as they both equal , a true condition is generated which enables the while loop to run, a false condition generated would not enable the while loop.

x=True 
while x==True: 
  print("This line of code will repeat for as long as condition is true")
  # after line 7, the program goes back to line 6 to check if x still equal to True.


#Example 2 The following loop will not repeat forever. This is because in line 15, x is reassigned a new value, the program goes back to line 13 to check if x still equals to True, as it doesnt, the while loop will not run. Line 16 will run as its next instruction in the sequence . 
x=True 
while x==True:
  print("This loops repeats ")
  x=False
print("this line will run when the while loop stops running")

#Example 3 While loops can be used to repeat a certain action until a certain amount has been reached. For e.g a program that continues to print a number sequence until it exceeds a given number for instance 3. .
#     1     2    3
number=1
#while number !=4: this would have been another strategy.
while number<=4:
  print(number)
  number=number+1

#Example 4 Write a program which asks user to input a number, the program continues to ask for input until the total value exceeds 10 .
#solution 1
total=0
while total<10:
  number=int(input("enter an item"))
  total=total+number
print("your total is:",total)
#solution 2 
total=0
while True:
  number=int(input("enter the number"))
  total=number+total
  if total>=10:
    break

#Example 5 write a program which asks for user input and it doubles the input. It repeats until the user exceeds 3 goes.

goes=0
while goes<3:
  number=int(input("enter a number"))
  print(number*2)
  goes=goes+1

#Practise Problems 
#Problem 1 Bird Watching 
#Write a program which will ask user to enter bird sizes. 
#The program should stop after 8 bird sizes have been entered. 
#Size 1 is smallest, size 10 is largest. 
birds=0
while birds<8:
  size=int(input("enter the bird size"))
  birds=birds+1
print("total birds entered are",birds)
#Challenge
#The program should validate entry of size, so if size is between including 1 and 10 including 10, it should count as valid entry , otherwise program should prompt user to enter correct size.
birds=0
while birds<8:
  size=int(input("enter the bird size"))
  while size<0 or size>10:
    size=int(input("enter the correct bird size"))
  birds=birds+1
print("total birds entered are",birds)

#Example 6 While loops can be used for data verification for example repeating a certain action if data is within a limit or a certain value. We can look at three examples.

#Part a ) Write a program which asks for a password, if the password is incorrect, it continues to ask for password , otherwise it stops and says "You have been authorised !"
# solution 1
password=input("please enter correct password")
while password !="10g":
  password=input("please enter correct password")
print("you have been authorised")
# solution 2  
password="waffles"
while password !="10g":
  password=input("please enter correct password")

print("you have been authorised")

#Part b) Write a program which asks for an input,if the input is between the range of 1 and 10 it displays the number on screen if it isn't it asks for the input again until its in the right range , and printing it. 

number=int(input("enter a number"))
while number<1 or number>10:
  number=int(input("enter a number"))
print(number)


#part c) Write a program which asks user to guess a number, it continues to ask for number until the guess is correct! 
#soution 1 
number=0
while number != 72:
  number=int(input("guess a random number: "))
print("YAY! you have guessed correctly! ")

#solution 2
while True:
  number=int(input("enter a number"))
  if number==72:
    break
print("YAY! You have guessed correctly! ")



#Problem 2 Password verification and cheat 
#Write a program which asks for password , if the pAssword is correct it stops, other wise it continues to ask password for 3 more times, other wise it locks, 
total = 0
password= ""
while password != "spiderman":
  password = input("please enter the password: ")
  total=total + 1
  print("you have used tries:",total)
  if total>=3 and password!="spiderman":
    print("you have been locked out")
    break
if password=="spiderman":
  print("you have successfully logged in !")
# program a cheat code , if user types that the tries are reset back.
#solution 1
total = 0
password= ""
while password != "spiderman":
  password = input("please enter the password: ")
  total=total + 1
  if password=="reset":
    total=0
  print("you have used tries:",total)
  if total>=3 and password!="spiderman":
    print("you have been locked out")
    break
if password=="spiderman":
  print("you have successfully logged in !")
#solution2 
total=0
password=""
while password !="spiderman":
     password=input("enter password")
     if password=="reset":
          total=0
          print("you have used tries:",total)
     elif password !="spiderman":
          total=total+1
          print("you have used tries:",total)
     if total>2:
          print("you have been locked out:",total)
          break
if password=="spiderman":
     print("you have logged in successfully")



#Exam Practise Questions (Theme Park)
# 18 OCR Land is a theme park aimed at children and adults. Entrance tickets are sold online. An adult ticket to OCRLand costs £19.99, with a child ticket costing £8.99. 
#A booking fee #of £2.50 is added to all orders.
#One ride in OCR Land has a minimum height of 140 cm to ride alone or 120 cm to ride with an adult.
#Create an algorithm that:
#•asks the user to input 
#the height of the rider, in centimetres
#•if needed, asks if they are riding with an adult
#•outputs whether or not they are allowed to ride•repeats this process until 8 people have #been allowed to ride.

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

#Exam Practise Questions ( Election)
# 20 OCR town are holding an election with three candidates (A, B and C). An electronic voting booth will be used toallow people to vote. 
#Write an algorithm that:•Allows voters to enter either A, B or C.
#•Keeps track of how many times each candidate has been voted for.
#•As soon as one person has finished voting, allows the next person to vote.
#•At any point allows the official to type in “END”, which will print out the number of votes for each candidateand the total number of votes overall.

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


#Further practise 
# write a program which asks user for given grocery item, user should be able to type and view selected item. If user types in end , the program should end. 
item="random"
while item !="end":
  item=input("enter grocery item")
  print(item)

# write a program which asks user for given grocery item, user should be able to type and view selected item. If user types in end , the program should end. 
#Solution 1 we could define a variable with unsuitable data that would trigger the while loop. 
#password="waffles"
#Solution 2 We could define variable and assign user input to allow loop to repeat it self. 
password=input("enter your correct password")
while password !="10f":
  password=input("please enter the correct password")
print("well done you have been authorised")

# write a  program for border force airport control , to allow passengers to enter the aeroplane.
The program should ask passenger if they are , who they say they are, if they reply yes, the program should allow them to enter, if they say no, the program should not allow them. The program should repeat after 5 passengers have been entered, due to it's maximum load capacity.
#Solution
passengers=0
while passengers<5:
  response=input("are you the correct person")
  if response=="yes":
        print("you are allowed to enter")
        passengers=passengers+1
        print("passnegers boarded:",passengers)
  elif response=="no":
    print("you arent allowed")
print("max capacity reached of 5")
# Challenge 1 previous plane was reported for smugling tea, therefore the program should only let passenger onboard if they have no tea , otherwise not allowed. 
#Solution
passengers=0
while passengers<5:
  response=input("are you the correct person")
  if response=="yes":
    tea=input("are you carrying tea?")
    if tea=="yes":
        print("you arent allowed")
    elif tea=="no":
      print("you are allowed to enter")
      passengers=passengers+1
      print("passnegers boarded:",passengers)
  elif response=="no":
    print("you arent allowed")
print("max capacity reached of 5")
# Challenge: 2 Due to many complaints by the elderly flyers, the program should only allow passengers that are carrying tea , if they they they have a permit. 
#Solution
passengers=0
while passengers<5:
  response=input("are you the correct person")
  if response=="yes":
    tea=input("are you carrying tea?")
    if tea=="yes":
      permit=input("are you carrying tea permit?")
      if permit=="yes":
        print("you are allowed to enter")
        passengers=passengers+1
        print("passnegers boarded:",passengers)
      elif permit=="no":
        print("you arent allowed")
    elif tea=="no":
      print("you are allowed to enter")
      passengers=passengers+1
      print("passnegers boarded:",passengers)
  elif response=="no":
    print("you arent allowed")
print("max capacity reached of 5")