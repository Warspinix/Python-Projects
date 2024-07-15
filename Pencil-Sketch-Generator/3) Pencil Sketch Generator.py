import cv2
import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        process_image(file_path)

def process_image(file_path):
    image = cv2.imread(file_path)

    cv2.imshow("Image", image)
    cv2.waitKey(0)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale", gray_image)
    cv2.waitKey(0)

    inverted_image = 255 - gray_image
    cv2.imshow("Inverted", inverted_image)
    cv2.waitKey(0)

    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    inverted_blurred = 255 - blurred
    pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
    cv2.imshow("Sketch", pencil_sketch)
    cv2.waitKey(0)

    cv2.imshow("Original Image", image)
    cv2.waitKey(0)
    cv2.imshow("Pencil Sketch", pencil_sketch)

    key = cv2.waitKey(0)
    if key == 32:  # ASCII code for spacebar
            cv2.destroyAllWindows()

# Create the main window
root = tk.Tk()
root.title("Image Processing App")

# Create and set up the menu
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Options", menu=file_menu)
file_menu.add_command(label="Select Image", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

# Run the Tkinter main loop
root.mainloop()