from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Define the path to the pre-trained model
MODEL_PATH = os.path.join(os.getcwd(), "vgg16_model.h5")

# Ensure the model file exists
if not os.path.exists(MODEL_PATH):
    print(f"Warning: Model file not found at {MODEL_PATH}. Please ensure it is uploaded.")

# Routes
@app.route('/')
def base():
    """
    Base route to render the base page.
    """
    return render_template('base.html')

@app.route('/home')
def home():
    """
    Route to render the home page.
    """
    return render_template('base.html' ,user_image=None, diagnosis=None, confidence=None)

@app.route('/about')
def about():
    """
    Route to render the about page.
    """
    return render_template('about.html')

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    """
    Route to handle predictions. Accepts both GET and POST requests.
    """
    if request.method == 'POST':
        # Example: handle user input for predictions (e.g., file upload or form data)
        user_input = request.form.get('input_data')
        if user_input:
            # Placeholder logic for prediction
            prediction_result = f"Predicted result for input: {user_input}"
            return render_template('prediction.html', prediction=prediction_result)
        else:
            error_message = "No input data provided. Please enter valid data."
            return render_template('prediction.html', error=error_message)

    # Render the prediction page for GET requests
    return render_template('prediction.html')

@app.route('/model')
def model():
    """
    Route to display information about the model.
    """
    # Example information about the model
    model_info = "This is a pre-trained VGG16 model for image classification."
    return render_template('model.html', model_info=model_info)

@app.route('/flow')
def flow():
    """
    Route to display the project workflow.
    """
    # Example workflow information
    flow_info = "The workflow involves data preprocessing, model inference, and result visualization."
    return render_template('flow.html', flow_info=flow_info)

if __name__ == '__main__':
    # Ensure the app runs with debugging enabled
    app.run(debug=True)
