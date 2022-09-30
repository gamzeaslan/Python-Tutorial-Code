"""-------------SORULAR------------"""
website="http://www.sadikturan.com"
course="Python Kursu:Baştan Sona Python Programlama Rehberiniz(40 saat)"
#1-->'Hello World' karakter dizisinin baş ve sondaki karakterlerini silin-->strip metodu kullanılır
hello_world=" Hello World "
strip_degisken=hello_world.strip()
print(f"'Hello World' karakter dizisinin baş ve sondaki karakterlerini silin(strip metodu kullanıldı):{strip_degisken}\n")



#2-->'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin(iki çözüm yolu var)
#değişken tanımlaması
degisken="www.sadikturan.com"
#------------1.çözüm yolu-----------replace metodu kullanıldı
replace_degisken=degisken.replace('www.','').replace('.com','')
print(f"replace kullanılarak sadikturan yazısı elde edildi:{replace_degisken}")


#------------2.çözüm yolu-----------strip metodu kullanıldı
strip_degisken=degisken.lstrip('www.').rstrip('moc.')
print(f"strip kullanılarak sadik turan yazısı elde edildi:{strip_degisken}")
#eğer üsteki kod yerine şu kullanılsaydı da aynı çıktıyı üretir miydi:
strip_degisken=degisken.strip('www..moc')
print(f"strip kullanılarak sadik turan yazısı elde edildi:{strip_degisken}\n")#aynı çıktıyı üretti
#NOT:değişkenin hem sağ hem sol tarafından silme yapmak ve bunu  strip metodunu sadece bir kere kullanarak yapmak istiyorsak (soldan okunarak yazılmıi ifadeSağdanokunarak yazılmış ifade) şeklinde yapılmalıdır



#3-->'course' karakter dizisinin tüm karakterlerini küçük harf yapın-->lower
lower_degisken=course.lower()
print(f"course içindeki karakterler lower kullanılarak küçük harfe dönüştürüldü:{lower_degisken}\n")


#4-->'website' içinde kaç tane a karakteri vardır--2 çözüm yolu var
#------------1.çözüm yolu-----------split metodu kullanıldı
#eğer websitesini a harfine göre bölersem(split) ve ortaya çıkan dizinin eleman sayısını bulup 1 çıkartırak a karakteri sayısını bulmuş oluruz(2 tahta parçası=1 kesim noktası)
split_degisken=website.split('a')
a_sayisi=len(split_degisken)-1
print(f"websitesi split kullanılarak kaç tane a karakteri içerdiği hesaplandı:{a_sayisi}")

##------------2.çözüm yolu-----------count metodu kullanıldı
count_degisken=website.count('a')
print(f"count metodu kullanılarak kaç tane a karakteri içerdiği hesaplandı:{count_degisken}\n")



#5-->'website' 'www' ile başlayıp com ile bitiyor mu
#www ile başlama-->startswith(bool) metodu kullanılır
startswith_degisken=website.startswith('www')
print(f"website www ile başlıyor mu(startswith):{startswith_degisken}")
#com ile bitme-->endswith(bool) metodu kullanılır
endswith_degisken=website.endswith('com')
print(f"website com ile bitiyor mu(endswith):{endswith_degisken}\n")



#6-->'website' içinde '.com' ifadesi var mı-->find metodu kullanılır(index değerini döndürür < >=0)error
find_degisken=website.find('.com')
print(f"find metodu ile .com websitesinde var mı varsa başlangıç karakterinin indexi :{find_degisken}\n")



#7-->'course' içindeki karakterlerinin hepsi alfabetik mi-->isalpha(bool) metodu kullanılır
isalpha_degisken=course.isalpha()
print(f"'course' içindeki karakterlerinin hepsi alfabetik mi:{isalpha_degisken}\n")


#8-->'Contents' ifadesinin satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz
#50 karakter içine yerleştirme-->boşluk kullanılarak
degisken="Contents"
center_degisken=degisken.center(50)
print(f"center metoduyla boşluk karakteri baz alınarak 50 karakterlik yer ayrılır:{center_degisken}")
#50 karakter içine yerleştirme-->* kullanılarak
center_degisken=degisken.center(50,'*')
print(f"center metoduyla boşluk karakteri baz alınarak 50 karakterlik yer ayrılır:{center_degisken}")
#50 karakteri değişkeni sola yaslayarak sağa yerleştirme
ljust_degisken=degisken.ljust(50,'*')
print(f"ljust metoduyla boşluk karakteri baz alınarak 50 karakterlik yer ayrılır:{ljust_degisken}\n")

#9-->'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin--->replace kullanılır
replace_degisken=course.replace(' ','-')
print(f"replace metodu kullanılarak course içindeki boşluk karakterleri - ile değiştirildi:{replace_degisken}\n")



#10-->'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin-->replace metodu kullanılır
#değişken tanımlama yukarıda yapılmıştı
yeni_hello_world=hello_world.replace('World','There')
print(f"Hello World--->Hello There:{yeni_hello_world}\n")

#11-->'course' karakter dizisini boşluk karakterinden ayırın-->sprit metodu kullanılır
split_degisken=course.split()
print(f"couse split ile boşluk karakterini baz alarak ayırma:{split_degisken}\n")
 