from flask import Flask, render_template, request
import openai
import webbrowser

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = 'XXXXXXX'

# Read the system message from a file
with open('TrainDataSympany.txt', 'r') as f:
    system_message = f.read().strip()

# Define the default route to return the index.html file
@app.route("/")
def index():
    return render_template("index.html")

# Open the web page on Safari
webbrowser.get('safari').open_new_tab('http://127.0.0.1:5000/')

# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    
    # Get the message from the POST request
    message = request.json.get("message")

    # Send the message to OpenAI's API and receive the response
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": message}
    ]
    )
    if completion.choices[0].message!=None:
        return completion.choices[0].message

    else :
        return 'Failed to Generate response!'
    

if __name__=='__main__':
    app.run(debug=True)
