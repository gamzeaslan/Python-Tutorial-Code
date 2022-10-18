#regular expression (düzenli ifadeler),düzenli ifadelerin Python içinde ayrı olarak düşünülmesi gerektiğini söyleyenler dahi vardır
#bu ifadeler toplu aramalarda ya da listelemelerde çok zaman kazandıran yapılardır fakat kullanımı önerilmemektedir.Eğer Python'daki karakter dizisi metotları o anda yapmak istediğimiz şey için yeterli geliyorsa mutlaka o metotları kullanmalıyız.Çünkü karakter dizisi metotları, düzenli ifadelere kıyasla hem daha basit, hem de çok daha hızlıdır. Fakat eğer kod karmaşıklaşmaya başlamışsa bu noktada artık düzenli ifadeleri kullanmaya başlarız

#Python'daki düzenli ifadelere ilişkin her şey bir modül içinde tutulur bu modül re modülüdür
import re 
# print(dir(re))
# print(help(re))
#yardım bölümünden çıkmak için 'q' düğmesine basmanız gerekir
"""--------Match Metotu---------"""
#bu metotun işlevini bir örnek üzerinden inceleyelim
cumle="Python güçlü bir programlama dilidir"
# Varsayalım ki biz bu karakter dizisi içinde ‘python’ kelimesi geçip geçmediğini öğrenmek istiyoruz. Ve bunu da düzenli ifadeleri kullanarak yapmak istiyoruz. Düzenli ifadeleri bu örneğe uygulayabilmek için yapmamız gereken şey, öncelikle bir düzenli ifade kalıbı oluşturup, daha sonra bu kalıbı yukarıdaki karakter dizisi ile karşılaştırmak. Biz bütün bu işlemleri match() metodunu kullanarak yapabiliriz:
print(re.match("Python",cumle))
# Burada, ‘python’ şeklinde bir düzenli ifade kalıbı oluşturduk. Düzenli ifade kalıpları match() metodunun ilk argümanıdır (yani parantez içindeki ilk değer). İkinci argümanımız ise (yani parantez içindeki ikinci değer), hazırladığımız kalıbı kendisiyle eşleştireceğimiz karakter dizisi olacaktır.
# Klavyede ENTER tuşuna bastıktan sonra karşımıza şöyle bir çıktı gelecek:

# <_sre.SRE_Match object; span=(0, 6), match='python'>
# Bu çıktı, düzenli ifade kalıbının karakter dizisi ile eşleştiği anlamına geliyor. Yani aradığımız şey, karakter dizisi içinde bulunmuş.

# # Yukarıdaki çıktıda gördüğümüz ifadeye Python’cada eşleşme nesnesi (match object) adı veriliyor. Çünkü match() metodu yardımıyla yaptığımız şey aslında bir eşleştirme işlemidir (match kelimesi İngilizcede ‘eşleşmek’ anlamına gelir). Biz burada ‘python’ düzenli ifadesinin a değişkeniyle eşleşip eşleşmediğine bakıyoruz. Yani re.match("python", a) ifadesi aracılığıyla ‘python’ ifadesi ile a değişkeninin tuttuğu karakter dizisinin eşleşip eşleşmediğini sorguluyoruz. Bizim örneğimizde ‘python’ a değişkeninin tuttuğu karakter dizisi ile eşleştiği için bize bir eşleşme nesnesi döndürülüyor.

# # Bu çıktı, düzenli ifade kalıbının karakter dizisi ile eşleştiğini bildirmenin yanı sıra, bize başka birtakım bilgiler daha veriyor. Mesela bu çıktıdaki span parametresi, aradığımız ‘python’ karakter dizisinin, a değişkeninin 0. ila 6. karakterleri arasında yer aldığını söylüyor bize. Yani:
# a[0:6]

# 'python'
# Ayrıca yukarıdaki çıktıda gördüğümüz match parametresi de bize eşleşen ifadenin ‘python’ olduğu bilgisini veriyor.

# Bir de şu örneğe bakalım:

# re.match("Java", a)
# Burada ENTER tuşuna bastığımızda hiç bir çıktı almıyoruz. Aslında biz görmesek de Python burada “None” çıktısı veriyor. Eğer yukarıdaki komutu şöyle yazarsak “None” çıktısını biz de görebiliriz:

# print(re.match("Java", a))

# None
# Gördüğünüz gibi, ENTER tuşuna bastıktan sonra “None” çıktısı geldi. Demek ki “Java” ifadesi, “a” değişkeninin tuttuğu karakter dizisi ile eşleşmiyormuş. Buradan çıkardığımız sonuca göre, Python match() metodu yardımıyla aradığımız şeyi eşleştirdiği zaman bir eşleşme nesnesi (match object) döndürüyor. Eğer eşleşme yoksa, o zaman da “None” değerini döndürüyor.

# Biraz kafa karıştırmak için şöyle bir örnek verelim:

# a = "Python güçlü bir dildir"
# re.match("güçlü", a)
# Burada “a” değişkeninde “güçlü” ifadesi geçtiği halde match() metodu bize bir eşleşme nesnesi döndürmedi. Peki ama neden?

