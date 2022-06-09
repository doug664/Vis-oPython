# Misturando imagens das fichas

import	cv2
imagemFichasVermelhas	=	cv2.imread("./imagem/fichasvermelhas.jpeg")
imagemFichasPretas	=	cv2.imread("./imagem/fichaspretas.jpeg")
imagem	=	cv2.addWeighted(
			imagemFichasPretas,	0.2,	imagemFichasVermelhas,	1.0,	0
)
cv2.imshow("Resultado",	imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Continua na pagina 114...