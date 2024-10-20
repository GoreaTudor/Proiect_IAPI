import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import image_processing as ip
import os


class ImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Blurring and Compression App")
        self.root.geometry("800x600")
        self.image_path = None
        self.processed_image = None
        self.blur_type = tk.StringVar(value="Gaussian")
        self.kernel_size = tk.IntVar(value=3)
        self.save_format = tk.StringVar(value="JPEG")
        self.compression_quality = tk.IntVar(value=90)
        self.create_widgets()


    def create_widgets(self):
        upload_button = tk.Button(self.root, text="Upload Image", command=self.upload_image)
        upload_button.pack(pady=10)

        blur_frame = tk.Frame(self.root)
        blur_frame.pack(pady=10)

        tk.Label(blur_frame, text="Select Blur Type:").grid(row=0, column=0, padx=5)
        ttk.Combobox(blur_frame, textvariable=self.blur_type, values=["Gaussian", "Box", "Median"]).grid(row=0,
                                                                                                         column=1,
                                                                                                         padx=5)

        tk.Label(blur_frame, text="Kernel Size:").grid(row=1, column=0, padx=5)
        tk.Spinbox(blur_frame, from_=3, to_=15, increment=2, textvariable=self.kernel_size).grid(row=1, column=1,
                                                                                                 padx=5)

        blur_button = tk.Button(blur_frame, text="Apply Blur", command=self.apply_blur)
        blur_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.image_label = tk.Label(self.root)
        self.image_label.pack()

        save_frame = tk.Frame(self.root)
        save_frame.pack(pady=10)

        tk.Label(save_frame, text="Save As:").grid(row=0, column=0, padx=5)
        ttk.Combobox(save_frame, textvariable=self.save_format, values=["JPEG", "PNG"]).grid(row=0, column=1, padx=5)

        tk.Label(save_frame, text="Compression Quality:").grid(row=1, column=0, padx=5)
        tk.Spinbox(save_frame, from_=10, to_=100, textvariable=self.compression_quality).grid(row=1, column=1, padx=5)

        save_button = tk.Button(save_frame, text="Save Image", command=self.save_image)
        save_button.grid(row=2, column=0, columnspan=2, pady=10)


    def upload_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
        if self.image_path:
            self.display_image(self.image_path)


    def display_image(self, image_path):
        image = Image.open(image_path)
        image.thumbnail((400, 400))
        self.photo_image = ImageTk.PhotoImage(image)
        self.image_label.config(image=self.photo_image)


    def apply_blur(self):
        if not self.image_path:
            messagebox.showwarning("No Image", "Please upload an image first.")
            return

        image = cv2.imread(self.image_path)
        kernel_size = self.kernel_size.get()

        if self.blur_type.get() == "Gaussian":
            self.processed_image = ip.apply_gaussian_blur(image, kernel_size)
        elif self.blur_type.get() == "Box":
            self.processed_image = ip.apply_box_blur(image, kernel_size)
        elif self.blur_type.get() == "Median":
            if kernel_size % 2 == 1:  # Ensure the kernel size is odd
                self.processed_image = ip.apply_median_blur(image, kernel_size)
            else:
                messagebox.showerror("Kernel Size Error", "Kernel size for Median Blur must be odd.")
                return

        display_image = ip.convert_bgr_to_rgb(self.processed_image)
        display_image = Image.fromarray(display_image)
        self.display_processed_image(display_image)


    def display_processed_image(self, image):
        image.thumbnail((400, 400))
        self.photo_image = ImageTk.PhotoImage(image)
        self.image_label.config(image=self.photo_image)


    def save_image(self):
        if self.processed_image is None:
            messagebox.showwarning("No Processed Image", "Please apply blur before saving.")
            return

        save_path = filedialog.asksaveasfilename(defaultextension=f".{self.save_format.get().lower()}",
                                                 filetypes=[
                                                     (self.save_format.get(), f"*.{self.save_format.get().lower()}")])

        if save_path:
            temp_path = "temp_image.png"
            cv2.imwrite(temp_path, self.processed_image)

            ip.compress_image(temp_path, save_path, format=self.save_format.get(),
                              quality=self.compression_quality.get())

            os.remove(temp_path)
            messagebox.showinfo("Success", f"Image saved as {save_path}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageApp(root)
    root.mainloop()
