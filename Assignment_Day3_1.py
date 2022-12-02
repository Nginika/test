# ask the pilot what his current altitude is
current_alt = int(input("What is your current altitude (ft)? - "))
if current_alt > 10000:
    print("you should go around")
elif (current_alt > 5000) & (current_alt < 10000):
    print("Bring the plane to a thousand ft and then land the plane")
else:
    print("Land the plane safely at a thousand ft")
