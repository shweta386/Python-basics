"""
Write a function called rectangle_area that takes length and breadth
as parameters and prints the area.
"""


def rectangle_area(length, breadth):
    area = length * breadth
    print("The area of the rectangel is ", area)


l = int(input("Enter the Leangth:"))
b = int(input("Enter the Breadth:"))
rectangle_area(l, b)
