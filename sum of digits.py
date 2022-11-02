a=int(input())
k=str(a)
if len(k)==1:
    print(int(k[0]))
elif len(k)<=2:
    print((int(k[0])+(int(k[1]))))
elif len(k)<=3:
    print((int(k[0])+(int(k[1])+(int(k[2])))))
elif len(k)<=4:
    print((int(k[0])+(int(k[1])+(int(k[2])+(int(k[3]))))))
elif a==10000:
    print("end")
