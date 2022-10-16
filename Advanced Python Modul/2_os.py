#hazır modülün içe aktarılması
import os
#hazır modül içindeki metotların ve özel fonksiyonların listelenmesi
# print(dir(os))

#mevcut işletim sisteminin adının yazılması
print(os.name)

#mevcut çalışma dizinini ekrana yazdırma
print(os.getcwd())

#mevcut dizini değiştirme
# os.chdir('C:\\')
print(os.getcwd())

#mevcut dizinin üstüne çıkma
# os.chdir('..')
print(os.getcwd())

#mevcut dizinin iki dizin üstüne çıkmak için
os.chdir('../..')#  yukarıdaki dizin değiştirme işlemi yorum satırı yapılmazsa yukarıya çıkılacak dizin kalmadığından tüm çıktılar aynı sonucu verir

print(os.getcwd())


#klasör oluşturma
# os.mkdir("newdir")#FileExistsError-->Halen varolan bir dosya oluşturulamaz hatası verir-->bu kod parçası yüzünden kod sadece bir kez çalıştırılır ve eğer sonraki tekrar çalıştırmak istiyorsak bu satır yorum satırı yapılmalıdır


# os.makedirs("newdir/newdir1_1")#burada mevcut dosya konumunda bir dizin oluşturuldu


#mevcut dosya konumunda belirtilen dosyalanın adını değiştirmek(rename) için:
# os.rename("newdir","yeniKlasor")--->bu kod parçası da bir kez çalıştırıldıktan sonra yorum satırı haline getirilmelidir çünkü dosya adı ilk çalıştırılmada değiştirildiğinden ikinci çalıştırma işleminde dosya bulunmaz

#mevcut dosya konumunda belirtilen dosyaları remove etmek için
#C:\\ yer alan newdir remove etmek için önce o dizine gitmeliyiz
# os.chdir('../../..')#şuan C:\\ dizini altındayız
print(os.getcwd())

#bu dizinde yer alan newdir dosyasını remove edelim
# os.rmdir("newdir")#bu kod parçası da sadece bir kez çalıştırılabilir ikinci çalıştırmada dosya bulunamıyacağından hata verir---->FileNotFoundError


#şimdi onedrive içerisinde bulunan yeniklasor içindeki newdir_1 klasörünü silersek
print(os.getcwd())
# os.chdir('C:\Users\90544\OneDrive')

"""escape karakterler nasıl normal karaktere dönüştürlür????"""

print(os.getcwd())
#bu dizin içerisideki yeniKlasor içindeki newdir_1 klasörünü sil
#dizini silmek için bu metot kullanılır
# os.removedirs('yeniKlasor/ewdir1_1')#slash yönüne dikkat et --->yine sadece bir kez çalıştırılıcak kod parçası-->bunların sadece bir kez çalıştırılmasının nedeni program çalıştığında dosyayı bulamamasından kaynaklıdır

# #mevcut dosya dizinindeki klasörleri listelemek için :
# print(os.listdir())#parametre olarak dosya dizin yolu girilir ve o dizindeki klasörler listelenir


#eğer dosyalar listelenirken sadece belirli koşulu sağlayan dosyaları listelemek istiyorsak

#eğer sadece .py uzantılı dosyaları listelemek istiyorsak:

for file in os.listdir():
    if(file.endswith('.py')):
        print(file)#hiçbir sey yazdırmadı çünkü mevcut dosya konumunda bu uzantıda bir klasör yok
print(os.getcwd())

#masaüstüne git
os.chdir('..')

#masaüstüne .py uzantılı bir klasör oluşturursak
# os.mkdir("python.py")-->klasör oluşturulduğundan bu satır yorum satırı yapılır
print(os.getcwd())

#bu kodlar tekrar çalıştırıldığında hata verebilir çünkü burada oluşturulan dosyalar silindi veya önceden oluşturuldu


#os modülü altında yer alan path sınıfı dosya uzantılatıyla ilgili işlemler yaparlar 
#path classı bünyesinde bulunan abspath metotu aracılığıyla parametre olarak girilen dosyanın tam dosya konumunun dizini ekrana yazdırılır

print(os.path.abspath("Python_Eğitim_Kodlari"))#-->parametre olarak girilen dosyanın tam konumunu verir


