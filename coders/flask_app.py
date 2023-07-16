from flask import Flask, request
from calls import generate_output
from processor import process_request

app = Flask(__name__)

@app.route("/process", methods=['POST'])
def process():
    # Get the prompt from the request JSON
    prompt = request.json['prompt']
    
    # Process the request
    processed_data = process_request(prompt)
    
    # Return the processed data as JSON response
    return {'processed_data': processed_data}

if __name__ == "__main__":
    # Run the Flask app in debug mode
    app.run(debug=True)
