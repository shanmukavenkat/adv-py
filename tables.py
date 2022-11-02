n=int(input())
count=1
for i in range(1,11):
    t=str(i)
    count=n*i
    count=str(count)
    table=(str(n) + " X " + t +  " = "+ count)
    print(table)
