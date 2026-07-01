# End to start while loop
start = int(input("Enter Start : "))
end = int(input("Enter End : "))

i = start

while i >= end:
    print(i, end=" ")
    i -= 1
