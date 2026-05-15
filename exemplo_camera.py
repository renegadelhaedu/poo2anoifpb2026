#pypi - repositório de pacotes python
#para instalar use o pip install nome_pacote
#instalando um pacote externo

import cv2
rtsp_url = "rtsp://nyfb:kk247n@192.168.0.104:554/live"
#cap = cv2.VideoCapture(rtsp_url, cv2.CAP_FFMPEG)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erro ao abrir o fluxo RTSP")
    exit()

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow("oi", frame)

        if cv2.waitKey(2) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()