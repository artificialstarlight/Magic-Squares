import random
import math
def generate_triangle():
    global otherlist
    mylistofnumbers = list(range(1,1000))
    mylistsquared = [i**2 for i in mylistofnumbers]
    otherlist = []
    for j in range(len(mylistsquared)-1):
        for k in range(j):
            otherlist.append(mylistsquared[j] - mylistsquared[k])
            
def searchtriangle():
    global rows
    global cols
    global num1
    global num2
    rows = []
    cols = []
    num1 = []
    num2 = []
    #picks a random number from the list
    #for i in otherlist:
    randnum = random.choice(otherlist)
    #randnum = 3360
    #determines how many times it is in the list
    count = otherlist.count(randnum)
    print("The number " + str(randnum) + " was found " + str(count) + " times in the triangle")
    print("Col: Row: The two numbers subtracted to get " + str(randnum) + " at these coordinates:")
    print("---------------------------------------")
    for i, x in enumerate(otherlist):
        if x == randnum:
            i = i+1
            row = (int(math.sqrt(i*8)-1))//2
            col = i - (row*(row+1))//2-1
            col1 = col+1
            row2 = row+2
            num_1 = row2*row2
            num_2 = col1*col1
            print(col1,row2," ",num_1,num_2)
            rows.append(row2)
            cols.append(col1)
            num1.append(num_1)
            num2.append(num_2)

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
                            print()
                            print("Arithmetic progressions found:")
                            print(prog1)
                            print(prog2)
                            print()
                            return True
   if prog1 == [] and prog2 ==[]:
       print("No two arithmetic progressions could be found.")
       return False

def generate_square():
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
    matrix = [[int(j*4)for j in i] for i in matrix]
    
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
    
def print_square(matrix):
    for i in range(0, 3):  
        for j in range(0, 3):  
            print(matrix[i][j], end = " ")  
        print()
        
def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

def howmanysquare(matrix):
    for i in matrix:
        for j in i:
            print(is_square(j), end=' ')
        print() 

def main():
    square = False
    while square == False:
        generate_triangle()
        searchtriangle()
        if find_progression() == True:
            find_progression()
            print_square(generate_square())
            print()
            print("How many are squares?")
            howmanysquare(generate_square())
            square = True
main()
