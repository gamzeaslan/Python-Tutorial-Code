#değişken tanımlamaları
first_name="Gamze"
last_name="Aslan"

print("isim: " + first_name+ " " +"soyisim: " + last_name)
#yukarıdaki gibi bir birleştirme işleminde hata payı yüksektir bu yüzden formatlama işlemi gerçekleştirilir

"""----------------formatlama-----------------"""

#yukarıdaki çıktının aynısını:
print("isim:{}--soyisim:{}".format(first_name,last_name))
#şeklinde de  elde edebiliriz


#formatlamada  değişkenlerin yerleri değiştirilebilir
print("isim:{0}--soyisim:{1}".format(first_name,last_name))
print("isim:{1}--soyisim:{0}".format(last_name,first_name))

#değişkenlerin yerlerini değiştirmek için indekslemek yerine harflendirme de yapılabilir
print("isim:{f}--soyisim:{l}".format(f=first_name,l=last_name))

#tüm bunlar yerine aşağıdaki yapı da kullanılabilir
print(f"isim:{first_name}--soyisim:{last_name}")

#NOT:ctrl+k+c:yorum satırı yapma------ctrl+k+u:yorum satırını silme