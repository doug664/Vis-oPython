# Exibindo valor do canal da imagem em RGB
# 0 - canal Blue
# 1 - canal Green
# 2 - canal Red

import cv2

imagem = cv2.imread('./imagem/frutas.jpg')
img_canal = imagem[150, 150, 0]
print(img_canal)