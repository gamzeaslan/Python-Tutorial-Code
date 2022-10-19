import re
"""group() metotu"""
#Bu bölümde doğrudan düzenli ifadelerin değil ama düzenli ifadeler kullanılarak üretilen eşleşme nesnelerinden bahsedeceğiz.Bu metot düzenli ifadeleri kullanarak eşleştirdiğimiz karakter dizilerini görme imkanı sağlıyordu
cumle="python bir programlama dilidir"
nesne=re.search("(python) (bir) (programlama) (dilidir)",cumle)
print(nesne.group())#eşleşen karakter dizileri ekrana yazdırılır
#çıktısı:python bir programlama dilidir.Grupladığmız bu ifadelere tek tek erişebiliriz
print(nesne.group(0))#null
print(nesne.group(1))#python
print(nesne.group(2))#bir
print(nesne.group(3))#programlama
print(nesne.group(4))#dilidir

"""groups() metotu"""
#bu metot bize kullanabileceğimiz bütün gruplarıbir demet(tuple) halinde sunar:
print(nesne.groups())#çıktı:('python', 'bir', 'programlama', 'dilidir')

print()
print()

"""ÖZEL DİZİLER"""
#Düzenli ifadeler içinde metakarakterler dışında özel anlamlar taşıyan bazı başka ifadeler de vardır.Boşluk karakterinin yerini tutan özel dizi:\s
#Bu sembol bir karakter dizisi içinde geçen boşlukları yakalamak için kullanılır
a = ["5 Ocak", "27Mart", "4 Ekim", "Nisan 3"]
for i in a :
    nesne=re.search("[0-9]\s[A-Za-z]+",i)#nesne=re.search("[0-9]\\s[A-Za-z]+",i)
    if nesne:
        print(i)#çıktı:5 Ocak 4 Ekim

print()
print()

#Ondalık sayıların yerini tutan özel dizi \d 
#Bu sembol bir karakter dizisi içinde geçen ondalık sayıları eşleştirmek için kullanılır.Buraya kadar olan örneklerde bu işlevi yerine getirmek için [0-9] ifadesinden yararlanıyorduk.Şimdi artık aynı işlevi daha kısa yoldan \d dizisi ile yerine getirebiliriz

a = ["5 Ocak", "27Mart", "4 Ekim", "Nisan 3"]
for i in a :
    nesne=re.search("\d\s[A-Za-z]",i)
    if nesne:
        print(i)

print()
print()

#alfanümerik karakterlerin yerini tutan özel dizi:\w
#bu sembol bir karakter dizisi içinde geçen alfanümerik karakterleri ve buna ek olarak "_" karakterini bulmak için kullanılır
a = "abc123_$%+"
print(re.search("\w*",a).group())# a içerisindeki alfanümerik karakterlerin sıfır veya daha fazla olması durumunda eşleşme gerçekleşir
#yukarıdaki ifade=[A-Za-z0-9_] ifadesi ile denktir

#ÖZETLE
#1-->\s özel dizisi boşluk karakterlerini avlıyor 
#2-->\d özel dizisi ondalık sayıları avlıyor
#3-->\w özel dizisi alfanümerik karakterleri ve "_" karakterini avlıyor

#BUNLARIN BÜYÜK HARFLİ VERSİYONLARI
#1-->\S özel dizisi boşluk olmayan karakterleri avlar
#2-->\D özel dizisi ondalık sayı olmayan karakterleri avlar.Yani [^0-9] ile eşdeğerdir
#3-->\W özel dizisi alfanümerik olmayan karakterleri ve "_" olmayan karakterleri avlar.Yani [^A-Za-z0-9_] eşdeğerdir

print()
print()

"""DÜZENLİ İFADELERİN DERLENMESİ"""
#compile metodu
#en başta da söylediğimiz gibi düzenli ifadeler karakter dizilerine göre daha yavaş çalışır.Nacak düzenli ifadelerin işleyişini hızlandırmanın da bazı yolları vardır .Bu yollardan biri de compile metodunu kullanmaktır."compile" kelimesi "derlemek" anlamına gelmektedir.İşte biz de bu compile() metodu yardımıyla düzenli ifade kalıplarımızı kulllanmadan önce derleyerek daha hızlı çalışmalarını sağlayabiliriz.Derleme işlemi büyük projelerde büyük önem taşımaktadır
liste=["Python2.7", "Python3.2", "Python3.3","Python3.4", "Java"]
derleme=re.compile("[A-Za-z]+[0-9]\.[0-9]")
for i in liste:
    nesne=derleme.search(i)
    if nesne:
        print(i)

print()
print()


#Burada ilk başta düzenli ifade kalıbımızı derledik ve derleme işlemi yaparken parametre olarak oluşturduğumuz düzenli ifadeyi girdik(patterns) sonra for döngüsü ile liste elemanalarına erişim sağladık ve bu elemanlar üzerinden derlenen pattern bilgisi üzerinden searc metodunu çağırdık ve buna da parametre olarak arama yapavağız ifadeyi yazdık

"""compile()ile derleme seçenekleri"""