#dirname() ile parametre olarak tam konumu verilen bir dosyanın dizin ismi verilir
print(os.path.dirname("C:/Users/90544/OneDrive/Python_Eğitim_Kodlari"))#ters slachları düzelt
print(os.path.dirname(os.path.abspath("Python_Eğitim_Kodlari")))#üstteki kod ile aynı çıktıyı verir


#ilgili dosyanın mevcut dizinde olup olmadığını bilgisini sorgulatmak için exists metotu kullanılır 
print(os.path.exists("file.py"))#bool değer döndürür---->False
#eğer farklı bir dizin için bir dosyanın olup olmadığını kontrol etmek istiyorsak bu kontrolu yapmamızın sebebi herhangi bir dosyayı oluşturmadan önce o dosyanın olup olmadığını kontrol etmek için olabilir  ,
print(os.path.exists("C://users/90544"))#True değerini döndürür


#parametre olarak girilen dizinin kalsör mü ya da dosya mı olduğunu kontrol etmek için isfile(dosya) ve isdir(klasör) metotları kullanılır
print(os.path.isfile("C://users/90544"))#bool değeri döndürür-->False
print(os.path.isdir("C://users/90544"))#bool değeri döndürür-->True

print(os.path.join("C://,deneme,deneme_1"))#burada ilk parametrenin altına ikinci parametreyi,ikinci parametrenin altına üçüncü parametreyi koyar fakat eğer exists metotu ile bu dosyaların varlığı konrol edilirde false değeri döner çünkü bu metot dosya oluşturmaz var olan dosyaları birbirine ekler alt dizin olarak 



#eğer herhangi bir dosyayı ya da klasörü dizinden ayırıp bu parçalardan bir liste oluşturmak istersek split metotunu kullanırız 
print(os.path.split("C://,deneme")) 
#eğer bir dosya ile o dosyanın uzantısını ayırıp bir liste haline getirmek istersek splitext metotu kullanılır
print(os.path.splitext("os.py"))








