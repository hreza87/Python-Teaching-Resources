##############Introduction to 2 Dimensional Data structures################

#Create a list manually
# This is how we create a 2d list and add items to it manually. 
#Athlete database
athlete=[
        ["tom",45,160],
        ["jacob",18,120],
        ["Carl",28,140]
        ]

# misconception, you can write the 2d list as follows it will still work. To think of 2d list , it is simply a list of 1d lists. 
athlete=[["tom",45,160],["jacob",18,120],["Carl",28,140]]

# (Important) Data Structure Fundamental skills 

# Skill 1 Accessing a specific list in 2d list 
print(athlete[1]) # this will output ["tom", 45, 160].

#Skill 2 Accessing a single element in a 2d list.
print(athlete[1][0]) # this will display tom. 

# Skill 3 How to access a 2d list using a for loop. This utilizes skill 1 & a loop. 
for i in range(3):# this loop iterates through each list one by one.
    print(athlete[i])
# Skill 4 How to iterate through each element in 2d list, would utilise skill 2 and nested for loop. 
for i in range(3):
  for j in range(3):
    print(athlete[i][j])
#Better version which uses len function. Ideally suited to meet exam requirements. 
for i in range(len(athlete)): #counts how many lists there are uses this as range.
  for j in range(len(athlete[i])):#counts how many elements there are in list[i].
    print(athlete[i][j])    
    
# Skill 5 How to modify a list, for example replacing an element.
athlete[0][0]="Charlie"# this will get rid of Tom and replace with CHarlie. 

# Skill 6 Adding a new item to a list. 
#Example 1 
athlete[0].append(303)
#Example 2

#Let's take a look at some practice Examples highly useful for exam revision. We should be able to query data structures for example do things like counting items, finding items, filtering items or using data to calculate averages. 

#Example 1 Using 2D list to query information such as looking for a search item.
  #Write code to search for name "jacob" in the 2d list,and display message if found.
athlete=[
        ["tom",45,160],
        ["jacob",18,120],
        ["Carl",28,140]
        ]

for i in range(len(athlete)): #counts how many lists there are uses this as range.
  for j in range(len(athlete[i])):#counts how many elements there are in list[i].
    if athlete[i][j]=="jacob":
      print("Item has been found")
  #Challenge Add code for item not found. 
found=0     
for i in range(len(athlete)): #counts how many lists there are uses this as range.
  for j in range(len(athlete[i])):#counts how many elements there are in list[i].
    if athlete[i][j]=="jacob":
      print("Item has been found")
      found=found+1
if found==0:
  print("item not found")
  #Challenge Make the program interactive so that user can type in their search query for name.

athlete=[
        ["tom",45,160],
        ["jacob",18,120],
        ["Carl",28,140]
        ]
name=input("enter name to search for ")# Modified part to the algorithm. 
found=0     
for i in range(len(athlete)): #counts how many lists there are uses this as range.
  for j in range(len(athlete[i])):#counts how many elements there are in list[i].
    if athlete[i][j]==name:# individual name replaced with variable reference. 
      print("Item has been found")
      found=found+1
if found==0:
  print("item not found")

  #Challenge , the program will fail if you enter integer value for search. HOw can you fix this program. 

#Solution 1 we could use casting to convert integer in the 2d list into a string while making the comparison.
athlete=[
        ["tom",45,160],
        ["jacob",18,120],
        ["Carl",28,140]
        ] 
name=input("enter name to search for ")# Modified part to the algorithm. 
found=0     
for i in range(len(athlete)): #counts how many lists there are uses this as range.
  for j in range(len(athlete[i])):#counts how many elements there are in list[i].
    if athlete[i][j]==name or str(athlete[i][j])==name:# individual name replaced with variable reference. 
      print("Item has been found")
      found=found+1
if found==0:
  print("item not found")

#Example 2 Using 2D list to query information and carrying out a numerical calculation such as finding total items that match something.
#Write an algorithm that counts how many names exist in the 2d list that match the search
athlete=[
        ["tom",45,160],
        ["jacob",18,120],
        ["Carl",28,140],
        ["jacob",19,123]
        ] 
name=input("enter name to search for ")# Modified part to the algorithm. 
found=0     
for i in range(len(athlete)): #counts how many lists there are uses this as range.
    if athlete[i][0]==name # this line automatically sifts each list and checks the name. 
    found=found+1
print("the number of names that match your search are ",found)

#Example 3 Write an algorithm that automatically calculates average age of each athelete.
athlete=[
        ["tom",45,160],
        ["jacob",18,120],
        ["Carl",28,140],
        ["jacob",19,123]
        ] 
totalage=0     
for i in range(len(athlete)): #counts how many lists there are uses this as range.
    totalage=totalage+ athlete[i][1] # this line automatically sifts each list and accesses age. 
    
print("average age is ",totalage/(len(athlete)) # len(athlete) counts how many lists there are, which equates to number of athletes. 


#Exam Questions 

#Exam Question 30 a) Part iv to find out how many minutes student 0 played from monday to friday. 
hoursplayed=[
            [60,180,200,60,100],
             [30,60,30,10,35],
             [45,0,0,15,30],
             [0,60,20,15,45],
             ]
totalmin=0
for i in range(len(hoursplayed[0])):# this uses length of student[0] list which would equate to 5 , as there were 5 times played during the week. 
  totalmin=totalmin+hoursplayed[0][i]
print(totalmin)

#Exam Question 30 Part c
hoursplayed=[
            [60,180,200,60,100],
             [30,60,30,10,35],
             [45,0,0,15,30],
             [0,60,20,15,45],
             ]
counter=0
total=0
for i in range(len(hoursplayed)):
  for j in range(len(hoursplayed[i])):
    print(hoursplayed[i][j])
    total=total+hoursplayed[i][j]



#Exam Question 38 

discount=[["PVFC7",10],["CPU5",5],["BGF2",15]]

def checkdiscount(price,code):
  newprice=price
  size=len(discount)
  for x in range(size):
    if discount[x][0]==code:
      newprice=newprice-discount[x][1]
  return newprice

print(checkdiscount(35,"TNT"))
