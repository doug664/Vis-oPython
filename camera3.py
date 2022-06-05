# capturando imagem de uma webcam
import cv2

captura = cv2.VideoCapture(0)

while True:
    ret, frame = cv2.imread()
    cv2.imshow('Captura de video', frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

captura.release()
cv2.destroyAllWindows()