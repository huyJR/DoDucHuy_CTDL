# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 14:41:21 2023

@author: OS
"""
"""
# Selection Sort
def selectionsort(A):# tạo function selctionsort với đối số truyền tham chiếu là mảng A
    n=len(A) # lưu kích thước của mảng A vào biến n
    print(n)
    for i in range(n-1): # vòng lặp for đầu tiên duyệt mảng đến n-1
        position = i  # đặt vị trí là i 
        for j in range(i+1,n): # dùng vong lặp for để 
            if A[j] <A[position]:# nếu vị trí thứ position lớn hơn vị trí thứ j thì ta hoán đổi vị trí
                position=j
        temp=A[i]           # 3 lệnh tiếp theo là hoán đổi 2 vị trí với nhau 
        A[i]=A[position]
        A[position]=temp
        
A=[3,5,8,9,2,4]
print("Orginal Array:", A)
s=selectionsort(A)
print("Sorted Array:",A)"""
""" 
# Insertion Sort   
def insertionsort(A): # tạo Function sắp xếp array
    n=len(A)    # lưu kích thước vào n 
    for i in range(1,n): # dùng vong lặp for để duyệt array từ 1 đến n
        cvalue = A[i] # lưu giá trị thứ i là cvalue, vòng lặp đầu tiên i=5
        position = i # lưu vị trí thứ i là posittion
        while position > 0 and A[position-1]>cvalue: # điều kiện nếu giá trị sau nó lớn hơn giá trị tại position
            A[position] = A[position -1] # đổi giá trị position hiện với giá trị giá trị sau nó
            position = position -1 # lùi position về 1 
        A[position] = cvalue # cho giá trị position bằng giá trị cvalue
        
A=[3,5,8,9,2,4]
print("Orginal Array:", A)
insertionsort(A)
print("Sorted Array:", A)"""

"""
#Bubble Sort 
def bubblesort(A):# tạo function sắp xếp array bằng bubble ( nghĩa là từ cuối lên) 
        n=len(A) # kích thước của array đc lưu vào biến n
        for passes in range(n-1,0,-1): # vòng lặp for bắt đầu từ n-1 giảm về 0  
            for i in  range(passes):# vòng lặp for cho passes
                if A[i]>A[i+1]: # nếu vị trí hiện tại lớn hơn vị trí kế nó thì thực hiện đổi vị trí 
                    temp = A[i]# đặt biến tạm lưu giá trị tại i
                    A[i]=A[i+1] # đổi giá trị cho nhau 
                    A[i+1]=temp # giá trị ban đầu i đc gán vào i+1

A=[3,5,8,9,2,4]
print("Orginal Array:", A)
bubblesort(A)
print("Sorted Array:", A)"""

"""
#Shell Sort 
def shellsort(A): # tạo function sắp xếp array 
    n = len(A) # kích thước của mảng A được lưu vào n 
    gap = n // 2 # tạo biến gap bằng kích thước chia doi 
    while gap > 0:
        for i in range(gap, n):
            temp = A[i]
            j = i
            while j >= gap and A[j - gap] > temp:
                A[j] = A[j - gap]
                j -= gap
            A[j] = temp
        gap //= 2
       
A=[3,5,8,9,2,4]
print("Orginal Array:", A)
shellsort(A)
print("Sorted Array:", A)"""

#Merge Sort 
def mergesort(A,left,right):
    if left <right:
        mid =(left+right)//2
        mergesort(A, left, mid)
        mergesort(A, mid+1,right)
        merge(A,left,mid,right)

def merge(A,left,mid,right):
    i = left 
    j=mid+1
    k=left
    B=[0]*(right+1)
    while i<= mid and j<=right:
        if A[i] < A[j]:
            B[k] =A[i]
            i+=1
        else:
            B[k] = A[j]
            j+=1
        k+=1
    while i<=mid: 
        B[k] = A[i] 
        i+=1
        k+=1
    while j<=right:
        B[k]=A[j]
        j+=1
        k+=1
    for x in range(left, right +1):
        A[x] = B[x] 

A=[3,5,8,9,2,4]
print("Orginal Array:", A)
mergesort(A,0,len(A)-1)
print("Sorted Array:", A)        

"""
#Quick Sort 
def quicksort(A,low,high):
    if low <high:
        pi=partition(A,low ,high)
        quicksort(A, low, pi-1)
        quicksort(A, pi+1, high)
        
def partition(A,low,high):
    pivot = A[low]
    i= low+1
    j=high 
    while True:
        while i<=j and A[i]<=pivot:
            i=i+1
        while i<=j and A[j]>pivot:
            j=j-1
        if i <=j:
            A[i],A[j] =A[j],A[i]
        else:
            break
    A[low],A[j] = A[j],A[low]
    return j

A=[3,5,8,9,2,4]
print("Orginal Array:", A)
quicksort(A, 0,len(A)-1)
print("Sorted Array:", A)"""

"""
#Count Sort 
def countsort(A):
    n=len(A)
    maxsize = max(A)
    carray = [0]*(maxsize +1) 
    for i in range(n):
        carray[A[i]] = carray[A[i]]+1
    i=0
    j=0
    while i< maxsize +1:
        if carray[i] >0:
            A[j] = i 
            j+=1
            carray[i] = carray[i] -1 
        else:
            i+=1
            
A=[3,5,8,9,2,4]
print("Orginal Array:", A)
countsort(A)
print("Sorted Array:", A)"""

"""
#Radix Sort 
def radixsort(A):
    n=len(A) 
    maxelement = max(A)
    digits = len(str(maxelement))
    l=[]
    bins=[l]*10
    for i in range(digits):
        for j in range(n):
            e=int((A[j]/pow(10,i))%10)
            if len(bins[e])>0:
                bins[e].append(A[j])
            else:
                bins[e] = [A[j]] 
        k=0
        for x in range(10):
            if len(bins[x]) >0 :
                for y in range(len(bins[x])):
                    A[k] = bins[x].pop(0)
                    k+=1
                    
A=[63, 764,812,514,27,98]
print("Orginal Array:", A)
radixsort(A)
print("Sorted Array:", A)"""
            



