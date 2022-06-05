import cv2

img = cv2.imread('./imagem/terra.jpg')
cv2.imshow('Terra', img)
cv2.waitKey(0)
cv2.destroyAllWindows()