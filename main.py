import os
import qrcode
from qrcode.constants import ERROR_CORRECT_H
from dotenv import load_dotenv
import logging
from pathlib import Path
import validators

# Load environment variables
load_dotenv()

# Environment Variables for Configuration
url = os.getenv("QR_DATA_URL", "https://github.com/saisrinivas194")
output_dir = os.getenv("QR_CODE_DIR", "qr_codes")
output_file = os.getenv("QR_CODE_FILENAME", "githubQR.png")
fill_color = os.getenv("FILL_COLOR", "black")
back_color = os.getenv("BACK_COLOR", "white")

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

def is_valid_url(url):
    """Validate the provided URL."""
    if validators.url(url):
        return True
    else:
        logging.error(f"Invalid URL provided: {url}")
        return False

def create_directory(path):
    """Create the output directory if it doesn't exist."""
    try:
        path.mkdir(parents=True, exist_ok=True)
        logging.info(f"Directory created: {path}")
    except Exception as e:
        logging.error(f"Failed to create directory {path}: {e}")
        exit(1)

def generate_qr_code(data, path, fill_color='black', back_color='white'):
    """Generate a QR code and save it to the specified path."""
    if not is_valid_url(data):
        return  # Exit the function if the URL is not valid

    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        # Create an image of the QR code
        img = qr.make_image(fill_color=fill_color, back_color=back_color)

        # Save the image
        img.save(path)
        logging.info(f"QR code successfully saved to {path}")

    except Exception as e:
        logging.error(f"An error occurred while generating or saving the QR code: {e}")

def main():
    # Ensure the output directory exists
    create_directory(Path(output_dir))

    # Generate and save the QR code
    output_path = Path(output_dir) / output_file
    generate_qr_code(url, output_path, fill_color, back_color)

if __name__ == "__main__":
    main()
