for num in range(30, 300):
    if num % 7 == 0:
        print ("abc")
    elif num % 13 == 0:
        print ("xyz")
    elif num % 13 == 0 and num % 7 == 0:
        print ("a-z")
    else:
        print (num)

