#1-->Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın
from tkinter import E


def kelime_tekrari(kelime,adet):
    sayi=1
    while(sayi<=adet):
        print(kelime)
        sayi+=1

kelime_tekrari("Hello",5)

print()
print()

# ya da
def kelime_tekrari_2(kelime,adet):
    print(kelime*adet)#yan yana 5 tane "Hello" yazdırır (alt alta yazdırmak için ne yapabiliriz??)
kelime_tekrari_2("Hello",5)



#------------------------------------------------------------------------------------------------




#2-->Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınız
def list_cevirme (*list_1):
    list=[]#boş liste tanımlandı
    for item in list_1:#parametre değerleri item atandı
        list.append(item)#item elemanları başta tanımlanan boş listenin sonuna eklenir
    return list#başta tanımlanan liste return edilir

print(list_cevirme(12,23,34,345,5,4))

#3-->Gönderilen 2 sayı arasındaki tüm asal sayıları bulun 
def asal_sayi(baslangic,bitis):
    
    while(baslangic<=bitis):
        sayac=0
        for item in range(2,baslangic-1):
            if(baslangic%item==0):
                sayac+=1
        if(sayac==0):
            print(baslangic)       
        baslangic+=1        
           
asal_sayi(12,25)



                
#------------------------------------------------------------------------------------------------   




#4-->Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürünüz
def bolen_sayisi(number):
    for item in range(1,number+1):
            if(number%item==0):
                print(f"{number} sayisinin bolenleri:{item}")
    
    
               
bolen_sayisi(15)            