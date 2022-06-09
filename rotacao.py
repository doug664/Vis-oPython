# fazendo a rotação de uma imagem com o metodos
#getRotataionMatrix2D e  o warpAffine

import cv2 
import numpy as np

imagem = cv2.imread('./imagem/folha.jpg', 0)
totalLinhas, totalColunas = imagem.shape
matriz = cv2.getRotationMatrix2D(
    (totalColunas/2, totalLinhas/2), 90, 1
)

imagemRotacionada = cv2.warpAffine(
    imagem,
    matriz,
    (totalColunas, totalLinhas)
)

#Para salvar a imagem modificada
#cv2.imwrite('./imagem/Folha90graus.jpg', imagemRotacionada)
cv2.imshow("Resultado", imagemRotacionada)


cv2.waitKey()
cv2.destroyAllWindows()