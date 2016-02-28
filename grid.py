# Jeff Kropelnicki
# GIS 5578
# Homework one grid
 
# INPUT MATRIX------------------
import numpy as np
import string

grid = [[1,1,2,4,1,7,1,7,6,9],\
        [1,2,5,3,9,1,1,1,9,1],\
        [7,4,5,1,8,1,2,0,0,4],\
        [1,4,1,1,1,1,1,1,8,5],\
        [9,0,0,0,0,0,1,1,9,8],\
        [7,4,2,1,8,2,2,2,9,7],\
        [7,4,2,1,7,1,1,1,0,5],\
        [3,4,5,3,4,5,9,1,0,9],\
        [0,0,5,1,1,1,9,7,7,7]]

print ''
for i in grid:
   print i
        

print""    #printing a blank line for spacing
grid_array = np.array(grid) #naming the grid an array for latter use

row = len(grid)         #gets the length of the grid meaning it counts the rows      
print "Number of rows " + str(row)

col = len(grid[0])      #get the length of grid at the first point meaning it counts the columns
print "Number of columns " + str(col)

cells = row * col       #timing the number of row and number of columns to get number of cells
print"Number of cells " + str(cells)
print ""
# ************************************




# ****** PUT YOUR CODE HERE **********
# Calculate the sum and average
# and display (ie. print) the values
# with some text that tells the user
# what value s/he is looking at;
# similarly, calculate the min, max,
# and range of values within grid;
# there are quite a few built-in list
# functions that can make your life
# easy
Sum = np.sum(grid)   #using numpy to get the sum of the grid
print ("Sum ") + str(Sum)
Mean = np.mean(grid)  #using numpy to get the mean of the grid
print ("Average value ") + str(Mean)
minimum = np.min(grid)  #using numpy to get the minnimum value of the grid
print ("Minimum ") + str(minimum)
maximum = np.max(grid)  #using numpy to get the mix value of the grid
print ("Maximum ") + str(maximum)
Range = np.ptp(grid_array)  #using numpy and ptp function to get the range
print ("Range ") +str(Range)
print ""
# ************************************

# USER SELECTED ROW -----------------
rowID = 1 # hard-coded user input for testing

# What does the following if-clause do?
# Expand this to include columns
rowID = int(raw_input("Select which row to print ")) #asks user to pick a row and convert it to int
#print type(rowID)
if rowID > row - 1 or rowID < 0:    #chacks that the picked number is in range
   print "Row index out of range"         #if not in range print
   print "Setting to default -> the 1st row" #if not in range output row 0 
   rowID = 0                              #starting point 
selectedRow = grid[rowID]                 #naming the selectedRow with the user input on the grid
print "row", rowID, "values:",            #printing row with user input plus the values in the user selected row
print selectedRow

colID = int(raw_input("Select which column to print ")) #asks user to pick a column and convert it to int
#print type(colID)                                      #a test to check for type

if colID > col - 1 or colID < 0:             #chacks that the picked number is in range
   print "Column index out of range"   #if not in range print
   print "Setting to default -> the 1st column" #if not in range output row 0 
   colID = 0

selectedCol = grid_array[: , colID]       #naming the selectedCol with the user input on the grid but with the gird as array
outCol = list(selectedCol)                      #Converting array to list for the 1,2,3,4
print "Calumn", colID, "values:",         #printing column with user input plus the values in the user selected column        
print outCol
print""                       #printing a blank line for spacing




#Ask user to pick a X coordinate

inCal = int(raw_input("Pick a X coordinate: ")) #Ask user to pick a X coordinate
if inCal > col - 1 or inCal < 0:             #checks that the picked number is in range
   print "Column index out of range"   #if not in range print
   print "Setting to default -> the 1st column" #if not in range output row 0 
   inCal = 0


inRow = int(raw_input("Pick a y coordinate: ")) #Ask user to pick a y coordinate
if inRow > row - 1 or inRow < 0:    #chacks that the picked number is in range
   print "Row index out of range"         #if not in range print
   print "Setting to default -> the 1st row" #if not in range output row 0 
   inRow = 0                              #starting point 


# ************* PUT YOUR CODE HERE *************

selCell =  grid_array[inRow, inCal] #sets selCell to the coordinate the user picked from the grid array.
print "Cell " + str(inRow) + "," + str(inCal )+ " value: ", #Print the row picked and col picked then the number at there coorfinate
print selCell
print"" #prints a blank line for spacing 


# ************* PUT YOUR CODE HERE *************
# Use the 'enumerate' function to display the row id/index and the
# corresponding row values for all rows in the grid
# You will need to research how the enumerate function works
# Use the enumerate funtion on your grid to determine a column from a 2D grid
# Convert the values to a list, which can be converted to a numpy array
for j, i in enumerate(grid): # this is a loop that counts the rows and gives it a sequence value
   print "row id "+ str(j) + " values:", i #prints row number id the new value and then row. 