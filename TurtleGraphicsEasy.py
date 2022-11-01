from turtle import *

# create function to draw squares
def square():
  for i in range(4):
    forward(100)
    right(90)

# set speed to 0 to speed up process
speed(0)
# set color to green
color('green')
# run for loop to repetitively draw squares
for i in range(20):
  square() # call square function
  right(18) # Turn right by 18°. 18° * 20 iterations = 360°
  
# end the program
done() 