# Aslında bu gayet normal. Çünkü match() metodu bir karakter dizisinin sadece en başına bakar. Yani “Python güçlü bir dildir” ifadesini tutan a değişkenine re.match(“güçlü”, a) gibi bir fonksiyon uyguladığımızda, match() metodu a değişkeninin yalnızca en başına bakacağı ve a değişkeninin en başında “güçlü” yerine “python” olduğu için, match() metodu bize olumsuz yanıt veriyor.

# Aslında match() metodunun yaptığı bu işi, karakter dizilerinin split() metodu yardımıyla da yapabiliriz:

# a.split()[0] == "python"

# True
# Demek ki a değişkeninin en başında “python” ifadesi varmış. Bir de şuna bakalım:

# a.split()[0] == "güçlü"

# False
# Veya aynı işi sadece startswith() metodunu kullanarak dahi yapabiliriz:

# a.startswith("python")
# Eğer düzenli ifadelerden tek beklentiniz bir karakter dizisinin en başındaki veriyle eşleştirme işlemi yapmaksa, split() veya startswith() metotlarını kullanmak daha mantıklıdır. Çünkü split() ve startswith() metotları match() metodundan çok daha hızlı çalışacaktır.

# match() metodunu kullanarak birkaç örnek daha yapalım:

# sorgu = "1234567890"
# re.match("1", sorgu)

# <_sre.SRE_Match object; span=(0, 1), match='1'>

# re.match("1234", sorgu)

# <_sre.SRE_Match object; span=(0, 4), match='1234'>

# re.match("124", sorgu)
# İsterseniz şimdiye kadar öğrendiğimiz şeyleri şöyle bir gözden geçirelim:

# Düzenli ifadeler Python’ın çok güçlü araçlarından biridir.

# Python’daki düzenli ifadelere ilişkin bütün fonksiyonlar re adlı bir modül içinde yer alır.

# Dolayısıyla düzenli ifadeleri kullanabilmek için öncelikle bu re modülünü import re diyerek içe aktarmamız gerekir.

# re modülünün içeriğini dir(re) komutu yardımıyla listeleyebiliriz.

# match() metodu re modülü içindeki fonksiyonlardan biridir.

# match() metodu bir karakter dizisinin yalnızca en başına bakar.

# Eğer aradığımız şey karakter dizisinin en başında yer alıyorsa, match() metodu bir eşleştirme nesnesi döndürür.

# Eğer aradığımız şey karakter dizisinin en başında yer almıyorsa, match() metodu “None” değeri döndürür.

# Daha önce söylediğimiz gibi, match() metodu ile bir eşleştirme işlemi yaptığımızda, eğer eşleşme varsa Python bize bir eşleşme nesnesi döndürecektir. Döndürülen bu eşleşme nesnesi bize span ve match parametreleri aracılığıyla, eşleşen karakter dizisinin sorgu dizisi içindeki yerini ve eşleşen dizinin ne olduğu söylüyor. span parametresinin değerine span() adlı bir metot yardımıyla erişebiliyoruz. Örneğin:

# import re
# sorgu = 'Bin kunduz'
# eşleşme = re.match('Bin', sorgu)
# eşleşme

# <_sre.SRE_Match object; span=(0, 3), match='Bin'>

# eşleşme.span()
# (0, 3)
# Ancak, match() metodu ile bulunan şeyin ne olduğunu eşleşme nesnesinin match parametresine bakarak görebilsek de, bu değeri bir kod yardımıyla alamıyoruz. Çünkü eşleşme nesnelerinin span() metoduna benzeyen bir match() metodu bulunmaz.

# Ama istersek tabii ki bulunan şeyi de programatik olarak alma imkânımız var. Bunun için group() adlı bir başka metottan yararlanacağız:

# kardiz = "perl, python ve ruby yüksek seviyeli dillerdir."
# eşleşme = re.match("perl", kardiz)
# eşleşme.group()

# 'perl'
# Burada, re.match("perl", kardiz) komutunu bir değişkene atadık. Hatırlarsanız, bu fonksiyonu komut satırına yazdığımızda bir eşleşme nesnesi elde ediyorduk. İşte burada değişkene atadığımız şey aslında bu eşleşme nesnesinin kendisi oluyor. Bu durumu şu şekilde teyit edebilirsiniz:

# type(eşleşme)

# <class '_sre.SRE_Match'>
# Gördüğünüz gibi, eşleşme değişkeninin tipi bir eşleşme nesnesi (match object). İsterseniz bu nesnenin metotlarına bir göz gezdirebiliriz:

# dir(eşleşme)
# Dikkat ederseniz yukarıda kullandığımız group() metodu listede görünüyor. Bu metot, doğrudan doğruya düzenli ifadelerin değil, eşleşme nesnelerinin bir metodudur. Listedeki öbür metotları da sırası geldiğinde inceleyeceğiz. Şimdi isterseniz bir örnek daha yapıp bu konuyu kapatalım:

# iddia = "Adana memleketlerin en güzelidir!"
# nesne = re.match("Adana", iddia)
# nesne.group()

