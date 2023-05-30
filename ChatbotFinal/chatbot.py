from flask import Flask, render_template, request, jsonify
import openai
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import webbrowser

# Set up OpenAI API credentials
openai.api_key = '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'

# Read the system message from a file
with open('TrainDataSympany.txt', 'r') as f:
    system_message = f.read().strip()

with open('Text_no.txt', 'r') as f:
    system_message_no = f.read().strip()

# Load dataset for classifier
data = pd.read_csv("Data for Classifier.csv")

# Extract input features (customer requests) and target labels
X = data.iloc[:, 0]  
y = data.iloc[:, 1]  

# Create an instance of CountVectorizer and convert text data to numerical features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=77)

# Create an instance of MultinomialNB and train the model on the training data
clf = MultinomialNB()
clf.fit(X_train, y_train)

app = Flask(__name__)

# Define the default route to return the index.html file
@app.route("/")
def index():
    return render_template("index.html")

# Open the web page on Safari
webbrowser.get('safari').open_new_tab('http://127.0.0.1:5000/')

# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    
    # Get the message from the user
    message = request.json.get("message")

    # Convert the message into numerical features using the vectorizer
    message_features = vectorizer.transform([message])
    
    # Use the classifier to predict whether the chatbot can answer the request or not
    answerable = clf.predict(message_features)[0]

    if answerable == 1:

        # Send the message to OpenAI's API and receive the response
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        # Send the system message along with the user message
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": message},
        ]
        )
        if completion.choices[0].message != None:
            return completion.choices[0].message
        else:
            return 'Failed to generate response!'
        
    else:
        # Send the message to OpenAI's API and receive the response
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        # Send the system message
        messages=[
            {"role": "system", "content": system_message_no},
        ]
        )
        if completion.choices[0].message != None:
            return completion.choices[0].message
        else:
            return 'Failed to generate response!'

if __name__ == '__main__':
    app.run(debug=True)
