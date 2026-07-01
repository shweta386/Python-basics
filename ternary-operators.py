# normal way
age=int(input("Enter age:"))
if age<=18:
    status="minor"
else:
    status="adult"
# shorten way

status = "minor" if age<=18 else "adult"
print(status)