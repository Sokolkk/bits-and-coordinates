#задание 1
cor = "0000001010000001000110000010001001101001" 
x=int(cor[3:14],2)*(2**(-3)#декодируем значения
y=int(cor[15:26],2)*(2**(-3))
z=int(cor[27:38],2)*(2**(-3))
print("x = " + str(x) + "м")
print("y = " + str(y) + "м")
print("z = " + str(z) + "м"+"\n")

#задание 2
cor=int(cor,2) 
print ("Имеющуюся строку бит из текстовой формы \n" +
"перевести в двоичное число = " + str(cor)+"\n")
cor = '{0:b}'.format(cor)#превращаем двоичное число в биты   
x=int(cor[0:8],2)*(2**(-3)) #декодируем значения
y=int(cor[9:20],2)*(2**(-3))
z=int(cor[21:32],2)*(2**(-3))
print("x = " + str(x) + "м")
print("y = " + str(y) + "м")
print("z = " + str(z) + "м")

#задание 3
x=cor[0:7]
y=cor[9:19]
z=cor[21:31]
cor=y+x+z
with open('задание3.bin', 'w') as f:
    f.write(cor+"\n"+ str(int(cor,2)) )

 
