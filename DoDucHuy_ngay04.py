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
def shellsort(A): # Định nghĩa hàm sắp xếp bằng thuật toán Shell Sort
    n = len(A) # Lấy kích thước của mảng A
    gap = n // 2 # Khởi tạo khoảng cách ban đầu bằng một nửa kích thước mảng
    while gap > 0: # Bắt đầu vòng lặp chính, dựa vào khoảng cách
        for i in range(gap, n): # Duyệt qua mảng từ vị trí gap đến cuối
            temp = A[i] # Lưu giá trị của phần tử tại vị trí i vào biến tạm thời
            j = i # Khởi tạo biến j bằng i
            while j >= gap and A[j - gap] > temp: # Kiểm tra và di chuyển phần tử trong khoảng cách
                A[j] = A[j - gap] # Di chuyển phần tử tại vị trí j - gap lên vị trí j
                j -= gap # Giảm giá trị của j đi khoảng cách
            A[j] = temp # Đặt giá trị tạm thời (temp) vào vị trí j sau khi tìm được vị trí đúng cho nó
        gap //= 2 # Giảm khoảng cách xuống một nửa để tiếp tục với khoảng cách nhỏ hơn

A = [3, 5, 8, 9, 2, 4] # Mảng đầu vào
print("Original Array:", A) # In ra mảng ban đầu
shellsort(A) # Gọi hàm sắp xếp Shell Sort
print("Sorted Array:", A) # In ra mảng sau khi sắp xếp
"""


"""
#Merge Sort 
def mergesort(A, left, right):
    if left < right:
        mid = (left + right) // 2  # Tìm phần tử giữa của mảng.
        mergesort(A, left, mid)     # Sắp xếp nửa trái của mảng.
        mergesort(A, mid + 1, right)  # Sắp xếp nửa phải của mảng.
        merge(A, left, mid, right)   # Trộn hai nửa đã sắp xếp lại với nhau.

def merge(A, left, mid, right):
    i = left
    j = mid + 1
    k = left
    B = [0] * (right + 1)  # Tạo một mảng tạm thời B để chứa kết quả trộn.
    while i <= mid and j <= right:
        if A[i] < A[j]:  # So sánh phần tử ở nửa trái và nửa phải.
            B[k] = A[i]  # Đặt giá trị của A[i] vào B[k] nếu A[i] nhỏ hơn A[j].
            i += 1
        else:
            B[k] = A[j]  # Đặt giá trị của A[j] vào B[k] nếu A[j] nhỏ hơn hoặc bằng A[i].
            j += 1
        k += 1
    while i <= mid:  # Sao chép phần tử còn lại từ nửa trái (nếu còn).
        B[k] = A[i]
        i += 1
        k += 1
    while j <= right:  # Sao chép phần tử còn lại từ nửa phải (nếu còn).
        B[k] = A[j]
        j += 1
        k += 1
    for x in range(left, right + 1):  # Sao chép mảng tạm thời B vào mảng gốc A.
        A[x] = B[x]

A = [3, 5, 8, 9, 2, 4]  # Mảng đầu vào
print("Original Array:", A)  # In ra mảng ban đầu
mergesort(A, 0, len(A) - 1)  # Gọi hàm sắp xếp Merge Sort
print("Sorted Array:", A)  # In ra mảng sau khi sắp xếp
Giải thích từng phần:

mergesort là hàm chính của thuật toán sắp xếp trộn. Nó thực hiện sắp xếp mảng A từ vị trí left đến right.
merge là hàm trộn hai mảng con đã sắp xếp (một nửa từ left đến mid và một nửa từ mid+1 đến right) lại với nhau để tạo một mảng đã sắp xếp.
Vòng lặp while trong hàm merge so sánh và trộn từng phần tử của hai mảng con thành mảng kết quả. Phần tử nào nhỏ hơn sẽ được đưa vào mảng kết quả.
Cuối cùng, sau khi mảng con đã trộn, chúng ta sao chép kết quả từ mảng tạm thời B vào mảng gốc A.
Cuối cùng, sau khi sắp xếp mảng A, bạn in ra mảng sau khi sắp xếp.

