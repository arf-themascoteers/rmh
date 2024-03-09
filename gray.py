import cv2
import matplotlib.pyplot as plt

file_path = 'gray.png'
gray_image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
plt.imshow(gray_image, cmap='gray')
plt.show()
print(gray_image.shape)