#fonksyona argüman girişi olarak fonksiyon girilemesi

#toplama fonksiyonu
def toplama(*args):
    toplam=0
    for i in args:
        toplam +=i
    return toplam

    #çıkarma fonksiyonu
def cikarma(*args):
    cikarma=0
    for i in args:
        cikarma -=i
    return cikarma


    #çarpma fonksiyonu
def carpma(*args):
    carpma=1
    for i in args:
        carpma*=i
    return carpma


    #bölme fonksiyonu
def bolme(number1,number2):
    return number1/number2


#yukarıdaki tüm fonksiyonları eleman olarak alıcak bir fonksiyon tanımlıyalım
def islem(p1,p2,p3,p4,islem_adi):
    if(islem_adi=="toplama"):
        return toplama(12,23,34,354,45)

    elif(islem_adi=="çıkarma"):
        return cikarma(2,23,-34,53)  

    elif(islem_adi=="çarpma"):
        return carpma(12,23,24)

    elif(islem_adi=="bölme"):
        return bolme(12,23)
    else:
        print("Geçersiz işlem girişi")



#yukarıda tanımlanan islem fonksiyonun kod içerisinde çağrılması
print(islem(toplama,cikarma,carpma,bolme,"toplama"))
print(islem(toplama,cikarma,carpma,bolme,"çıkarma"))
print(islem(toplama,cikarma,carpma,bolme,"çarpma"))                    
print(islem(toplama,cikarma,carpma,bolme,"bölme"))
print(islem(toplama,cikarma,carpma,bolme,"toplamaa"))
