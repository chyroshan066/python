weight = int(input("Weight: "))
measurement = input("(K)g or (L)bs: ")

if measurement == "k" or measurement == "K":
    weight *= 2.2046226218
    print("Weight in Lbs: ", weight)
elif measurement == "l" or measurement == "L":
    weight /= 2.2046226218
    print("Weight in Kg: ", weight)