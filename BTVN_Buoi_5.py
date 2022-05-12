print("Bài 1: Nhap day so. Tim so lon nhat, nho nhat, vi tri")
n = int(input("Nhap so phan tu trong day so: "))

max = min = int(input(f"Nhap phan tu thu 1: "))
vitri_max = vitri_min = 1
for i in range(2, n+1):
    tg = int(input(f"nhap phan tu thu {i}: "))
    if tg >= max :
        max = tg
        vitri_max = i
    if tg < min:
        min = tg
        vitri_min = i     
print(f"Gia tri max la: {max}, ở vị trí: {vitri_max}")
print(f"Gia tri min la: {min}, ở vị trí: {vitri_min}")
print("**************************************************************")
print("Bài 2: Nhap day so. Tinh tong. Tong so le")
n = int(input("Nhap so phan tu trong day so: "))
tong = tong_le = 0
b = bl = ""
kt = "+"
for i in range(1, n+1):
    if i < n+1: 
        a = int(input(f"Phần tử thứ {i}: "))
        tong +=a
        b += str(a)
        if a%2 != 0 :
            tong_le +=a
            bl += str(a)
print(f"Tong day so: {kt.join(b)} = {tong}")
print(f"Tong ca so le trong day: {kt.join(bl)} = {tong_le}")