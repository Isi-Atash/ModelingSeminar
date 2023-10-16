import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

hs = int(input())
ms = int(input())
lines = []

for i in range(hs):
    row = input()
    lines.append(row)

# Initialize empty matrices for header and input
header_matrix = []
input_matrix = []

# Create the header matrix from the input
for line in lines:
    header = [ord(char) for char in line[:hs]]
    header_matrix.append(header)
    input_values = [ord(char) for char in line[hs:]]
    input_matrix.append(input_values)

# Print the header and input matrices separately
for header_row, input_row in zip(header_matrix, input_matrix):
    print(f"{header_row} {input_row}")


