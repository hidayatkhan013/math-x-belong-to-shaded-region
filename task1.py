import math
try:
    x=float(input("Enter value of x : "))
except:
  print("X must be Number")
else:
    y=math.pow(x,5)*math.sqrt(abs(x-1))+abs(25-pow(x,5))
    print(f"x= {x} and y={y}")