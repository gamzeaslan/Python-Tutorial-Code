def outer (number):
    def inner(number):
        return number*10
    return inner(number)#burada geriye döndürülen bir değerdir bir fonksiyon değildir

print(outer(10))#çıktı-->100

#eğer outer içinde inner ın çıktısını return etmek yerine inner fonksiyonun kendisini return etmemiz gerekirse

#üs alma fonksiyonu tanımlıyalım-->iki parametre lazim--->taban(outer func) ve kuvvet(inner func) 

print()
print()

"""Üs Alma"""
def dis_taban(taban):
    def ic_kuvvet(kuvvet):
        return(taban**kuvvet)#fonksiyonu kod içerisinde çağırdığımızda bu iki parametreyi nasıl giriş olarak vereceğiz---->bunun için dış fonk içinde iç fonk return edilmeli 
    # return ic_kuvvet(12)--->böyle sadece fonk çıktısını return etmiş oluruz
    return ic_kuvvet#böyle fonksiyonun kendisini return etmiş oluruz


taban=dis_taban(int(input("Taban: ")))#şu an taban değerine aslında inner fonksiyonun kendisi referans edilmiş olur
print(taban(int(input("Kuvvet: "))))


print()
print()

"""Yetki Düzeyi Sorgulama"""
def dis_sayfa(sayfa):
    def ic_yetki(yetki):
        if(yetki=="admin"):
            print(f"{yetki} yetkisindeki kişinin {sayfa} erişimi vardır")
        else:
            print(f"{yetki} yetkisindeki kişinin {sayfa} erişimi yoktur")
    return ic_yetki        


sayfa=dis_sayfa("Ana Sayfa")
sayfa("anonim")
sayfa("admin")


print()
print()


"""Toplama ve çarpma işlemleri"""
def dis_islem_adi(islem_adi):
    def toplam(*args):
        toplam=0
        for i in args:
            toplam +=i
        return toplam

    def carpma (*args):
        carpma=1
        for i in args:
            carpma *=i
        return carpma 

    #dış fonksiyona parametre olarak girilen değere göre hangi fonksiyonun return edileceğine if else bloku ile karar verilir
    if(islem_adi=="toplama"):
        return toplam
    elif(islem_adi=="çarpma"):
        return carpma
    else:
        print("Tanımsız işlem girişi")

toplama=dis_islem_adi("toplama")
print(toplama(12,23,34,24,11))

carpma=dis_islem_adi("çarpma")
print(carpma(12,23,1,2))

