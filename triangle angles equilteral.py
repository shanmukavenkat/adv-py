a=int(input())
b=int(input())
c=int(input())
if a==b and b==a:
    print("Equilateral")
elif a!=b and b!=a and c!=a and c!=b:
    print("Scalene")
elif a==c and a!=b:
    print("Isosceles")