# 'Adana'
# Peki, eşleştirmek istediğimiz düzenli ifade kalıbı bulunamazsa ne olur? Öyle bir durumda yukarıdaki kodlar hata verecektir. Hemen bakalım:

# nesne = re.match("İstanbul", iddia)
# nesne.group()
# Hata mesajımız:

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'NoneType' object has no attribute 'group'
# Böyle bir hata, yazdığınız bir programın çökmesine neden olabilir. O yüzden kodlarımızı şuna benzer bir şekilde yazmamız daha mantıklı olacaktır:

# nesne = re.match("İstanbul", iddia)
# if nesne:
#     print("eşleşen ifade:", nesne.group())
# else:
#     print("eşleşme başarısız!")


""" ---------search() Metotu---------"""
#match metodu karakter dizilerinin sadece en başına bakar eğer tüm dizi üzerinde bir arama işlemi yapmak istiyorsak search() metodu kullanılır bu metot sonucu geriye döndürülen değer bir match objesidir

#yani match metodu ile search öetdu arasındaki fark:match metodu bir karakter dizisinin en başına bakıp bir eşleşme yaparken,search metodu karakter dizisinin genelinde bir arama işlemi yapar.Yani biri eşleştirir,öbürü arar.Tıpkı match metodunda olduğu gibi search metodunda da span() ve group() metotlarından faydalanarak bulunan şeyin hangi aralıkta olduğunu ve  bu şeyin  ne olduğunu görüntüleyebiliriz

cumle="Python güçlü bir programlama dilidir"
nesne=re.search("bir",cumle)
#eğer arama sonucu bir nesne geriye dönmezse kod hata verir programdaki bu çökmeyi engellemek için if-else yapısı kullanılır 
if nesne:#sanırımı koşul ifadesi olarak nesnenin verilmesinin sebebi bunun geriye bir bool ifade döndürmesinden kaynaklanmaktadır
    print(f"nesnenin bulunduğu aralık:{nesne.span()}")
    print(f"aranılan nesne: {nesne.group()}") 

#hep karakter dizileri üzerinde örnek verdik şimdi de listeler üzerinde örnek verelim
    
liste = ["elma", "armut", "kebap"]
#eğer böyle bir kullanım yapmaya çalışırsak
# re.search("elma",liste)-->bu kullanım yanlıştır çünkü düzenli ifadeler doğrudan listeler üzerinde işlem yapamaz , karakter dizileri üzerinde işlem yapabilir    
for  i in liste:
    nesne= re.search("elma",i)
    if nesne:
        print(f"eleman bulundu : {nesne.group()}")#for içinde yazıldığından her eleman için bir çıktı üretilir 
    else:
        pass
        # print("eleman bulunamadı")
        

#daha karmaşık bir örnek yaparsak
from urllib.request import urlopen #burada urllip paketi içindeki request modülü içerisindeki urlopen metodu programın içine aktarıldı
f=urlopen("https://python-istihza.yazbel.com/")

#for döngüsü ile bu sayfa içeriğine tek tek ulaşılır 
for i in f:
    nesne=re.search(b'yazbel',i)#bu bir karakter dizisi değil byte dizisidir
    if nesne:
        print(nesne.group())#bir çıktı üretmiyor ya linkten kaynaklı ya da aranılan ifadeden kaynaklı----->byte türünden bir arama işlemi yapınca çıktı üretti  



kelime=input("python-istihza.yazbel.com'da aramak istediğiniz kelime: ")
f = urlopen("https://python-istihza.yazbel.com/") 
#şimdi sayfayı okuyarak bu sayfayı str türüne dönüştüreceğiz
str_f=str(f.read())
#şimdi search metodu ile bir arama işlemi gerçekleştirirsek
nesne=re.search(kelime,str_f)
if nesne:
    print(nesne.group())

#burada search ile arama işlemi yapmadan çnce str() metodu yardımıyla karakter dizisine dönüştürüyoruz.Böylece kullanıcıdan gelen karakter dizisini bayt dizisine çevirmemize gerek kalmaz 



"""findall()"""
#eğer bir topluluk içerisinde herhengi bir ifadeyi arayaıp bu ifadeyi içeren tüm değerleri bulup bir liste içerisine atmak istiyorsak hatta bu yeni oluşturduğumuz liste uzunluğundan bu ifadenin topluluk içerinde kaç kez geçtiğini de hesaplayabiliriz 

#aslında bu metodu kullanmadan sadece search metodunu kullanarak da bu işlemi gerçekleştirebiliriz ancak yolu biraz uzatmamız gerekir
 
metin ="Python, yazılım geliştirme ve veri analizi için kullanılan  Python bir programlama dilidir. Genellikle bir web sunucusunda web uygulamaları kullanmak için kullanılır. Günümüzde Python en çok kullanılan programlama dillerinden biridir Python."

#bu metin içerisinde geçen Python kelimelerini bulmak istiyorsak

#eğer bu işlemi search metotu ile yaparsak

