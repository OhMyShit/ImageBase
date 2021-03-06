import cv2

cap = cv2.VideoCapture(1)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
outfile = cv2.VideoWriter('output.avi', fourcc, 25., (640, 480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        outfile.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xfff == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()