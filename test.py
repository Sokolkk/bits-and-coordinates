#задание 1
cor = "0000001010000001000110000010001001101001" 
x=int(cor[3:13],2)*(2**(-3))*2#декодируем значения
y=int(cor[15:25],2)*(2**(-3))*2
z=int(cor[27:37],2)*(2**(-3))*2
print("x = " + str(x) + "м")
print("y = " + str(y) + "м")
print("z = " + str(z) + "м"+"\n")

#задание 2
cor=int(cor,2) 
print ("Имеющуюся строку бит из текстовой формы \n" +
"перевести в двоичное число = " + str(cor)+"\n")
cor = '{0:b}'.format(cor)#превращаем двоичное число в биты   
x=int(cor[0:7],2)*(2**(-3))*2 #декодируем значения
y=int(cor[9:19],2)*(2**(-3))*2
z=int(cor[21:31],2)*(2**(-3))*2
print("x = " + str(x) + "м")
print("y = " + str(y) + "м")
print("z = " + str(z) + "м")

#задание 3
x=cor[0:7]
y=cor[9:19]
z=cor[21:31]
cor=y+x+z
with open('задание3.txt', 'w') as f:
    f.write(cor+"\n"+ str(int(cor,2)) )

 