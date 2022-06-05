import cv2

imagem = cv2.imread('./imagem/frutas.jpg')
img_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
matiz, saturacao, valor = cv2.split(img_hsv)

cv2.imshow('canal H', matiz)
cv2.imshow('canal S', saturacao)
cv2.imshow('Canal V', valor)

img_merge = cv2.merge((matiz, saturacao, valor))
img3 = cv2.cvtColor(img_merge, cv2.COLOR_HSV2BGR)

cv2.imshow('Imagem segmentada e depoius convertida',img3)

cv2.waitKey(0)
cv2.destroyAllWindows()