#re.IGNORECASE veya re.I
#Python da büyük-küçük harf duyarlılığı vardır.Yani eğer "python" kelimesini arıyorsanız alacağınız çıktılar arasında "Python" olmayacaktır.Çünkü "python" ve "Python" birbirinden farklı karakter dizisidir.İşte yukarıda belirtilen derleme seçeneği ile bize büyük-küçük harfe dikkat etmeden arama imkanı sağlar
metin = """Programlama dili, programcının bir bilgisayara ne yapmasınıistediğini anlatmasının standartlaştırılmış bir yoludur. Programlamadilleri, programcının bilgisayara hangi veri üzerinde işlem yapacağını,verinin nasıl depolanıp iletileceğini, hangi koşullarda hangi işlemlerin yapılacağını tam olarak anlatmasını sağlar. Şu ana kadar 2500’den fazla programlama dili yapılmıştır. Bunlardan bazıları: Pascal, Basic, C, C#,C++, Java, Cobol, Perl, Python, Ada, Fortran, Delphi programlama dilleridir."""
derleme=re.compile("programalama",re.IGNORECASE)#burada programlama patternini IGNORECASE modunda derler
print(derleme.findall(metin))


print()
print()

#re.DOTALL veya re.S
#yukarıda . metakarakterinin yeni satır(\n) karakteri dışındaki tüm karakterleri karşıladığını belirtmiştik peki biz bu karakteri de karşılamasını istersek o zaman derleme işlemini re.DOTALL modunda yapmamız gerek

a = "Ben Python,\nMonty Python"
derleme=re.compile("Python.*",re.DOTALL)
nesne=derleme.search(a)
if nesne:
    print(nesne.group())#çıktısı:
                        #     Python,
                        # Monty Python

"""Düzenli İfadelerle Metin/Karakter Dizisi Değiştirme İşlemleri"""
#sub() metodu
#Şimdiye kadar hep düzenli ifadeler yoluyla bir karakter dizisini nasıl eşleştireceğimizi inceledik. Ama tabii ki düzenli ifadeler yalnızca bir karakter dizisi “bulmak”la ilgili değildir. Bu araç aynı zamanda bir karakter dizisini “değiştirmeyi” de kapsar. Bu iş için temel olarak iki metot kullanılır. Bunlardan ilki sub() metodudur.İkincisi ise subn() metodudur
a = "Kırmızı başlıklı kız, kırmızı elma dolu sepetiyle \
anneannesinin evine gidiyormuş!"
derle = re.compile("kırmızı", re.IGNORECASE)
print(derle.sub("yeşil", a))
#Burada karakter dizimiz içinde geçen bütün “kırmızı” kelimelerini “yeşil” kelimesiyle değiştirdik. Bunu yaparken de re.IGNORECASE adlı derleme seçeneğinden yararlandık.

# Elbette sub() metoduyla daha karmaşık işlemler yapılabilir. Bu noktada şöyle bir hatırlatma yapalım. Bu sub() metodu karakter dizilerinin replace() metoduna çok benzer. Ama tabii ki sub() metodu hem kendi başına replace() metodundan çok daha güçlüdür, hem de beraber kullanılabilecek derleme seçenekleri sayesinde replace() metodundan çok daha esnektir. Ama tabii ki, eğer yapmak istediğiniz iş replace() metoduyla halledilebiliyorsa en doğru yol, replace() metodunu kullanmaktır…
print()
print()

"""subn()metodu"""

#Tek farkı, subn() metodunun bir metin içinde yapılan değişiklik sayısını da göstermesidir.Bu metot çıktı olarak iki öğeli bir demet verir. Birinci öğe değiştirilen metin, ikinci öğe ise yapılan değişiklik sayısıdır. Yani kullanıcıya değişiklik sayısını göstermek için yapmanız gereken şey, bu demetin ikinci öğesini almaktır

metin = """Karadeniz Ereğlisi denince akla ilk olarak kömür ve demir-çelik
gelir. Kokusu ve tadıyla dünyaya nam salmış meşhur Osmanlı çileği ise ismini
verdiği festival günleri dışında pek hatırlanmaz. Oysa Çin'den Arnavutköy'e
oradan da Ereğli'ye getirilen kralların meyvesi çilek, burada geçirdiği değişim
sonucu tadına doyulmaz bir hal alır. Ereğli'nin havasından mı suyundan mı
bilinmez, kokusu, tadı bambaşka bir hale dönüşür ve meşhur Osmanlı çileği
unvanını hak eder. Bu nazik ve aromalı çilekten yapılan reçel de likör de bir
başka olur. Bu yıl dokuzuncusu düzenlenen Uluslararası Osmanlı Çileği Kültür
Festivali'nde 36 üretici arasında yetiştirdiği çileklerle birinci olan Kocaali
Köyü'nden Güner Özdemir, yılda bir ton ürün alıyor. 60 yaşındaki Özdemir,
çileklerinin sırrını yoğun ilgiye ve içten duyduğu sevgiye bağlıyor: "Erkekler
bahçemize giremez. Koca ayaklarıyla ezerler çileklerimizi" Çileği toplamanın zor
olduğunu söyleyen Ayşe Özhan da çocukluğundan bu yana çilek bahçesinde
çalışıyor. Her sabah 04.00'te kalkan Özhan, çileklerini özenle suluyor. Kasım
başında ektiği çilek fideleri haziran başında meyve veriyor."""

derle = re.compile("çile[kğ]", re.IGNORECASE)
def degistir(nesne):
    a = {"çileğ":"eriğ", "Çileğ":"Eriğ", "Çilek":"Erik", "çilek":"erik"}
    b = nesne.group().split()
    for i in b:
        return a[i]

ab = derle.subn(degistir, metin)
print("Toplam {} değişiklik yapılmıştır.".format(ab[1]))
"""sub ve subn sonra tekrar çalış"""