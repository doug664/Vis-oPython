import cv2 

imagem = cv2.imread('./imagem/frutas.jpg')
valorPixel = imagem[150,150]
print(valorPixel)
