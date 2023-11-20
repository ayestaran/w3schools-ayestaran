total = 0
print()
for count in range(1,5):
    base = 8
    height = 3
    x = (base * height)/2
    print ("total: " + str(total))
    print ("count: " + str(count))
    print ("base: " + str(base))
    print ("height: " + str(height))
    print ("x: " + str(x))
    print ("output: " + str(total/3))
    print()
    if count < 4:
    	total = total + x
result = total/3
print ("result: " + str(result))
