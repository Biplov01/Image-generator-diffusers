import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import os

# Initialize the Stable Diffusion model
model_id = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

def generate_image(prompt):
    """
    Generate an image based on the provided prompt and save it to a file.
    """
    # Generate the image
    image = pipe(prompt).images[0]
    
    # Define filename for saving the image
    image_filename = f"{prompt.replace(' ', '_')}_image.png"
    image.save(image_filename)
    
    return image_filename

def main():
    """
    Main function to handle user input and image generation.
    """
    while True:
        # Ask the user for the image prompt
        prompt = input("Enter words related to image (or type 'exit' to quit): ")
        
        if prompt.lower() == 'exit':
            print("Exiting the application.")
            break
        
        # Generate the image
        image_filename = generate_image(prompt)
        print(f"Image generated and saved as {image_filename}")
        
        # Optionally, you can display the image here if you have a GUI or prefer to open it in default viewer
        # For simplicity, we'll just confirm the image was saved
        print(f"Image saved at: {os.path.abspath(image_filename)}")

if __name__ == "__main__":
    main()
