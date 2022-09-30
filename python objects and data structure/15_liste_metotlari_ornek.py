#liste tanımalaması
from distutils.command.clean import clean
from os import remove
from unicodedata import name


names=["Ali","Yağmur","Hakan","Deniz"]
years=[1998,2000,1998,1987]

#1--> "Cenk" ismini listenin sonuna ekleyiniz-->append metodu kullanılır
print(list)
names.append('Cenk')
print(f"Append metodu kullanılarak dizinin sonuna 'Cenk' karakteri eklendi:{names}\n")



#2-->"Sena" değerini listenin başına ekleyininiz
print(list)
names.insert(0,"Sena")
print("insert metodu ile 'Sena' ifadesi dizinin başına eklendi:{names}\n")


#3-->"Deniz" isimini listeden siliniz
#bunun için 2 metot vardır
#1.metot:pop()
"""names.pop()-->def olarak en son iindekstenki değeri siler"""
#2.metot:remove()
names.remove('Deniz')
print(f"Deniz karakteri remove metodu ile listeden kaldırıldı:{names}\n")



#4-->"Deniz" isiminin  indexi nedir
#deniz karakteri remove metodu ile kaldırıldığından tekrar eklemeliyiz
print(list)
names.append('Deniz')
print(f"deniz karakterinin indeksi:{names.index('Deniz')}\n")

#5-->"Ali" listenin bir elemanı mıdır
#bunu çözmenin iki yolu var 
#1.yol
is_ali="Ali" in names
print(f"Ali karakteri dizide var mı(in):{is_ali}\n")
#2.yol
ali_sayisi=names.count("Ali")
print(f"Dizideki ali karakterinin sayısı:{ali_sayisi}\n")

#6-->Liste elemanını ters çevirin
print(names)
names.reverse()
print(f"dizi ters çevrildi:{names}\n")



#7-->Liste elemanlarını alfabetik olarak sıralayınız
print(names)
names.sort()
print(f"Dizi elemanları sıralandı:{names}\n")


#8-->years listesini rakamsal büyüklüğe göre sıralayınız
print(years)
years.sort()
print(f"years listesinin küçükten büyüğe sıralamış hali:{years}\n")


#9-->str="Chevrolet,Dacia" karakter dizisini listeye çeviriniz
str="Chervolet,Dacia"
str_list=str.split(',')
print(f"str diziye çevrildi:{str_list}\n")


#10-->years dizisinin en büyük ve en küçük elemanı nedir
print(f"years en küçük eleman:{min(years)}")
print(f"years en büyük eleman:{max(years)}\n")



#11-->years dizisinde kaç tane 1998 değeri vardır
print(f"years listesindeki 1998 eleman sayısı:{years.count(1998)}\n")



#12-->years dizisinin tüm elemanlarını siliniz
print(years)
years.clear()
print(f"years dizisi clear metodu ile silindi:{years}\n")



#13-->Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız
markalar=[]
marka=input("giriş:")
markalar.append(marka)
marka=input("giriş:")
markalar.append(marka)
marka=input("giriş:")
markalar.append(marka)
#kullanıcı tarafından oluşturulan dizinin ekrana yazırılıması
print(f"kullanıcı tarafından oluşturulan dizi:{markalar}\n")

