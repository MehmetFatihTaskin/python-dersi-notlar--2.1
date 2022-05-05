import math
küre_capı = int(input("cm cinsinden giriniz:"))
print("Küre hesplama progrmına hoş geldiniz")
print("Küre çapını giriniz.")
pi = math.pi
küre_alan = 4*pi*(küre_capı/2)**2
küre_hacmi = 4/3 * pi * (küre_capı/2)**3
print("capı:" , küre_capı, "olan kürenin alanı:" ,
küre_alan, "cm ve hacmi: ",küre_hacmi ,"cm dir")

print("nokta")