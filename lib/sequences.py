#!/usr/bin/env python3

def print_fibonacci(length):
    fib=[0,1]
    while length !=0 and length>0:
        for i in range(2,length):
            fib.append(fib[i-1]+fib[i-2])
        print(fib)
    print('Empty list')
       

print_fibonacci(0)