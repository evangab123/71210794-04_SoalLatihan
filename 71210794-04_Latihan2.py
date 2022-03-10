def cek_digit_belakang(bil1,bil2,bil3):
    a = bil1 % 10000 % 1000 % 100 % 10
    b = bil2 % 10000 % 1000 % 100 % 10
    c = bil3 % 10000 % 1000 % 100 % 10
    if a == b or b == c or c == a:
        return True
    else:
        return False

userbil1 = input("Masukan Angka pertama : ")
userbil2 = input("Masukan Angka kedua : ")
userbil3 = input("Masukan Angka ketiga : ")

try:
    bil1 = int(userbil1)
    bil2 = int(userbil2)
    bil3 = int(userbil3)
    x = cek_digit_belakang(bil1,bil2,bil3)
    print(x)

except:
    print("Masukan anda tidak valid")