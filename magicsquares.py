import random
import math
import json


#creates a triangle of square differences and saves it to a file
def generate_triangle():
    global otherlist
    mylistofnumbers = list(range(1,1000))
    mylistsquared = [i**2 for i in mylistofnumbers]
    otherlist = []
    for j in range(len(mylistsquared)-1):
        for k in range(j):
            otherlist.append(mylistsquared[j] - mylistsquared[k])
    with open("triangle.json","w") as file:
        json.dump(otherlist, file)

#loads the previous triangle instead of creating a new one
def load_previous():
    global otherlist
    with open("triangle.json","r") as file:
        otherlist = json.load(file)

#saves the list of numbers that don't generate arithmetic progressions
    #(bad numbers) to a file
def save_badnums():
    with open("badnums.json","w") as file1:
        json.dump(badnums,file1)
    return True

#loads the "bad numbers"
def load_badnums():
    global badnums
    with open("badnums.json") as file1:
        badnums = json.load(file1)
    return badnums

#searches the triangle for numbers that generate arithmetic progressions  
def searchtriangle(badnums):
    global rows
    global cols
    global num1
    global num2
    global randnum
    global count
    rows = []
    cols = []
    num1 = []
    num2 = []
    randnum = 0
    
    #picks a random number from the list
    #makes sure it's not a "bad number"
    #Take repeats out of badnums list
    badnums = list(dict.fromkeys(badnums))
    while randnum in badnums:
        randnum = random.choice(otherlist)
    #determines how many times it is in the list
    count = otherlist.count(randnum)
    #determines the row, column of the number
    #as well as the two numbers subtracted at that point to get that number
    for i, x in enumerate(otherlist):
        if x == randnum:
            i = i+1
            row = (int(math.sqrt(i*8)-1))//2
            col = i - (row*(row+1))//2-1
            col1 = col+1
            row2 = row+2
            num_1 = row2*row2
            num_2 = col1*col1
            rows.append(row2)
            cols.append(col1)
            num1.append(num_1)
            num2.append(num_2)

#Finds arithmetic progressions..
def find_progression():
   global prog1
   global prog2
   x = 0
   prog1 = []
   prog2  = []
   for i in rows:
       for k in range(len(rows)):
            for j in cols:
                for l in range(len(cols)):
                    if i == j:
                        p1 = num2[k-1]
                        p2 = num2[l-1]
                        p3 = num1[l-1]
                        if p3 - p2 == p2 - p1 and x == 0:
                            x = x + 1
                            prog1 = [p1,p2,p3]
                        elif p3-p2 == p2-p1 and x == 1:
                            x = x+1
                            prog2 = [p1,p2,p3]
                            return True
   #If there's no progressions found, append the number chosen to
    #the "bad numbers" list, and return false
   if prog1 == [] and prog2 ==[]:
       badnums.append(randnum)
       return False

#Generates a square using the arithmetic progressions.
def generate_square():
    global matrix
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    i = 0

    c = prog1[1]
    d = prog1[0]
    h = prog1[2]
    b = prog2[0]
    f = prog2[2]
    g = prog2[1]
    
    matrix = [
              [a,b,c],
              [d,e,f],
              [g,h,i]
                         ]
    #multiply everything by 4 so everything's an int
    matrix = [[int(j*4)for j in i] for i in matrix]
    #Now solve for the diagonals
    Sum = 0
    for i in range(0, 3):  
        for j in range(0, 3):  
            Sum += matrix[i][j]  
    Sum = Sum//2
  
    for i in range(0, 3):  
        rowSum = 0
        for j in range(0, 3):  
            rowSum += matrix[i][j]  
        matrix[i][i] = Sum - rowSum
    return matrix

#Prints it out   
def print_square(matrix):
    for i in range(0, 3):  
        for j in range(0, 3):  
            print(matrix[i][j], end = " ")  
        print()

#Determines whether a singular number is square     
def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

#Checks to see how many of the numbers in the square are square numbers
#Uses the above function is_square
def howmanysquare(matrix):
    for i in matrix:
        for j in i:
            print(is_square(j), end=' ')
        print()
        
#Checks to see if it's a magic square 
def is_magic(mat):
    N = 3
    s = 0 
    for i in range(0, N) : 
        s = s + mat[i][i]
    s2 = 0
    for i in range(0, N) : 
        s2 = s2 + mat[i][N-i-1] 
    if(s!=s2) : 
        return False 
    for i in range(0, N) : 
        rowSum = 0;      
        for j in range(0, N) : 
            rowSum += mat[i][j] 
        if (rowSum != s) : 
            return False 
    for i in range(0, N): 
        colSum = 0
        for j in range(0, N) : 
            colSum += mat[j][i] 
        if (s != colSum) : 
            return False
    return True

#Some user-friendliness
def choose_options():
    global choice
    global choice1
    print("Do you want to generate a new triangle of square differences")
    print("to search from, or use previous one?")
    print("1. Generate new    2. Load previous")
    choice = input(">>> ")

#here's the main.
def main():
    square = False
    choose_options()
    if int(choice) == 1:
        generate_triangle()
    else:
        load_previous()
    badnums = load_badnums()
    while square == False:
        searchtriangle(badnums)
        if find_progression() == True:
            find_progression()
            print()
            print("Arithmetic progressions found:")
            print(prog1)
            print(prog2)
            print()
            print("---------------------------------------")
            print()
            print_square(generate_square())
            print()
            print("How many are squares?")
            print()
            howmanysquare(generate_square())
            print()
            print("Is it magic?")
            print(is_magic(matrix))
            square = True
            save_badnums()
            
#I'll add the if name == main stuff later
main()
