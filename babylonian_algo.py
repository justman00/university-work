import random
import math


def bab_sqrt(num):
    num_len = len(str(num)) // 2
    x0 = random.randint(pow(10, num_len), 3 * pow(10, num_len))

    x1 = (x0 + num / x0) / 2

    def helper(xn):
        xn1 = (xn + num / xn) / 2

        if(xn == xn1):
            return xn
        else:
            return helper(xn1)

    return round(helper(x1), 2)


print(bab_sqrt(9))
