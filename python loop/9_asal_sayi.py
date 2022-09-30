"""Girilen bir sayının asal olup olmadığını bulun """
#ilk kullanıcıdan sayı girişi alınmalı
number=int(input("Sayı: "))
baslangıc_degeri=2#eğer 1 alınırsa tüm sayılar asal olarak kabul edilmez
carpan_sayisi=0
while(baslangıc_degeri<number):
    if(number%baslangıc_degeri==0):
        carpan_sayisi+=1
        baslangıc_degeri+=1
    else:
        baslangıc_degeri+=1    

if (carpan_sayisi==0 and number!=1):
    print("Asal sayıdır")
    
elif(number==1):
    print("Asal değildir")

else:
    print("asal sayı değildir")    
