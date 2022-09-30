"""--------STRING METOTLARI---------"""

#değişken tanımlama
degisken="Bugün hava yağmurlu"


#1-->upper metodu(cumle.upper()):Cümledeki kelimelerin tüm harflerini büyük harf yapar
upper_degisken=degisken.upper()
print(f"upper metodu kullanıldı: {upper_degisken}")


#2-->lower metodu(cumle.lower()):Cümledeki kelimelerin tüm harflerini küçük harf yapar
lower_degisken=degisken.lower()
print(f"lower metodu kullanıldı:{lower_degisken}")


#3-->title metodu(cumle.title()):Cümledeki her kelimenin baş harfini büyük harf yapar
title_degisken=degisken.title()
print(f"title metodu kullanıldı:{title_degisken}")


#4-->capitalize metodu(cumle.capitalize()):Cümleyi büyük harfle başlatır
capitalize_degisken=degisken.capitalize()
print(f"capitalize metodu kullanıldı:{capitalize_degisken}")


#5-->strip metodu(cumle.strip()):Cümlenin başındaki ve sonundaki boşluk karakterlerini yok eder
strip_degisken=degisken.strip()
print(f"strip metodu kullanıldı:{strip_degisken}")
#soldan silme karakter girişi zorunlu
strip_degisken=degisken.lstrip('B')
print(f"strip soldan karakter silme:{strip_degisken}")
#sağdan karakter silme
strip_degisken=degisken.rstrip('ul')#sağdan okuma yaptığı için tersten yazılmalıdır
print(f"strip sağdan karakter silme:{strip_degisken}")
"""strip ile farklı indekslerdeki karakterleri silme
strip_degisken=degisken.strip('gün.va') işe yaramıyor ??
print(f"split ile farklı konumlardaki karakter gruplarını silme:{strip_degisken}")"""



#6-->split metodu(cumle.split('baz alınacak ifade')):Cümledeki kelimeleri boşluk karakterini baz alarak böler ve bir dizi oluşturur bu kelimelerden.Bu dizi herhangi bir değişene atanırsa bu değişken artık bir dizidir ve index değerleriyle bu dizinin elemanlarına ulaşılabilir.
split_degisken_1=degisken.split()
print(f"split boşluk karakterini baz alarak kullanıldı:{split_degisken_1}")
#eğer boşluk karakteri yerine başka bir karakter baz alınarak cümle parçalansaydı 
split_degisken_2=degisken.split('a')
print(f"split a karakterini baz alarak kullanıldı:{split_degisken_2}")#artık diiz elamanları içerisinde a karakteri bulunmamaktadır



#7-->join('kelimeleri birleştirirken aralarına koyulacak ifade'.join(cumle)):Split metoduyla parçalanan cümle join metoduyla tekrar birleştirilebilir
#önce değişkeni split metodunu kullanarak parçalayalım
degisken=degisken.split()
#şimdi parçalanmış bu cümleyi birleştirelim
degisken=' '.join(degisken)#'*'.join(degisken) ifadesi kullanılsaydı parçalanmış ifadeleri * karakteriyle birleştirirdi
print(f"join metodu boşluk karakteri baz alınarak kullanıldı:{degisken}")



#8-->find metodu(cumle.find('kelime')):Herhangi bir karakterin cümlede olup olmadığını ve varsa bu karakterin ya da kelimenin ilk harfinin indexini veren metottur .Eğer kelime cümlede varsa pozitif yoksa negatif çıktı verir
#pozitif çıktı:
find_degisken_pozitif=degisken.find('B')
print(f"Pozitif ve 0 çıktısı için find metodu kullanıldı:{find_degisken_pozitif}")
#negatif çıktı için:
find_degisken_negatif=degisken.find('ş')
print(f"Negatif çıktı için find metodu kullanıldı:{find_degisken_negatif}")
#find içerisinde de splitte olduğu gibi sağdan ve soldan işlemler gerçekleştirilebilir
#find de sağdan ve soldan işlem gerçekleştirme indeks değerinde farklılığa sebep olur
"""#find soldan indeks hesaplama
#find_degisken_1=degisken.lfind()olmayan öznitelik ekleme hatası veriyor
print(f"find metodu ile a karakterinin soldan başlanarak  hesaplanan indeksi :{find_degisken_1}")"""
#find sağdan indeks hesaplama
find_degisken_2=degisken.rfind('a')
print(f"find metodu ile a karakterinin sağdan başlanarak hesaplanan indeksi:{find_degisken_2}")
#sağdan okumaya başladı fakat sağdan ilk karşısına çıkan a karakterinin soldan başlanarak hesaplanan indeks değerini çıktı olarak verdi



#9-->startswith metodu(cumle.startswith('başlangıç harf')):Bu metot cümlenin hangi harfle başladığını bulmak için kullanılan bir metottur ve boolena değeri döndürür
startswith_degisken_1=degisken.startswith('B')
print(f"startswitch metodu kullanıldı 1:{startswith_degisken_1}")
startswith_degisken_2=degisken.startswith('A')
print(f"startswitch metodu kullanıldı 2:{startswith_degisken_2}")



#10-->endswith metodu:Kullanımı startswith metoduyla aynıdır tek fark startswith deki gibi cümlenin hangi harfle başladığını değil hangi harfle bitiğini kontrol eder
endswith_degisken_1=degisken.endswith('u')
print(f"endswitch metodu kullanıldı 1 :{endswith_degisken_1}")
endswith_degisken_2=degisken.endswith('a')
print(f"endswith metodu kullanıldı 2 :{endswith_degisken_2}")



