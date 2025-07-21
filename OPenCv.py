import cv2 as cv

image_path = "/home/kiprotich/Downloads/imread.jpg"
image = cv.imread(image_path)

if image is None:
    print("Failed to load image. Check the file path.")
else:
    print("Image Matrix:\n", image)              # Show raw pixel data
    print("\nImage Shape:", image.shape)         # (rows, cols, channels)
    print("Image Data Type:", image.dtype)       # e.g., uint8

    cv.imshow("image", image)
    cv.waitKey(0)
    cv.destroyAllWindows()
