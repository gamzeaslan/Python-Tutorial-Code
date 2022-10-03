#toplama işlemi için fonk tanımlama:
#geriye değer döndürmeyen fonk
def toplama_1(x,y):
    print(x+y)

def toplama_2(x,y):
    return(x+y)

#tanımlanmış fonksiyonları kullanma

#geriye değer döndürmeyen fonksiyon aynen yazılır
toplama_1(12,23)

#geriye geğer döndüren fonksiyon ya bir değişene atanır ve bu değişken ekrana yazdırılır .Eğer üzerinde herhangi bir işlem yapılmıyıcaksa değişkene atanmadan da direkt ekrana yazdırılabilinir
degisken=toplama_2(12,23)
print(degisken)
print()
print(toplama_2(12,23))


#--------------------------------

#parametre olarak str alınırsa
def say_hello(name):
    print(f"Hello {name}!")

say_hello("Gamze")

#eğer parametelere def deger atamak istersek

def say_hello_1(name="user"):
    print(f"Hello {name}")

say_hello_1("Gamze")
say_hello_1()

#--------------------------------
#yaş hesaplayan metot
def yas_hesaplama(dogum_yili):
    return (2022 - dogum_yili)

print(f"yaş: {yas_hesaplama(2001)}")

#emeklilik yaşını hesaplayan fonksiyon
def emeklilik_yas_hesaplama(dogum_yili):
    """
    DOCSTRING:Dogum yiliniza gore emekliliginize kac yil kaldi
    INPUT:Dogum yili
    OUTPUT:Hesaplanan yil bilgisi
    """
    yil= 65-yas_hesaplama(dogum_yili)#kullanıcının emekliliğine kaç yıl kaldığı hesaplandı 
    if(yil>0):
        print(f"Emekli olmanıza kalan yıl:{yil}")
    else:
        print("Emekli durumundasınız")

emeklilik_yas_hesaplama(2001)            


#bu şekilde paratez içinde belirtilen fonksiyondaki yorum satırlarını ekrana yazdırır bu bilgiler kullanıcı için doc görevi görebilir
print(help(emeklilik_yas_hesaplama))


list=[1,2,3]
print(help(list.append))#burada ise append metodunun listede nasıl kullanıldığına ilişkin bir doc getirir