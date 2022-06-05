# Atribuindo novos valores ao pixel na imagem

import cv2

imagem = cv2.imread('./imagem/frutas.jpg')
print(imagem[150,150]) # valor original

imagem[150,150] = [255,255,255]

print(imagem[150,150])# exibe o valor alterado do pixel