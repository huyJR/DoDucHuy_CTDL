# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 23:04:02 2023

@author: OS
"""

                     # buổi 4 
# các phép thủ thuật toán trong mảng 
"""array = [3, 5,6,7,8,10]
print(array[1])
print(array[0:2])
print(array[:-2]) # lấy trừ 2 phần tử cuối """
#tim max 
"""def timmax(x):
    max=x[0] # giả sử giá trị ban đầu là max 
    for num in x:  # vòng vặp để lấy các giá trị trong array 
        if num>max : # điều kiện tìm số max 
           max = num  # ở trường hợp này nên cận thận khi bạn cho num = max nó sẽ trả về không có nghĩa là bạn cho giá trị max ban đầu=vói num
            
    return max
    
    
    
array=[0,2,4,5,1,3,8,10]
kq = timmax(array)
print("so max là: ", kq )"""

# tìm min         
def timmin(x):
    min=x[0] # giả sử giá trị ban đầu là max 
    for num in x:  # vòng vặp để lấy các giá trị trong array 
        if num<min : # điều kiện tìm số max 
           min=num  # ở trường hợp này nên cận thận khi bạn cho num = max nó sẽ trả về không có nghĩa là bạn cho giá trị max ban đầu=vói num
            
    return min
    
    
    
array=[0,2,4,5,1,3,8,10]
kq = timmin(array)
print("so min là: ", kq )

#interview question 1 : đảo ngược mảng với mảng là số
"""def daonguocmang(x):
    # khởi tạo vị trí  ban đầu và vị trí cuối của mảng
    start=0
    end=len(x)-1
    # thực hiện hoán đổi các vị  của mảng 
    while end>start:
        x[start],x[end] = x[end],x[start]# hoán đổi vị trí với nhau 
        start = start+1 # thực hiện với vị trí phần tử thứ 2 trong mảng 
        end = end-1 # thực hiện với vị trí phần tử kế cuối trong mảng 
     
        
array=[3,5,6,3,8] # tạo Array 
daonguocmang(array)# gọi hàm và truyền tham chiếu đến function 
print(array) #in ra mảng sau khi được gọi hàm """

# interview question 2: kiểm tra xem có phải là pailnarome hay là không 
"""def ktmang(x):
    # khởi tạo vị trí  ban đầu và vị trí cuối của mảng
    start=0
    end=len(x)-1
    
    # thực hiện kiểm tra có phải là palindrome hay không 
    while end>start:
        if x[start]!=x[end]: #kiểm tra 2 phần tử trong mảng 
            return -1
        start = start+1 # thực hiện với vị trí phần tử thứ 2 trong mảng 
        end = end-1 # thực hiện với vị trí phần tử kế cuối trong mảng 
        
    return 1


array="radxr" # tạo Array với chữ là radar
kq=ktmang(array)# gọi hàm và truyền tham chiếu đến function 
print(kq)

if kq == 1 : 
    print(" palindrome")
else:
    print(" not palindrome")
        
print(array) #in ra kết quả sau khi được gọi hàm """

#interview 3: thực hiện nhập vào một sô interger và in ra số đảo của nó 

"""number=int(input("nhap vao so number"))
print("so ban dau nhap", number)
daoNumber = 0 

while number !=0 :
    digit = number % 10 # tách lấy số cuối của number vid dụ 4321 thành 1 
    daoNumber = daoNumber*10 +digit # đảo ngược số của number từ số cuối lên 12 
    number = number //10 #tách số number 4321 thành 432
    
print(" so dao nguoc la ", daoNumber)#in ra so dao ngược """

#interview question 4 : thực hiện kiểm tra 2 chữ có phải là 
"""def la_anagram(word1, word2):
    # Loại bỏ khoảng trắng và chuyển sang chữ thường
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()

    # Sắp xếp các ký tự và so sánh sorted ở đây là 1 hàm sắp xếp lại 
    return sorted(word1) == sorted(word2)

# Kiểm tra hai từ
result = la_anagram("listen", "islent")

if result:
    print("Hai từ là anagram.")
else:
    print("Hai từ không phải là anagram.")"""
    
#interview question 5: tìm số giống nhau trong mảng  
"""def timsogiong(a):#tạo một function để tìm số giống 
    sogiong = set() #tạo một set() để tìm số giống nhau trong array
    sodaco = set()  #tạo một set() để thêm các giá trị array vào ngoài ra 
    for so in a: # đưa từng các giá trị trong mảng ra để xét đk if ở dưới 
     if so in sodaco : # nếu giá trị trong mảng giống với giá trị trong set() đã có thì trả về true ngược lại trả về false
         sogiong.add(so) # thực hiện đk nếu giá trị giống với trong mảng 
     else: 
         sodaco.add(so) # ngược lại nếu khác thì thêm giá trị đó vào 
         
    return sogiong # trả về các số giống nhau sau khi kết thúc vòng lặp 


a=[1,2,3,4,2,6,7,1]
kq=timsogiong(a) #gọi hàm tham chiếu mảng a đến function 
print("so giong là :", kq)"""


class Node: #khoi tạo class Node
     
   def __init__(self): #khởi tạo phương thức với tham số self
        self.data = data # gán giá trị của tham số data vào thuộc tính data 
        self.nextNode = None #gán giá trị None cho thuộc tính nextNode và thuộc tính này tham chiếu đến nút tiếp theo trong 

class Linkedlist:
    # giá trị khởi tạo ban đầu 
    def __init__(self):
        self.head = None #gán phần tử đầu tiên trong Linked List là None(nghĩa là danh sách ban đầu ko có phần tử nào  ),
        self.numberOfNone = 0 # theo dõi số lượng Nút trên LinkedList 
    #thêm vào một phần tử đầu vào danh sách liên kết 
    def insert_start(self,data): #tạo function chèn nút vào vị trí đầu với 2 tham số là self và data 
        self.numberOfNode =   self.numberOfNode+1 # cập nhật nút sau khi chèn thêm nút
        new_node = Node(data) # nhập giá trị mới data 
        
        if not self.head: # kiểm tra xem LinkedList có rỗng hay không 
            self.head = new_node # trường hợp rỗng thì giá trị mới tạo là giá trị đầu 
        else:
            new_node.nextNode=self.head # nếu ko rỗng thì nó sẽ tham chiếu vào đến nút đầu tiên(vì NextNode được đặt là None)
            self.head = new_node # gán giá trị mới là ở nút đầu tiên 
            
    #thêm một phần tử vào cuối vào danh sách liên kết
  def insert_end(self, data):
        self.numberOfNode =   self.numberOfNode+1 
        new_node = Node(data)
        
        actual_node = actual_node.nextNode
        
        while actual_node.nextNode is not None :
            actual_node =actual_node.nextNode
            
        actual_node.nextNode=new_node
        