'''
Para	 executar	 esse
método,	 quatro	 parâmetros	 são	 requeridos.	 O	 primeiro	 deles	 é	 a
imagem	que	receberá	o	tratamento,	e	o	segundo	indica	o	tamanho
do	filtro.	Quanto	maior	o	valor	do	segundo	parâmetro,	mais	lenta
será	a	 execução	 desse	método,	não	 sendo	 recomendado	 trabalhar
com	 valores	 superiores	 a	 5	 em	 processamento	 de	 imagens	 em
tempo	real.

Geralmente,	os	mesmos	valores	são	utilizados	no	terceiro	e	no
quarto	 parâmetro.	 O	 terceiro	 é	 conhecido	 como(sigma	e	o	quarto	como	(sigma	space).	Na	prática,	quando menores	 que	 10,	 esses	 valores	 não	 apresentam	 resultados
significativos	no	tratamento	de	ruído	e	suavização.

 mas, quando	 maiores	 que	 150,	 podem	 provocar	 um
tratamento	 muito	 intenso,	 fazendo	 com	 que	 a	 imagem	 perca
detalhes	importantes.	 Quanto	maior	 o	 valor	 do	 parâmetro	 sigma
color,	maior	 será	 a	mistura	 das	 cores	 vizinhas,	 e	 quanto	maior	 o
valor	do	 parâmetro	 sigma	 space,	maior	 será	a	influência	 do	filtro
nos	pixels	vizinhos	–	desde	que	suas	cores	sejam	próximas.

valores	do	segundo,	terceiro	e	quarto	parâmetro	devem	ser
inteiros	e	positivos.
'''
import cv2
imgori = cv2.imread('./imagem/moedas.jpg')
imgTra = cv2.bilateralFilter(imgori, 9, 75, 75)

cv2.imshow('Original', imgori)
cv2.imshow('Tratada', imgTra)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Contnua na pagina 134