for i in metin.split():#eğer split ile ayırmazsak sadece bir kez yazdırır ekrana Python çıktısını
    nesne=re.search("Python",i)
    if nesne:
        print(nesne.group())

print()
print()


#eğer işlemi bu kadar uzatmak istemiyorsak findall metodunu kullanırız
print(re.findall("Python",metin))
print(len(re.findall("Python",metin)))#buradan bu karakterin metinde kaç kere geçtiğini hesaplayabiliriz


print()
print()


#Bu zamana kadar işlediğimiz örneklerde her düzenli ifade kendisi ile eşleşiyordu yani eğer bir cümle içerinde python kelimesini aramak istiyorsak search ya da match metotlarına parametre olarak python ifadesini ilk parametre olarak veririz bu şekilde python ifadesinin kendisi ile eşleştiğini söyleyebiliriz fakat kendisi ile eşleşmeyen ifadeler de vardır burada devreye metakarakterler giriyor 


"""META KARAKTERLER"""
#“Düzenli ifadeler en başta kendileriyle eşleşirler”. Buradan şu anlam çıkıyor: Demek ki bir de kendileriyle eşleşmeyen düzenli ifadeler var
#Metakarakterler kısaca programlama dilleri için özel anlam ifade eden sembollerdir .Mesela \n karakteri gibi kendileriyle eşleşmezler python bu karakteri gördüğünde yeni satıra geçer


# Python’da bulunan temel metakarakterleri topluca görelim:

# [ ] . \* + ? { } ^ $ | ( )


"""[] METAKARAKTERİ"""
liste=["özcan", "mehmet", "süleyman", "selim","kemal", "özkan", "esra", "dündar", "esin","esma", "özhan", "özlem"]
# bu listedeki özcan,özhan ve özkan elemanlarını [] metakarakterini kullanarak ayıklıyacağız
# print(re.search("öz[chk]an",liste))-->Bu kodu böyle yazamayız çünkü düzenli ifadeler listeler üzerinde çalışmaz string dizileri üzerinde çalışır
for i in liste:
    nesne=re.search("öz[chk]an",i)
    if nesne:
        print(nesne.group())
# ya da 
for i in liste:
    if re.search("öc[chk]an",i):
        print(i)        
#yukarıdaki örnekte belli olmasa da group yerine direkt değişkenin kendisini ekrana çıktı olarak verirsek sadece almak istediğimiz kısım değil ilgisiz kısımlar da gelecektir(mesela isim yanında soyisim bilgisi de verilmişse group metodunu kullandığımızda çıktı olarak sadece isim bilgisi verilir fakat değişkenin kendisini direkt ekrana yazdırırsak hem isim hem de soyisim bilgisi ekrana yazdırmış oluruz)   

#Python yukarıdaki kodda belirttiğimiz köşeli parantez içinde gördüğü bütün karakterleri tek tek liste öğelerine uyguluyor 
      


print()
print()


a=["23BH56","TY76Z","4Y7UZ","TYUDZ","34534"]

#bu listedeki elemanlardan sadece sayıyla başlayanları(başlangıçta bir arama yapacağımızdan search yerine match metodunu kullanmalıyız) ekrana yazdırmak istersek:
for i in a :
    nesne=re.match("[0-9]",i)
    if nesne:
        print(i)#burada çıktı olarak direkt elemanları 

print()
print()

for i in a :
    nesne=re.match("[0-9]",i)
    if nesne: 
        print(nesne.group())#burada ise 2,4 ve 3 çıktılarını verir yani sadece eşleşme sonucunu verir tüm elemanı çıktı olarak vermez

print()
print()

#eğer çıktı olarak sadece“TY76Z” öğesini çıktı olarak vermek istiyorsak:
for i in a:
    nesne=re.match("[A-Z][A-Z][0-9]",i)#eğer match yerine search metodunu kullanırsak bu metot tüm öğe içerisinde arama yapacağından 23'BH5'6 çıktısını da ekrana yazdırır bu yüzden match metodu kullanırız.Karakter dizisi içindeki geri kalan harfler ve sayılar otomatik olarak eşleşecektir 
    if nesne:
        print(i) 
        #burada da öğenin kendisini ekrana yazdırmak yerine group metodunu kullanarak yazdırırsak TY7 çıktısını alırız yani sadece aranılan kısımın çıktısını alırız


print()
print()


#eğer büyük harfle ya da sayıyla başlayan öğeleri yazdırmak istiyorsak
for i in a :
    nesne=re.match("[0-9A-Z]",i)
    if nesne:
        print(i)#burada çıktı olarak büyük harfle başlayan ya da sayıyla başlayan öğeleri çıktı olarak ekrana yazdırır



print()
print()

""".(NOKTA) METAKARAKTERİ"""
#bu metakarakter yeni satır(\n) karakteri hariç 
liste=["esma","esra","eslem","esen","eren","zesra"]
for  i in liste:
    nesne=re.search("es.a",i)#esma,esra ve zesra çıktıları üretildi search metodu kullanıldığında.Burada öğe genelinde bu karakterler arandığından bazen alakasız çıktılar alabiliriz
    if nesne:
        print(i)


