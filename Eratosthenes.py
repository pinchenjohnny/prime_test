def Eratosthenes(n, prime_list):
    is_prime = [True] * (n+1)
    count = 0
    for i in range(2, n+1):
        if is_prime[i] == True: #! key point
            prime_list[count] = i
            count += 1
            # filtering
            tmp = i
            while(tmp <= n):
                is_prime[tmp] = False
                tmp += i # mulitple of i
    return count

if __name__ == "__main__":
    n = 100
    prime_list = [None] * n
    prime_nums = Eratosthenes(n, prime_list)
    print(f'num of prime in 1..n: {prime_nums}')
    for i in range(prime_nums):
        print(prime_list[i], end=' ')