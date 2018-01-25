# calculates greatest common divisor


def users_gcd(a, b):
    while (b):
        a,b= b, a%b
    return a

# test
# print users_gcd(77,21)