"""DOC
-->işletim sistemlerinin çalışma mantığı birbirlerinden farklıdır bu sebeple aynı işi farklı şekillerde yaparlar bu durum termainal kullanımında da görülmektedir örneğin listeleme işlemi için 
*w-->dir
*mac/linux-->ls komutları  kullanılır


-->aynı şekilde iki işletim sistemi arasında dizin ayraçları konusunda da farklılık vardır *w-->dizinleri biibinden ayırmak için  ters taksim \ 
*GNU/Linux-->aynı iş için düz taksim / işareti kullanılır


-->NOT:Düz taksim işaretini Windows da kabul eder, ancak Windows’un doğal dizin ayracı ters taksimdir.


-->bu yüzden her iki işletim sisteminde de çalışan bir program yazmak için oluşturulmuş bir ortak arayüz olarak kabul edilen ve iki işletim sistemi arasında tutarlı bir iletişm kurabilmek için os modülünü kullanırız.


-->Bu modül içerisinde yer alan nitelik(attribute) ve fonksiyonların neler olduğunu dir(os) komutuyla görüntüleyebiliriz


-->kodların hangi işletim sisteminde çalıştığını öğrenmek için os.name attribute kullanılır 
*eğer 'nt' ise Windows 
*'posix' ise MacOS ya da GNU/Linux işletim sistemidir


-->Kullandığımız işletim sisteminin kullandığı dizin ayracını bulmak için sep atribute kullanılır
*w-->os.sep çıktısı-->\\
*MacOS-GNU/Linux-->/ çıktısı verilir ekrana 
Bu attribute kullanılarak farklı işletim sistemlerine özgü dizin yolları oluşturabilirsiniz.Mesela:
*liste=["DOC","DOC_1","DOC_1_1"]
os.sep.join(liste) bu komutu
*windows da verdiğimizde-->DOC\\DOC_1\\DOC_1_1 çıktısını alırız('\\'.join(liste) ile aynı komuttur nerdeyse)
*GNU/Linux da verdiğimizde -->DOC/DOC_1/DOC_1_1 çıktısını alırız('/'.join(liste) ile maynı komuttur) böylece kullandığımı işletim sisteminin hangi dizin ayracını düşünmemize gerek kalmaz bunu python bizim için düşünür


-->o an içinde bulunduğumuz dizinin adını bulmak için getcwd() metotu kullanılır(os.getcwd())


-->Eğer mevcut dizinden başka bir dizine geçmek istiyorsak chdir() fonksiyonu kullanılır ve geçmek istediğimiz dizin bu fonksiyona parametre olarak verilir


-->Eğer dizin içerisindeki dosya ve klasörleri listelemek istersek listdir() fonksiyonu kullanılır ve parametre olarak dizin ismi girilir eğer mevcut konumdaki dizin içerisindeki klasör ve dosytaları listelemek istersek parametre olarak os.getcwd() fonksiyonun çıktısını veririz(os.listdir(os.getcwd()))
os.listdir() çıktısı liste türünde bir veri tipidir bu yüzden listeler üzerinde yapabildiğimiz tüm işlerimleri bunun üzerinde yapabiliriz mesela döngü kurabiliriz:
for i in os.listdir(os.getcwd()):
    print(i) ile dizin içindeki klasör ve dosyalar listelenir 
ya da bir dizin içindeki belli bir uzantıya sahip dosyaları ekrana yazdırabiliriz:
for i in os.listdir(os.getcwd()):
    if i.endswith('.py'):
        print(i)-->burada python dosyaları listelenir sadece     


-->os.listdir(os.getcwd())ile mevcut dizinin elemanlarını listeleriz bu fonksiyon yerine os.listdir('.') komutunu da kullanabiliriz burada 
burada parametre olarak verdiğim '.' karakter dizisi o anda içinde bulunduğumuz dizini temsil eder eğer bu karakter dizisini bilmiyorsak ya da elle yazmak istemiyorsak os.listdir(os.curdir) komutu kullanılır burada parametre olarak girilen os.curdir atribute '.' karşılık gelmektedir.Burada getcwd() metotu ile curdir atribute karıştırılmamalı getcwd()-->çıktı olarak o anda bulunduğumuz dizinin adını verir
*os.curdir ise bir işletim sisteminde o anda içinde bulunulan dizini temsil eden karakter dizi ne ise onun değerini barındırır.Bu değer çoğu işletim sisteminde '.' adlı karakter dizisidir
os.listdir(getcwd())=os.listdir('.')=os.listdir(os.curdir)


-->Çoğu işletim sisteminde bir üst dizini göstermek için '..' adlı karakter dizisi kullanılır(os.listdir('..')-->bir üst dizinin içeriğini listeler).Burada da yine tıpkı os.curdir niteliğinde olduğu gibi ,eğer bu karakter  dizisini kendiniz elle yazmak istemezseniz bu karakter dizisini içinde barındıran os.pardir adlı nitelikten yararlanılır -->os.listdir(os.pardir) ile bir üst dizinin içeriği listenir bu komut os.listdir('..') ile aynı çıktıyı verir


-->Parametre olarak girilen herhangi bir dosyayı bilgisayarda ilişkilendirilmiş programda açmak için sadece windows işletim sisteminde kullanılan startfile() fonksiyonu kullanılır.Örneğin:
***os.startfile("deneme.txt")



-->İşletim sisteminiz .txt uzantılı dosyaları hangi programla ilişkilendirmişse, startfile() fonksiyonu deneme.txt adlı dosyayı o programla açacaktır. Windows’ta .txt dosyaları genellikle Notepad programıyla ilişkilendirildiği için yukarıdaki komutu verdiğinizde muhtemelen deneme.txt dosyasının içeriği Notepad programı aracılığıyla görüntülenecektir.
***os.startfile('deneme.docx')-->Bu komut da deneme.docx dosyasının Microsoft Word adlı yazılımla açılmasını sağlayacaktır.
***Eğer bu fonksiyona parametre olarak dosya değil de dizin girersek dizini windows explorer(ya da default browser) ile açar-->os.startfile(os.curdir) bu komut ile mevcut dizin windows explorer ile açılır parametre olarak direkt dizin de girilebilinir.Bu fonksiyonla internet sayfalarını da açabiliriz-->os.startfile('www.google.com').Ancak bu komutun yalnızca Windows’ta çalışacağını unutmayın. O yüzden bunun yerine, daha önce öğrendiğimiz 'webbrowser' modülünü kullanmak daha doğru olacaktır.


-->Eğer yeni bir dizin oluşturmak istiyorsak bunun için mkdir() fonksiyonu girilir
*os.mkdir('yeniDizin')-->Bu komut o anda içinde bulunduğumuz dizin içinde 'yeniDizin' adlı bir dizin oluşturur
*os.mkdir("/home/istihza/Desktop/yenidizin")-->Bu komut ise yeniDizin adlı dizini belirtilen dizin üzerinde oluşturur
*Eğer oluşturulmaya çalışılan dizin zaten bilgisayar içerisinde var ise hata verir bu yüzden bu komu tsadece bir kez çalıştırılır ikinci çalıştırmada hata verir



-->mkdir() fonksiyonunda yeni dizini oluşturabilmek için bu yeni dizinin üstünde bulunan tüm dizinlerin önceden oluşturulmuş olması gerekiyor eğer önceden oluşturulmamış bir dizin altına yeni bir oluşturmaya çalışırsak hata alırız.Eğer dizin içerisinde dizin oluşturumak istiyorsak yani bir alt dizini oluşturmadan önce üst dizinlerin mevcut olma zorunluluğunu kaldırıp alt dizin oluştururken üst dizinleri de oluşturmak istiyorsak mkdirs() fonksiyonu kullanılır



-->herhangi bir dizinin adını değiştirmek için rename() fonksiyonu kullanılır parametre olarak rename('dizinin şimdiki adı','dizinin yeni adı') parametrelerini alır.Eğer dizinin yeni adı adlı dizin zaten bilgisayarda mevcut ve içi boşsa yukarıdaki komut GNU/Linux ta: eski dizin ,mevcut ve içi boş olan yeni dizinin üstüne yazılır .Windows da:hata verir


-->Eğer üstüne yazma işlemini her iki işletim sisteminde de gerçekleştirmek istiyorsak bunun için replace() fonksiyonu kullanılır 
*os.replace('deneme','test') bu fonksiyonda tıpkı rename fonksiyonunda olduğu gibi deneme adlı dizinin adını test olarak değiştirir sadece isim değişikliği yapmaz zaten sadece isim değişikliği yapsaydı bu fonksiyona ihtiyaç duyulmazdı ve rename fonksiyonu kullanılırdı ama bu fonksiyon ek olarak üstüne yazma işlemi yapar .Bu fonksiyon hem windows da hem GNU/Linux da deneme dizinini varolan(*) test dizinin üzerine yazmaya çalışır.Fakat burada da windows dan kaynaklı  çeşitli izin hataları oluşur """


