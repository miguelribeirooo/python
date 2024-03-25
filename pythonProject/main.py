import cv2

# Captura de vídeo da webcam
cap = cv2.VideoCapture(0)

while True:
    # Captura de frame da câmera
    ret, frame = cap.read()

    # Convertendo o frame para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Suavizando a imagem para remover ruídos
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detectando as bordas na imagem
    edges = cv2.Canny(blurred, 50, 150)

    # Encontrando contornos na imagem
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Desenhando bounding boxes ao redor dos objetos encontrados
    for contour in contours:
        # Obtendo as coordenadas do retângulo delimitador
        x, y, w, h = cv2.boundingRect(contour)

        # Desenhando o retângulo delimitador
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Exibir o frame
    cv2.imshow('Detecção de Objetos', frame)

    # Parar o loop ao pressionar a tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar a câmera e fechar as janelas
cap.release()
cv2.destroyAllWindows()
