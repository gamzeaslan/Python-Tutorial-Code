#Eğer programda hazır olarak bulunmayıp ancak bizim projemiz için lazım olan bir hata mesajı oluşturmak istiyorsak  raise kullanılır


#parola kontrolü yapan fonksiyon yazımı
def check_password(psw):

    import re

    if(len(psw)<8):
        raise Exception ("parola en az 8 karakter olmalıdır")

    elif not re.search("[a-z]",psw):
          raise Exception ("Parola küçük harf içermelidir")

    elif not re.search("[A-Z]",psw):
        raise Exception ("Parola büyük harf içermelidir")

    elif not re.search("[0-9]",psw):
        raise Exception ("Parola içerisinde rakam olmalıdır")

    elif not re.search("[_@$]",psw):
        raise Exception ("Parola alpha numeric karakter içermelidir")

    elif re.search("\s",psw):
        raise Exception ("Parola içerisinde boşluk karakteri bulunmamalıdır")

    else:
        print("geçerli parola")

#fonksiyon sonu

#amaç:kullanıcı tarafından uygun parola girilene kadar parola girişi istensin
while True:
    try:
        check_password(input("Parola: "))

    except Exception as ex:
        print(ex)   

    else:
        break

    finally:
        print("try except yapısı sonlandı")