#karşılaştırma operatörlerinimn sonuçları boolean türündedir

#değişken tanımlamaları
a,b,c,d=5,5,10,4

password="1234"
username="gamzeaslan"

#1--->== karşılaştırma operatörü
result=(a==b)#True
print(result)#result=sonuç

result=(a==c)#False
print(result)

result=("gmzsln"==username)#false
print(result)


#2-->!= karşılaştırma operatörü
result=(a!=b)#false
print(result)

result=("gmzsln" !=username)#true
print(result)

#3-->büyüktür(>) karşılaştırma operatörü
result=(a>b)#false
print(result)


#4-->küçüktür(<) karşılaştırma operatörü
result=(a<b)#false
print(result)


#5-->büyük eşittir (>=) karşılaştırma operatörü
result=(a>=b)#true
print(result)

#6-->küçük eşittir (<=) karşılaştırma operatörü
result=(a<=b)#true
print(result)

result=True + False + 40#sonuç :41 çıkar
print(result)