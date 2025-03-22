import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# List of image file paths
image_paths = [
    r'C:\Users\napha\Documents\MIT\Image\image_processing\images\circle_gaussian.png',
    r'C:\Users\napha\Documents\MIT\Image\image_processing\images\circle_mean.png',
    r'C:\Users\napha\Documents\MIT\Image\image_processing\images\circle_median.png',
    r'C:\Users\napha\Documents\MIT\Image\image_processing\images\circle_sharpened.png',
    r'C:\Users\napha\Documents\MIT\Image\image_processing\images\circle.png',
    r'C:\Users\napha\Documents\MIT\Image\image_processing\images\logo_canny_edge.png',
    r'C:\Users\napha\Documents\MIT\Image\image_processing\images\logo_x.png',
    r'C:\Users\napha\Documents\MIT\Image\image_processing\images\logo_y.png',
    r'C:\Users\napha\Documents\MIT\Image\image_processing\images\logo.png'
]

# Load images
images = [mpimg.imread(path) for path in image_paths]

# Display images in a grid
def display_images_in_grid(images, titles=None, cols=3):
    n_images = len(images)
    rows = (n_images + cols - 1) // cols
    fig, axes = plt.subplots(rows, cols, figsize=(15, 5 * rows))
    axes = axes.flatten()
    
    for i, (img, ax) in enumerate(zip(images, axes)):
        ax.imshow(img)
        if titles:
            ax.set_title(titles[i])
        ax.axis('off')
    
    # Hide any remaining empty subplots
    for ax in axes[n_images:]:
        ax.axis('off')
    
    plt.tight_layout()
    plt.show()

# Example usage:

display_images_in_grid(images)