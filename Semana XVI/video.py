import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("No se pudo abrir la webcam :(")
    quit()

while True: # while cap.isOpened()
    _, frame = cap.read()
    cv.imshow("WEBCAM", frame)
    # key = cv.waitKey()
    # print(key)
    if cv.waitKey(25) == ord("q"):
        break