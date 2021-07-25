#Modul to make geometry object 2d
#Which have feature to prints = 
#1. Square 
#2. Rectangle 
#3. Right triangle
#4. Equilateral traingle

#function to print square object
def printSquare (side):
    for i in range(side):
        #To print loop star without a newline
        print("* "*side)

#function to print rectangle object 
def printRectangle (height, length):
    for i in range(height):
        print("* "*length)

#function to print right triangle object 
def printRightTriangle(height):
    for i in range(1,height+1):
        print("* "*i)

#function to print equilateral triangle object 
def printEquilateralTriangle(height):
    space = height
    for i in range(1, height+1):
        print(" "*space, end=" ")
        print("* "*i)
        space-=1