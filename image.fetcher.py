import os
import requests
from urllib.parse import urlparse
from datetime import datetime

def fetch_image():
    # 🧠 Prompt user for an image URL
    image_url = input("🌐 Enter the image URL to fetch: ").strip()

    # 📁 Create the "Fetched_Images" directory if it doesn't exist
    image_dir = "Fetched_Images"
    os.makedirs(image_dir, exist_ok=True)

    try:
        # 🌍 Connect to the global community of the web
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()  # Will raise HTTPError for bad responses

        # 📸 Try to extract a filename from the URL
        parsed_url = urlparse(image_url)
        filename = os.path.basename(parsed_url.path)

        # If filename is empty or doesn't look like a file, generate one
        if not filename or '.' not in filename:
            extension = response.headers.get("Content-Type", "").split("/")[-1]
            if not extension:
                extension = "jpg"
            filename = f"image_{datetime.now().strftime('%Y%m%d%H%M%S')}.{extension}"

        file_path = os.path.join(image_dir, filename)

        # 💾 Save the image in binary mode
        with open(file_path, 'wb') as file:
            file.write(response.content)

        print(f"✅ Image saved successfully as: {file_path}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to fetch image: {e}")

if __name__ == "__main__":
    fetch_image()
