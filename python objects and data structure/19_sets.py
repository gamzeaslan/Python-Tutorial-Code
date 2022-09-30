#1-->bu listenin normal listeden farklı indekslenmemesidir yani bu listenin elemanlarına index değerleri kullanılarak ulaşılamaz ve index değeri içerne metotlar da kullanılamaz.hangi parantez kullanıldığı çok önemli .Parantezler sayesinde liste türü anlaşılıyor

fruits={'orange','apple','banana'}
print(fruits)



#2-->print(fruits[0]) indekslenemez



#3-->Bu listenin elemanlarına ulaşmak için döngüler kullanılır




#4-->bu listelere karakter eklemek için :
fruits.add('mango')
print(fruits)




#5-->eğer birden fazla karakter eklemek istiyorsak liste ekleyebiliriz
fruits.update(["grape","apple"])
print(fruits)




#6-->eğer listede var olan bir elemanı eklemek istersek eklemez eklenmiş listelerde her iki listede de aynı eleman varsa sadece bir tanesi toplam listeye eklenir




#7-->oluşturulmuş herhangi ibr listedeki tekrarlayan elemanları silmek istiyorsak:
set(fruits)#metodu kullanılır
print(fruits)




#8-->Eğer listeden bir eleman silmek istiyorsak
fruits.remove('mango')#mango elemanı silindi
print(fruits)
fruits.discard('apple')
print(fruits)



#9-->bu liste türünde index bazlı değil karakter bazlı girişler alan metotlar kullanılır




#10-->pop metodu gibi son indexe dayalı bir metot kullanırsak
fruits.pop()#son elemanı silme garantisi vermez çünkü index bazlı çalışır
print(fruits)