print()
print()

#eğer search yerine match metodu kullanırsak
for i in liste:
    nesne=re.match("es.a",i)
    if nesne:
        print(i)#burada çıktı olarak sadece esma ve esra öğeleri yazdırır ekrana -->burada baçtan itibaren bir arama daha doğrusu eşleşme yapılır

#NOT:Bu "." adlı metakarakter sadece tek bir karakterin yerini tutuyor
# Yani şöyle bir kullanım bize istediğimz sonucu vermez

print()
print()

liste = ["ahmet","kemal", "kamil", "mehmet","emet"]  
for i in liste:
    nesne=re.match(".met",i)
    if nesne:
        print(i)
        #burada . metakarakteri sadece bir karaktere karşılık geldiğinden çıktı olarak sadece "emet" çıktısını verir       



print()
print()


#bu . metakarakteri ile ilgili başka bir örnek verelim
a=["23BH56","TY76Z","4Y7UZ","TYUDZ","34534","56AV90"]   
#bu listeden:
# Herhangi bir karakterle başlayacak(. metakarakteri kullanacağız).Bu karakter sayı ,harf veya başka bir karakter olabilir 
#Ardından bir sayı veya alfabedeki küçük harflerden herhangi birisi gelicek
# Bu ölçütleri karşıladıktan sonra aradığımız karakter dizisi herhangi bir karakter ile devam edebilir     
for i in a:
    nesne=re.match(".[0-9a-z]",i)
    if nesne:
        print(i)


print()
print()


""" (*) YILDIZ METAKARAKTERİ """
#Bu metakarakter kendinden önce gelen bir düzenli ifade kalıbını sıfır veya daha fazla sayıda eşleştirir.Bir örnek üzerinde tanımı anlamaya çalışalım:
yeniliste=["st","sat","saat","saaat","set"]
for i in yeniliste:
    nesne=re.match("sa*t",i)#burada * metakarakteri a karakterinden sonra kullanıldığından s ve t karakterleri arasında 0 veya daha fazla sayıda a karakteri varsa eşleştirir.biz yazdığımız düzenli ifadede, aradığımız şeyin “s” harfi ile başlamasını, sıfır veya daha fazla sayıda “a” karakteri ile devam etmesini ve ardından da “t” harfinin gelmesini istemiştik. “set” öğesi bu koşulları karşılamadığı için süzgecimizin dışında kaldı.
    if nesne:
        print(i)
        #çıktı olarak:
        # st
        # sat
        # saat
        # saaat çıktılarını verir set öğesi arama kriterine uymadığından ekrana çıktı olarak yazdırılmaz 

#Burada * metakarakterinin kendinden önce gelen yalnızca bir karakterle ilgileniyor olması.Yukarıdaki örnekte sadece a karakteri için sıfır veya daha fazla bulunup bulunmamasıyla ilgili bir eşleşme işlemi gerçekleştiriyor.Eğer s içinde böyle bir eşleşme gerçekleştirmek istersek:"s*a*t" ya da [sa]*t şeklinde yazabiliriz.Bu iki seçenek içinden [sa]*t şeklindeki yazımı tercih etmelisiniz




print()
print()

#yukarıda .metakarakterini anlatırken bu karakterin sadece bir karakteri karşıladığı için yaptığımız bir örnekte istediğimiz bir sonucu alamamıştık şimdi aynı örneği hem . hem de * metakarakterini kullarak yapalım

liste = ["ahmet","kemal", "kamil", "mehmet","emet"] #tekrar aynı atamayı yapınca hata vermiyormuş sadece atama yaptıktan sonra tip dönüşümünü belirtmeden(metot kullanmadan) yapamazsın
for i in liste:
    nesne=re.match(".*met",i)
    if nesne:
        print(i)
#burada sonu met ile biten (met dahil) bütün öğeleri listeleyecektir
#Burada Python’a şu emri verdik: “Bana kelime başında herhangi bir karakteri (“.” sembolü herhangi bir karakterin yerini tutuyor) sıfır veya daha fazla sayıda içeren ve sonu da “met” ile biten bütün öğeleri ver!”.Kısaca ifade etmek gerekirse, sonu “met” ile biten her şey (“met” ifadesinin kendisi de dâhil olmak üzere) kapsama alanımıza girecektir


print()
print()

#bunu dosya uzantılarını ekrana yazdırmak ya da bir yere aynı uzantılı dosyaları bir klasöre toplamak istediğimizde yapabiliriz

dizin=["dosya.jpeg","dosya.mp3","dosya.doc","dosya2.mp3","dosya2.doc","dosya3.mp3"]
for i in dizin:
    nesne=re.match(".*mp3",i)
    if nesne:
        print(i)
        #burada çıktı olarak:
        
        # dosya.mp3
        # dosya2.mp3
        # dosya3.mp3 çıktılarını verir
 

print()
print()


#bu metakarakteri kullanılarak match metodunun search metodu gibi davranılması sağlanabilinir ama match() metodunu bu şekilde zorlamak yerine performans açısından en doğru yol bu tür işler için search() metodunu kullanmak olacaktır

