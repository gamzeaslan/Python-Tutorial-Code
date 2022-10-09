"""#1-->"""#Python da herhangi bir dosyayı açmak için open metodu kullanılır ve bu metot iki parametrelidir open(dosya adı ,dosya açılma modu) eğer oluşturacağımız dosyayı farklı bir dosya dizini içerisinde oluşturmak istiyorsak bunun için de open(dosya dizini,dosya açılma modu) şeklinde bir parametre girişi yapmalıyız

"""#2-->Dosya Erişme Modu: """#Dosya açılırken kullanılan 4 farklı mod bulunmaktadır .Eğer dosya açılırken herhengi bir dosya açma modu belirtilmemişse default olarak read modunda açılır Bunlar:

"""#2.1Read(r) Modu:"""#Varsayılan Değer(**).Eğer açılmak istenen dosya mevcut değilse error verir

"""2.2 Append (a) Modu: """#Ekleme yapmak için bir dosya açar eğer belirtilen dosya yoksa oluşturur.Eğer belirtlen dosya var ise o dosyayı açarak o dosya üzerine eklemeler yapar dosya içerisindeki mevcut bilgileri silmez 

"""2.3 Write (w) Modu: """#Yazmak amacıyla dosyayı açar .Eğer mevcuy dosya yok ise oluşturur.Append modu ile aralarındaki fark şudur:Write modu ekleme yaparken mevcut dosya bilgilerini silerek ekleme işlemini gerçekleştirir ancak append modu ise mevcut dosya üzerine ekleme yaparak yazma işlemin gerçekleştirir


"""2.4 Create (x) Modu: """#Dosya oluşturmak için kullanılan bir moddur.Eğer oluşturulmak istenen dosya mevcut ise hata verir(try except ile kod hata mesajı verilebilir)


"""EK :"""#Ek olarak dosyanın ikili mi yoksa metin modu olarak mı açılacağını belirleyebilir
#"t"-->Metin-->Varsayılan değer .Metin modu
#"b"-->İkili-->İkili mod(örn Görüntüler)


"""EK :"""#Dosyalar ikili ve metin olmak üzere ikiye ayrılır.Eğer bir dosyayı bir metin düzenleyici ile açtığınızda herhangi bir dilde yazılmış ‘okunabilir’ bir metin görüyorsanız, o dosya bir metin dosyasıdır. Mesela Notepad, Gedit, Kwrite veya benzeri metin düzenleyicileri kullanarak oluşturduğunuz dosyalar birer metin dosyasıdır.
#İkili dosyalar ise, metin dosyalarının aksine, metin düzenleyicilerle açılamayan, açılmaya çalışıldığında ise çoğunlukla anlamsız karakterler içeren bir dosya türüdür. Resim dosyaları, müzik dosyaları, video dosyaları, MS Office dosyaları, LibreOffice dosyaları, OpenOffice dosyaları, vb. ikili dosyalara örnektir.