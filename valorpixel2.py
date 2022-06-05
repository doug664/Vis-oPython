import cv2

imagem = cv2.imread('./imagem/frutas.jpg')

img_gray = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)

valorPixel = img_gray[150,150]
print(valorPixel)