import datetime
now = datetime.datetime.now()
your_birth = input("Enter your birth date in the format YYYY-MM-DD: ")
b_y = int(your_birth[:4])
b_m = int(your_birth[5:7])
b_d= int (your_birth[-2:])

y_y = now.year - b_y
y_m = now.month - b_m
y_d = abs(now.day - b_d)

if y_m < 0:
    y_m+=12
    y_y-=1
print(f'Your age is {y_y} old, {y_m} months and {y_d} days.') 