a="Python güçlü bir dildir"
print(re.match("güçlü",a))#çıktı:None
print(re.match(".*güçlü",a))#çıktı:<re.Match object; span=(0, 12), match='Python güçlü'>span dikkat et güçlü ifadesinin aralığını vermemiş güçlü ifadesine gelene kadar geçen tüm karakterleri de aralığa almış .Bu yapıyı kullanarak yanlıl aralık bulabiliriz bunun yerine search metodu kullanmalıyız

print()
print()

"""+ METAKARAKTERİ"""
#bu metakarakterler ,bir önceki metekarakterimiz olan "*" ile benzerdir."*" metakarakteri kendinden önceki sıfır veya daha fazla sayıda tekrar eden karakterleri ayıklıyordu."+" metakarakteri ise kendisinden önceki "bir" veya daha fazla sayıda tekrar eden karakterleri ayıklar 
liste=["ahmet","kemal", "kamil", "mehmet","emet","met"]
#eğer * metakarakterini kullanırsak 
for i in liste:#split metodu kullanmam saçma oldu zaten split metodu bir karakter dizisinin elemanlarını listeye dönüşütürür.Bunu bir listeye uygulayınca hata verir kod 
    nesne=re.match(".*met",i)
    if nesne:
        print(i)#burada met öğesini dahil eder (çünkü 0 veya daha fazlası )
        #Burada şu komutu vermiş olduk: ” Bana sonu ‘met’ ile biten bütün öğeleri ver!


print()
print()


#eğer * metakarakteri yerine + metakarakterini kullanırsak
for i in liste:
    nesne=re.match(".+met",i)
    if nesne:
        print(i)#burada met öğesi kabul edilmez (çünkü bir veya daha fazlası)
        #Burada şu komutu vermiş olduk: ” Bana sonu ‘met’ ile biten bütün öğeleri ver! Ama bana ‘met’ öğesini yalnız başına verme!”

print()
print()

# * metakarakteri ile + metakarakteri arasındaki farkın daha iyi anlaşılabilmesi için bir örnek daha inceleyelim
yeniliste=["st", "sat", "saat", "saaat", "falanca"]

# * metakarakterini kullanırsak
for i in yeniliste:
    nesne=re.match("sa*t",i)
    if nesne:
        print(i)#burada st dahil edilir 

print()
print()


# + metakarakter kullanırsak
for i in yeniliste:
    nesne = re.match("sa+t",i)
    if nesne:
        print(i)#burada st dahil edilmez

print()
print()

#yukarıda [] metakarakterini anlatırken aşağıdaki örneği incelemiştik:
a = ["23BH56", "TY76Z", "4Y7UZ", "TYUDZ", "34534"]
for i in a:
    nesne=re.match("[A-Z][A-Z][0-9]",i)
    if nesne:
        print(i)

print()
print()

#yukarıdaki kodu daha düzenli yazmak adına + metakarakterini kullanabiliriz
for i in a:
    nesne=re.match("[A-Z]+[0-9]",i)#ifadesi de kullanılabilir
    if nesne:
        print(i)

print()
print()


"""FAKAT"""
#eğer listeyi güncellersek
a.append("AGSZ9")
for i in a:
    nesne=re.match("[A-Z]+[0-9]",i)
    if nesne:
        print(i)#burada çıktı olarak:"TY76Z" ve "AGSZ9" öğelerin verir

print()
print()

"""? METAKARAKTERİ"""
#Hatırlatma: * metakarakteri sıfır ya da daha fazla sayıda eşleşmeleri kapsıyordu
#Hatırlatma: + metakarakteri bir ya da daha fazla sayuda eşleşmeleri kapsıyordu 
#İşse şimdi ? metakarakteri de eşleşme sayısının 0 ya da 1 olduğu durumları kapsıyor 
#bu üç metakarakter arasındaki farkı daha iyi görebilmek için aynı örnek üzerinde bu metakarakterleri kullanarak verdikleri çıktıları inceleyeceğiz
liste=["st","sat","saat","saaat","set"]

# * kullanımı
for i in liste:
    nesne=re.match("sa*t",i)
    if nesne:
        print(i)#çıktısı:
        # st
        # sat
        # saat
        # saaat

print()
print()

# + kullanımı
for i in liste:
    nesne=re.match("sa+t",i)
    if nesne:
        print(i)#çıktısı:
        # sat
        # saat
        # saaat

print()
print()

# ? kullanımı
for i in liste:
    nesne=re.match("sa?t",i)
    if nesne:
        print(i)#çıktısı:
        # st
        # sat

# ? metakararakterini daha iyi anlayabilmek için bir örnek daha inceleyelim

metin = """Uluslararası hukuk, uluslar arası ilişkiler altında bir
disiplindir. Uluslararası ilişkilerin hukuksal boyutunu bilimsel bir
disiplin içinde inceler. Devletlerarası hukuk da denir. Ancak uluslar
arası ilişkilere yeni aktörlerin girişi bu dalı sadece devletlerarası
olmaktan çıkarmıştır."""

