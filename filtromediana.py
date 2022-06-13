import cv2 
'''imgOri = cv2.imread('./imagem/moedas.jpg')
imgTra = cv2.medianBlur(imgOri, 5)

cv2.imshow('original', imgOri)
cv2.imshow('Tratada', imgTra)

cv2.waitKey(0)
cv2.destroyAllWindows()'''

'''
Apenas	 dois	 parâmetros	 são	 necessários	 para	 utilizá-lo.	 O
primeiro	deles	é	a	imagem	que	receberá	o	tratamento,	e	o	segundo
é	 um	 valor	 inteiro,	 ímpar	 e	 positivo,	 que	 indicará	 a	 sua
intensidade.
'''
#Tratamento de imagem com ruido sal e pimenta
imgOri = cv2.imread('./imagem/mulher.jpg')
imgTra = cv2.medianBlur(imgOri, 5)

cv2.imshow('original', imgOri)
cv2.imshow('Tratada', imgTra)

cv2.waitKey(0)
cv2.destroyAllWindows()