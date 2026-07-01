"""
Q4: A student scored marks in 3 subjects. Take all three as input,
calculate the total and average, and print both using an f-string.
"""

physics = int(input("Enter marks Physics:"))
Chemistry = int(input("Enter marks Chemistry:"))
maths = int(input("Enter marks Maths:"))
total=physics+Chemistry+maths
avg=total/3
print(f"Total marks:{total}")
print(f"Average:{avg}")
