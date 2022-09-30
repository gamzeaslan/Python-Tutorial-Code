"""1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın
-->100 üzerinden puanlama yapın her soru 20 puan
-->hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın"""
#random modülü import edildi
import random
#tahmin edilecek sayı oluşturuldu
tahmin_edilecek_sayi=random.randint(1,100)
#kullanıcıdan can bilgisinin girişi alındı
can=int(input("Can sayısı: "))
while(can>=0):
    if(can>0):
        tahmin=int(input("Tahmin: "))
        can-=1
        if(tahmin==tahmin_edilecek_sayi):
            print(f"Doğru tahmin kalan canınız:{can}")
            break
        elif(tahmin>tahmin_edilecek_sayi):
            print(f"aşağı ve kalan can sayınız:{can}")
        elif(tahmin<tahmin_edilecek_sayi):
            print(f"yukarı ve kalan can sayısı :{can}")    
    elif(can==0):
        print(f"Hakkınız bitmiştir sayı:{tahmin_edilecek_sayi}")  
        break      
























# if(can!=0):
#     while(can>0):
#         tahmin=int(input("Tahmininiz:"))
#         can-=1
#         if(tahmin_edilecek_sayi==tahmin):
#             print(f"Doğru tahmin ve kalan can sayısı :{can}")
#             break
#         elif(tahmin_edilecek_sayi>tahmin):
#             print(f"yukarı ve kalan can sayısı :{can}")
#         elif(tahmin_edilecek_sayi<tahmin):
#             print(f"aşağı ve kalan can sayısı:{can}")        
# elif(can==0):
#     print(f"hakkınız bitmiştir ve sayı:{tahmin_edilecek_sayi}")
        
  
      

 