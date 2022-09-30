"""
x=5---
y=10 ---->x,y,z=5,10,20
z=20---
iki değişkenin değerlerini değiştirme
x,y=y,x şeklinde değiştirilir
x =x+5--->x+=5
x =x-5--->x-=5
x =x*5--->x*=5
x =x/5--->x/=5
x =x%5--->x-=5
x =x//5--->x//=5
"""

values=1,2,3,4,5
print(type(values))

x,y,*z=values#burada z bir dizi olarak tanımlandı

print(x,y,z)
print(x,y,z[1])