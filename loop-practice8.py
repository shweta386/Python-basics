# Sum of all the numbers from 1 to 100.
start = int(input("Enter the start num:"))
end = int(input("Enter the end num:"))
i = start
total = 0
while i <= end:
    total = total + i
    i += 1
print(f"sum are {total}")