# ---------------------------
# -->eğer belirtilen dizindeki bir dosyayı silmek istiyorsak bunun için remove() fonksiyonu kullanılır.Bu komut dosyayı silmeden önce herhangi bir soru sormaz ve direkt siler bu yüzden kullanımı sırasında dikkatli olunmalıdır



# -->Eğer dosya yerine içi boş bir dizini silmek istersek bunun için os.rmdir() fonksiyonu kullanılır.İçi boş olmalı çünkü eğer silmeye çalıştığımız dizin içerisinde başka bir dizin ya da dosya varsa yani içi boş değilse bu fonksiyon hata verir
# *os.rmdir('anadizin')
# os.rmdir(r'anadizin/dizin1')
# os.rmdir(r'anadizin/dizin1/dizin2/dizin3')
# eğer silme işlemini yukarıdaki gibi dıştan içe doğru yapmaya çalışırsak yine hata alırız
# *os.rmdir(r'anadizin/dizin1/dizin2/dizin3/')
# os.rmdir(r'anadizin/dizin1/dizin2/')
# os.rmdir(r'anadizin/dizin1')
# os.rmdir(r'anadizin/')
# eğer silme işlemini alt dizinden üst dizine doğru yaparsak hata almayız ve silme işlemi başarılı olur



# -->yukarıdaki gibi aşamalı silme işlemi ile uğraşmak istemiyorsak removerdirs() fonksiyonu kullanılır bu fonksiyon ile içi boş dizin yolları silinebilir
# os.removedirs('anadizin/dizin1/dizin2/dizin3/dizin4')
# yukarıdaki silme işlemini removedirs() fonksiyonu ile tek satırda gerçekleştirebiliriz (anadizin ve dizin4 silme işlemine dahildir)


