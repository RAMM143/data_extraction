import fitz  # PyMuPDF
import PIL.Image
from google import genai
from google.genai import types  # if you need to use specific types, though passing a PIL image is supported


pdf_path = 'sample_health.pdf'  # path to your PDF file
doc = fitz.open(pdf_path)
images = []

for page in doc:
    pix = page.get_pixmap()
    # Convert the pixmap into a PIL Image (assumes RGB)
    img = PIL.Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    images.append(img)

print(f"Converted {len(images)} pages to images.")

# Define a prompt that instructs the model to extract the data
prompt_text = "Extract all the values and data from the following PDF pages about a person health related."

# Create a list of contents: first the prompt, then each image.
contents = [prompt_text] + images

client = genai.Client(api_key="AIzaSyD8VlcNSPmClQxXpKGMJ1JtWi-ygK4lVH8")  # Replace with your API key

response = client.models.generate_content(
    model="gemini-2.0-flash",   # Adjust the model variant if needed
    contents=contents
)

print("Extracted Data:")
print(response.text)
