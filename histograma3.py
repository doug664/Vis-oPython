# Histograma de imagem colorida, para a ikmagem colorida será feito um histograma para cada canal, uma vez que os canais separados estarm em tons de cinza

import cv2
import numpy as np
from matplotlib import pyplot as grafico

imagem = cv2.imread('./imagem/frutas.jpg')

azul, verde, vermelho = cv2.split(imagem)

grafico.hist(azul.ravel(), 256, [0,256])

grafico.figure()
grafico.hist(verde.ravel(), 256, [0, 256])

grafico.figure()
grafico.hist(vermelho.ravel(), 256, [0, 256])

grafico.show()

# o metodo figure permite cria uma nova figura que apresentada os histogramas em uma unica imagem