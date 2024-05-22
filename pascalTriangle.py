'''for x in range(5):
    if x == 0:
        print("     1")
    elif x == 1:
        print("    1  1")
    elif x == 2:
        print("   1 2 1")
    elif x == 3:
        print("  1 3 3 1")
    elif x == 4:
        print(" 1 4 6 4 1")
    elif x == 5:
        print("1 5 10 10 5 1")

'''

#n!/((n-r)!r!)

from math import factorial


#loop through each row
for i in range(6):
    #this loop will create the space
    for j in range(5-i+1):
        print(end=" ")
    #inside a particular loop, create another loop that will create the number of element
    for k in range(i + 1):
        sol = factorial(i)/(factorial(i-k)* factorial(k))
        print(int(sol), end=" ")
    print()








 