import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_images(images, titles, is_grayscale=None):
    plt.figure(figsize=(15, 10))
    for i in range(len(images)):
        plt.subplot(3, 3, i+1)
        if is_grayscale and is_grayscale[i]:
            plt.imshow(images[i], cmap='gray')
        else:
            plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
        plt.title(titles[i])
        plt.axis('off')
    plt.show()

# Load the image in color
image = cv2.imread('input.jpg', cv2.IMREAD_COLOR)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Smoothing Filters
mean_filtered = cv2.blur(image, (5, 5))
gaussian_filtered = cv2.GaussianBlur(image, (5, 5), 0)
median_filtered = cv2.medianBlur(image, 5)

# Image Gradient
sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
gradient_magnitude = cv2.magnitude(sobel_x, sobel_y)
cv2.normalize(gradient_magnitude, gradient_magnitude, 0, 255, cv2.NORM_MINMAX)
gradient_magnitude = np.uint8(gradient_magnitude)

# Sharpening
kernel_sharpening = np.array([[-1, -1, -1],
                               [-1,  9, -1],
                               [-1, -1, -1]])
sharpened_image = cv2.filter2D(image, -1, kernel_sharpening)

# Canny Edge Detection
canny_edges = cv2.Canny(gray_image, 100, 200)

# Display Results
display_images(
    [image, mean_filtered, gaussian_filtered, median_filtered, gradient_magnitude, sharpened_image, canny_edges],
    ['Original', 'Mean Filter', 'Gaussian Filter', 'Median Filter', 'Gradient Magnitude', 'Sharpened Image', 'Canny Edge Detection'],
    [False, False, False, False, True, False, True]
)

# Save Results
cv2.imwrite('mean_filtered.jpg', mean_filtered)
cv2.imwrite('gaussian_filtered.jpg', gaussian_filtered)
cv2.imwrite('median_filtered.jpg', median_filtered)
cv2.imwrite('gradient_magnitude.jpg', gradient_magnitude)
cv2.imwrite('sharpened_image.jpg', sharpened_image)
cv2.imwrite('canny_edges.jpg', canny_edges)
