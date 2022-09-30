#Javada olduğu gibi stringden sonra gelen sayılarla string toplama işlemi(birleştirme) gerçekleştirilmez ve kod hata verir.Kodun hata vermemesi için önce tür dönüşümü yapılmalı.Kod örneği:

#değişken tanımlama
first_name="Gamze"
last_name="Aslan"
integer_age=21


#-----Hatalı Kod----->print(first_name + " " + last_name + " " integer_age--->program hata verir
#int to string dönüşümü yapılmalıdır 
string_age=str(integer_age)

#şimdi string toplamayla ekrana işlemi yapılabilir
print(first_name + " " + last_name + " " + string_age)

#2-->aynı satır içinde satır atlatmak için \n ifadesi kullanılır.Kullanımı tırnak içi ile sınırlıdır
print("gamze aslan \nyaş=21")

#3-->string bir karakter dizini olduğundan indekleme mevcuttur .Python dizilerinde ilk karakter 0 dan son karakter -1 den başlayarak indekslenir 

#bir string tanımlayalım
string_dizi="Mavi Arabanın Tekerliği Patladı"

#bu string ifadenin ilk indisine erişim :
ilk_index=string_dizi[0]

#bu string ifadenin son indisine erişim:
son_index_1_yol=string_dizi[-1]

#ya da son indise erişim .Dizinin uzunluğunu bulup bu değerden bir çıkartırsak bulduğumuz sonuç dizinin sonuncu indexidir 

#string dizisinin karakter sayısını bulmak için:
string_karakter_sayisi=len(string_dizi)

#bu değerden bir çıkartarak son indexe ulaşırız
son_index=string_karakter_sayisi-1

#bu değere ulaşarak bu sting ifadenin son indisinin değerine ulaşmış oluruz
son_index_2_yol=string_dizi[son_index]

"""kısacası:
string_dizi[len(string_dizi)-1]  ifadesi de son indexin değerine ulaşmış oluruz
"""

#4-->Bu string ifadesinin herhanhi bir kesitini almak için:
string_dizi_kesit_1=string_dizi[2:6]#2 dahil fakat 6 dahik değildir

string_dizi_kesit_2=string_dizi[2:]#2 den başlar dizi sonuna kadar alır

string_dizi_kesit_3=string_dizi[:5]#baştan başlar 5 e(dahil değil) kadar alır

string_dizi_kesit_4=string_dizi[2:25:2]
"""yukarıdaki kodda 2 den (dahil) 25 e (dahil değil) kadar olan string karakterleri her 2 karakterde bir olacak şekilde kesitini alır"""

#ekrana yazdırma kesiti
print(string_dizi_kesit_4)#çıktısı:v rbnnTkriiP şeklindedir

string_deger="abc"
print(f"abc yi yan yana 3 kere yazdır ma{string_deger*3}")




