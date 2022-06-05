# Carregando um video com o openCv
import cv2 

captura = cv2.VideoCapture('./video/videoTeste.mp4')

while True:
    ret, frame = captura.read()
    cv2.imshow('Teste de Video', frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

captura.release() 
cv2.destroyAllWindows()