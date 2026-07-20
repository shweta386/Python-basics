"""
Write a function that ask a number from user and prints if that
number is odd or even.
"""


def odd():
    num = int(input("Enter the number:"))
    # for i in range(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")


odd()
