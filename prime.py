import math

def prime(n):
    if n==1:
        return False
    right_bound = int(math.sqrt(n))
    for i in range(2,right_bound+1):
        if n%i == 0:
            return False
    return True

if __name__ == "__main__":
    for n in range(1,20):
        if prime(n):
            print(n, end=' ')