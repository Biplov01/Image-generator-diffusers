import torch
from diffusers import StableDiffusionPipeline
from PIL import Image, ImageTk
import numpy as np
import cv2
import csv
import tkinter as tk
from tkinter import filedialog, messagebox

# Initialize the Stable Diffusion model
model_id = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

# Function to generate and save image based on prompt
def generate_image(prompt):
    # Generate the image
    image = pipe(prompt).images[0]
    
    # Define filename for saving the image
    image_filename = f"{prompt.replace(' ', '_')}_image.png"
    image.save(image_filename)
    
    # Return the image filename
    return image_filename

# Function to handle button click
def on_generate_click():
    # Get the text from the input field
    prompt = prompt_entry.get()
    
    if not prompt:
        messagebox.showwarning("Input Error", "Please enter a prompt.")
        return
    
    # Generate the image
    image_filename = generate_image(prompt)
    
    # Load and display the image
    img = Image.open(image_filename)
    img.thumbnail((400, 400))  # Resize for display
    img_tk = ImageTk.PhotoImage(img)
    
    # Update the label with the generated image
    img_label.config(image=img_tk)
    img_label.image = img_tk
    
    # Notify the user
    messagebox.showinfo("Success", f"Image generated and saved as {image_filename}")

# Create the main Tkinter window
root = tk.Tk()
root.title("Image Generator")

# Create and place widgets
prompt_label = tk.Label(root, text="Enter words related to image:")
prompt_label.pack(pady=10)

prompt_entry = tk.Entry(root, width=50)
prompt_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Image", command=on_generate_click)
generate_button.pack(pady=10)

img_label = tk.Label(root)
img_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