#11-->replace metodu(cumle.replace(değiştirilicek,yeni eklenecek)):Bu metot cümledeki seçilen karakterlerin yerlerini belirlediğimiz ifadelerle değiştirilemesini sağlar.Replace metodu devam ettirilebilir
replace_degisken=degisken.replace('ü','u').replace('ç','c').replace('ğ','g')#türkçe karakter kullanımı için 
print(f"replace metodu ile cümledeki türkçe karakterler değiştirildi:{replace_degisken}")
#değişim işlemşn yaparken değişimin karakter aralığını sınırlayabiliriz
replace_degisken_1=degisken.replace(' ','*',2)#max 3 arg alabiliyormuş
print(f"replace metodunu sınırlı aralıkta çalıştırma{replace_degisken_1}")#çıktı:Bugün*hava*yağmurlu



#12-->center metodu(cumle.centrel(alan)):Bu metot kullanılarak cümlenin sığdırılacağı alan belirlenir ve bu metot kullanılarak cümle ekranda ortalanabilir
center_degisken_1=degisken.center(50)
print(f"center metodu kullanıldı 50:{center_degisken_1}")
center_degisken_2=degisken.center(100)
print(f"center metodu kullanıldı 100:{center_degisken_2}")
#center metodu alanlar ayırırken ayırdığı alanda ne tutacağını da belirliyebiliriz def=" "
center_degisken_3=degisken.center(50,'*')
print(f"center metodu ile ayrılan alandaki her karakterde * tutma:{center_degisken_3}")



#12.1-->just metodu :aslında center metoduna bencer ama ljust metodu ile cümleyi sola yaslayıp alanı sağdan oluşturabiliriz
ljust_degisken=degisken.ljust(50,'*')
print(f"ljust metodunu kullanrak değişkeni sola yaslıyarak sağa 50 karakterlik * ekleme:{ljust_degisken}")
#-->eğer sağa yaslandırmış olsaysık 
rjust_degisken=degisken.rjust(50,'*')
print(f"rjust metodunu kullanrak değişkeni sağa yaslıyarak sola 50 karakterlik * ekleme:{rjust_degisken}")
#-->eğer sadece just metodu kullanırsak--->böyle bir metot yok 




#13-->count metodu(cumle.count(karakter)):Bu metotla parentez içine girilen metodun cümle içerisinde kaç tane olduğunu hesaplayabiliriz
count_degisken_1=degisken.count('a')#a karakteri cümlede kaç tane
print(f"count metodu ile a karakterinin cümlede kaç tane olduğunu hesaplama:{count_degisken_1}")

#-->eğer aradığımız ifade cümlede yoksa 0 değerini mi vericek yoksa error mesajı mı vericek
count_degisken_2=degisken.count('ş')
print(f"Cümlede bulunmayan bir ifade için count metodu kullanma:{count_degisken_2}")
#error mesajı vermedi 0 değerini çıktı olarak verdi

#-->eğer aradığımı karakterin sayısını tüm cümle için hesaplamak istemiyorsak
#Burada bir aralık belirtmemiz gerkir 
count_degisken_3=degisken.count('a',2,18)
print(f"count metodunu kullanarak a karakterini 2 -18 aralığındaki saysını hesaplama:{count_degisken_3}")

#-->eğer iki aralık vermek yerine aralığı sadece bir sayıyla ifade edersek
count_degisken_4=degisken.count('a',8)
print(f"count metodunu kullanarak 8 - aralığında a karakteri sayısı hesaplama:{count_degisken_4}")
#8.indeksli karakterden başlayarak sonuncu indekse kadarki tüm karakterlerde a karakterini hesapladı sonuç=2

#-->eğer aralıkta başı değilde sonu belirtirsek
#count_degisken_5=degisken.count('a',,14) şeklinde kullanıldığında hata veriyor




#14-->isalpha metodu(cumle.isalpha()):Bu metot ile cümlenin alfabetik olarak dizilip dizilmediğini döndürdüğü boolean değeri ile anlarız
isalpha_degisken=degisken.isalpha()
print(f"isalpha metodunu kullanarak cümle alfabetik olarak sıralanıyor mu:{isalpha_degisken}")#false

#-->eğer cümlede sayısal değer varsa
degisken_2="Bugün hava yağmurlu 3"
print(f"eğer cümlede sayısal değer varsa alfabetik olarak durumu nasıl olur:{degisken_2.isalpha()}")#false

#-->eğer cümle alfabetik olmasına rağmen sayısal değer varsa
degisken_3="a b c 3"
print(f"eğer cümle alfabetik olmasına rağmen sayısal değer varsa: {degisken_3.isalpha()}")#false



#15-->isdigit metodu :sayısal mı 
degisken_4="121"
degisken_5=121
print(f"str 121 isdigit:{degisken_4}")#121
print(f"int 121 isdigit:{degisken_5}")#121
#iki çıktı değeri de 121 boolean değer döndürmesi gerekmiyor muydu??? bu metodu araştır 



#16--->index metodu:find metodu yerine bu metodu kullanarak da karakterlerin indekslerini hesaplayabilir tek fark find metounda olmayan bir değerin indeksini hesaplamaya çalıştığımızda error vermez hatta negatif değer verir ve bu değerden bu karakterin bu değişkende olmadığını anlarız ancak indeks metodunda durum aynı değil olmayan bir karakterin indeks değerini index metodunu kullanarak hesaplamaya çalışırsak error alırız bu durumu hata yönetimi ile düzeltebiliriz
index_degisken=degisken.index('g')
print(f"index metodu ile  g karakterinin karakterini hesaplama:{index_degisken}")


