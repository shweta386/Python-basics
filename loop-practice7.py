"""
Print all the numbers which are divisible by 3 and 5, from 1 to 100.
"""

start = int(input("Enter the start num:"))
end = int(input("Enter the end num:"))
i = start
while i <= end:
    if i % 3 == 0 and i % 4 == 0:
        print(i)
    i += 1
