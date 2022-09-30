#kullanıcı tarafından girilen yarıçap ile dairenin alanı ve çevresinin hesaplanması


#kullanıcı girişi alma
string_yaricap=input("Yarıçap: ")

#string to float
float_yaricap=float(string_yaricap)

#pi değeri 
pi_degeri=3.14

#çevre hesabı
cevre_degeri=2*pi_degeri*float_yaricap

#alan hesabı
alan_degeri=pi_degeri*(pi_degeri**2)

#çevre değerini ekrana yazdırma
print(cevre_degeri)

#alan değerini ekrana yazdırma
print(alan_degeri)

