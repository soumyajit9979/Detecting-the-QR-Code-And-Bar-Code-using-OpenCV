import cv2
import numpy as np
from pyzbar.pyzbar import decode
import re
img = cv2.imread('book_1.png')
# cap = cv2.VideoCapture(0)
cap=img
# cap.set(3,640)
# cap.set(4,480)

# while True:

    # success, img = cap.read()
for barcode in decode(img):
    myData = barcode.data.decode('utf-8')
    print(myData)
    # bookid=myData["Book ID"]
    book_id = re.search(r'Book ID:\s*(\d+)', myData).group(1)
    title = re.search(r'Title:\s*(.+)', myData).group(1)
    author = re.search(r'Author:\s*(.+)', myData).group(1)
    print("this is the data: ",book_id,title,author)
    pts = np.array([barcode.polygon],np.int32)
    pts = pts.reshape((-1,1,2))
    cv2.polylines(img,[pts],True,(255,0,255),5)
    pts2 = barcode.rect
    cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX, 0.9,(255,0,255),2)

cv2.imshow('Result',img)
cv2.waitKey(0)