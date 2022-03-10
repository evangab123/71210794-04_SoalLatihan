print("===Program pengubahan suhu celsius!!===")
print("Menu:\n1. Celcius ke fahrenheit")
print("2. Celcius ke Reamur")

masukanuser1= input("Pilihan menu : ")
masukanuser2= input("Masukan Suhu dalam Celcius : ")

fahrenheit = lambda suhu : (9/5)* suhu + 32
reamur = lambda suhu: 0.8 * suhu 

try:
    menu = int(masukanuser1)
    suhu = int(masukanuser2)
    if menu == 1 :
        print("F =",fahrenheit(suhu)) 
    elif menu == 2:
        print("R =",reamur(suhu))

except:
    print("Masukan inputan anda tidak valid!")