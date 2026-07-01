# print start to end user input using loop
start = int(input("Enter Start : "))
end = int(input("Enter End : "))
i = start
while i <= end:
    print(i, end=" ")
    i += 1
print(f"the start value is {start} and value is {end}")
