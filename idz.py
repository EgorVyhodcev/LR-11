#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from threading import Thread
from math import factorial, cos


eps = .0000001


def inf_sum(x, check, num):
    summa = 1
    i = 1
    prev = 0
    while abs(summa - prev) > eps:
        prev = summa
        summa += ((-1)**i * (x**(2*i))) / factorial(2*i)
        #print(summa)
        i += 1
    print(f"The sum number: {num} is: {summa}")
    print(f"Check: cos({x}) = {check}")


if __name__ == '__main__':
    checksum1 = cos(0)
    thread1 = Thread(target=inf_sum, args=(0, checksum1, 1))
    thread1.start()
    checksum2 = cos(3)
    thread2 = Thread(target=inf_sum, args=(3, checksum2, 2))
    thread2.start()
