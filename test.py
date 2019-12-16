import random as rand
import math

# 确定算法


def Eratosthenes(n, prime_list):
    is_prime = [True] * (n+1)
    count = 0
    for i in range(2, n+1):
        if is_prime[i] == True:  # ! key point
            prime_list[count] = i
            count += 1
            # filtering
            tmp = i
            while(tmp <= n):
                is_prime[tmp] = False
                tmp += i  # mulitple of i
    return count

# 概率算法


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
    if x == 1 or x == n-1:  # 条件（1），条件（2）i=0
        return True
    # 条件（2）i=1..(s-1)
    for i in range(1, s):
        x = x*x % n  # 每个i不用重新计算x^(2i)，并且i很大时，不会溢出
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


def RepeatMillRab(n, k):
    for i in range(1, k+1):
        if MillRab(n) == False:
            return False  # 一定是合数
    return True  # 素数和强伪素数


if __name__ == "__main__":
    # n = 100..10000
    # RepeatMillRab()的出错概率
    n_list = [100]
    base = 1000
    for factor in range(1, 11):
        n_list.append(base*factor)

    print('n|error_rate')
    print('-|-')
    for n in n_list:
        # 每个n测试10次，error_rate取平均
        error_rate = 0
        times = 10  # 每个n测试10次

        for time in range(times):
            millrab_prime = set()
            millrab_prime_nums = 0
            for i in range(2, n+1):
                k = int(math.log2(n))  # 重复次数
                if RepeatMillRab(n, k):
                    millrab_prime.add(n)

            eratos_prime = [None]*n
            prime_nums = Eratosthenes(n, eratos_prime)
            eratos_prime = set(eratos_prime)
            eratos_prime.discard(None)

            # millrab会误判强伪素数，故millrab_prime在eratos_prime基础上，多了误判的强伪素数
            diff = millrab_prime.difference(eratos_prime)
            error_rate += len(diff)/prime_nums

        error_rate /= 10
        print(f'{n}|{error_rate}')
