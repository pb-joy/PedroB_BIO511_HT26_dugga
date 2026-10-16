#This is the answer sheet for the Python Dugga ofr student Pedro Bastos

#Question 1

#a) Save your own name as a string to a variable
my_name = "pedro"

#b) Calculate and print the length of your name

name_length = len(my_name) #len() returns the length of the string
print ("Name length:", name_length)

#c) Choose a letter that occurs in my name at least once. Print the number of times the letter occurs.

count = 0 #we create a count variable that we will use in the loop
my_name = my_name.lower() # makes sure all the letters are lower case
my_name_list = list(my_name) # converts the string into a list of letters

#for loop that calculates the number of appearances of the letter o
for letter in my_name_list:
    if letter == "o":
        count += 1 
    else:
        continue

print ("Number of times letter o occurs:", count)

#Question 2:

my_list= [1,5,"4","six", 3.14]

#a) For each item in my_list try to convert it to an int and add it to a new list called new_list

new_list = []

for item in my_list:
    try:
        integer = int(item)
        new_list.append(integer)
    except ValueError:
        print (item , "is an invalid literal and cannot be converted to an int")

#b) Put the conversion loop in a function called clean_list()

def clean_list(list):
    new_list = []
    for item in my_list:
        #we use try to make sure we can convert the argument into an int
        try:
            integer = int(item)
            new_list.append(integer)
        except ValueError:
            print (item , "is an invalid literal and cannot be converted to an int")
    return new_list

new_list = clean_list(my_list)
print(new_list)

#c)

sum_of_neighbours = []
n=1

for i in new_list:
    #we use try so when the list reaches the last argument it doesn't run into an index error and simply stops the loop
    try:
        sum_of_neighbours.append( i + new_list[n])
        n+=1
    except IndexError:
        continue


print(sum_of_neighbours)

#Question 3

#a)

import pandas as pd
import matplotlib.pyplot as plt
import os

#We create a scatter plot as instructed with the matlap library
file_path= "cnv_data.csv"
cnv_df= pd.read_csv(file_path)

plt.scatter(cnv_df ['position_mb'] , cnv_df ['log2_ratio'])
plt.title('Position vs Log2 Ratio')
plt.xlabel('Position_mb')
plt.ylabel('log2_ratio')
plt.savefig("plot.png")
plt.show()


#b)
# we already completed this assignment in the previous step

#c)

# input takes the file_path, the wished x axis, y axis and out put path
file_path= input("Select the file you wish to plot: ")
x_axis= input("Select x axis:")
y_axis= input("Select y axis:")
output_path= input("Select output path:")
cnv_df= pd.read_csv(file_path)

plt.scatter(cnv_df [x_axis] , cnv_df [y_axis])
plt.savefig(output_path)
plt.show()


#Question 4

#a)

import random

i = 0
score1 = 0
score2 = 0
score3 = 0

while i < 20:
    dice_roll1 = random.randint(1,6)
    dice_roll2 = random.randint(1,6)
    if dice_roll1 > dice_roll2:
        score1 += 1
    elif dice_roll1 < dice_roll2:
        score2 += 1
    else:
        score3 += 1
    i+=1

score = {"Alice won" : score1 , "Bob won": score2 , "Draw" : score3  }

print(score)

#b)

def game (name1, name2, num):
    i = 0
    score1 = 0
    score2 = 0
    score3 = 0

    while i < 20:
        dice_roll1 = random.randint(1,6)
        dice_roll2 = random.randint(1,6)
        if dice_roll1 > dice_roll2:
            score1 += 1
        elif dice_roll1 < dice_roll2:
            score2 += 1
        else:
            score3 += 1
        i+=1
    score = {name1 : score1 , name2 : score2 , "Draw" : score3  }

    return score

name1 = input ("Choose player 1:")
name2 = input ("Choose player 2:")
num = input ("Choose the number of games played:")

score = game (name1, name2, num)
print(score)

 
         
    