"""-----------------TUPLE-----------------------"""

#list değişken tanımlaması:
list=[12,23,"A"]


#tuple 1.tanımlaması
tuple_1=(1,'iki',3)
#tuple 2.tanımlaması
tuple_2=2,'üç',4

#ekrana yazdırma:
print(f"liste elemanları:{list}")
print(f"1.tuple elemanları:{tuple_1}")
print(f"2.tuple elemanları:{tuple_2}\n\n")





#1-->list de olduğu gib tupleda da index numaralarından elemanlarına ulaşılabilinir
print(f"listenin 1.indeksdeki elemanı:{list[1]}")
print(f"1.tuple ın 0.indeksdeki elemanı:{tuple_1[0]}")
print(f"2.tuple ın 1.indeksdeki elemanı:{tuple_2[1]}\n\n")





#2-->list de olduğu gibi tupleda da atanmış listeye yeni bir liste toplu olarak atanabilir.Aynı durum tuple içinde geçerlidir
#eski listeyi ekrana yazdırma
print(f"liste elemanları:{list}")
#listeye yeni toplu liste ataması
list=[10,20,'C']
print(f" yeni liste elemanları:{list}\n")

#eski 1.tuple elemanlarını ekrana yazdırma
print(f"1.tuple elemanları:{tuple_1}")
#tuple yeni toplu tuple ataması-->2.tuple değerlerini 1.tuple atama
tuple_1=tuple_2
print(f"1.tuple ,2.tuple değerleri toplu olarak atandı:{tuple_1}\n\n")




#3-->tuple ile list arasındaki fark:list in elemanalarına atama yapıldıktan sonra bu değerler eleman bazlı olarak güncellenebiliyor fakat tuple da bu durum söz konusu değil yani tuple da atama yapılan elemana ,eleman bazlı olarak tekrar atama yapılarak güncellenemez sadece toplu atama yapılabilinir eleman bazlı atama yapılamaz

#-->tuple_1[1]="a" eğer bu kodu çalıştırırsak kod hata verir
#-->list[1]="a" eğer bı kodu çalıştırırsak kod hata vermez



#4-->tuple da kullanabileceğimiz metotlar:count ve index metotlarıdır

