# com o metodo shape se pode exibir no console o total de linhas e colnuas de uma matriz da imagem e também a quantidade de canais imagem
# quando a imagem é rgb são 3
# quando em tons de cinza são 2

import cv2
imagem = cv2.imread('./imagem/frutas.jpg')

print(imagem.shape) # (462, 624, 3)


# Usando o metodo size ele retorna o total de pixels da imagem, qunado rgb o total é a combinação das linhas, colunas e os canais, pegando esse valor e divindindo por 3 o resultado é o produto das linhas pelas colunas
# qunado a imagem é em tons de cinza o metodo size já retorna o produto das linhas pelas colunas

print(imagem.size)# 864864
print(imagem.size/3)
