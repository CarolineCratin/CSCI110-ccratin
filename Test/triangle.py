# Write a program that prints out what type of triangle the input lengths form. 
# For example:
# 1, 1, 1 forms an equilateral triangle
# 2, 3, 4 forms a scalene triangle
# 1, 1, 3 cannot form a triangle
# 1, 3, 3 forms a isosoles triangle
# 3, 4, 5 forms a right scalene triangle

import math
import sys

def triangle_checker(len1, len2, len3):
    # print if the triangle is scalene/isosoles/equilateral and if it's right
    if len1 == len2 == len3:
        print("this is a equilateral triangle")
    elif len1 == len2 or len2 == len3 or len1 == len3:
        print("this is a isosoles triangle")
    elif len3^2 == len1*len1 + len2*len2:
        print("this is a right scalene triangle")
    else:
        print("fuk")
    print("One day I will solve this triangle business.")

def main():
    len1 = int(sys.argv[1])
    len2 = int(sys.argv[2])
    len3 = int(sys.argv[3])
    triangle_checker(len1, len2, len3)

if __name__ == "__main__":
    main()