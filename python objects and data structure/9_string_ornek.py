#değişken tanımlama
website="http://www.sadikturan.com"
course="Python Kursu: Baştan Sona Python Programlama Rehberiniz(40 saat)"

"""-----SORULAR-----"""

#1-->'course' karakter dizisinde kaç karakter bulunmaktadır 
course_karakter_sayisi=len(course)
print(f"course toplam karakter sayısı:{course_karakter_sayisi}")


#2-->'website'içinden www karakterlerini alın
website_www_karakterleri=website[7:10]
print(f"www karakterleri:{website_www_karakterleri}")


#3-->'website' içinden com karakterlerini alın
website_com_karakterleri=website[-3:]
#veya website[len(website)-3:len(website)] ifadeside kullanılabilir
print(f"com karakterleri:{website_com_karakterleri}")


#4-->'course' içinden ilk 15 ve son 15 karakterlerini alın
#ilk 15 karakter
course_ilk_15_karakter=course[:16]
print(f"course ilk 15 karakter: {course_ilk_15_karakter}")

#son 15 karaker
course_son_15_karakter=course[len(course)-15:len(course)]
print(f"course son 15 karakter:{course_son_15_karakter}")

#5-->'course' ifadesindeki karakterleri tersten yazdırın
#dizi olarak tanımlayıp en son indeksi başa koymak işe yaramıyo
ters_course=course[::-1]#en  baştan başlar ama 1 er 1 er azaltarak gider
print(f"ters course:{ters_course}")


#6-->name,surname,age,job değikenleriyle "benim adım name , yaşım age ve mesleğim job" şeklinde ekrana yazdırın
name="Gamze"
surname="Aslan"
age=21
job="Yazılım Mühendisi"
print(f"benim adım {name} , yaşım {age} ve mesleğim {job}.")



#7-->'Hello world' ifadesindeki w harfini W ile değiştirin
#hello_world="Hello world"-->hello_world[6]="W" şeklinde bir atama yapılamaz onun yerine dizi parçalara bölünerek eklenir
hello_world="Hello world"
degistirilmis_hali=hello_world[:6] + "W"+ hello_world[-4:]
print(f"hello world değiştirilmiş hali:{degistirilmis_hali}")