#                                   --------------Liste:Dizi----------

from re import U

#değişken tanımlama
message="Hello There. My name is Gamze Aslan"

#message string ekrana yazdırma
print(f"message string:{message}")

# yukarıdaki ifade bir string ifadedir.Bu ifadenin uzunluğu:
print(f"Message string karakter uzunluğu:{len(message)}")#35

#bu değişkenin ilk indisine:
print(f"message string ilk indeksi:{message[0]}\n")#H


#--------------------------------------------------------------------------------------------------

#eğer bu değişkeni bir dizi haline getirisek

#message liste haline getirme
mesage_dizi=message.split()

#message list ekrana yazdırma
print(f"message list:{mesage_dizi}")

#karakter uzunluğu:
print(f"message list dizi uzunluğu:{len(mesage_dizi)}")#7

#ilk indeks
print(f"message list ilk indeksi:{mesage_dizi[0]}\n")#Hello

#-----------------------------------------------------------------------------------------------------
#listeleri toplama---toplamada listelerin yerleri önemli
list_1=[12,23,34]
list_2=['A','B','C']

#list_1 in üzerine list_2 ekleme
list_1_2=list_1+list_2
print(f"list_1 +list_2:{list_1_2}")

#list_2 nin üzerine list_1 ekleme
list_2_1=list_2 + list_1
print(f"list_2 + list_1:{list_2_1}\n")

#-----------------------------------------------------------------------------------------------------
#liste içine liste yerleştirme
list_12=[list_1,list_2]
print(f"liste içine liste yerleştirme 1-2:{list_12}")

list_21=[list_2,list_1]
print(f"liste içine liste yerleştirme 2-1:{list_21}\n")

#liste içinde liste elemanlarına erişim
print(f"list_12 nin 0.indeksli elemanı=list_1:{list_12[0]}")

#listenin içindeki listenin elemanlarına erişim
print(f"liste içindeki listenin elemanlardan 12 ye erişim=list[0]:{list_12[0][0]}\n")
