#1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
number=int(input("Sayı: "))
if(number>=0 and number<=100):
    print("Girilen sayı 0 ile 100 arasındadır")

else:
    print("girilen sayı 0 ile 100 arasında değildir")

#-----------------------------------------------------------------------------------------------------

#2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

number=int(input("sayı: "))
if(number%2==0):
    if(number>0):
        print("pozitif çift")
    else:
        print("negatif çift veya 0")    
else:
    if(number>0):
        print("pozitif tek")
    else:
        print("negatif tek veya 0") 
            

   #--------------------------------------------------------------------------------------------------  
#3- Email ve parola bilgileri ile giriş kontrolü yapınız. 
email=input("email: ")
sifre=input("şifre: ")
if(email=="gamzeaslan"):
    if(sifre=="123"):
        print("giriş başarılı")
    else:
        print("şifre yanlış") 
else:
    print("email yanlış") 
    if(sifre=="123"):
        print("email yanlış----şifre doğru2")
    else:
        print("şifre yanlış") 

#-----------------------------------------------------------------------------------------------------

#4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
number_1=int(input("1.sayı: "))
number_2=int(input("2.sayı: "))
number_3=int(input("3.sayı: "))
if(number_1>number_2 and number_1>number_3):
    if(number_2>number_3):
        print(f"{number_1}>{number_2}>{number_3}")
    elif(number_3>number_2):
        print(f"{number_1}>{number_3}>{number_2}")
    else:
        print(f"{number_1}>{number_2}={number_3}") 

elif(number_2>number_1 and number_2>number_3):
    if(number_1>number_3):
        print(f"{number_2}>{number_1}>{number_3}")
    elif(number_3>number_1):
        print(f"{number_2}>{number_3}>{number_1}")
    else:
        print(f"{number_2}>{number_1}={number_3}")


elif(number_3>number_1 and number_3>number_2):
    if(number_1>number_2):
        print(f"{number_3}>{number_1}>{number_2}")
    elif(number_2>number_1):
        print(f"{number_3}>{number_2}>{number_1}")
    else:
        print(f"{number_3}>{number_1}={number_2}")

else:
    print(f"{number_2}={number_1}={number_3}")


#-----------------------------------------------------------------------------------------------------

#5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
"""Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
   a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
   b-) Finalden 70 alındığında ortalamanın önemi olmasın."""

#Kullanıcıdan sınav notlarını al
vize_not__1=float(input("1.vize notu: "))
vize_not__2=float(input("2.vize notu: "))
final_not=float(input("final notu: "))

ort=(vize_not__1 + vize_not__2 + final_not)/3

#1.durum
if(ort>=50):
    if(final_not>=50):
        print(f"ortalama:{ort} ve geçme durumu:başarılı")
    else:
        print(f"ortamalama:{ort} ve geçme durumu:başarısız")
else:
    print(f"ortalama:{ort} ve geçme durumu :başarısız ")            


#2.durum
if(ort>=50):
    if(final_not>=70):
        print(f"ortalama:{ort} ve final notu 70 ve üstü geçme durumu:başarılı")
    else:
        print(f"ortalama:{ort} final notu 70 altı ve geçme durumu:başarısız")   
else:
    print(f"ortalama:{ort} ve geçme durumu:başarısız")         

#-----------------------------------------------------------------------------------------------------

"""6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
   Formül: (Kilo / boy uzunluğunun karesi)
   Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
   0-18.4    => Zayıf 
   18.5-24.9 => Normal  
   25.0-29.9 => Fazla Kilolu
   30.0-34.9 => Şişman (Obez)"""

   #kullanıcıdan istenilen bilgileri alma
isim=input("isim: ")
kilo=float(input("kilo: "))
boy=float(input("boy: "))
index=float(kilo/boy)**2
if(index>=0 and index<=18.4):
    print("Zayıf")
elif(index>=18.5 and index<=24.9):
    print("Normal")
elif(index>=25.0 and index<=29.9):
    print("Fazla Kilolu")
elif(index>=30.0 and index<=34.9):
    print("Obez")      
       

#İNDEX HESABINDAN YANLIŞ SONUÇ ÜRETİYOR    