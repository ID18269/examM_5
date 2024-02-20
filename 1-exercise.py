n = input('insert number: ')
def prime_numbers(n):
    num = 2
    count = 0
    while count < n:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            yield num
            count += 1
        num += 1

n = 10
prime_gen = prime_numbers(n)

for prime in prime_gen:
    print(prime)

