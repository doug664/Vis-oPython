#Histograma em imagem binaria

import cv2
imagem = cv2.imread('./imagem/imagem.jpg', 0) # O paramentro 0(zero) indica a leitura da imagem em tons de cinza
totalPixelPreto = 0
totalPixelBranco = 0

for x in range(0, 499):
    for y in range(0, 499):
        if imagem[x,y] == 255:
            totalPixelBranco += 1
        else:
            totalPixelPreto += 1

print(totalPixelBranco)
print(totalPixelPreto)

# OBS:
#Salvar uma	 imagem	 binária	 utilizando	 um	 formato	 compactado,	como JPEG,	 poderia	 resultar	 em	 pixels	 com	 valores	intermediários,	em tons	de	cinza,	não	apenas	pretos	e	brancos.

'''
OBS:
Mesmo	 sendo	 um	 algoritmo	 simples	 e	 de	fácil	 entendimento,
esse	 procedimento	com o for, não	 é	 muito	 utilizado	 para	 obter	 o	 total	 de pixels	 de	 cada	 cor.	Isso	 porque	 a	 biblioteca Matplotlib	 possui	 afunção		hist	,	que,	além	de abstrair	essa	 tarefa,	gera	a	figura	que
ilustra	 o	 histograma	 de	 cores	 da	 imagem.
'''