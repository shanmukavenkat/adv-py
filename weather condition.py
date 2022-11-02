a=int(input("enter weather conditions:"))
if a<0:
    print("Freezing weather")
elif 0<=a<10:
    print("Very Cold weather")
elif 10<=a<20:
    print("Cold weather")
elif 20<=a<30:
    print("Normal")
elif 30<=a<40:
    print("Hot")
elif a>=40:
    print("Very Hot")

