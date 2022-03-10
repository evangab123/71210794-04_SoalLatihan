def cek_angka(a,b,c):
    if a == b or b ==c or c==a or a==b==c:
        return False
    elif a + b == c or b + c == a or c + a == b:
        return True
    else : 
        return False
usera = input("Masukan Angka pertama : ")
userb = input("Masukan Angka kedua : ")
userc = input("Masukan Angka ketiga : ")
try:
    a = int(usera)
    b=  int(userb)
    c = int(userc)
    x = cek_angka(a,b,c)
    print(x)
except:
    print("Masukan anda tidak valid")