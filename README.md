# Chatbot with OpenAI Integration

This is a simple chatbot application that uses the OpenAI GPT-3.5 language model to generate responses to user queries. The chatbot is implemented using Flask, a web framework for Python.

## Prerequisites

Before running the application, make sure you have the following dependencies installed:

- Python 3.x
- Flask
- pandas
- scikit-learn
- seaborn
- matplotlib
- openai

You can install these dependencies using pip:

Copy code into shell
pip install flask pandas scikit-learn seaborn matplotlib openai

## Setup
1. Clone the repository or download the source code files.
2. Navigate to the project directory in your terminal.
3. Open the Python file app.py and replace the value of openai.api_key with your own OpenAI API key. If you don't have an API key, sign up for OpenAI and obtain one.$
4. Make sure you have the required data files in the project directory:
- TrainDataSympany.txt: Contains the system message to be used by the chatbot when answering requests.
- Text_no.txt: Contains the system message to be used when the chatbot cannot answer a request.
- Data for Classifier.csv: Contains the training data for the classifier. It should have two columns: "input" (customer requests) and "label" (target labels indicating whether the chatbot can answer the request or not).
5. Save the changes to app.py and close the file.

## Usage

To run the chatbot, follow these steps:

1. Open a terminal and navigate to the project directory.
2. Run the following command:
  python app.py

3. The Flask application will start running on http://127.0.0.1:5000/.
4. Open a web browser and visit http://127.0.0.1:5000/ to interact with the chatbot.
5. Enter your query or request in the text box and click "Send".
6. The chatbot will generate a response based on the input and display it on the web page.

## Additional Notes

- The chatbot uses the MultinomialNB classifier from scikit-learn to predict whether it can answer a request or not. The classifier is trained on the provided training data.
- The OpenAI GPT-3.5-turbo model is used to generate responses. The system message and user message are sent to the API for generating the response.
- If the classifier predicts that the chatbot can answer the request (answerable=1), both the system message and user message are sent to the API. Otherwise, only the system message is sent.
- The response from the OpenAI API is displayed on the web page.
- The application also opens the web page automatically in Safari browser using webbrowser module. You can change the browser by modifying the code in app.py.
- The application runs in debug mode (debug=True) so that you can see detailed error messages if any occur. It's recommended to disable debug mode in a production environment.
