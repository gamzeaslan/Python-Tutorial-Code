
#------------------------LİSTE METOTLARI--------------------------

#liste tanımlama
list=["a","b","c","d","e"]




#1-->append metodu(dizi.append(eklenilecek ifade)):Bu metotla eklemek istediğimiz değeri parantez içinde belirterek bu değeri listenin en sonuna ekleriz
list.append("f")#f karaketeri dizinin sonuna eklendi
print(f"f karakteri dizinin sonuna eklendi:{list}\n")




#2--> insert metodu(dizi.insert(index ,eklenilecek ifade):eğer listede belirttiğimiz yere eklemek yapmak istersek bu durumda insert metodu kullanırız
print(list)
list.insert(1,'b.0')
print(f"insert metodu kullanılarak 1.indeksten önce b.0 karakteri eklendi:{list}\n")




#3-->pop metodu(list.pop(index)):diziden eleman silmek istediğimizde bunu pop metodunu kullanarak yapabiliriz pop parantezine yazılan index değerine karşılık gelen değeri siler eğer herhangi bir index değeri yazılmazsa def olarak en sondaki elemanı siler
print(list)
list.pop(1)#b.0 silinecek
print(f"listedeki 1.indekteki eleman silinecek:{list}")
#eğer bir indes değeri girilmezse
list.pop()
print(f"indeks değeri belirtilemeden pop metodunu kullanma:{list}\n")



#4-->remove metodu(dizi.remove(karakter)):Eğer silinecek ifadeyi index bazlı olarak silmek yerine direkt karakteri belirterek silmek istersek remove metodunu kullanırız
print(list)
list.remove("a")#a karakteri listeden kaldırılacak
print(f"a karakteri remove metodu kullanılarak listeden kaldırıldı:{list}\n")



#5-->sort metodu(dizi.sort()):Bu metot ile sayısal değerler küçükten büyüğe , string ifadelerde alfabetik olarak sıralanır
print(list)
list.sort()
print("Listenin sıralanmış hali:{list}\n")



#6-->reverse metodu(list.reverse()):Bu metot ile mevcut listenin elemanları ters çevrilir eğer sort ile küçükten büyüğe sıraladığımız listeyi ters çevirirsek büyükten küçüğe sıralanmış halini elde etmiş oluruz-->bu tarz işlemlerde eğer liste üzerinden doğrudan işlem yapmasını istiyorsak herhangi bir yeni atama yapmamıza gerek yoktur
print(list)
list.reverse()
print(f"Listenin ters çevrilmiş hali:{list}\n")



#7-->count metodu(dizi.count(karakter)):Bu metot ile belirtilen karakterin dizideki tekrarlanma sayısı hesapalanır-->sonuç bir değere atanmalı ya da  direkt bir çıktı  olarak yazılmalıdır
print(f"count metodunu kullanarak dizideki 'b' karaketerinin sayısını hesapalama:{list.count('b')}\n")



#8-->clear metodu:dizi.clear():Bu metot ile dizi temizlenir ve tüm elemanları silinir
list.clear()
print(f"dizi clear metodu kullanılarak silindi:{list}\n")