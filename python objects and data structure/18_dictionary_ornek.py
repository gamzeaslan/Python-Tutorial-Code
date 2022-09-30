"""
ogrenciler={
    '120':{
        'ad':'Ali',
        'soyad':'Yılmaz',
        'telefon':'532 000 00 02'
          },

     '125':{
        'ad':'Can',
        'soyad':'Korkmaz',
        'telefon':'532 000 00 02'
           },

      '128':{
         'ad':'Volkan',
         'soyad':'Korkmaz',
         'telefon':'532 000 00 03'
            }         
}
"""



#1-->Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dic içinde saklayınız
print("**********1.öğrenci bilgi girişi**********")
ogrenci_no_1=input("1.öğrencini numarası: ")
ogrenci_ad_1=input("1.öğrencinin adı: ")
ogrenci_soyad_1=input("1.öğrencinin soyadı: ")
ogrenci_tel_no_1=input("1.çğrencinin telefon numarası: \n\n")

print("**********2.öğrenci bilgi girişi**********")
ogrenci_no_2=input("2.öğrencini numarası: ")
ogrenci_ad_2=input("2.öğrencinin adı: ")
ogrenci_soyad_2=input("2.öğrencinin soyadı: ")
ogrenci_tel_no_2=input("2.çğrencinin telefon numarası: \n\n")

print("**********3.öğrenci bilgi girişi**********")
ogrenci_no_3=input("3.öğrencini numarası: ")
ogrenci_ad_3=input("3.öğrencinin adı: ")
ogrenci_soyad_3=input("3.öğrencinin soyadı: ")
ogrenci_tel_no_3=input("3.çğrencinin telefon numarası: \n\n")

print("------Kullanıcı tarafından alınan bilgiler listeye eklendi arama yapabilirsiniz")
ogrenciler_dic={ogrenci_no_1:{
                               '1.Öğrenci Adı':ogrenci_ad_1,
                               '1.Öğrencinin Soyadı':ogrenci_soyad_1,
                               '1.Öğrencinin Telefon Numarası':ogrenci_tel_no_1
                             },

                ogrenci_no_2:{
                               '2.Öğrencinin Adı':ogrenci_ad_2, 
                               '2.Öğrencinin Soyadı':ogrenci_soyad_2,
                               '2.Öğrencinin Telefon Numarası':ogrenci_tel_no_2
                            },

                ogrenci_no_3:{
                              '3.Öğrencinin Adı':ogrenci_no_3,
                              '3.Öğrencinin Soyadı':ogrenci_soyad_3,
                              '3.öğrencinin Telefon Numarası':ogrenci_tel_no_3
                            }                        

                }




#2-->Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin
ogrenci_no=input("Öğrenci Numarası: ")
print(f"{ogrenci_no} numaralı öğrencinin bilgileri gösteriliyor")
print(ogrenciler_dic[ogrenci_no])
#bundan farklı olarak alınan her öğrenci bilgidi applet metodu ile listeye eklenir
