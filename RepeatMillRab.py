import MillRab as mr
import Eratosthenes as eratos
import math

def RepeatMillRab(n, k):
    for i in range(1, k+1):
        if mr.MillRab(n) == False:
            return False # 一定是合数
    return True # 素数和强伪素数

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
        times = 10 # 每个n测试10次

        for time in range(times):
            millrab_prime = set()
            millrab_prime_nums = 0
            for i in range(2, n+1):
                k = int(math.log2(n)) # 重复次数
                if RepeatMillRab(n, k):
                    millrab_prime.add(n)

            eratos_prime = [None]*n
            prime_nums = eratos.Eratosthenes(n, eratos_prime)
            eratos_prime = set(eratos_prime)
            eratos_prime.discard(None)

            # millrab会误判强伪素数，故millrab_prime在eratos_prime基础上，多了误判的强伪素数
            diff = millrab_prime.difference(eratos_prime)
            error_rate += len(diff)/prime_nums
        
        error_rate /= 10
        print(f'{n}|{error_rate}')