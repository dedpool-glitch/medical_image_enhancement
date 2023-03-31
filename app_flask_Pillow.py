import cv2
from flask import Flask, request, render_template
from PIL import Image
import io
import base64

def process_image(image):
    grey_img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    clahe=cv2.createCLAHE(clipLimit=3.0,tileGridSize=(5,5))
    clahe_img=clahe.apply(grey_img)
    return clahe_img

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_image', methods=['POST'])
def process_image():
    # Get the uploaded file
    file = request.files['file']
    
    # Read the image data
    image_data = file.read()
    
    # Create a Pillow image from the image data
    image = Image.open(io.BytesIO(image_data))
    
    # Process the image (replace this with your own image processing code)
    processed_image = process_image(image)
    
    # Convert the processed image to a base64-encoded string
    buffered = io.BytesIO()
    processed_image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    
    # Render the result page with the processed image
    return render_template('result.html', img_str=img_str)

if __name__ == '__main__':
    app.run(debug=True)

