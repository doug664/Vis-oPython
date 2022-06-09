#Reduzindo o tamanho de uma imagem com o resize
# os parametros fx e fy definem se a imagem será ampliada ou reduzida
# quando 1.0 não terá ajuste, mas alterado para menos a imgem fica menor, alterando para mais a imagem fica ampliada

import cv2
import numpy as np

imagemOriginal = cv2.imread('./imagem/folha.jpg')

imagemReduzida = cv2.resize(
    imagemOriginal, None, fx = 0.5, fy = 0.5,
    interpolation = cv2.INTER_CUBIC
)

cv2.imshow('Resultado', imagemReduzida)

cv2.waitKey(0)
cv2.destroyAllWindows()


'''
A	 biblioteca	 OpenCV	 nos	 fornece	 5	 opções	 de	 funções	 de
interpolação	 e,	 geralmente,	 a	 mais	 utilizada	 é	 a
cv2.INTER_CUBIC	.
'''