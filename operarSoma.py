# fazendo a operação de adição em imagens

'''
Geralmente,	 para	 que	 as	 operações	 de	 adição	 e	 mistura
possam	ser	realizadas,	é	necessário	que	as	imagens	possuam	a
mesma	 dimensão	 (largura	 x	 altura)	 e	 tipo	 (8	 bits,	 por
exemplo).

'''
import	cv2
imagemFichasVermelhas	=	cv2.imread("./imagem/fichasvermelhas.jpg")
imagemFichasPretas	=	cv2.imread("./imagem/fichaspretas.jpg")
imagem = cv2.add(imagemFichasVermelhas,	imagemFichasPretas)
cv2.imshow("Resultado",	imagem)
cv2.imwrite('./imagem/imagem-com-adição.jpg', imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()