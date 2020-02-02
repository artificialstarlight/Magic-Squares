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

- Plug these progressions into the magic square matrix, and solve for the diagonals.


