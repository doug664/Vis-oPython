# Fazendo a oeração de translação na imagem com o metodo float32

import cv2 
import numpy as np

imagemOriginal = cv2.imread('./imagem/folha.jpg')
totalLinhas, totalColunas = imagemOriginal.shape[:2]

matriz = np.float32([[1,0,100], [0,1,100]])
imagemDeslocada = cv2.warpAffine(
    imagemOriginal,
    matriz,
    (totalColunas, totalLinhas)
)

cv2.imshow('Resultado', imagemDeslocada)

cv2.imwrite('./imagem/folhaDeslocada.jpg', imagemDeslocada)

cv2.waitKey(0)
cv2.destroyAllWindows()