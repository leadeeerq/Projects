import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('1.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Detecting characters (or digits only)
hImg, wImg, _ = img.shape
# OEM_CUBE_ONLY, PSM_SINGLE_BLOCK
# config = r'--oem 1 --psm 6 outputbase digits'
# boxes = pytesseract.image_to_boxes(img, config=config)
boxes = pytesseract.image_to_boxes(img)

for box in boxes.splitlines():
    box = box.split(' ')
    # print(box)
    x, y, width, height = int(box[1]), int(box[2]), int(box[3]), int(box[4])
    cv2.rectangle(img, (x, hImg - y), (width, hImg - height), (255, 255, 0), 2)
    cv2.putText(img, box[0], (x, hImg - y + 20), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 2)

# Detecting words
hImg, wImg, _ = img.shape
boxes = pytesseract.image_to_data(img)

for idx, box in enumerate(boxes.splitlines()):
    box = box.split('\t')
    print(box)
    # Skip the first row (with headers) and take rows with not empty value in last position
    if idx != 0 and box[-1] != '':
        x, y, width, height = int(box[-6]), int(box[-5]), int(box[-4]), int(box[-3])
        cv2.rectangle(img, (x, y), (width+x, height+y), (255, 255, 0), 2)
        cv2.putText(img, box[-1], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 2)

cv2.imshow('Image', img)
cv2.waitKey(0)

