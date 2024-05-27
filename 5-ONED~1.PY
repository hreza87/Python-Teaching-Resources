##############Introduction to 1 Dimensional Data structures################

#Create a list manually
# This is how we create a 1d list and add items to it. 
videogames=["Elden ring","Call of duty","SF2","Pacman","Roblox","Five nights","Trains in World 3","Assasins Creed","Mortal Kombat","Hitman"]

# (Important) Data Structure Fundamental skills 
# Skill 1 Accessing a single element in a list
print(videogames[2])

# Skill 2 How to access a list using a for a loop. This utilizes skill 1 & for a loop. 
for i in range(10):
  print(videogames[i])
#Accessing entire list is not a popular way for OCR, but quick for seeing changes in data. 
print(videogames)

# Skill 3 How to modify a list, for example replacing an element.
videogames[0]="Roblox"# this will get rid of Elden ring and store Roblox instead. 

# Skill 4 Adding a new item to a list. 
videogames.append("New video game")

#Some important functions to remember.
#Using len function to access 1-dimensional data structures.
#In the example below, len would count how many characters are in the variable name and display the count.
name="NathanWalker"
print(len(name))

#Let's use "Skill 2" How to access a list using a for loop, and apply the len function.
for i in range(len(videogames)): #len function counts elements in the videogames list and provides that as range.
  print(videogames[i]) 

# we could use a while loop to iterate through the list as well. 
videogames=["Elden ring","Call of duty","SF2","Pacman","Roblox","Five nights","Trains in World 3","Assasins Creed","Mortal Kombat","Hitman"]
x=0
while x<len(videogames):
  print(videogames[x])
  x=x+1

#Let's take a look at some practice Examples highly useful for exam revision. We should be able to query data structures for example do things like counting items, finding items, filtering items or using data to calculate averages. 

#Example 1 Write additional code that would count the number of games in the list and display the total. 
for i in range(len(videogames)):
  print(videogames[i])

  #Solution
total=0
for i in range(len(videogames)):
  print(videogames[i])
  total=total+1
print("the total games are:",total)

# Example 2 Write a program that would check for games that have names longer than 10 characters. It will display a count of these games.

#Solution 
videogames=["Elden ring","Call of duty","SF2","Pacman","Roblox","Five nights","Trains in World 3","Assasins Creed","Mortal Kombat","Hitman"]
count=0 #keeps track of how many game names longer then 10 characters. 
for i in range(len(videogames)):
  if len(videogames[i])>10:# we could use selection to compare the length of each game with our criteria.
    count=count+1

print(count,"are the number of games that have long names then 10 chars")

#Example 3 Write code to check if a certain game exists within the video games list. Display a message game that exists.
videogames=["Elden ring","Call of duty","SF2","Pacman","Roblox","Five nights","Trains in World 3","Assasins Creed","Mortal Kombat","Hitman"]
for i in range(len(videogames)):
  if videogames[i]=="Call of duty":
    print(videogames[i]," exists on the system")
# else:  
#    print("video game does not exist") # Read below
#Adding the else part would not  be a good idea as each iteration not matching the criteria will result in non #existent message

  #Challenge Example 3 continued, add additional code that would display the message video game don't exist.
videogames=["Elden ring","Call of duty","SF2","Pacman","Roblox","Five nights","Trains in World 3","Assasins Creed","Mortal Kombat","Hitman"]
found=0
for i in range(len(videogames)):
  if videogames[i]=="Call of duty":
    print(videogames[i]," exists on the system")
    found=found+1
if found==0:
  print("item does not exist in the list")

#Example 4 Write a program that allows the user to enter grocery items in a list called groceries, when the user types in end, the program stops, and displays all the items that have been entered. 

#Solution 1 
groceries=[]
item=209   #assign a value that will simply trigger the while loop into running itself. 
while item !="end": # as per the question the criteria is typing end will stop the while loop. 
  item=input("enter an item")
  groceries.append(item)
#simply displays the list 
for i in range(len(groceries)):
  print(groceries[i])

#Solution 2 
groceries=[]

while True:
  item=input("enter an item")
  groceries.append(item)
  if item=="end":
    break
#simply displays the list 
for i in range(len(groceries)):
  print(groceries[i])


#Example 5 Write an algorithm that will populate a list called places[] with the word "emptyspace" 10 times.
places=[]
for i in range(10):
  places.append("emptyspace")

print(places)
#challenge Write additional code that will allow the user to pick a position and modify the list in a way, so if the user picks 1, list should appear as "chosen","emptyspace","emptyspace" .....
position=int(input("enter a position for chosen word to be placed"))
places[position-1]="chosen"
print(places)
#Further challenge Write additional code so that the user can pick a position and also write a new word to be stored in the list.

position=int(input("enter a position for chosen word to be placed"))
word=input("enter a new word")
places[position-1]=word
print(places)

#Exam Questions 
#https://pitsfordschool0-my.sharepoint.com/:b:/g/personal/hrizvi_pitsfordschool_com/ERnPQD3cyUVBjBt5PNI5rdwBRKmWFlYkHtu9eYhyvIoAvQ?e=O9rSSw

#Exam Question 20 
a=0
b=0
c=0
vote="random"
while vote !="end":
  vote=input("enter a,b or c to vote")
  if vote=="a":
    a=a+1
  elif vote=="b":
    b=b+1
  elif vote=="c":
    c=c+1
print("votes for candidate a",a)
print("votes for candidate b",b)
print("votes for candidate c",c)
  
#Exam Question 28
studentnames=["Rob", "Anna", "Huw", "Emma", "Patrice", "Iqbal"]
present=0
absent=0
for i in range(len(studentnames)):
  print(studentnames[i])
  attendance=input("are they present yes/no?")
  if attendance=="yes":
    present=present+1
  elif attendance=="no":
    absent=absent+1

print(present,"students are present")
print(absent,"students are absent")
#Exam Question 31 
students=["helen","adam","lydia","Kwaku","priya","cham"]
print(students)
#The following block of code will displace each name by one place. 
  students[5]=students[4]
  students[4]=students[3]
  students[3]=students[2]
  students[2]=students[1]
  students[1]=temp
print(students)
#Exam Solution The jumps will repeat the block of code above as per user's input so entering jumps would displace names forward by that amount. 
students=["helen","adam","lydia","Kwaku","priya","cham"]
print(students)

jumps=int(input("enter jumps to make"))
for i in range(jumps):
  temp=students[5]
  students[5]=students[4]
  students[4]=students[3]
  students[3]=students[2]
  students[2]=students[1]
  students[1]=temp
print(students)


#Exam Question 35
studentdata=["Kirstie","Homework forgotten","-2","False"]
if studentdata[3]=="True":
  print("letter sent home")
elif studentdata[3]=="False":
  print("letter not sent home")

#Exam Question 39 

numbers=[]

for i in range(100):
  numbers.append("")

print(numbers)

while True:
  position=int(input("enter a position"))
  if numbers[position-1]=="":
    numbers[position-1]="A"
  elif numbers[position-1]=="A":
    print("taken")
  print(numbers)
  count=0
  for i in range(len(numbers)):
    if numbers[i]=="":
      count=count+1

  print(count)
