import cv2

# Carregando as imagens RGB e segmentando(separação) canais
imagem = cv2.imread('./imagem/frutas.jpg')
azul, verde, vermelho = cv2.split(imagem)

#Exibindo imagens com canais separados
cv2.imshow('Canal R', vermelho)
cv2.imshow('Canal G', verde)
cv2.imshow('Canal B', azul)

cv2.imwrite('frutas-canal-vermelho.jpeg', vermelho)
cv2.imwrite('frutas-canal-verde.jpeg', verde)
cv2.imwrite('frutas-canal-azul.jpeg', azul)

cv2.waitKey(0)
cv2.destroyAllWindows()
