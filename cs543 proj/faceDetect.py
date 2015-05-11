import cv2

def detect(path):
    img = cv2.imread(path)
    cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rects = cascade.detectMultiScale(gray, 1.01, 10)

    if len(rects) == 0:
        return [], img
    rects[:, 2:] += rects[:, :2]
    return rects, img

def box(rects, img, fileName):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), (127, 255, 0), 2)
    cv2.imwrite(fileName + '_box.jpg', img);
    cv2.imshow('detected.jpg', img);
    

fileName = 'face8'
rects, img = detect(fileName + '.jpg')
# rects, img = detect("face4_recovery.jpg")
print len(rects)
box(rects, img, fileName)
cv2.waitKey(0)
rects, img = detect(fileName + '_recovery.jpg')
box(rects, img, fileName + '_removal')
cv2.waitKey(0)
