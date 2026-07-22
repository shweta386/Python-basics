"""
Write a function called min_of_three that takes three numbers and returns
the smallest without using any built-in function.
"""
def min_of_three(n1,n2,n3):
    if n1<n2 and n1<n3:
        return n1
    elif n2<n1 and n2<n3:
        return n2
    else :
        return n3
n4=int(input("Enter the num1:"))
n5=int(input("Enter the num2:"))
n6=int(input("Enter the num3:"))
print(min_of_three(n4,n5,n6))