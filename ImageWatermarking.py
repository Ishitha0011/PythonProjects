import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Watermarking App")

        # Canvas for displaying images
        self.canvas = tk.Canvas(root, width=600, height=400)
        self.canvas.pack()

        # Buttons for loading image and applying watermark
        self.btn_load = tk.Button(root, text="Load Image", command=self.load_image)
        self.btn_load.pack(pady=10)

        self.btn_watermark_text = tk.Button(root, text="Add Text Watermark", command=self.add_text_watermark)
        self.btn_watermark_text.pack(pady=5)

        self.btn_watermark_image = tk.Button(root, text="Add Image Watermark", command=self.add_image_watermark)
        self.btn_watermark_image.pack(pady=5)

    def load_image(self):
        # Open a file dialog to select an image file
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png;*.bmp")])
        if file_path:
            self.image = Image.open(file_path)
            # Resize image to fit within the canvas
            self.image.thumbnail((600, 400))
            self.photo = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

    def add_text_watermark(self):
        if hasattr(self, 'image'):
            watermark_text = "Your Watermark Text"
            draw = ImageDraw.Draw(self.image)
            font = ImageFont.truetype("arial.ttf", 36)  # Adjust font and size as needed
            text_width, text_height = draw.textsize(watermark_text, font)
            text_position = ((self.image.width - text_width) // 2, self.image.height - text_height - 10)
            draw.text(text_position, watermark_text, fill="white", font=font)
            self.update_canvas()
        else:
            messagebox.showwarning("Error", "Please load an image first.")

    def add_image_watermark(self):
        if hasattr(self, 'image'):
            file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
            if file_path:
                watermark_image = Image.open(file_path)
                # Resize watermark image to fit within the main image
                watermark_image.thumbnail((self.image.width // 4, self.image.height // 4))
                self.image.paste(watermark_image, (10, 10), watermark_image)
                self.update_canvas()
        else:
            messagebox.showwarning("Error", "Please load an image first.")

    def update_canvas(self):
        # Update displayed image on the canvas
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

def main():
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