# -->Eğer dosyalar hakkında bilgi almak istiyorsak stat() fonksiyonu kullanılır .Almacağımız bilgi türü:dosyanın boyutu,oluşturulma tarihi, değiştirilme tarihi ve erişilme tarihi gibi bilgilerdir .
# **print(os.stat('dosya adi')) bu komut ile acağımız çıktı:
# **os.stat_result(st_mode=33279, st_ino=17732923532961356,
# **st_dev=1745874298, st_nlink=1, st_uid=0, st_gid=0,
# **st_size(dosyanın boyutu-byte türünden-kb dönüştürmek için 1024 böl)=495616, st_atime(dosyaya en son **erişilme tarihi)=1416488851, st_mtime(dosyanın son değiştirilme tarihi)=1415275662,
# **st_ctime(dosyanın oluşturulma tarihi/Windows da)=1415275658) 
# şeklindedir
# Bu kendi içinde birtakım nitelikler barındıran özel bir veri tipidir .Bu veri tipinin barındırdığı nitelikleri görmek için dir(os.stat()) komutu kullanılabilinir
# *NOT:GNU/Linux’ta bir dosyanın ne zaman oluşturulduğunu öğrenmek mümkün değildir. Dolayısıyla dosya.st_ctime komutu yalnızca Windows’ta bir dosyanın oluşturulma tarihi verir. Bu komutu GNU/Linux’ta verdiğimizde elde edeceğimiz şey dosyanın son değiştirilme tarihidir.


# -->Python içerisinde sistem komutlarını ya da başka programları çalıştırmak için os.system('dosya adi') komutu kullanılır.???Burada notepad de yazılan bir python temelli dosya burada çalıştırılabilir anlamına mı gelmektedir????



# -->Kriptografi de  ya da rasgele parola üretmede kullanılan ve rastgele bayt dizileri elde etmek için kullanılan fonksiyon urandom() fonksiyonudur
# os.urandom(12)-->bu fonksiyon 12 bayttan oluşan rastgele bir dizi oluşturur

# ----------------walk() fonksiyonu--------------
# import os
# # def tara(dizin):
# #     #O anda içinde bulunduğumuz dizinin konumunu baslangic adlı değişkene atıyoruz çünkü ddaha sonra buraya dönmemiz gerekecek:
# #     baslangic=os.getcwd()

# #     #ardından dosyalar adlı bir boş liste oluşturuyoruz tüm dizileri buraya atacağız
# #     dosyalar=[]

# #     #daha sonra tara() fonksiyonuna parametre olarak verilen dizin adlı dizinin içine giriyoruz:
#     os.chdir(dizin)


#     #bu dizin içerisine girdikten sonra mevcut dizin içerisindeki bütün öğeleri lisdir() fonksiyonu ile tek tek tarıyoruz
#     for oge in os.listdir(os.curdir):

#         #eğer tarama sırasında karşılaştığımız öğe bir dizin değil ise :
#         if not os.path.isdir(oge):
#             #bu öğeyi doğrudan en başta tanımladığımız dosyalar adlı listeye ekliyoruz
#             dosyalar.append(oge)

#         #Ama eğer tarama sırasında karşılaştığımız öğe bir dizin ise :
#         else:
#             #tara() fonksiyonunun en başına dönüp , tanımladığımız bütün işlemleri bu dizin üzerine özyinelemeli(recursive) olarak uyguluyoruz ve elde ettiğimiz öğeleri dosyalar adlı listeye extend() metotu ile işliyoruz-->listeleri birleştirmek için kullanılan bir fonksiyondur(metot??)      
#             dosyalar.extend(oge)
#     #for döngüsünden çıktıktan sonra en baştaki konuma tekrar dönebilmek için aşağıdaki komutu çalıştırıyoruz:
#     os.chdir(baslangic)
#     #eğer bu şekilde başa dönmezsek dizin yapısı içindeki ilk alt dizine girildikten sonra programımız o konumda takılı kalacağı için öteki üst dizinlerin içini tarayamaz 



#Yukarıdaki yöntem doğru olsa da Python'da bir dizini en dibe kadar taramanın en iyi yolu değildir .Python bu iş için bize özel bir fonksiyon sunar.Bu fonksiyon walk()fonksiyonudur.Bu fonksiyon dizinler içerisinde yürünmesini sağlar """


