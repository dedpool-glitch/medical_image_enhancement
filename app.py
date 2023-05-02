from flask import Flask, request, send_file
from PIL import Image
import io
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/')
def homepage():
    return """
<!DOCTYPE html>
<html>
<head>
  <title>Image Processing</title>
</head>
<body>
  <h1>Image Processing</h1>
  <form action="process_image" method="post" enctype="multipart/form-data">
    <input type="file" name="image_file" accept="image/*"><br><br>
    <input type="submit" value="Process">
  </form>
</body>
</html>
"""

@app.route('/process_image', methods=['POST'])
def process_image():
    img_bytes = request.files['image_file'].read()
    image = Image.open(io.BytesIO(img_bytes))
    img = np.array(image)
    clahe=cv2.createCLAHE(clipLimit=3.0,tileGridSize=(5,5))
    grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    clahe_img=clahe.apply(grey_img)
    
    
    # Process the image using your Python function
    processed_image =Image.fromarray(np.uint8(clahe_img))
    processed_image.resize((300,300),resample=0)

    
    # Save the output image to a buffer
    output_buffer = io.BytesIO()
    processed_image.save(output_buffer, format='PNG')
    output_buffer.seek(0)
    
    return send_file(output_buffer, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)


