
import cv2

imagem = cv2.imread('./imagem/frutas.jpg')

img_gray = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY )
cv2.imshow('Imagem em tons de cinza', img_gray)

#alva a imagem em um caminho
#cv2.imwrite('imagem-em-tons-de-cinza.jpg', img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()

