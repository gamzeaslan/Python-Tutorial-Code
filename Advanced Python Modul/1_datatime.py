#hazır modül kullanılmadan önce import edilmelidir
from datetime import datetime,timedelta

#eğer modül içerisinden sadece belli şeyleri impport ediceksek
from datetime import datetime#--->from -modül -import -import edilecek kısım

#modülün alt bileşenlerini listelemek için
print(dir(datetime))

simdi=datetime.now()
print(simdi)#çıktı:2022-10-12 16:56:48.442795 şeklindedir

simdi=datetime.today()
print(simdi)#çıktı:2022-10-12 16:56:48.442795 şeklindedir

#ikiside aynı çıktıyı veriyorsa neden sadece biri kullanılmıyor:
"""datetime.now() ve datetime.today() arasındaki fark şudur:
today:yalnızca bugünün tarihini def değeri 12:00:00 dır 
now:ise çalışan iş parçacığının çalışma saatini verir-->kodun çalıştığı bilgisayarın saatini verir

yani eğer zaman diliminden kaynaklı bir farklılık yaşanırsa bu metotaların çalıması sonucu çıktılar farklı olabilir
"""


#yukarıda oluşturulan simdi değişkenin gösterdiği zamana gün,ay vb olarak erişilebiliinir

#yıla erişim
print(f"yıl: {datetime.now().year}")

#aya erişim
print(f"ay: {datetime.now().month}")

#güne erişim
print(f"gün: {datetime.now().day}")

#aynı şekilde hour-->saat // minute-->dk // second-->saniyeye erişilebilinir

now=datetime.today()
import time

print(datetime.ctime(now))#bu bir datetime objesi bekler parametre olarak--->bu metot şuanla alakalı daha açıklayıcı bir tarih bilgisi verir-->çıktısı:Wed Oct 12 18:20:41 2022 şeklindedir


# herhangi bir zamanı herhangi bir zaman birimine formatlamak için:

# şimdiki zaman bilgisinden yıl bilgisini çeker
print(datetime.strftime(now,'%Y'))
# eğer metota zaman üzerinden erişmek istersek
print(now.strftime('%Y'))#yine çıktı olarak belirtilen zamandaki yıl bilgisini verir--->now bir nesne mi??

# buradaki formatlar şunlar:
print(now.strftime('%X'))#saat,dakika ve saniye bilgisini verir
print(now.strftime('%d'))#mevcut tarihin gün bilgisini verir
print(now.strftime('%A'))#mevcut tarihini gün adını verir
print(now.strftime('%B'))#mevcut tarihin ay bilgisini full name olarak verir
print(now.strftime('%b'))#mevcur tarihini ay bilgisini kısaltarak verir

# bir satırda birden fazla zaman biriminin bilgisini isteyebiliriz
print(now.strftime('%Y %B %A'))#çıktı :2022 October Wednesday şeklindedir eğer formatların yerini değiştirirsek
print(now.strftime('%A %B %Y'))#çıktıda değişir:Wednesday October 2022 parametre sıralaması önemlidir
from datetime import date



# time isimli bir datetime türünden bir obje tanımlarsak
time=datetime(2010,1,8,13,24,45)
# tanımladığımız objeyi ekrana yazdırma
print(time)

# tanımladığımız obje üzerinden bir formatlama yapmak istersek
print(time.timestamp())#mevcut time değerini saniye cinsinden verir
print(datetime.fromtimestamp(time.timestamp()))#parametre olarak verdiğimiz değişkenin saniye türünden olması lazım .Burada yukarıda saniyeye dönüştürdüğümüz zaman ifadesini tekrardan 2010-01-08 13:24:45 biçimine dönüştürdük

# str zaman ifadesini datetime türünden bir nesneye dönüştürmenin farklı ama uzun bir yolu daha vardır :
time_2="12 April 2022"
# split metodunu kullanarak bu karakter dizisini parçalarız
gun,ay,yil=time_2.split()#def olarak boşluk karakteri alır
print(f"{gun} {ay} {yil}")

#eğer str türünden zaman ifadesi yukarıdaki gibi açıklayı elemanlardan oluşmazsa :
time_3="24 April 2022 hour 12:23:34"
# yukarıdaki zaman ifadesini eğer split metodunu kullanarak elemanlarını parçalarsak yukarıdaki gibi her elemanı bir zaman ifadesini karşılık gelmediği için önce zaman ifadesine karşılık gelmeyen ifadeleri bu karakter dizisinden silmeliyiz
gun,ay,yil,saat=[i for i in time_3.split() if 'hour' not in i]
print(f"{gun} {ay} {yil} {saat} ")
# yukarıdaki ifade hem uzun hem de buradan saat ,dakika ve saniye ifadelerine ayrı ayrı ulaşamıyoruz
# bunun için strptime() metotu kullanılır
t="15 April 2019 hour 10:12:30"#str zaman ifadesi bilgisayar içinde tanımlı olan bir zaman ifadesine çevirmek için:
t=datetime.strptime(t,'%d %B %Y hour %H:%M:%S')#çıktı:2019-04-15 10:12:30 şeklindedir ve yukarıdaki metotla karıştırma 
# strptime!=strftime

# bundan sonra str türünden girilen tarih bilgisine mevcut metotlarla erişebilirz
print(t.day)
print(t.year)#str türünden girilen zaman bilgisi artık bilg tarafından da kabul edilen bir zaman ifadesidir





# str zaman ifadesini for döngüsünü kullanarak parçalara ayırabiliriz fakat bu işlem sonucunda aldığımız çıktılar bir datetime nesnesi değildir bu yüzden datetime içinde geçerli olan metotlar kullanılamaz

time="15 April 2020 hour 10:23:34"
gun,ay,yil,saat=[i for i in time.split() if 'hour' not in i]
print(gun,ay,yil,saat)

#date cocorresponding(zaman damgası):genellikle UNIX'te kullanılan ve belirli bir olayın meydana geldiği tarih ve saati gösteren kodlanmış bilgilerdir. Bu bilgi mikrosaniyeler kadar doğru olabilir. Datetime örneğine karşılık gelen bir POSIX zaman damgasıdır.


#timestamp() işlevi belirtilen bir date corresponding(zaman damgası) karşılık gelen tarihi döndürmek için kullanılır--->döndürdüğü değer saniye türündendir daha düzgün bir zaman ifadesine çevirmek için-->fromtimestamp() metotu kullanılır


# print(datetime.fromtimestamp(now))--->Bu ifade error verir parametre hatası verir  
#datetime modul metotu olan timestamp() ,datetime öreneğine karşılım gelen zaman damgasını döndürür.Dönüş değeri floattır

"""YUKARIDAKİ SANİYE ÇIKTISINI NORMAL ZAMAN İFADESİNE ÇEVİRMEK???"""

#iki zaman arasındaki farkı hesaplamak için :
#1--->şimdi zamanı hesaplayalım
now=datetime.now()

#2-->şimdi belirli bir tarihi datetime nesnesi olarak tanımlıyalım
birthday=datetime(1999,12,12,23,23,12)

fark=now-birthday#buradan elde ettiğimz şey bir timedelta nesnesidir .Bu nesne tarihler arasındaki farkı gün,saniye vb olarak tutan özel bir veri tipidir
print(fark)



#herhangi bir tarihe gün eklemek ya da çıkarmak için:
now=datetime.now()
result=now+timedelta(days=100)#timedelta kullanılmadan önce program içine import edilerek aktarılmalıdır eğer zaten direkt import datetime kullanımışsa gerek yok fakat from datetime import kullanılmışsa ek olarak timedelta da import edilmelidir
print(now)
print(result)




