#!/usr/bin/env python3

def print_fibonacci(length):
    fib=[0,1]
    for i in range(2,length):
        fib.append(fib[i-1]+fib[i-2])
    print(fib)
       

print_fibonacci(9)