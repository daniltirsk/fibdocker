import sys

def findFib(n):
    if n<0:
        print("Incorrect input")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return findFib(n-1)+findFib(n-2)

print(findFib(int(sys.argv[1])))
