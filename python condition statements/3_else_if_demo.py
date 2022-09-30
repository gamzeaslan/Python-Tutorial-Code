"""1--> Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır."""
name=input("isim:")
age=int(input("yaş: "))
egitim=input("Eğitim durumu: ")
if(age>=18):
    print("yaş geçerli")
    if(egitim=="üniversite" or egitim=="lise"):
        print("eğitim durumu geçerli\nEhliyet alabilirsiniz")
    else:
        print("Eğitim durumundan kaynaklı ehliyet alamazsınız")  
else:
    print("yaş durumundan kaynaklı ehliyet alamazsınız")          
    if(egitim=="üniversite" or egitim=="lise"):
        print("eğitim durumu geçerli\nEhliyet alabilirsiniz")
    else:
        print("Eğitim durumundan kaynaklı ehliyet alamazsınız")

#----------------------------------------------------------------------------------------------------

"""2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre
  not aralığına karşılık gelen not bilgisini yazdırınız.
  0 -24  => 0
  25-44  => 1
  45-54  => 2
  55-69  => 3
  70-84  => 4
  85-100 => 5"""
not_1=int(input("1.sınav notu: "))
not_2=int(input("2.sınav notu: "))
not_3=int(input("sözlü notu: "))
ort=(not_1 +not_2+not_3)/3


if(ort>=0 and ort<=24):
    print("0")


elif(ort>=25 and ort<=44):
    print("1")

elif(ort>=45 and ort<=54):
    print("2")
    
elif(ort>=55 and ort<=69):
    print("3")


elif(ort>=70 and ort<=84):
    print("4")


elif(ort>=85 and ort<=100):
    print("5")
else:
    print("hatalı giriş")


#-----------------------------------------------------------------------------------------------------


"""3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere
  göre hesaplayınız.
  1. Bakım => 1. yıl     
  2. Bakım => 2. yıl      
  3. Bakım => 3. yıl     
  ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız..
  *** datetime modülünü kullanmanız gerekiyor.  
  (simdi) - (2018/8/1) => gün"""
import datetime