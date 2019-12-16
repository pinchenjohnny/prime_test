import random as rand
import Eratosthenes as eratos

def Btest(a, n):
    # 测试a是否属于B(n)
    # a,n由MillRab()传进来，a从2..n-2中随机出，n是大于4的奇数
    
    # 初始s,t, n-1=(2^s)t
    s = 0
    t = n-1
    # 求s,t
    while t % 2 == 1:
        s += 1
        t /= 2
    # t现在为奇，且n-1=(2^s)t仍成立

    # 判断a是否属于B(n)
    x = a**t % n
    if x == 1 or x == n-1: # 条件（1），条件（2）i=0
        return True
    # 条件（2）i=1..(s-1)
    for i in range(1, s):
        x = x*x % n # 每个i不用重新计算x^(2i)，并且i很大时，不会溢出
        if x == n-1:
            return True
    # 条件（1）（2）都不满足
    return False

def MillRab(n):
    # n < 4时
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    # n为偶数时
    if n % 2 == 0:
        return False
    # n为大于4的奇数
    a = rand.randint(2, n-2)
    return Btest(a, n)

if __name__ == "__main__":
    ns = 100
    millrab_prime = set()
    millrab_prime_nums = 0
    for n in range(ns):
        if MillRab(n):
            millrab_prime.add(n)
            millrab_prime_nums += 1

    eratos_prime = [None]*ns
    eratos_prime_nums = eratos.Eratosthenes(ns, eratos_prime)
    eratos_prime = set(eratos_prime)
    eratos_prime.discard(None)
    
    # print(millrab_prime)
    # print(eratos_prime)
    # millrab会误判强伪素数，故millrab_prime在eratos_prime基础上，多了误判的强伪素数
    diff = millrab_prime.difference(eratos_prime)
    print(f'num of MillRab false primes: {len(diff)}')
    print(diff)