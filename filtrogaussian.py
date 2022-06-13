import cv2 

imgORI = cv2.imread('./imagem/moedas.jpg')
imgTra = cv2.GaussianBlur(imgORI, (5,5), 0)

cv2.imshow('Original', imgORI)
cv2.imshow('Tratada', imgTra)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Para lembrar
# cv2.GaussianBlur(imgORI, (5,5), 0)
# 1 - imagem a ser processada
# 2 - máscara	de	ordem	3x3 , 5x5 e etc
# 3 - 	sigma, pode ser 0,1,2,3,4,5...