#bu metinde "uluslararası" kelimesini bulmak istiyoruz fakat metin içerisindeki bazı yerlerde uluslararası,Uluslararası ya da uluslar arası gibi kullanımların olduğunu görüyoruz tüm bu kullanımları kapsıyan bir yapı oluşturmamız lazım:
for i in metin.split():
    nesne=re.search("[Uu]luslar ?arası",i)#burada yukarıda belirttiğimiz tüm durumları kapsıyan bir aram işlemi gerçekleştirilicektir metinde
    if nesne:
        print(i)#bu döngü çıktısı olarak uluslar arası ifadesi alınmaz çünkü metini split metodu yardımıyla elemanlarını parçalayıp bir listeye atadık yani buradaki döngüde uluslar bir döngü arası bir döngü elemanı olarak kabul edilir
        #çıktısı: Uluslararası Uluslararası şeklidedir


print()
print()


#burada searc metodu işlevsiz kaldı findall metodunu kullanacağız
print(re.findall("[Uu]luslar ?arası",metin))#çıktısı:['Uluslararası', 'uluslar arası', 'Uluslararası'] şeklindedir
#boşlu karakterinin sıfır ya da bir kez geçtiği durumlar

print()
print()

"""{} METAKARAKTERİ"""
#eğer bundan öncek metakarakterlerde olduğu gibi metakarakter tarafından belirtilen karakter sayısını manuel olarak belirtmek istiyorsak o zaman {min tekrar degeri,max tekrar degeri} şeklinde metakarakter kullanımı yaparız

liste=["st","sat","saat","saaat","saaaat","set"]

for i in liste:
    nesne=re.match("sa{2}t",i)#buradaki 2 sayısı direkt tekrar sayısını verir
    if nesne:
        print(i)#çıktısı:saat şeklindedir

print()
print()

for i in liste:
    nesne=re.match("sa{2,4}t",i)
    if nesne:
        print(i)#çıktısı:
        # saat
        # saaat
        # saaaat şeklindedir

#aslında bu metakarakter kullanılarak ?,* ve + metakarakterleri elde edilebilir

print()
print()

""" ^ ŞAPKA METAKARAKTERİ"""
#bu metakarakterin 2 işlevi vardır 
"""1.işlevi:"""
#Birinci işlevi ,bir karakter dizisinin en başındaki veriyi sorgulamaktır.Yani aslında match() metodunun varsayılan olarak yerine getirdiği işlevi metakarakter yardımıyla açıkça belirterek yerine getirebiliyoruz
#aslında bu metakarakter yardımıyla search metodunu match metodu gibi kullanabiliriz(match metodunu .* metakarakterleri yardımıyla search metodu ile aynı işlevde  kullanabilmemiz gibi )
a = ['23BH56', 'TY76Z', '4Y7UZ', 'TYUDZ','34534', '1agAY54']
for i in a :
    nesne=re.search("[A-Z]+[0-9]",i)
    if nesne:
        print(i)#çıktısı:
        # 23BH56
        # TY76Z
        # 4Y7UZ
        # 1agAY54

print()
print()

for i in a:
    nesne=re.search("[A-Z]+[0-9]",i)
    if nesne:
        print(nesne.group())#sadece aranılan kısmı çıktı olarak verir.O yüzden yukarıdaki kod oldukça hassas bir çıktı verir
        #çıktısı:
        # BH5
        # TY7
        # Y7
        # AY5

print()
print()

#eğer search yerine match metodu kullanırsak:
for i in a:
    nesne=re.match("[A-Z]+[0-9]",i)
    if nesne:
        print(i)#çıktısı:TY76Z şeklindedir.Bu çıktıyı almamızın sebebi match() metodunun karakter dizilerinin en başına bakıyor olması.Buradaki çıktının aynısını search metodu ile de almak için ^ metakarakterinden yararlanacağız

print()
print()

for i in a:
    nesne=re.search("^[A-Z]+[0-9]",i)
    if nesne:
        print(i)#çıktısı:TY76Z şeklidedir match ile elde ettiğimiz çıktının aynısını search metodu ile de elde ettik
        print(nesne.group())#çıktısı:TY7 şeklindedir

print()
print()

#group metodunu kullanarak değişkenin tamamını yazdırmak için bunu açıkça belirtmemiz gerekiyor bu metot aradığımız kısımı bize çıktı olarak verdiğinden arama yaptığımız kısımda açıkça belirtmeliyiz
for i in a:
    nesne=re.search("[A-Z]+[0-9].*",i)
    if nesne:
        print(f"çıktı:{nesne.group()}")

print()
print()

#yukarıdaki aramayı genel için değil en baştan yapmak için:
for i in a:
    nesne=re.search("^[A-Z]+[0-9].*",i)
    if nesne:
        print(i)#çıktısı:'TY76Z'
        print(nesne.group())#çıktısı:'TY76Z'

print()
print()

"""2.işlevi"""
#hariç alamına gelmektedir.Bu görevini sadece [] metakarakterinin içinde kullanıldığı zaman yerine getirir .Yani eğer [] dışında ise başa bakma eğer [] içinde ise hariç işlevini yerine getirmektedir

