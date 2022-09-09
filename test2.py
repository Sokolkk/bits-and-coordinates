#задание 1
cor = "0000001010000001000110000010001001101001" 
x=int(cor[3:14],2)*(2**(-3))#декодируем значения
y=int(cor[15:26],2)*(2**(-3))
z=int(cor[27:38],2)*(2**(-3))
print("x = " + str(x) + "м")
print("y = " + str(y) + "м")
print("z = " + str(z) + "м"+"\n")

#задание 2
cor=list(cor)#преобразуем строку в бинарный массив
cor = list(map(int, cor))#преобразуем элементы массива в инт
print("бинарный массив : " + str(cor))
x=cor[3:14]#соотносим части списка координатам
y=cor[15:26]
z=cor[27:38]
def decoder(COORD): #создаем декодер
    res = 0
    for i in COORD: res = (res << 1) | i
    COORD = res * (2**(-3))
    return COORD
x = decoder(x)
y = decoder(y)
z = decoder(z)
print("x, y, z : " + str(x)+ "м, "+ str(y)+ "м, "+ str(z)+ "м ")

#задание 3
cor = "0000001010000001000110000010001001101001" 
cor=int(cor,2)
print("число: " + str(cor))
def swapBits(x, p1, p2, n) :
    xor = (((x >> p1) ^ (x >> p2)) & ((1 << n) - 1))
    return x ^ ( (xor << p1) | (xor << p2))
cor = swapBits(cor, 3, 15, 11)
with open('задание3.bin', 'w') as f:
     f.write(str(cor))
