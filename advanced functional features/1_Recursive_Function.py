# #bir fonksiyon oluşturalım
# def greeting (name):
#     print(f"Hello {name}")

# #oluşturulan bu fonksiyonu arg ile birlikte çağıralım
# greeting("A")

# #eğer arg kullanmadan bu fonksiyonu ekrana yazdırırsak
# print(greeting)
# print()

# #fonksiyon bir objedir bu objeyi referans eden yeni bir değişken oluşturursak
# sayHello=greeting
# print(sayHello)#greeting ve sayhello nun adresleri aynıdır
# print()

# #eğer bu referanslardan birini silersek-->data silinmez hatta nesneyi referans gösteren tüm değişkenleri silersek obje hala bellektedir sadece artık bu nesne üzerinde işlem yapabileceğimiz herhangi bir değişken(referans) yoktur-->anonim nesne-->Javada Garbage Collection ile silinirsi peki python da?? -->pyhonda da GC vardır
# del sayHello

# print(greeting)#silinme işleminde sonra adres değişmez


# #fonksiyon içinde fonksiyon tanımlaması-->Encapsulation(Kapsülleme)
# def outer(number):
#     print("Dış/outer")
#     def inner(number):
#         print("iç/inner")
#         return number+1#-->++number işe yaramıyor 

#     #outer func içinde inner func çalışması için çağrılması gerekir
#     print(inner(number))#13
#     #ya da 
#     number2=inner(number)
#     print(number,number2)#12 13 aynı sonucu üretmesinin sebebi aynı arg değerinin gönderilmesinden kaynaklanmaktadır     


# #outer fonksiyonunun çıktısını ekrana yazdırırsak
# print(outer(12))#-->Arg bir fazlasını ekrana yazdırmaz çünkü inner func , outer func içinde tanımladık çağırmadık -->tanımlamak ve çeğırmak farklı şeylerdir
# #inner()-->bu fonksiyona buradan erişilemez sadece outer func üzerinden erişim gerçekleştirilir



"""RECURSIVE FUNC"""
#faktoriyel hesaplama-->5=5*4!(fonk kendi kendisini çağırması)

def outer(number):

    #fonksiyonun parametre girişinde oluşabilecek hataları oluşturalım

    #eğer int tipinin dışında bir veri tipi parametre olarak girilirse
    if not isinstance(number,int):
        raise TypeError("Parametre olarak girilen değer int tipinde değildir")


    if number<0:
        raise ValueError("Sıfırdan küçük sayıların faktoriyeli hesaplanamaz")    


    def inner(number):
        if(number<=1):
            return 1

        return number*inner(number-1)#iş yapan kısım inner func olduğundan inner return edildi
    #iç fonk tanımlaması yapıldı ancak herhangi bir çıktı üretebilmesi için dış fonk içinde çağırılmalı

    return inner(number)

#fonksiyonu try except içinde çağıralım
try:
    print(outer(4))
    
except Exception as ex:
    print(ex)    

