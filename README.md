
# Flow Image Studio

AI-powered image generation automation tool that automates image generation through Google Flow using Playwright.

## Overview

Flow Image Studio is a desktop-based automation tool designed to simplify the process of generating multiple images from a list of prompts.

The application provides a simple interface where users can:

- Enter multiple image prompts
- Assign timestamps to prompts
- Automatically send prompts to Google Flow
- Monitor generation progress
- Detect newly generated images
- Download generated images in 2K resolution
- Convert downloaded images to JPG format
- Save images using timestamp-based filenames
- Continue processing multiple prompts automatically

## Key Features

### Automated Prompt Processing
Users can enter multiple prompts in the application and process them sequentially.

### Google Flow Automation
The application connects to an existing Chrome session and interacts with Google Flow using Playwright.

### Generation Monitoring
The automation waits for a newly generated image to appear before moving to the download stage.

### 2K Image Download
Generated images are downloaded from Google Flow at 2K resolution.

### Automatic JPG Conversion
Downloaded images are converted to RGB JPG format and saved with high-quality JPEG compression.

### Timestamp-Based File Naming
Images are saved using their associated timestamps, making the generated files easy to organize.

### Progress Tracking
The Streamlit interface displays the progress of the image generation process and identifies completed or failed generations.

## Technology Stack

- Python
- Streamlit
- Playwright
- Pillow
- Google Flow
- Google Chrome
- GitHub

## Project Structure

```text
Flow Image generation/
│
├── app.py
├── flow_engine.py
├── flow_automation.py
├── launch_flow.vbs
├── start.bat
├── README.md
├── flow_extension/
│   ├── manifest.json
│   ├── popup.html
│   └── popup.js
│
├── operolabs_logo_transparent.png
└── OperoLabs_Flow_Image_Studio.ico
```
## How It Works

The user enters image prompts through the Flow Image Studio interface.

The application connects to an existing Chrome session.

Playwright opens the Google Flow interface.

Each prompt is entered and submitted sequentially.

The automation detects the newly generated image.

The image is downloaded in 2K resolution.

The downloaded file is converted to JPG.

The final image is saved using its timestamp.

The interface updates the generation progress.
## Requirements

- Windows
- Python 3.x
- Google Chrome
- Google Flow access
- Playwright
- Pillow
- Streamlit

## Technology Stack

- Python
- Streamlit
- Playwright
- Pillow
- Google Flow
- Google Chrome

## Key Features

- Automated prompt processing
- Sequential image generation
- Generation progress tracking
- Automatic detection of newly generated images
- 2K image downloads
- Automatic JPG conversion
- Timestamp-based file naming
- Organized output handling

## Author

**Hasina Mumtaz Laskar**

AI Automation Project — Flow Image Studio
