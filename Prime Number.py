a = int(input("Enter the number to check \n"))
if a > 1:
    for x in range(2,a):
        if (a % x) == 0:
            print("{} is not a prime number".format(a))
            break
    else:
        print("{} is a prime number".format(a))
else:
    print("not a prime number")
   