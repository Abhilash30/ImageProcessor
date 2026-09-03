import cv2
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "../../images/reciept.jpeg")
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


if image is None:
    print(f"Error: Could not load image from {image_path}")
    exit()

blurred = cv2.GaussianBlur(image, (5, 5), 0) #Gaussianblur to remove noise and uneveness

threshold_value, otsu_thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret, thresh = cv2.threshold(blurred, 128, 255, cv2.THRESH_BINARY)
print(f"Otsu's computed optimal threshold value: {threshold_value}")
cv2.imwrite("NormalThresholding_processed_doc.jpg", thresh)
cv2.imwrite("Otsu_processed_doc.jpg", otsu_thresh)
