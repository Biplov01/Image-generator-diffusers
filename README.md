# Image Generation Application

This repository contains two versions of an image generation application using the Stable Diffusion model. The applications generate images based on text prompts provided by the user.

## Features

1. **Tkinter-Based Application**:
   - A GUI-based application using Tkinter that allows users to input text prompts and generate images.
   - Displays the generated images directly within the Tkinter window.

2. **Console-Based Application**:
   - A console-based application that allows users to input text prompts via the command line.
   - Saves the generated images to disk and provides the filename in the console.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/image-generation-app.git
   cd image-generation-app
2. Install Dependencies: Ensure you have Python 3.7 or later installed. You can use a virtual environment to manage dependencies.

bash

pip install torch diffusers pillow numpy opencv-python-headless
Run the Applications:

3. For the Tkinter-based application, run:
bash

python tkinter_app.py
For the console-based application, run:
bash

python console_app.py