# """iç içe geçmiş dosya yığınlarından dosya uzantılar aynı olan ya da benzer olan dosyaları bir yerde toplamak istiyorsak.Bunu istememizin sebebi benzer dosyaları tek bir elle bulup istediğimiz yere taşıyabilme kolaylığı sağlamaktır """

# #dosya uzantılarını içeren bir liste tanımlarız
# uzantilar=['txt','doc','xls',
#             'jpeg','pdf','zip',
#             'mp3','ogg','jpeg'
#           ]
# sablon_1=["{}.{}".format('dosya',i) for i in uzantilar[:4]]#txt,doc ve xls uzantıları dosya.txt,dosya.doc ve dosya.xls şeklinde eleman olarak sablon_1 listesi içine aktarıldı-->sablon_1=[dosya.txt,dosya.doc,dosya.xls] şeklinde olur

# sablon_2=['resim{}.{}'.format(i,uzantilar[-1]) for i in range(1,5)]#sablon_2=[resim1.jpeg,resim2.jpeg,resim3.jpeg,resim4.jpeg] şeklinde olur

# sablon_3=['{}.{}'.format('dosya',i) for i in uzantilar[4:]]#sablon_3=[dosya.jpeg,dosya.pdf,dosya.zip,dosya.mp3,dosya.ogg] şeklinde olur

# #şimdi şablonları ve şablonları içerecek dizin alanlarını tuple olarak alan bir dosyalar adlı bir liste tanımlıyalım
# dosyalar=[('anadizin',sablon_1),
#           ('resimler',sablon_2),
#           ('baskadosyalar',sablon_3)]

# #şimdi bu anadizin,resimler ve baskadosyalar adlı dizinleri belirtilen hiyerarşik düzende oluşturalım-->anadizin//resimler//baskadosyalar

# # os.makedirs(os.sep.join(dosya[0] for dosya in dosyalar))#dosya[0]=anadizin/resimler/baskadosyalar

# #şimdi dosyaları ilgili dizinlere ekleme işlemi yapılıcak
# for dizin,sablon in dosyalar:
#     for s in sablon:
#         open(os.sep.join([dizin,s]),'w')#burada şablon içeriğini dizine ekler
#     os.chdir(dizin)#bunu yapamamızn sebebi anadizin içerisine resimleri ,resimler içerisine baskadosyaların dosyalarını aktarabilmek için yani anadizine girip resimlerin sablonlarını ekledi sonra resimlere girip baskadosyalarin şablonlarını ekledi    


# #yukarıda yaptığımı her şeyi walk fonksiyonu ile daha kolay ve daha az satırda yapabiliriz

# #aşağıdaki for döngüsüyle bir dizinin en derindeki dosyasına kadar ekrana yazdırırız
# for i in os.walk('anadizin'):
#     print(i)

# #çıktı olarak üç öğeli bir demet(tuple) vardır.Çıktının diğer kısımlarını da incelerseniz aynı yapıyı göreceksiiniz.Dolayısıyla os.walk() komutu bize şu üç öğeden oluşan bir demet verir:
# # (kökdizin,altdizinler,dosyalar)    
# # Yukarıdaki çıktıyı incelediğinizde bu yapıyı rahatlıkla görebilirsiniz:

# # kökdizin    => 'anadizin'
# # altdizinler => ['resimler']
# # dosyalar    => ['dosya.doc', 'dosya.jpeg',
# #                 'dosya.txt', 'dosya.xls']

# # kökdizin    => 'anadizin\\resimler'
# # altdizinler => ['başkadosyalar']
# # dosyalar    => ['resim1.jpeg', 'resim2.jpeg',
# #                 'resim3.jpeg', 'resim4.jpeg']

# # kökdizin    => 'anadizin\\resimler\\başkadosyalar'
# # altdizinler => []
# # dosyalar    => ['dosya.jpeg', 'dosya.mp3',
# #                 'dosya.ogg', 'dosya.pdf',
# #                 'dosya.zip']
# #mesela bu üç öğeli demet içinden yalnızca dosyaları almak isterseniz şöyle bir komut verebilirsiniz:
# for kokdizin,altdizinler,dosyalar in os.walk('anadizin'):
#     print(f"KÖK DİZİNLER: {kokdizin}")
#     print(f"ALT DİZİNLER:{altdizinler}")
#     print(F"DOSYALAR:{dosyalar}")

