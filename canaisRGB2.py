import cv2

# Carregando a imagem e segmentando canais
imagem = cv2.imread('./imagem/frutas.jpg')
azul, verde, vermelho = cv2.split(imagem)

#Combinando os tês canais em uma unica imagem
img = cv2.merge((azul, verde, vermelho))

cv2.imshow('Imagem combinada', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Para exibir a matriz com os valores ods pixels no console
#rint(azul)
#print(verde)
#print(vermelho)
