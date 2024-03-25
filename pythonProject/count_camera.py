import cv2
import numpy as np

def detect_and_count_significant_blue_tip_descents():
    cap = cv2.VideoCapture(0)
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])
    one_cm_equivalent_px = 162

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 100:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                cordenadaX = "{:.2f}".format(x / one_cm_equivalent_px)
                cordenadaY = "{:.2f}".format(y / one_cm_equivalent_px)
                text = f'Coordenadas: (X:{cordenadaX}cm, Y:{cordenadaY}cm)'
                cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        cv2.imshow('Camera', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

detect_and_count_significant_blue_tip_descents()
