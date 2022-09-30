#NOT:çoklu yorum satırı için """ üç tırnak ya da üç tek tırnak kullanımı yapılabilinir

#--------------Müşteri bilgileri--------------
musteri_adi="Gamze"
musteri_soyadi="Aslan"
musteri_tam_adi=musteri_adi + ' ' + musteri_soyadi
musteri_cinsiyet="Kadın"
#musteri_cinsiyet=True (True=Kadın - False=Erkek) şeklinde de bir atama yapılabilir
musteri_tc_no=12345678910
musteri_dogum_yili=2001
musteri_yasi=21

#--------------müşteri sipariş geçmişi--------------
siparis1=110
siparis2=1100.5
siparis3=356.95

# Tüm siparişlerin toplamı
toplam_siparis=siparis1 + siparis2 + siparis3

#Toplam siparişi ekrana yazdırma 
print("Toplam sipariş tutarı:",toplam_siparis)

#string ve int değerleri birlikte ekrana yazdırmak istiyorsak 
#print("string",integer) komutunu çalıştırırız

