
#IDENTITY (KİMLİK) OPERATOR-->IS
#-->(x==y) == (x is y)-->Identity (Kimlik) Operatörleri/True/False)
#-->(x!=y) == (x is not y)


#değişken atamaları
x=y=[1,2,3]
z=[1,2,3]
#yukarıdaki x ile y aynı referansa sahipken z bunlarla aynı liste elemanlarına sahip olsa bile aynı referansa sahip değildir

result=(x==y)
print(result)

result=(x is y)
print(result)

result= (x!=y)
print(result)

result= (x is not y)
print(result)


#MEMBERSHIP(ÜYELİK) OPERATOR:IN
#-->dizi[1] == (1 in dizi)-->Membership(Üyelik) Operatörleri(True/False)

#değişken tanımlama
x=['banana','apple']
result=(x[0])
print(result)

result=('banana' in x)#banana x dizisinin elemanıdır:True/False
print(result)

result=('banana' not in x)#banana x dizisinin elemanı değildir:True/False
print(result)