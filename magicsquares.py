#I'll fix the global variables later..I know.

import random
import math
import json

#generates a triangle of square differences
def generate_triangle():
    global triangleslice
    global mylistsquared
    mylistofnumbers = list(range(1,2000))
    mylistsquared = [i**2 for i in mylistofnumbers]
    triangle = []
    for j in range(len(mylistsquared)-1):
        for k in range(j):
            triangle.append(mylistsquared[j] - mylistsquared[k])
    triangleslice = triangle[len(triangle)//2:]


    
#saves the list of numbers that don't generate arithmetic progressions
#(bad numbers) to a file
#bad and naughty numbers get put in the badnums list
def save_badnums():
    with open("badnums.json","w") as file1:
        json.dump(badnums,file1)
    return True

#loads the "bad numbers"
def load_badnums():
    global badnums
    with open("badnums.json","r") as file1:
        badnums = json.load(file1)
    return badnums

#searches the triangle slice for numbers that generate arithmetic progressions  
def searchtriangle(badnums):
    global randnum
    global count
    rows = []
    cols = []
    #randnum = 3360
    #randnum = 138600
    randnum = 0
    #Take repeats out of badnums list
    badnums = list(set(badnums))
    #picks a random number from the list
    #makes sure it's not a "bad number"
    while randnum in badnums:
        randnum = random.choice(triangleslice)
    #Determines how many times it's in the list
    count = triangleslice.count(randnum)
    #find the two numbers subtracted to give you randnum at each occurrence
    for n in mylistsquared:
        for m in mylistsquared:
            if m - n == randnum:
                rows.append(m)
                cols.append(n)
    return rows,cols

#Finds arithmetic progressions..
def find_progression(rows,cols):
   x = 0
   prog1 = []
   prog2 = []
   emptytup = tuple()
   for r in rows:
       for l1 in range(len(rows)):
            for c in cols:
                for l2 in range(len(cols)):
                    #if row shares a value with a column:
                   if math.sqrt(r) == math.sqrt(c):
                        p1 = cols[l1-1]
                        p2 = cols[l2-1]
                        p3 = rows[l2-1]
                        if p3 - p2 == p2 - p1 and x == 0:
                            x = x+1
                            prog1 = [p1,p2,p3]
                        elif p3-p2 == p2-p1 and x == 1:
                            x = x+1
                            prog2 = [p1,p2,p3]
                            return prog1,prog2
   #If there's no progressions found, append the number chosen to
    #the "bad numbers" list, and return false
   if len(prog1) < 3 or len(prog2) < 3:
      badnums.append(randnum)
      return emptytup

#Generates a square using the arithmetic progressions.
def generate_square(prog1,prog2):
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

    e = (d+f)/2

    matrix = [
              [a,b,c],
              [d,e,f],
              [g,h,i]
                         ]
    #multiply everything by 4 so everything's an int
    matrix = [[int(j*4)for j in i] for i in matrix]
    #Now solve for the diagonals
    Sum = matrix[1][0]+matrix[1][1]+matrix[1][2]
    matrix[0][0] = Sum - matrix[0][1] - matrix[0][2]
    matrix[2][2] = Sum - matrix[2][1] - matrix[2][0]
    return matrix

#generate another square
#rearrange the progressions
def generate_square2(prog1,prog2):
    global matrix2
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
    i = prog2[0]
    a = prog2[2]
    e = prog2[1]
    
    matrix2 = [
              [a,b,c],
              [d,e,f],
              [g,h,i]
                         ]
    Sum = matrix2[0][0]+matrix2[1][1]+matrix2[2][2]
    matrix2[0][1] = Sum - matrix2[0][0]-matrix2[0][2]
    matrix2[1][2] = Sum - matrix2[1][1] - matrix2[1][0]
    matrix2[2][0] = Sum - matrix2[2][1] - matrix2[2][2]
    return matrix2

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
        
#same as above, doesn't print anything tho 
def howmanysquarenoprint(matrix):
    numtrue = 0
    for i in matrix:
        for j in i:
            if is_square(j):
                numtrue = numtrue + 1
    return numtrue

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

#here's the main.
def main():
    square = False
    generate_triangle()
    load_badnums()
    while square == False:
        rows,cols = searchtriangle(badnums)
        tup = find_progression(rows,cols)
        if tup != tuple():
            prog1 = tup[0]
            prog2 = tup[1]
            prog1,prog2 = find_progression(rows,cols)
            print()
            print("Arithmetic progressions found:")
            print(prog1,prog2)
            print()
            print("---------------------------------------")
            print()
            print()
            print_square(generate_square(prog1,prog2))
            print()
            print("How many are squares?")
            print()
            howmanysquare(generate_square(prog1,prog2))
            print()
            print("Is it magic?")
            print(is_magic(matrix))
            print()
            print_square(generate_square2(prog1,prog2))
            print()
            print("How many are squares?")
            print()
            howmanysquare(generate_square2(prog1,prog2))
            print()
            print("Is it magic?")
            print(is_magic(matrix2))
            square = True
            save_badnums()
#I'll add the if name == main stuff later
main()
