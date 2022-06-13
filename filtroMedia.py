#O	 filtro	 de	 média	 pode	 ser	 aplicado	 pela	 função	 blur		 da
'''biblioteca	 OpenCV,	 que	 requer	 apenas	 dois	 parâmetros.	 O
primeiro	 refere-se	 à	 imagem	 que	 será	 submetida	 ao	 filtro,	 o
segundo,	 à	 dimensão	 da	 máscara	 que	 será	 aplicada.'''

import cv2 
imgOriginal = cv2.imread('./imagem/moedas.jpg')

imgTratada = cv2.blur(imgOriginal, (5,5))

cv2.imshow('Original', imgOriginal)
cv2.imshow('Tratada', imgTratada)

cv2.waitKey(0)
cv2.destroyAllWindows()
