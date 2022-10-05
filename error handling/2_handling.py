# number_1=int(input("1.sayı: "))
# number_2=int(input("2.sayı: "))

# try:
#     sonuc=number_1/number_2

# except ZeroDivisionError:
#     print("Bir sayının sıfıra bölünmesi tanımsızlık yapar")

# except ValueError:
#     print("int tipinde değerler giriniz")

#  #eğer bu iki hata mesajını tek except içinde toplamak istersek   

# try:
#     sonuc=number_1/number_2

# except(ZeroDivisionError,ValueError):
#     print("Hatalı giriş yaptınız")


# #eğer hatalarla ilgili detay bilgileri ekrana yazdırmak istersek
# try:
#     sonuc=number_1/number_2

# except Exception as ex:#tüm hatalar için kullanılan genel bir ifadedir
#     print(f"Hatalı giriş yaptınız: {ex}")

while True:
    try:
        x=int(input("X: "))
        y=int(input("Y: "))
        sonuc=x/y
    except Exception as ex:
        print("Yanlış giriş yapıtınız ",ex) 
    else:
        print(sonuc)
        break#herhangi bir hatalı giriş yapılmamışsa while döngüsü kırılır
    finally:
        print("try except sonlandı")
           
    




    







   
