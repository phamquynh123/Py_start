
list1 = [1, 2, 3]

list2 = ["a", "b", "c"]

list3 = [7, 3.5, "Quynh"]

print(list1[0])
print(list2[1])
print(list3[2])


lst = []
lst.append(4)
lst.append(3)
lst.append(6)
print(lst)



# Cho một list các số nguyên n phần tử lst được nhập từ bàn phím. Bạn hãy viết chương trình hiển thị ra màn hình số nhỏ nhất trong list vừa nhập.
print("Nhap do dai chuoi n=")
n = int(input())
lst = []
print("Nhap cac phan tu: ")
for i in range(n):
    print(" phan tu thu ", i +1 )
    lst.append(int(input()))
min_value = lst[0]
for i in lst:
    if i < min_value:
        min_value = i
print( "phan tu nho nhat la : ", min_value)