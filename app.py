from flask import Flask, render_template, request, redirect, url_for
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
from dotenv import load_dotenv
from PIL import Image
import os
import io

# Load environment variables
load_dotenv()
api_key = os.getenv("API_KEY")
endpoint = os.getenv("ENDPOINT")

# Initialize Flask app
app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = "static/uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Initialize Azure client
credentials = CognitiveServicesCredentials(api_key)
client = ComputerVisionClient(endpoint, credentials)

# Helper function to process images for Azure
def process_image_for_azure(image_path, max_dim=4200, max_size_mb=4):
    """Resize and compress images to meet Azure's requirements."""
    img = Image.open(image_path)
    if img.width > max_dim or img.height > max_dim:
        img.thumbnail((max_dim, max_dim))
    if img.mode != "RGB":
        img = img.convert("RGB")
    output_buffer = io.BytesIO()
    quality = 95
    while quality >= 10:
        output_buffer.seek(0)
        output_buffer.truncate()
        img.save(output_buffer, format="JPEG", quality=quality, optimize=True)
        if len(output_buffer.getvalue()) <= max_size_mb * 1024 * 1024:
            break
        quality -= 5
    return output_buffer.getvalue()

# Flask Routes
@app.route("/", methods=["GET", "POST"])
def index():
    """Render the upload form."""
    if request.method == "POST":
        # Check if a file was uploaded
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        
        # Save the uploaded file
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(file_path)

        # Process and analyze the image
        image_bytes = process_image_for_azure(file_path)
        features = [VisualFeatureTypes.tags, VisualFeatureTypes.description, VisualFeatureTypes.objects]
        analysis = client.analyze_image_in_stream(io.BytesIO(image_bytes), features)

        # Pass the relative path to the template
        image_url = f"uploads/{file.filename}"

        # Render results
        return render_template("result.html", analysis=analysis, image_url=image_url)
    
    return render_template("index.html")

# Run the app
if __name__ == "__main__":
    app.run(debug=True)