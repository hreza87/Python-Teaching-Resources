#introduction to for loops 
#Example 1 for loop with single parameter.
for i in range(11):
  print("Hello World")

#Example 2 for loop with minimum and maximum parameters for the range
for i in range(1,11):
  print(i)

#Example 3 For loop with minimum,maximum parameters and steps which means the increment i should take to iterate the loop. 
for i in range(0,11,3):
  print(i)

#Example 4 For loop with maximum, minimum parameter, negative steps to reduce the value of i while iterating the loop. 
for i in range(10,0,-1):
  print(i)

#learning note: i is a variable that keeps track of iterations in a for loop.
#it's sole purpose is not to display numbers but can be used for that purpose.
# i is very useful to access elements in an array . 


#strategy 1 
for i in range(1,10,2): # can edit this line 
  print(i)# can't change this line 

#strategy2
for i in range(10):#only add one parameter or min,max
  print((i+1)*3)# can edit this line any way you like.

#strategy3
number=3# can create a variable
for i in range(10):# use a parameter.
  print(number) # can edit this line and below any way you like
  number=number+2

#Practise problem 1
#create an algorithm which asks user to enter a word and how many times they want it to print. The algorihm should print the word . 

#name=input("enter a word")
#amount=int(input("enter amount of times you wish to print"))
#for i in range(amount):
#  print(name)

#Practise problem 2
#Create a sequence of numbers 2-20
#strategy 1 applied
for i in range(2,21,2):
  print(i)

#strategy 2 applied
for i in range(10):
  print((i+1)*2)
  
#strategy 3 applied 
number=2
for i in range(10):
  print(number)
  number=number+2

#Practise problem 3
#Write an algorithm which produces sequence from 3-11 with increments of 2.
#it outputs the total value.
total=0
for i in range(3,12,2):
  print(i)
  total=total+i
print(total,"is the total value")
  
#Practise problem 4
#Create a sequence of 1-10. 
#Algorithm should print odd or even underneath each number.
#Hint odd numbers divided by 2 leave 1 as remainder and 1 if odd.

for i in range(1,11):
  if i%2==0:
    print(i,"is even number")
  elif i%2==1:
    print(i,"is odd number")