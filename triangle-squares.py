import math
from itertools import count, islice, combinations
import time
import itertools

def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(math.sqrt(n)-1)))

def prime_pairs(x):
    factorlist=[]
    loop=2
    returnlist = []
    while loop<=x:
        if x%loop==0:
            x/=loop
            factorlist.append(loop)
        else:
            loop+=1
            #return factorlist
    for L in range(1, len(factorlist)+1):
             for subset in set(itertools.combinations(factorlist,L)):
                 returnlist.append(subset)
    return returnlist

def divisors(n):
    ds = []
    for x in range (1, n+1):
        if (n % x) == 0:
            ds.append(x)
    return ds

def repeats(l1):
    seen = {}
    dupes = []
    for x in a:
        if x not in seen:
            seen[x] = 1
        else:
            if seen[x] == 1:
                dupes.append(x)
            seen[x] += 1
    return seen

def prod_tuple(val) : 
    res = 1 
    for ele in val: 
        res *= ele 
    return res  

def least_efficient_triangle(n,maxcol):
    columns = []
    rows = []
    r = int(math.sqrt(n + 1))
    for r in range(maxcol+1,0,-1):
        for c in range(maxcol,0,-1):
            if (r**2)-(c**2) == n:
                columns.append(c)
                rows.append(r)
    return [columns,rows]

def poor_efficient_triangle(n,l1,combos):
    cols = []
    rows = []
    for i in combos:
        if i[0]**2 - i[1]**2 == n:
            rows.append(i[0])
            cols.append(i[1])
    return [cols,rows]
            
def triangle(n,maxcol):
    print("Generating triangle..")
    pairs = prime_pairs(n)
    if len(pairs) >= 2:
        crs = []
        results = []
        evens = []
        for p in pairs:
            if len(p) >= 2:
                res = prod_tuple(list(p))
                results.append(res)
        for r in results:
            if r % 2 == 0:
                evens.append(r)
        evens = sorted(evens)
        if len(evens) >= 2:
            differences = [j-i for i in evens for j in evens]
            for d in differences:    
               c = d // 2
               r2 = n + c**2
               r = int(math.sqrt(r2))
               if c > 0:
                   if r**2 - c**2 == n:
                       crs.append([c,r])
            crs = set(tuple(ele) for ele in crs)
            crs = sorted(list(crs))
            return crs
    return None     

def give_progressions(values,n):
    progs1 = []
    progs2 = []                                                                               
    columns = []
    rows = []
    for i in values:
        columns.append(i[0])
        rows.append(i[1])
    shared_values = set(columns) & set(rows)
    shared_values = list(shared_values)
    #if len(shared_values) >= 3:
    for x,s in enumerate(shared_values):
        r = (s**2)-n
        c = n+r
        c2 = n + (s**2)
        if x == len(shared_values)-2:
            progs1.append(r)
            progs1.append(c)
            progs1.append(c2)
        if x == len(shared_values)-1:
            progs2.append(r)
            progs2.append(c)
            progs2.append(c2)
    if len(progs1) == 3 and len(progs2) == 3:
        return [progs1,progs2]
    return False

    
def on_triangle(num):
    if num % 2 != 0:
        return True
    elif num % 4 == 0:
        return True
    elif is_prime(num):
        return True
    else:
        return False
        
def generate_square(prog1,prog2):
    print("Making the square..")
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
def generate_square2(prog2,prog1):
    print("Rearranging the square...")
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
    matrix2[0][1] = Sum - matrix2[0][0] - matrix2[0][2]
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
def is_square(num):
  return num == math.isqrt(num) ** 2

#Checks to see how many of the numbers in the square are square numbers
#Uses the above function is_square
def howmanysquare(matrix):
    for i in matrix:
        for j in i:
            try:
                print(is_square(j), end=' ')
            except ValueError:
                print("False",end = " ")
        print()
        
def num_squares(matrix):
    count = 0
    for i in matrix:
        for j in i:
            try:
                if is_square(j):
                    count = count + 1
            except ValueError:
                continue
    return count


def num_multiples(matrix):
    num_muls = 0
    num_non = 0
    for i in matrix:
        for j in i:
            for n in divisors(j):
                if math.sqrt(j/n).is_integer():
                    num_muls = num_muls + 1
                else:
                    num_nom = num_non + 1
    return num_muls

 
def is_magic(mat):
    print("Determining is this one is ~magical~")
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


def go_brr(n,values):
    print("Going brrr")
    num_instances = len(values)
    progs = give_progressions(values,n)
    if progs == False:
        return False
    print(progs)
    prog1 = progs[0]
    prog2 = progs[1]
    matrix1 = generate_square(prog1,prog2)
    matrix2 = generate_square2(prog1,prog2)
    return [matrix1,matrix2]




start = time.time()
for n in range(138601,1000000):
    if on_triangle(n):
        values = triangle(n,200000)
        if values != None:
            matricies = go_brr(n,values)
            if matricies != False:
                matrix1 = matricies[0]
                matrix2 = matricies[1]
                if num_squares(matrix1) >=7 or num_squares(matrix2) >=7:
                    if num_multiples(matrix1) != 54 and num_multiples(matrix2) != 54:
                        print("WE GOT A WINNER BOIS!!!")
                        print()
                        print_square(matrix1)
                        print()
                        print("How many square?")
                        print()
                        howmanysquare(matrix1)
                        print()
                        print("Is magic? " + str(is_magic(matrix1)))
                        print()
                        print_square(matrix2)
                        print()
                        print("How many square?")
                        print()
                        howmanysquare(matrix2)
                        print()
                        print("Is magic? " + str(is_magic(matrix2)))
                        break

end = time.time()
print("Done in " + str(end-start) + " seconds.")

"""values = triangle(138600,1000000)
matricies = go_brr(138600,values)
matrix1 = matricies[0]
matrix2 = matricies[1]
print()
print_square(matrix1)
print()
print("How many square?")
print()
howmanysquare(matrix1)
print()
print("Is magic? " + str(is_magic(matrix1)))
print()
print_square(matrix2)
print()
print("How many square?")
print()
howmanysquare(matrix2)
print()
print("Is magic? " + str(is_magic(matrix2)))"""