for i in a:
    nesne=re.match("[A-Z0-9][^a-z]",i)#yani büyük harfle ya da sayıyla başlayan ama küçük harfle devam etmeyen öğeleri arar
    if nesne:
        print(f"çıktı:{i}")
        # çıktı:23BH56
        # çıktı:TY76Z
        # çıktı:4Y7UZ
        # çıktı:TYUDZ
        # çıktı:34534
#Yukarıda aradığımız ölçütler:
#Aradığımız öğe bir sayı veya büyük harf ile başlamalı
#En baştaki sayı veya büyük harften sonra küçük harf GELMEMELİ (Bu ölçütü “^” işareti sağlıyor)

print()
print()


#eğer yukarıdaki sayı veya büyük harfle başlama ve sonrasına küçük harf gelmemeli durumunu bir veya daha fazla sayıda küçük harf gelmemeli yapmak istersek
for i in a:
    nesne=re.match("[0-9A-Z][^a-z]+",i)
    if nesne:
        print(i)

"""$ METAKARAKTERİ"""
#karakter dizilerinde başta arama yapmak için [] dışında ^ metakarakteri kullanılır.Eğer bu arama işlemini başta değil sonda yapmak istiyorsak $ metakarakterini kullanırız
liste = ["at", "katkı", "fakat", "atkı", "rahat",
"mat", "yat", "sat", "satılık", "katılım"]
for i in liste:
    nesne=re.search("at$",i)#match kullanmak saçma olur 
    if nesne:
        print(i)


print()
print()

#Burada $ metakarakteri ile at ile biten öğeleri listeleriz eğer at ile başlayan öğeleri listelemek istersek

for i in liste:
    nesne=re.match("^at",i)#başta arama yaptığımızdan match kullanmak daha mantıklı olur
    if nesne:
        print(i)


print()
print()

#Gördüğünüz gibi, “^” işareti bir karakter dizisinin nasıl başlayacağını belirlerken, “$” işareti aynı karakter dizisinin nasıl biteceğini belirliyor. Hatta istersek bu metakarakterleri birlikte de kullanabiliriz:
for  i in liste:
    nesne=re.search("^at$",i)#at ile başlayıp at ile biten öğeler 
    if nesne:
        print(i)#çıktı:at

"""\(TERS BÖLÜ) METAKARAKTERİ"""
#Bu işaret bildiğimiz “kaçış dizisi”dir… Peki burada ne işi var? Şimdiye kadar öğrendiğimiz konulardan gördüğünüz gibi, Python’daki düzenli ifadeler açısından özel anlam taşıyan bir takım semboller/metakarakterler var. Bunlar kendileriyle eşleşmiyorlar. Yani bir karakter dizisi içinde bu sembolleri arıyorsak eğer, bunların taşıdıkları özel anlam yüzünden bu sembolleri ayıklamak hemencecik mümkün olmayacaktır. Yani mesela biz “$” sembolünü arıyor olsak, bunu Python’a nasıl anlatacağız? Çünkü bu sembolü yazdığımız zaman Python bunu farklı algılıyor.

liste = ["10$", "25€", "20$", "10TL", "25£"]
#eğer dolarları listelemek istersek:
#Python “$” işaretinin özel anlamından dolayı, bizim sayıyla biten bir karakter dizisi aradığımızı zannedecek, dolayısıyla da herhangi bir çıktı vermeyecektir. Çünkü listemizde sayıyla biten bir karakter dizisi yok… Peki biz ne yapacağız? İşte bu noktada “\” metakarakteri devreye girecek
for i in liste:
    nesne=re.match("[0-9]+\$",i)#yani metakarakterlerin kendisiyle eşleşmesi için \ metakarakteri kullanılır
    if nesne:
        print(i)

print()
print()

print("\\n")#çıktı :\n dir 

"""| DİK ÇİZGİ METAKARAKTERİ"""
#bu metakarakter,birden fazla ifade kalıbını birlikte eşleştirmemizi sağlar

liste = ["at", "katkı", "fakat", "atkı", "rahat","mat", "yat", "sat", "satılık", "katılım"]
for i in liste:
    nesne=re.search("^at|at$",i)#at ile biten veya başlayan karakterleri arar
    if nesne:
        print(i)
"""PARANTEZ() METAKARAKTERİ"""

#bu metakarakter yardımıyla düzenli ifadeleri gruplayacağız.Bu metakarakter bizim bir karakter dizisinin isteiğimiz kısımlarını ayıklamamıza çok büyük kolaylıklar sağlayacak
from urllib.request import urlopen

url = "http://belgeler.istihza.com/py3/index.html"
f = urlopen(url)

çıktı = "Başlık: {};\nBağlantı: {}\n"
regex = 'href="(.+html)">(.+)</a>'#düzenli ifade kalıbı oluşturulmuş(biraz html bilgisi gerek)

for i in f:
     nesne = re.search(regex, str(i, 'utf-8'))
     if nesne:
             print(çıktı.format(nesne.group(2),
                                nesne.group(1)))