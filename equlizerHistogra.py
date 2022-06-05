

#OBS:
# imgens superexpostas(com muita luminosidade) o histograma apresenta elementos mais concentrados a direita
# imagens subexpostas (com baixa luminosidade) apresenta elementos concentrados a esquerda
#imagens com baixo nivel de contraste ou seja menor nitidez o seu histograma ´é mais estreito e os elementos são concentrados em intervalos menores
# imgens com alto nivel de constrasate apresentam histogramas largos com elementos distribuidos por toda faixa de tons de cinza disponivel

'''
O	 objetivo	 da	 equalização	 de	 histograma	 é	 justamente
modificar	 a	 tonalidade	 dos	 pixels	 da	 imagem,	 com	 intuito	 de
redistribuir	 o	 histograma.	 Isso	 resultará	 em	 uma	 imagem	 mais
nítida,	contendo	 pixels	 com	 tonalidades	 de	cinza	variando	 de	0	a 255
'''

import cv2
import matplotlib 
import numpy as np
from matplotlib import pyplot as grafico

imagemOriginal = cv2.imread('./imagem/fumaca.jpg', 0)

#img_gray = cv2.cvtColor(imagemOriginal, cv2.COLOR_BGRA2GRAY)

imagemEqualizada = cv2.equalizeHist(imagemOriginal)

cv2.imshow('Imagem Original', imagemOriginal)

cv2.imshow('Imagem Equalizada', imagemEqualizada)

grafico.hist(imagemOriginal.ravel(), 256, [0, 256])

grafico.figure()
grafico.hist(imagemEqualizada.ravel(), 256, [0,256])

grafico.show()


#continua na pagina do livro 95


