# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 02:03:02 2023

@author: OS
"""

# bai 1 tính giai thua bang de quy 
"""def tinhgiaithua(x):
    if(x==0 or x==1):
        return 1
    else:
        return x*tinhgiaithua(x-1)

gt=int(input("nhập vào số cần tính : "))
print(gt)

result=tinhgiaithua(gt)
print("giai thua cua ", gt," là" , result)"""

# bai2 fibonacci
"""def fibonacci(n):
    if n<=0 :
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
a=int(input("nhap vao so can tinh fibonacci:"))
kq=fibonacci(a)

print("tong so fibonacci là:", kq)"""

#bai 3 interview 1: tính f(n)=n%10+f(n/10)
"""def tinhtong(n):
    if n==0:
        return 0
    else:
        return n%10 + tinhtong(int(n//10))
    

a=int(input("nhap vao so can tinh:"))
kq=tinhtong(a)
print("so can tinh la",kq)"""
#bai 3 interview 2 : tính ươc chung lơn nhat cua 2 so 
"""import math 

a=48 
b=18 

result_gcd= math.gcd(a,b)
print("ươc chung lơn nhat của :", a, " và", b, "la", result_gcd)
    #cách 2
print("cách 2")
result_gcd2=math.gcd(b,a%b)
print("ươc chung lơn nhat của :", a, " và", b, "la", result_gcd)"""

#bai3 interview 4 : tính f(n)= n%2 + 10*f(n/2) chuyển từ hệ 10 sang nhị phân 

def transfer_nhiphan(n):
    if n==0:
        return 0
    else:
        return n%2 + 10*transfer_nhiphan(n//2)
    
a=int(input("nhap vào so can tinh"))
kq=transfer_nhiphan(a)
print(" so can tinh la:", kq)






