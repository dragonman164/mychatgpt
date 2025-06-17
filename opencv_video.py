import cv2 

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.rectangle(frame, (50, 50), (200, 200), (0, 255, 0), 3)

    cv2.circle(frame, (150, 150), 40, (255, 0, 0), -1)

    cv2.putText(frame, "Hello OpenCV", (10, 400),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
    
    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()