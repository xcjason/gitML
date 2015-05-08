import cv2

def detect(path):
    img = cv2.imread(path)
    cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rects = cascade.detectMultiScale(gray, 1.1, 5)

    if len(rects) == 0:
        return [], img
    rects[:, 2:] += rects[:, :2]
    return rects, img

def box(rects, img):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), (127, 255, 0), 2)
    cv2.imwrite('detected.jpg', img);
    cv2.imshow('detected.jpg', img);
    cv2.waitKey(0)
    cv2.destroyAllWindows()

rects, img = detect("face4.jpg")
print len(rects)
box(rects, img)
