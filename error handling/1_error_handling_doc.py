"""Hata Türleri"""
#1-->Programcı Hatası(error)
#2-->Program Kusurları ve Mantık Hatası(Bug)
#3-->İstisnalar(Expection)


"""Programcı Hatası(Error)"""
#Bu hata programcıdan kaynaklıdır.Programcının yaptığı syntax hatasından kaynaklı çıkan hata mesajıdır.Bu hata düzeltilmeden program çalışamıyacağından bu tür hataların farkedilmesi ve çözülmesi kolaydır


"""Program Hatası ve Mantık Hatası(Bug)"""
#Bu hata progamın çalışr durumunda herhangi bir hata vermez fakat istenşlenin dışında sonuıç üretir bu yüzden fark edilmesi zor bir hata türüdür.Mesela bir dairenin alanını hesaplarken eğer alan formülünü yanlış tanımlarsak program çalışır ancak yanlış sonuç üretir


"""İstisnalar(Expection)"""
#Bu hata türünde program bazı istisnalardan kaynaklı hata verir.Bu tür hatalarda error hatasında olduğu gibi düzeltilmeden çalıştırılmaz program

"""İstisna Hataları"""
#print(a)-->Tanımlanmayan bir değişkeni yazdırmaya çalışırsak "NameError" hatasını alırız

#int("a2b")-->Şeklinde değişken türünün dışındaki türleri değişkene atamaya çalışırsak "ValueError" hatasını alırız

#print(10/0)-->herhangi bir sayıyı 0 a bölmeye çalışırsak "ZeroDivisionError" hatasını alırız

#print("denem"e)-->Şeklinde bir syntax hatası yaparsak "SyntaxError" hatasını alırız

#error hangling-->hata yönetimi

#eğer biz program bu istisnalarla karşılaştığında hem error vermesini hem de hata mesajını ekrana yazdırmasını istiyorsak o zaman try expect yapısını kullanırız


"""Try-Expect Kullanımı"""
#try:hata ile karşılaşabileceğimiz yerleri blok içine aldığımız kısım

#expect istisna mesajı:kullanıcıya gösterilecek bilgilendirme mesajı 


#bir expect bloku ile birden fazla hata için hata mesajı oluşturabiliriz
#expect(hata_1,hata_2,hata_3):hata mesajı-- şeklinde 3 hata içinde aynı hata mesajı verilir burdaki sıkıntı her hata için aynı mesajın verilmesi ve genel bir mesaj olması kullanıcı bu mesajla sadece bir hata yaptığını anlar ne tür bir hata yaptığını anlamaz

#eğer hataların detay mesajlarını da beraberinde ekrana yazdırmasını istiyorsak
#----------------------sonra doldur burayı

#expect blokundan sonra finally bloku açılı ve çalıştırılır ve yapının amacı:Bir örnek üzerinden anlatırsak mesela bir dosya açıp üzerinde herhangi bir işlem yaptıktan sonra mutlaka dosyayı kapatmamız lazım.işte burada finally bloku kullanıyoruz


#sistem içinde olmayan ama bizim programımız için geçerli olan bir hatayı program içinde tanımlıyabiliz.Bunu da raise ile tanımlayabiliriz