"""     

"""
#Quick Sort 
def quicksort(A, low, high):
    if low < high:
        pi = partition(A, low, high)  # Bước 1: Tìm pivot và đặt pivot vào vị trí đúng
        quicksort(A, low, pi - 1)  # Bước 2: Sắp xếp nửa trái của mảng
        quicksort(A, pi + 1, high)  # Bước 3: Sắp xếp nửa phải của mảng

def partition(A, low, high):
    pivot = A[low]  # Chọn pivot là phần tử đầu tiên trong mảng
    i = low + 1
    j = high
    while True:
        while i <= j and A[i] <= pivot:
            i += 1  # Di chuyển i sang phải cho đến khi gặp phần tử lớn hơn hoặc bằng pivot
        while i <= j and A[j] > pivot:
            j -= 1  # Di chuyển j sang trái cho đến khi gặp phần tử nhỏ hơn pivot
        if i <= j:
            A[i], A[j] = A[j], A[i]  # Swap hai phần tử nếu i <= j
        else:
            break  # Khi i > j, dừng vòng lặp
    A[low], A[j] = A[j], A[low]  # Đặt pivot vào vị trí đúng trong mảng
    return j  # Trả về vị trí của pivot

A = [3, 5, 8, 9, 2, 4]  # Mảng đầu vào
print("Original Array:", A)  # In ra mảng ban đầu
quicksort(A, 0, len(A) - 1)  # Gọi hàm sắp xếp Quick Sort
print("Sorted Array:", A)  # In ra mảng sau khi sắp xếp
Giải thích từng phần:

quicksort là hàm chính của thuật toán sắp xếp nhanh. Nó chia mảng thành các phần tử nhỏ hơn và lớn hơn pivot, sau đó đệ quy sắp xếp các phần tử này.
partition là hàm để tìm pivot và đặt pivot vào vị trí đúng. Hàm này sử dụng phần tử đầu tiên của mảng làm pivot và sử dụng phương pháp chia mảng thành hai phần: một phần chứa các phần tử nhỏ hơn hoặc bằng pivot và một phần chứa các phần tử lớn hơn pivot.
Bước 1 trong quicksort là chọn pivot và đặt pivot vào vị trí đúng trong mảng.
Bước 2 và Bước 3 của quicksort đệ quy sắp xếp nửa trái và nửa phải của mảng tương ứng.
Cuối cùng, sau khi sắp xếp mảng A, bạn in ra mảng sau khi sắp xếp.
"""

"""
#Count Sort  (em làm không kịp ạ )
def countsort(A):
    n = len(A)  # Số lượng phần tử trong mảng
    maxsize = max(A)  # Tìm giá trị lớn nhất trong mảng để xác định kích thước mảng đếm.
    carray = [0] * (maxsize + 1)  # Tạo một mảng đếm có kích thước maxsize + 1, ban đầu tất cả phần tử bằng 0.

    for i in range(n):
        carray[A[i]] = carray[A[i]] + 1  # Đếm số lần xuất hiện của mỗi phần tử trong mảng và lưu vào mảng đếm.

    i = 0
    j = 0
    while i < maxsize + 1:
        if carray[i] > 0:
            A[j] = i  # Bắt đầu xếp mảng dựa trên thông tin đếm.
            j += 1
            carray[i] = carray[i] - 1  # Giảm số lượng xuất hiện của phần tử đã xếp.
        else:
            i += 1

A = [3, 5, 8, 9, 2, 4]  # Mảng đầu vào
print("Original Array:", A)  # In ra mảng ban đầu
countsort(A)  # Gọi hàm sắp xếp Counting Sort
print("Sorted Array:", A)  # In ra mảng sau khi sắp xếp

countsort tạo một mảng đếm carray để đếm số lần xuất hiện của từng phần tử trong mảng A.

Vòng lặp for duyệt qua mảng A và cập nhật mảng đếm carray theo số lần xuất hiện của từng phần tử trong mảng.

Sau khi hoàn thành đếm, mảng A sẽ được sắp xếp lại dựa trên thông tin trong mảng đếm carray.

Vòng lặp while cuối cùng được sử dụng để tái sắp xếp mảng A dựa trên thông tin trong mảng đếm.

"""

"""
#Radix Sort (em làm không kịp ạ )
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
            