# #Kök dizin değişkeni ile dosyalar değişkenini birleştirirsek bir  dosyanın tam adresini elde edebilirsiniz
# for kokdizin,altdizin,dosyalar in os.walk('anadizin'):
#     print(os.sep.join([kokdizin,dosyalar]))#burada kokdizini dosyalarla dizin ayaracı ile birleştirir
# #burada dosyalar değişkenin bize verdiği veri tipi bir listedir.O yüzden liste üzerinde uygulayabildiğimiz işlemleri bunun üzerinde de uygulayabiliriz
# for kokdizin,altdizin,dosyalar in os.walk('anadizin'):
#     for i in dosyalar:
#         if (i.endswith('.jpeg')):
#             print(i)#burada .jpeg uzantılı dosyaları sadece ekrana yazdırır   




# """------------------------------------------------------------"""
# #os.environ niteliği(environ=çevre):kullandığımız işletim sistemindeki çevre değişkenleri hakkında bilgi edinmemizi sağlar
# #bu nitelik bir sözlüktür(dic).Bu yüzden bu sözlüğe erişim için:
# for key,value in os.environ.items():
#     print(key.ljust(10),value)
# #sözlük içerisindeki bir değere erişmek için:
# os.environ['HOMEPATH']
# #Yalnız, Windows ve GNU/Linux işletim sistemlerinde çevre değişkenleri ve bunların adları birbirinden farklı olduğu için, doğal olarak environ niteliği de farklı işletim sistemlerinde farklı çıktılar verir. Birden fazla işletim sistemi üzerinde çalışacak şekilde tasarladığımız programlarda bu duruma dikkat etmeliyiz. Örneğin Windows’ta kullanıcı adını veren çevre değişkeni ‘USERNAME’ iken, GNU/Linux’ta bu değişken ‘USER’ olarak adlandırılır.    
# """------------------------------------------------------------"""

# #os.path-->os modülü üzerinde dir() fonksiyonunu uyguladığımızda orada path adlı bir attribute görülür.Bu attribute kendi içinde pek çok önemli fonksiyon ve başka nitelik barındırır

# #os.path.expanduser() fonksiyonu bilgisayardaki kullanıcıya ait dizinin adresini verir:os.path.expanduser('~').Bu fonksiyonu kullanarak Windows da belirli bir kullanıcı ismi ve dizini de oluşturabilirsiniz

# #os.path.split()-->split() fonksiyonu bir yol adresinin son kısımını baş kısmından ayırır.BU fonksiyonu kullarak dosya adlarını dizin adlarından ayırabilirsiniz


# #Modüllerin kaynak dosyalarını görmemizi sağlayan __file__ adlı bir araç kullanılır
# print(os.__file__)
# #Normalde __file__ niteliğini yalnızca modül adlarına uygulayabilirsiniz.Modüllerin  nitelik ve fonsiyonları üzerinde __file__ aracı kullanılamaz
# # #ama os modülünün path niteliği için durum biriaz farklıdır.__file__,os.path üzerinde kullanılabiliyor.os.path niteliği Windows’ta ntpath, GNU/Linux’ta ise posixpath adlı bir modüle atıfta bulunuyor.
# # Dolayısıyla aslında biz os.path niteliğini kullanırken, eğer Windows’ta isek ntpath adlı bir modülü, ama eğer GNU/Linux’ta isek posixpath adlı bir modülü içe aktarmış oluyoruz.

# # Eğer os.path adlı ortak bir arayüz olmasaydı, yukarıda os.path başlığı altında incelediğimiz araçları kullanabilmek için, kullandığımız işletim sistemine göre posixpath veya ntpath modüllerinden uygun olanını kendimiz elle içe aktarmak zorunda kalacaktık:
# # if os.name == 'nt':
# #     import ntpath as path

# # else:
# #     import posixpath as path
# # Ama Python programlama dilinin bize os.path adlı niteliği sunmuş olması sayesinde Windows işletim sistemi için ntpath, GNU/Linux işletim sistemi için ise posixpath modülünü ayrı ayrı içe aktarmamıza gerek kalmıyor. Bütün işi bizim yerimize Python hallediyor. Böylece farklı işletim sistemlerine ilişkin birbirinden farklı işlemleri, os.path adlı tek bir arayüz üzerinden gerçekleştirebiliyoruz.