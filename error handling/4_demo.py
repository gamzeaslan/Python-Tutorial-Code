"""#1-->Liste elemanları içindeki sayısal değerleri bulunuz"""

liste=["1","2","5a","10b","abc"]
import re
for list in liste:
    if re.search("[0-9]",list):
        if not re.search("[a-z]",list):
            print(list)




"""#2-->Kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayı olduğundan emin olunuz aksi halde hata mesajı yazınız"""

while True:
    result=input("Sayı: ")
    if (result == 'q'):
        break
    
    try:
        number=float(result)
        print(f"Girdiğiniz sayı:{number}")
        continue#eğer break kullanırsak sayısal değer girdiğimiz anda döngü kırılır ama bizden istenen döngünün sadece 'q' ile kırılmasıdır

    except Exception as ex:
        print(f"Geçersiz değer girdiniz: {ex}")
        continue
        



"""#3-->Girilen parola içerisinde türkçe karakter hatası veriniz"""

def turkce_karakter(str):
    import re 
    if re.search("[çğıİşöÜ]",str):
        raise Exception ("Türkçe karakter kullandınız")
    else:
        print("Türkçe karakter kullanılmamaktadır")    

try:
    turkce_karakter(input("Parola: "))

except Exception as ex:
    print(ex)


"""#4-->Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları verin""" 
def faktoriyel(numb):
    if(numb<0):
        raise Exception ("Negatif değerlerin faktöriyeli alınamaz")
    else:
        result=1
        numb_2=numb
        while numb>0:
            result*=numb
            numb-=1
        print(f"{numb_2}!={result}")    

try:
    faktoriyel(int(input("Sayı: ")))
except Exception as ex :
    print(ex)    

finally:
    print("try except yapısı sonlandı")