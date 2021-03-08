try:
    x=float(input("Enter value of x : "))
    y=float(input("Enter value of y : "))
except:
    print("X Or Y must be Number")
else:
    # this is the eqution of line of shaded region you can find by two point formula
    temp=-(x+7)/7
    if x<=0 and y<=0 and y>=temp:
        print(f"Yes x= {x} and y={y} belong to Shaded region" )
    else:
        print(f"NO x= {x} and y={y} does not belong to Shaded region" )
