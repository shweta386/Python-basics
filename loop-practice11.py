"""
Ask a number from the user, and count all the factors.

Enter a number = 10
4

Enter a number = 100
9
"""

num = int(input("Enter a number="))
i = 1
count = 0
while i <= num:
    if num % i == 0:
        count = count + 1
        # print(count)
        print(i)
    i += 1
print(f"total={count}")