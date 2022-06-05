import cv2

imagem = cv2.imread('./imagem/frutas.jpg')

img_hsv = cv2.cvtColor(imagem, cv2.COLOR_RGB2HSV)
matiz, saturacao, valor = cv2.split(img_hsv)

cv2.imshow('canal H', matiz)
cv2.imshow('canal S', saturacao)
cv2.imshow('Canal V', valor)

cv2.waitKey(0)
cv2.destroyAllWindows()