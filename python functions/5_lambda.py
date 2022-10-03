"""Eğer tanımlamak istediğimiz fonksiyonu sadece bir kez kullanıcaksak anonim tanımlamak isteyebiliriz---->bunu lambda ile  sağlarız"""


#parametre olarak girilen sayının karesini alan bir fonksiyon tanımlıyalım
def kare_alma_1(number):
    print("Sayının karesi alındı")#Javadaki durum burada geğerli değildir :ekrana yazdırma işleminin return e göre konumu önemli değil
    return number**2
    print("Sayının karesi alındı")

#liste tanımlama
numbers=[12,23,34,45,2,33]

#anonim kare alma fonksiyonu:
result=lambda number:number**2 #herhangi bir çıktı üretmez
#eğer numbers listesinin elemanları için bu anonim metodu kullanırsak


result=lambda number:number**2,numbers#çıktı listenin kendisidir
#eğer sonuçları bir liste içine atayıp listeyi ekrana çıktı olarak yazdırırsak
result=list(map(lambda number:number**2,numbers))#numbers listesinin elemanlarının tek tek kareleri hesaplandı hesaplanan her değer result listesi içine yerleştirldi
print(result)
#eğer anonim listeye bir isim atarsak en başta oluşturulan fonksiyondan hiçbir farkı kalmaz 
kare_alma=lambda number:number**2




#eğer tüm elemanları yeni oluşturduğumuz listenin içine atamak istemezsek-->bunun için filter fonksiyonu kullanılır

result=list(filter(lambda number:number%2==0,numbers))#eğer mod işlemi içinde parantez kullanılırsa bunu ayrı bir arg olarak alacağı için error verir
print(result)
    


    