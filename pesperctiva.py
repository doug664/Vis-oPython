# fazendo ajuste de perspectiva com warperspective e getPerspectiveTransform

import numpy as np
import cv2

imagem = cv2.imread('./imagem/sudoco.jpg')

pontosIniciais = np.float32(
    [
        [189,87],
        [459,84],
        [192,373],
        [484,372]
    ]
)

pontosFinais = np.float32(
    [
        [0,0],
        [500,0],
        [500,0],
        [500,500]
    ]
)

matriz = cv2.getPerspectiveTransform(
    pontosIniciais, pontosFinais
)

imagemModificada = cv2.warpPerspective(
    imagem, matriz, (500,500)
)

cv2.imshow('Imagem original', imagem)
cv2.imshow('Imagem Modificada', imagemModificada)

cv2.imwrite('./imagem/perspercitiva.jpg', imagemModificada)

cv2.waitKey()
cv2.destroyAllWindows()

#OBS: para o codigo funcionar é preciso dos valores exatos do s pixels da imagem escolhida