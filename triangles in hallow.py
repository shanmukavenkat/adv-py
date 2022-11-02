n = int(input()) 
for i in range(0,n):
    if i == 0: #first row
       print("* " * n)
    elif (i== n-1): #last row
        left_spaces = "  " * (n-1)
        print(left_spaces + "*")
       
    else:
        left_spaces = "  " * (i)          
        hollow_spaces = "  " * (n-i-2)
        print(left_spaces+"* " +hollow_spaces + "* " ) #left space, star, hollow space, star
