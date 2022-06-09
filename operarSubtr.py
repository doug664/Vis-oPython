# Utilizando a operação de subtração nas imagens

import	cv2
imagemFichaPosicao1	=	cv2.imread("./imagem/fichasvermelhas.jpg")
imagemFichaPosicao2	=	cv2.imread("./imagem/fichaspretas.jpg")
imagem	=	cv2.subtract(imagemFichaPosicao1,	imagemFichaPosicao2)
cv2.imshow("Resultado",	imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()