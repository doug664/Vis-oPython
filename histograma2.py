'''
OBS:
Mesmo	 sendo	 um	 algoritmo	 simples	 e	 de	fácil	 entendimento,
esse	 procedimento	com o for, não	 é	 muito	 utilizado	 para	 obter	 o	 total	 de pixels	 de	 cada	 cor.	Isso	 porque	 a	 biblioteca Matplotlib	 possui	 afunção		hist	,	que,	além	de abstrair	essa	 tarefa,	gera	a	figura	que
ilustra	 o	 histograma	 de	 cores	 da	 imagem.
'''
import cv2 
import numpy as np
from matplotlib import pyplot as grafico

imagem = cv2.imread('./imagem/imagem-em-tons-de-cinza.jpg', 0)
grafico.hist(imagem.ravel(), 256, [0,256])
grafico.show()

# o metodo ravel transforma a imagem em um vetor de uma linha e n colunas

'''
A  função	 hist possui 3	parâmetros fundamentais:	

    - o	 primeiro	 é	 a	 imagem	 com	 a	 qual	 desejamos trabalhar.

    - o	 segundo	 é	 o	 número	 de	 elementos	 distintos	 que
    podem	 ser	 representados.

    - o	 terceiro	indica	 o	intervalo	 entre	 os
    elementos.	 

Como se	 trata	 de	 uma imagem	 em	 tons	 de	 cinza,	 é válido	lembrar	que	estes elementos	são	números	inteiros,	variando de	0	(preto)	a	225	(branco), ou seja, 256 tonalidades distintas
'''

'''
imagem processada com baixo nível	 de	 contraste	 são	 caracterizadas	 por	 apresentarem
histogramas	estreitos,	ou	seja,	muitos	elementos	concentrados	em
intervalos	pequenos.
'''