def is_prime(s_n):
    for i in range(0, 1000):
        if s_n % 2 == 0 and s_n != 2:
            return False
        if s_n == 0 or s_n == 1:
            return False
        return True

s_n = int(input('enter some number from "0" for "1000" ' ))
print(is_prime(s_n))
