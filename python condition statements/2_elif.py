#kullanıcı tarafından girilen iki sayının birbirlerine göre durumları:
#sayılar üzeriden sayısal bir karşılaştırma yapılacağından kullanıcıdan alınan girişler int dönüştürülmeli
number_1=int(input("1.sayı: "))
number_2=int(input("2.sayı: "))

if(number_1<number_2):
    print("1.sayı <2.sayı")
elif(number_1>number_2):#else if
    print("1.sayı>2.sayı")    
else:
    print("1.sayı=2.sayı")

#kullanıcı tarafından sayının 0 a göre durumunu bulan program:---->NEDEN ÇALIŞMIYOR-->ÇÜNKÜ BU BLOKU ELSE İÇİNDE YAZMIŞIM
number=int(input("Sayı: "))
if (number<0):
    print("Negatif")
elif(number>0):
    print("Pozitif")  
else:
    print("Sıfırdır")      


    