# Magic-Squares
A python 3 program to generate magic squares with square numbers in them. 

This program finds 3x3 magic squares with perfect square numbers in them, in hopes of finding
the elusive 3x3 magic square of perfect squares. 

# The algorithm:
- Generate a triangle of square differences. 

- Pick a random number known to be in the triangle.

- Determine how many times it appears.

- Find each row and column for every time it appears.

- Determine if two values are shared between the row and columns.

- If so, generate two arithmetic progressions of square numbers.

- Plug these progressions into the magic square matrix, and solve for the diagonals

# Problems:
  
- Slow

- ~~Generates a new triangle every time~~ FIXED

- Only finds two arithmetic progressions for every compatible number when more can be found

- Only uses two arithmetic progressions to generate a square, and doesn't rearrange the progressions to try new
combinations

- ~~Chooses a random number each time, doesn't have a list saved of random numbers known to not work~~ FIXED


I will work on fixing the above problems....


# If you want to use this yourself:

Have Python 3 installed on your system, and make sure you have the json module installed.
Create a file, anywhere, and place the .py and two .json files in there.
Run the .py file
