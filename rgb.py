import cv2
import matplotlib.pyplot as plt

file_path = 'rgb.png'
image = cv2.imread(file_path)
print(image.shape)

blue, green, red = cv2.split(image)

plt.imshow(blue, cmap="gray")
plt.show()

plt.imshow(green, cmap="gray")
plt.show()

plt.imshow(red, cmap="gray")
plt.show()

rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_image)
plt.show()