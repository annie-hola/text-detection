import cv2
import easyocr
import matplotlib.pyplot as plt 

# read image
image_path = 'image/demo.jpeg'

img = cv2.imread(image_path)

# instance text detector
reader = easyocr.Reader(['en'], gpu=False)

# detect text on image
text_ = reader.readtext(img)

print(text_)

# thresold to put text
threshold = 0.25 

# draw bbox and text
for t_, t in enumerate(text_):
    print(t)

    bbox, text, score = t

    if score > threshold:
        # (0, 255, 0) -> RGB -> green
        # 5 -> thickness
        # bbox: ([[80, 1219], [437, 1219], [437, 1269], [80, 1269]], 'GLYCERIDES', 0.7417769417498916)
        cv2.rectangle(img, bbox[0], bbox[2], (0, 255, 0), 5)
        
        cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()