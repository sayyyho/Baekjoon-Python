n, m = map(int, input().split())

def find_gcd_lcm(x, y):
    if x % y == 0: 
        print(y)
        print(n*m // y)
        return
    find_gcd_lcm(y, x % y)

find_gcd_lcm(n,m)

# import math

# a, b = map(int, input().split())

# print(math.gcd(a, b))
# print(math.lcm(a, b))